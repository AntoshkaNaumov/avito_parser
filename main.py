import requests
from fake_useragent import UserAgent


ua = UserAgent()

headers = {
"Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
query = {
    "search_query": "весна"
}
# r = requests.get('https://httpbin.org/get', headers=headers)
r = requests.get('https://www.youtube.com/results', headers=headers, params=query)

# print(type(r))

# print(r.status_code)
#print(r.headers)
# print(r.content)
#print(r.text)
# print(r.json)

data = {
    "custemail": "Anton.naumov@inbox.ru",
    "custname": "Anton",
    "custtel": "1111111",
    "delivery": "",
    "size": "small",
    "topping": "bacon"
}
r = requests.post('http://httpbin.org/post', headers=headers, data=data)
#print(r.json())
#print(r.json()['form'])
#print(r.json()['form']['custemail'])

url = 'https://www.shutterstock.com/shutterstock/videos/1078354736/preview/stock-footage-drone-video-of-sunflower-field-in-a-beautiful-evening-sunset-k-aerial-view-of-sunflowers-in.webm'

r = requests.get(url, headers=headers, stream=True)

#print(r.content)
#print(r.raw.read(20)) # чтение данных

#with open('1.webm', 'wb') as fd: # парсинг видео файла
#    for chunk in r.iter_content(chunk_size=1024 * 100):
#        fd.write(chunk)
#        print('Write chunk 100kb')

r = requests.get('https://', headers=headers)
#print(r.status_code)
#print(r.headers)
#print(r.content)

url_2 = 'https://wp-content/uploads/lifeweaver.jpg'
r = requests.get(url_2, headers=headers, stream=True)
# with open('1.jpg', 'wb') as fd: # парсинг картинки
#    for chunk in r.iter_content(chunk_size=1024 * 10):
#        fd.write(chunk)
#        print('Write chunk 10kb')

#r = requests.get(url_2, headers=headers)
#with open('2.jpg', 'wb') as fd: # парсинг картинки
#    fd.write(r.content) # content содержит бинарные данные

url_3 = 'https://httpbin.org/headers'

#headers = {
    #"User-Agent": ua.random # используем случайного User-Agent
#}

#for i in range(1, 11):
#    headers = {
#        "User-Agent": ua.random  # используем случайного User-Agent
#    }

#    res = requests.get(url_3, headers=headers)
#    print(res.json())

url_4 = 'https://i0.wp.com/milkboys.net/wp-content/uploads/lifeweaver.jpg'

print(url_4.split('/')[-1])

def get_name(file_url):
    return file_url.split('/')[-1]

r = requests.get(url_4, headers={"UserAgent" : ua.random})

with open(get_name(url_4), 'wb') as fd: # парсим картику и записываем в файл
    fd.write(r.content)
