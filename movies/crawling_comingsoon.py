import requests, json
from bs4 import BeautifulSoup

file = open("comingsoon.json", "w", encoding="utf-8")

html = requests.get("https://www.cgv.co.kr/?NaPm=ct%3Dl3lqoeqf%7Cci%3Dcheckout%7Ctr%3Dds%7Ctrx%3D%7Chk%3Ded8fb41231f4290efba5f687ab1bfe2a6f6ba90e#none")
soup = BeautifulSoup(html.text, 'lxml')

comingsoon_data = []
num = 1
for i in range(25, 39):

    title = soup.find_all('strong', class_='movieName')[i]
    print("제목:", title.string)

    poster = soup.find_all('div', class_='img_wrap')[i]
    poster_path = poster.img.get('src')
    # print("포스터:", poster_path)

    day = soup.find_all('div', class_='movieAgeLimit_wrap')[i]
    d_day = day.div.span.string
    # print("d-day", d_day)

    fields = {
        'title': title.string,
        'poster_path': poster_path,
        'd_day': d_day,
    }
    data = {
        "model": "movies.comingsoon",
        "pk": num,
        "fields": fields,
    }
    comingsoon_data.append(data)
    num += 1
file.write(json.dumps(comingsoon_data, indent=3, ensure_ascii=False))

file.close()
