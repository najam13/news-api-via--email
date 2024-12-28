import requests
from send_email import send_email

topic = "tesla"
api_key = "14529cccb9fb487cb6b7d6cd0633add3"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&apiKey="
       "14529cccb9fb487cb6b7d6cd0633add3"
       "language = en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
body = ""
# Access the article title and description
for article in content["articles"][0:20]:
    if article["title"] is not None:
        body = ("subject: Today's news" + "\n "
                + body + article["title"] + "\n"
                + article["description"] + "\n"
                + article["url"] + 2*"\n")

body = body.encode("utf-8")
send_email(message=body)
