import csv

import requests

from model import Items


class PetrovichParser:

    def __init__(self, url):
        self.url = url

    @property
    def cookies(self):
        cookies = {
            'SIK': 'eQAAAPWLPm2MIkQS6ZoKAA',
            'SIV': '1',
            '_ym_uid': '1663439206598552002',
            'UIN': 'eQAAADoD_jloRLxecTo6Nggjwn5ZShsYjiJEEhN1BgA',
            '_hjSessionUser_3028204': 'eyJpZCI6IjY4NDM2OGY1LTBhYzAtNWYzNy05MmI3LTQ5ZTZiM2ZmZDA4YiIsImNyZWF0ZWQiOjE2NjYzNzM4ODYxMjQsImV4aXN0aW5nIjpmYWxzZX0=',
            'u__geoCityGuid': 'bd10887b-2da4-11df-942d-0023543d7b52',
            'u__geoUserChoose': '',
            'C_LluH7oMNDkiteESEe4aFGaEO-H4': 'AAAAAAAACEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8D8AAGBbdNvpQWtTCAVsFU2BTigYmYtznsQ',
            'ssaid': '498cb7a0-36b6-11ed-bbcf-f7a2d0f9b74b',
            'dd_custom.lastViewedProductImages': '[]',
            'tmr_lvid': '9d91fc7cf9c13ca34603170bf58fd252',
            'tmr_lvidTS': '1663439206309',
            '_ym_d': '1682616696',
            'FPID': 'FPID2.2.VF9qPWzUnil%2FTfKBVcWJbNmK3KPnVrmv5WdLnL6VvfA%3D.1673884597',
            'count_buy': '0',
            'js_SIK': 'eQAAAPWLPm2MIkQS6ZoKAA',
            'ser_ym_uid': '1663439206598552002',
            'aplaut_distinct_id': 'WRTNpFWhQzSM',
            'rrpvid': '680741462479977',
            'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
            'adrcid': 'APl9S3IF5GMDj5REiHQxgbQ',
            'rcuid': '62bb542dd72cc4000158ed8e',
            'js_FPID': 'FPID2.2.VF9qPWzUnil%2FTfKBVcWJbNmK3KPnVrmv5WdLnL6VvfA%3D.1673884597',
            'ser_adrcid': 'APl9S3IF5GMDj5REiHQxgbQ',
            'SNK': '122',
            'u__typeDevice': 'desktop',
            '_gid': 'GA1.2.1900852933.1682857991',
            'FPLC': 'gHQBpOtkIv12%2BCBjnq6A9get2ue0W6if%2FfeTTeBHdzD4pXb5REKPH9p3gFwZPiEJs8mwF52JsHwTLyCeyfOTB7DY4cpdYgVSuCLKqx7s%2F0KwvaTGDYU4hUNnbVIhfQ%3D%3D',
            '_ym_visorc': 'b',
            '_dc_gtm_UA-23479690-1': '1',
            '_ym_isad': '2',
            'dd__persistedKeys': '[%22custom.lastViewedProductImages%22%2C%22custom.lt13%22%2C%22custom.ts14%22%2C%22user.isReturning%22]',
            'dd_user.isReturning': 'true',
            '_gat_ddl': '1',
            'dd_custom.lt13': '2023-04-30T12:33:14.366Z',
            'dd_custom.ts14': '{%22ttl%22:2592000%2C%22granularity%22:86400%2C%22data%22:{%221682553600%22:2%2C%221682812800%22:1}}',
            'digi_uc': 'W1siY3YiLCIxMDU2NzkiLDE2ODI4NTc5OTQ1OTFdXQ==',
            'mindboxDeviceUUID': 'd05c2d00-f8bc-42f3-a899-23f08a42f14c',
            'directCrm-session': '%7B%22deviceGuid%22%3A%22d05c2d00-f8bc-42f3-a899-23f08a42f14c%22%7D',
            '_gat_popmechanicManualTracker': '1',
            '_ga_XW7S332S1N': 'GS1.1.1682857991.2.1.1682858026.25.0.0',
            '_ga': 'GA1.2.2032785346.1682616696',
            '__tld__': 'null',
            'dd__lastEventTimestamp': '1682858027486',
            'rr-testCookie': 'testvalue',
        }
        return cookies

    @property
    def headers(self):
        headers = {
            'authority': 'api.petrovich.ru',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'cookie': 'SIK=eQAAAPWLPm2MIkQS6ZoKAA; SIV=1; _ym_uid=1663439206598552002; UIN=eQAAADoD_jloRLxecTo6Nggjwn5ZShsYjiJEEhN1BgA; _hjSessionUser_3028204=eyJpZCI6IjY4NDM2OGY1LTBhYzAtNWYzNy05MmI3LTQ5ZTZiM2ZmZDA4YiIsImNyZWF0ZWQiOjE2NjYzNzM4ODYxMjQsImV4aXN0aW5nIjpmYWxzZX0=; u__geoCityGuid=bd10887b-2da4-11df-942d-0023543d7b52; u__geoUserChoose=; C_LluH7oMNDkiteESEe4aFGaEO-H4=AAAAAAAACEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8D8AAGBbdNvpQWtTCAVsFU2BTigYmYtznsQ; ssaid=498cb7a0-36b6-11ed-bbcf-f7a2d0f9b74b; dd_custom.lastViewedProductImages=[]; tmr_lvid=9d91fc7cf9c13ca34603170bf58fd252; tmr_lvidTS=1663439206309; _ym_d=1682616696; FPID=FPID2.2.VF9qPWzUnil%2FTfKBVcWJbNmK3KPnVrmv5WdLnL6VvfA%3D.1673884597; count_buy=0; js_SIK=eQAAAPWLPm2MIkQS6ZoKAA; ser_ym_uid=1663439206598552002; aplaut_distinct_id=WRTNpFWhQzSM; rrpvid=680741462479977; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; adrcid=APl9S3IF5GMDj5REiHQxgbQ; rcuid=62bb542dd72cc4000158ed8e; js_FPID=FPID2.2.VF9qPWzUnil%2FTfKBVcWJbNmK3KPnVrmv5WdLnL6VvfA%3D.1673884597; ser_adrcid=APl9S3IF5GMDj5REiHQxgbQ; SNK=122; u__typeDevice=desktop; _gid=GA1.2.1900852933.1682857991; FPLC=gHQBpOtkIv12%2BCBjnq6A9get2ue0W6if%2FfeTTeBHdzD4pXb5REKPH9p3gFwZPiEJs8mwF52JsHwTLyCeyfOTB7DY4cpdYgVSuCLKqx7s%2F0KwvaTGDYU4hUNnbVIhfQ%3D%3D; _ym_visorc=b; _dc_gtm_UA-23479690-1=1; _ym_isad=2; dd__persistedKeys=[%22custom.lastViewedProductImages%22%2C%22custom.lt13%22%2C%22custom.ts14%22%2C%22user.isReturning%22]; dd_user.isReturning=true; _gat_ddl=1; dd_custom.lt13=2023-04-30T12:33:14.366Z; dd_custom.ts14={%22ttl%22:2592000%2C%22granularity%22:86400%2C%22data%22:{%221682553600%22:2%2C%221682812800%22:1}}; digi_uc=W1siY3YiLCIxMDU2NzkiLDE2ODI4NTc5OTQ1OTFdXQ==; mindboxDeviceUUID=d05c2d00-f8bc-42f3-a899-23f08a42f14c; directCrm-session=%7B%22deviceGuid%22%3A%22d05c2d00-f8bc-42f3-a899-23f08a42f14c%22%7D; _gat_popmechanicManualTracker=1; _ga_XW7S332S1N=GS1.1.1682857991.2.1.1682858026.25.0.0; _ga=GA1.2.2032785346.1682616696; __tld__=null; dd__lastEventTimestamp=1682858027486; rr-testCookie=testvalue',
            'origin': 'https://petrovich.ru',
            'referer': 'https://petrovich.ru/catalog/18978/',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        }
        return headers

    def params(self, offset: int):
        params = {
            'limit': '50',
            'offset': offset,
            'path': '/catalog/18978/',
            'city_code': 'spb',
            'client_id': 'pet_site',
        }
        return params

    def save_csv(self, items):
        with open('data.csv', mode="a", newline='') as file:
            writer = csv.writer(file)
            for product in items.products:
                writer.writerow([product.code, product.title, product.price.gold])

    def parse(self):
        offset = 0
        while True:
            print(offset)
            response = requests.get(
                self.url,
                params=self.params(offset=offset),
                cookies=self.cookies,
                headers=self.headers,
            )
            if response.status_code != 200:
                break
            items = Items.parse_obj(response.json()['data'])
            print(items)
            self.save_csv(items)
            offset += 50
            #print(response.json())

if __name__ == '__main__':
    url = 'https://api.petrovich.ru/catalog/v3/sections/18978/products'
    PetrovichParser(url).parse()
