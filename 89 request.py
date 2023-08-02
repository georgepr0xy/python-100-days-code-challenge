import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://erp.aktu.ac.in/webpages/oneview/oneview.aspx")
# print(response.text)

url = "https://erp.aktu.ac.in/"
r = requests.get(url)
# print(r.text)


# s =BeautifulSoup(r.text,"html.parser")
# print(s.prettify)
for heading in r.find_all("div"):
    print(heading.text)