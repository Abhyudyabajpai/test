import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
# To see the html view of the website:
# print(response.text)
soup = BeautifulSoup(response.text,"html.parser")
articles = soup.find_all("article")
#print(articles)
with open("blog_data.csv","w") as file:
    csv_write = writer(file)
    csv_write.writerow(["title","link","date"])
# For looking to the all the headings
    for article in articles:
        # print(article.find("a").get_text())
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find("time")["datetime"]
         # print(title,url,date)
        csv_write.writerow([title,url,date])