readme_content = '''# Time.com Latest Stories API

**A simple API to fetch the latest 6 stories from Time.com in JSON format.**

## Usage

**Endpoint:** `http://<localhost>/getTimeStories`

Make a GET request to the above endpoint, and the API will respond with the latest 6 stories.

Example Response:
```json
[
    {
        "title": "Story 1 Title",
        "link": "https://time.com/story-1"
    },
    {
        "title": "Story 2 Title",
        "link": "https://time.com/story-2"
    },
    ...
]



