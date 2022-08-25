import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import choice

web = "https://quotes.toscrape.com"
url_ext = "/page/1"
quotes = []

while url_ext:
    response = requests.get(f"{web}{url_ext}")
    soup = BeautifulSoup(response.text,"html.parser")
    data = soup.find_all(class_ = "quote")

    for i in data:
        quotes.append({
            "text": i.find(class_="text").get_text(),
            "author": i.find(class_="author").get_text(),
            "link": i.find("a")["href"]
            })

    next = soup.find(class_="next")
    if next:
        url_ext = next.find("a")["href"]
    else:
        url_ext = False
#scrapes all pages of the site, appends each quote

quote = choice(quotes)
print("Here's a quote:")
print(quote["text"])
url_ext = quote["link"]
res = requests.get(f"{web}{url_ext}")
soup = BeautifulSoup(res.text,"html.parser")
birthday = soup.find(class_ = "author-born-date").get_text()
location = soup.find(class_ = "author-born-location").get_text()
first_letter = quote["author"][0]
last_letter = quote["author"][quote["author"].find(" ")+1]

#takes randomly select quote and gives it the user, grabs future hint information in the authors birthday and birth location

count = 0
print ("Guess the author of the quote \n you have 4 chances!")
guess = "name"
while guess != quote["author"].lower() and count < 5:
    guess = input("Please enter your guess here: ").lower()
    count += 1
    if guess == quote["author"].lower():
        print ("Correct")
        break
    elif count == 1:
        print (f"The first letter of the authors first name is {first_letter}")
    elif count == 2:
        print (f"The first letter of the authors last name is {last_letter}")
    elif count == 3:
        print (f"The author was born on {birthday}")
    elif count == 4:
        print (f"The author was born in {location}")
    elif count == 5:
        print ("Sorry better luck next time!")
#takes inputs and gives hints as required until author is correct
