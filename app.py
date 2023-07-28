import re
import json
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 5000

def get_time_stories(url):
    response = requests.get(url)
    if response.status_code in [301, 302]:
        return get_time_stories(response.headers['location'])
    return response.text

def extract_stories(data_res):
    stories = re.findall(r'<a href="/.*?/">\s*<h3 class="latest-stories__item-headline">.*?</h3>', data_res)

    links = [re.search(r'/(.*?)/', story).group(0) for story in stories]

    titles = [re.search(r'>(.*?)<', story).group(1) for story in stories]

    data = [{"title": title, "link": f"https://time.com{link}"} for title, link in zip(titles, links)][:6]

    return data

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/getTimeStories":
            data_res = get_time_stories("https://www.time.com")
            data = extract_stories(data_res)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(data), "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps({"message": "Route not found"}), "utf-8"))

def run_server():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Server running on port: {PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
