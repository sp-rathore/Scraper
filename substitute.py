import  requests
from bs4 import BeautifulSoup

search = input(" Please enter the search parameter :  ")
params = {"q" : search}

r = requests.get("https://www.bing.com/search", params=params)
#print (r.text)
soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.find_all("li", {"class" : "b_algo"})
#print(links)

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]
    print("item_text : ", item_text)
    print("item_href: ", item_href)
