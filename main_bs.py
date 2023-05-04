from bs4 import BeautifulSoup
import re
import requests
import fake_useragent
import certifi
print(certifi.where())

# soup = BeautifulSoup('<a></b></a>', 'lxml')
# print(soup)

with open('page.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

# print(soup)
# print(soup.a)  # получаем только первую ссылку
title = soup.title
# print(title)
# print(title.name)
# print(title.attrs)
# print(title.text)

# print(title.get_text())

# print(title.string)
h1 = soup.h1
# print(h1)
# print(h1.attrs)
# print(h1.attrs['class'])
# print(h1['class'])
# print(h1.get('class'))
# print(h1.has_attr('class')) # проверить наличие атрибута
# print(h1.text.strip())
# print(h1.get_text(strip=True, separator=' '))  # получение текста

# find() find_all() для поиска по дереву
# print(soup.find('a'))
# print(soup.find('nav').find('a').text)
# print(soup.find('nav').find('a').get('href'))

links = soup.find('nav').find_all('a', class_="p-2 link-secondary")
links2 = soup.find('nav').find_all('a', attrs={'class': "p-2 link-secondary"})
links3 = soup.find('nav').find_all('a', attrs={'class': "link-secondary"})
links4 = soup.find('nav').find_all(title='test')
# print(links)
# for link in links:

    # print(f'{link.get_text(strip=True)} - {link.get("href")}')
# print(links3)

# print(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']))
# print(soup.find_all(re.compile('^h[1-6]')))
# print(soup.find_all(True))  # все теги

ua = fake_useragent.UserAgent()

# r = requests.get('https://www.yandex.ru/', headers={"User-Agent": ua.random})

# print(r)

#el = soup.find('table', class_='table').find_parent('div', 'col-md-8')
el = soup.find('table', class_='table').find_next_siblings()
# el = soup.find('table', class_='table').find_previous_sibling()
el = soup.find('table', class_='table').find_next()
el = soup.find('table', class_='table').find_all_next()
el = soup.find('table', class_='table').find_parent().find_next().find_next()
el = soup.find('table', class_='table').find_parent().find('font')
print(el)
