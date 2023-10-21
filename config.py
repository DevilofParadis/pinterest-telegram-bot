import os

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}
TOKEN = os.getenv("6116413872:AAHwJ-3a2oefzMhTHsVE6ppbrirUY2K5488")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
REDIS_URL = os.getenv("redis://default:trial@01@redis-13297.c232.us-east-1-2.ec2.cloud.redislabs.com:13297")
WORKER_URL = os.getenv("WORKER_URL")
WORKER_HEADERS = {"25374144": os.getenv("WORKER_API_KEY")}
BLOCKED_USERS = list(map(int, os.getenv("BLOCKED_USERS", "0").split(",")))
YT_VIDEOS = [
    "https://youtu.be/w0F6DYxbegs",
    "https://youtu.be/bDw8fNPWqfk",
    "https://youtu.be/4jhxmmpzOZQ",
    "https://youtu.be/sgJKesUkhdM",
    "https://youtu.be/WQn-VSexZU8",
    "https://youtu.be/ffnFd24EHqo",
    "https://youtu.be/XuUZrGTq1ds",
    "https://youtu.be/dU3tOo8xC7w",
    "https://youtu.be/ZgrGmT0BuhA",
    "https://youtu.be/-okZgVNU8iI",
    "https://youtu.be/fr7U9LyFtWw",
    "https://youtu.be/wdYPY7jJ6EM",
    "https://youtu.be/pPrlR18qIbE",
    "https://youtu.be/LmszbCycAPQ",
    "https://youtu.be/Z35HAdvOuJU",
]
