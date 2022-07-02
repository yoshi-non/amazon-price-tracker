import requests
from bs4 import BeautifulSoup
# import os
# from dotenv import load_dotenv
# load_dotenv()

amazonURL = "https://www.amazon.co.jp/React%E3%83%8F%E3%83%B3%E3%82%BA%E3%82%AA%E3%83%B3%E3%83%A9%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0-%E7%AC%AC2%E7%89%88-%E2%80%95Web%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E9%96%8B%E7%99%BA%E3%81%AE%E3%83%99%E3%82%B9%E3%83%88%E3%83%97%E3%83%A9%E3%82%AF%E3%83%86%E3%82%A3%E3%82%B9-Alex-Banks/dp/4873119383/ref=sr_1_1?crid=1BCQ7J8Y6KZGQ&keywords=amazon+react&qid=1656773731&sprefix=%2Caps%2C441&sr=8-1"


def amazonTrackingPrice():
    amazonPage = requests.get(amazonURL)
    soup = BeautifulSoup(amazonPage.content, "html.parser")

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="price").get_text()
    convertedPrice = price[1:7].replace(",", "")
    intPrice = int(convertedPrice)
    print(title)
    print(intPrice)

    if(intPrice > 3000):
        sendLineNotify()


def sendLineNotify():
    print("lineに通知がいきました")
    # lineNotifyToken = "os.environ['TOKEN_KEY']"
    lineNotifyToken = "your token"
    lineNotifyApi = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {lineNotifyToken}"}
    data = {"message": "今がお買い時です!" + amazonURL}
    requests.post(lineNotifyApi, headers=headers, data=data)


amazonTrackingPrice()
