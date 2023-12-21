import requests
from bs4 import BeautifulSoup

def main():
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    locations = soup.find_all("location")
    
    for location in locations:
        city = location.find("city").text
        date = location.find("data").find("tmef").text
        weather = location.find("data").find("wf").text
        print(f"{date} {city} : {weather}")

if __name__ == "__main__":
    main()