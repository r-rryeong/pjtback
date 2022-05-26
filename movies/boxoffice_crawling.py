import requests, json
from bs4 import BeautifulSoup

file = open("boxoffice.json", "w", encoding="utf-8")

boxoffice_data = []
num = 1
# 연도별 영화 순위
for i in range(2022, 2011, -1):
    html = requests.get(f"https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={i}%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84")
    soup = BeautifulSoup(html.text, 'lxml')
    
    for j in range(0, 10):

        t = soup.find_all('div', class_='scm_ellipsis _ellipsis')[j]
        title = t.strong.string
        # print("제목:", title)

        date = soup.find_all('dl', class_='movie_item')[j]
        release_date = date.dd.string.strip()
        lst_d = list(release_date)
        lst_d.pop()
        release_date = "".join(lst_d)
        # print("개봉일:", release_date)

        a = list(soup.find_all('dl', class_='movie_item')[j])
        audience = a[-2].string
        # print("관객수:", audience)

        poster = soup.find_all('div', class_='thumb')[j]
        poster_path = poster.a.img.get('src')
        lst = list(poster_path)
        lst.insert(49, '0')
        lst.insert(54, '0')
        poster_path = "".join(lst)
        # print("포스터:", poster_path)

        fields = {
            'title': title,
            'release_date': release_date,
            'audience': audience,
            'poster_path': poster_path,
            'year': i,
        }
        data = {
            "model": "movies.boxoffice",
            "pk": num,
            "fields": fields,
        }
        boxoffice_data.append(data)
        num += 1
  

html = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%97%AD%EB%8C%80+%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4#")
soup = BeautifulSoup(html.text, 'lxml')
# 역대 영화 순위
for j in range(0, 20):

    t = soup.find_all('div', class_='scm_ellipsis _ellipsis')[j]
    title = t.strong.string
    # print("제목:", title)

    date = soup.find_all('dl', class_='movie_item')[j]
    release_date = date.dd.string.strip()
    lst_d = list(release_date)
    lst_d.pop()
    release_date = "".join(lst_d)
    # print("개봉일:", release_date)

    a = list(soup.find_all('dl', class_='movie_item')[j])
    audience = a[-2].string
    # print("관객수:", audience)

    poster = soup.find_all('div', class_='thumb')[j]
    poster_path = poster.a.img.get('src')
    lst = list(poster_path)
    lst.insert(49, '0')
    lst.insert(54, '0')
    poster_path = "".join(lst)
    # print("포스터:", poster_path)

    fields = {
        'title': title,
        'release_date': release_date,
        'audience': audience,
        'poster_path': poster_path,
        'year': 9999,
    }
    data = {
        "model": "movies.boxoffice",
        "pk": num,
        "fields": fields,
    }
    boxoffice_data.append(data)
    num += 1

file.write(json.dumps(boxoffice_data, indent=3, ensure_ascii=False))

file.close()
