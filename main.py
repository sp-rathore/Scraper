import os
from io import BytesIO
from bs4 import BeautifulSoup
import requests

search = input("Enter the term you want to search here :  ")
params = {"q": search}

##r=requests.get("https://www.bing.com/search", params=params)

r=requests.get("https://en.wikipedia.org/wiki", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.find_all("li", {"class": "b_algo"})


for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        try:
            print("Parent: ", item.find("a").parent)
            print("Summary : ", item.find("a").parent.parent.find("p").text)
        except:
            print("Parent or Summary not found for the search query")


'''
'''