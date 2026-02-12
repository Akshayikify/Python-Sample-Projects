import requests

status_code = {}
websites = [
    "https://www.google.com/",
    "https://github.com",
    "https://stackoverflow.com",
    "https://www.canva.in",
    "https://www.youtube.com"
]

def check_website():
    for website in websites:
        try:
            response = requests.get(website, timeout=5)
            status_code[website] = "Up" if response.status_code == 200 else "Down"
        except requests.exceptions.RequestException:
            status_code[website] = "Down"

    print(status_code)

check_website()
