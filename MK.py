import json
import re
from datetime import datetime
from newspaper import Article

i = 0  # id number
file_path="./MK.json"
news_format_json = {}
news_format_json['MK'] = []
for y in range(2020, 2021):
    for m in range(1, 2):
        for n in range(0, 10001):

            url = "https://www.mk.co.kr/news/economy/view/{}/{:02d}/{}/".format(y, m, n)  # "economy is meaningless because article shown is determined by 'n'
            art = Article(url, keep_article_html=True)

            try:
                art.download()
                art.parse()
                art2 = art.text.split()
            except:
                print("***** error article *****")
                continue
            if len(art2) == 0:
                print("***** blank article *****")
                continue

            print(i)
            # print("\n{}, {}, {}\n".format(y, m, n))
            # print(art.title)
            # print(art.authors)
            # print(art.text)

            match = re.search("\d{4}\.\d{2}\.\d{2}", art.html)
            dt = datetime.strptime(match.group(), "%Y.%m.%d")

            news_format_json['MK'].append({
                "id": i,
                "title": art.title,
                "text": art.text,
                "timestamp": [dt.year, dt.month, dt.day],
                "html": art.article_html
            })

            i += 1

with open(file_path, 'w', encoding='utf-8') as outfile:
    json.dump(news_format_json, outfile, indent=4, ensure_ascii=False)

print(news_format_json)