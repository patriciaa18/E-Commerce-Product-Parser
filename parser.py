from urllib.request import urlopen
import json
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager

# link should look like this -> https://shopee.co.id/api/v4/item/get?itemid=7658713227&shopid=48382819
api_url = input("Input Shopee Network Response (search'get?itemid' in network response-> copy link): ")

# To use Chrome browser
driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())

# Getting response
driver.get(api_url)
url_list = []
for request in driver.requests:
    if request.response:
        url_list.append(request.url)
# Make sure the link is true
for i, elem in enumerate(url_list):
    if "get?itemid" in elem:
        print("Found API...")

# Getting api from list
api = url_list[i]
print("Getting breadcrumbs from {api}...".format(api=api))     
  
# store response
response = urlopen(api)
data_json = json.loads(response.read())

cat1 = data_json["data"]["categories"][0]["display_name"]
cat2 = data_json["data"]["categories"][1]["display_name"]
cat3 = data_json["data"]["categories"][2]["display_name"]
  
# print the wanted response
breadcrumbs = "Kategori: {cat1} > {cat2} > {cat3}".format(cat1=cat1, cat2=cat2, cat3=cat3)
print(breadcrumbs)   
