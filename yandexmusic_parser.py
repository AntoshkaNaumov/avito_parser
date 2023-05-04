import requests
from pprint import pprint

cookies = {
    'my': 'YwA=',
    'gdpr': '0',
    '_ym_uid': '1645464466702207110',
    'amcuid': '4972560311656757599',
    'yabs-frequency': '/5/DG0006FposC00000/swvnE0daUaQCIYVT_4lBOD0FPunAG_XztkPw8z93Z4eWc44EFE6kx6wCIY3L9HG9nvsNNunAG2FTgilyTwjQZ4fWGDlxQQ6MVdECIY2m8OCwW-74HunAW9VypjGn6h1UZ4eWlaSEXY_52M6DIk01hBPJbmeQbKQCIY0oszepqxP8LOnAOCTxRYUSzk98ZKeW0cb_gdMKKKv0ZKh00TbmYRSKiv9DZ4gWsfAap4CIwdACIe0QpcoU-EXqN8nA80On2LdlHRHtZ4f0bqyobYOQBagCIc1Zu8-izch6QOnAm57lnHVa9vzpZKe00Vk3U5LI8fvdZ4fWbUDqs4l_UKoCIg2LwjxeEKWnLenAe6DAzBnKAfvuZKgW0XtEUwKHQlDzZKf00G00/',
    'yandexuid': '7872100861644332491',
    'yuidss': '7872100861644332491',
    'i': '+ycTOVKvunUZtk0Z3w8LJc+Ag9MF+B/PVQw70ohZwC7pECuGCbm73EAwMcTA+gyD1SfAbExvekYv4Qr5mT9xMG7cfqM=',
    'ymex': '1681375022.oyu.1868299921678656871#1710192872.yrts.1678656872#1982923719.yrtsi.1667563719',
    'yandex_gid': '238',
    '_ym_d': '1681809619',
    'skid': '7243681941681843731',
    'is_gdpr': '1',
    'is_gdpr_b': 'COjOQRDQswEYASgC',
    '_ym_isad': '2',
    'ys': 'wprid.1682603824010769-14360474782664529643-balancer-l7leveler-kubr-yp-vla-25-BAL-8215#c_chck.1158039492',
    'yp': '1712743624.p_cl.1681207623#1714139823.p_sw.1682603823#1714040611.p_undefined.1682504610#1997963823.pcs.0#1699295310.pgp.5_27795962#1699099655.stltp.serp_bk-map_1_1667563655#1683402702.ygu.1#1684961137.hdrc.0#1682887517.mcv.0#1682887517.szm.1%3A1920x1080%3A1195x927#1683063255.mcl.',
    'cycada': 'IN43k+C7R9V7OeV9vuhQNHeg7FN1aohd5i+du07WdcY=',
    'device_id': 'b605646f863b548e4baf0699503de9f38f040b896',
    '_ym_visorc': 'b',
    'active-browser-timestamp': '1682604027030',
    '_yasc': 'hPLIZcCF/n9seZU2bC+b0pJHZAddgnyvpCnMG7Pg0D2X9dC7yY1u6Ga3rwv0IDpb6RvN1Bc6KQjd1YTEooU=',
    'bh': 'EkEiQ2hyb21pdW0iO3Y9IjExMiIsICJHb29nbGUgQ2hyb21lIjt2PSIxMTIiLCAiTm90OkEtQnJhbmQiO3Y9Ijk5IhoFIng4NiIiECIxMTIuMC41NjE1LjEzOCIqAj8wOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUlwiQ2hyb21pdW0iO3Y9IjExMi4wLjU2MTUuMTM4IiwiR29vZ2xlIENocm9tZSI7dj0iMTEyLjAuNTYxNS4xMzgiLCJOb3Q6QS1CcmFuZCI7dj0iOTkuMC4wLjAiIg==',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': 'my=YwA=; gdpr=0; _ym_uid=1645464466702207110; amcuid=4972560311656757599; yabs-frequency=/5/DG0006FposC00000/swvnE0daUaQCIYVT_4lBOD0FPunAG_XztkPw8z93Z4eWc44EFE6kx6wCIY3L9HG9nvsNNunAG2FTgilyTwjQZ4fWGDlxQQ6MVdECIY2m8OCwW-74HunAW9VypjGn6h1UZ4eWlaSEXY_52M6DIk01hBPJbmeQbKQCIY0oszepqxP8LOnAOCTxRYUSzk98ZKeW0cb_gdMKKKv0ZKh00TbmYRSKiv9DZ4gWsfAap4CIwdACIe0QpcoU-EXqN8nA80On2LdlHRHtZ4f0bqyobYOQBagCIc1Zu8-izch6QOnAm57lnHVa9vzpZKe00Vk3U5LI8fvdZ4fWbUDqs4l_UKoCIg2LwjxeEKWnLenAe6DAzBnKAfvuZKgW0XtEUwKHQlDzZKf00G00/; yandexuid=7872100861644332491; yuidss=7872100861644332491; i=+ycTOVKvunUZtk0Z3w8LJc+Ag9MF+B/PVQw70ohZwC7pECuGCbm73EAwMcTA+gyD1SfAbExvekYv4Qr5mT9xMG7cfqM=; ymex=1681375022.oyu.1868299921678656871#1710192872.yrts.1678656872#1982923719.yrtsi.1667563719; yandex_gid=238; _ym_d=1681809619; skid=7243681941681843731; is_gdpr=1; is_gdpr_b=COjOQRDQswEYASgC; _ym_isad=2; ys=wprid.1682603824010769-14360474782664529643-balancer-l7leveler-kubr-yp-vla-25-BAL-8215#c_chck.1158039492; yp=1712743624.p_cl.1681207623#1714139823.p_sw.1682603823#1714040611.p_undefined.1682504610#1997963823.pcs.0#1699295310.pgp.5_27795962#1699099655.stltp.serp_bk-map_1_1667563655#1683402702.ygu.1#1684961137.hdrc.0#1682887517.mcv.0#1682887517.szm.1%3A1920x1080%3A1195x927#1683063255.mcl.; cycada=IN43k+C7R9V7OeV9vuhQNHeg7FN1aohd5i+du07WdcY=; device_id=b605646f863b548e4baf0699503de9f38f040b896; _ym_visorc=b; active-browser-timestamp=1682604027030; _yasc=hPLIZcCF/n9seZU2bC+b0pJHZAddgnyvpCnMG7Pg0D2X9dC7yY1u6Ga3rwv0IDpb6RvN1Bc6KQjd1YTEooU=; bh=EkEiQ2hyb21pdW0iO3Y9IjExMiIsICJHb29nbGUgQ2hyb21lIjt2PSIxMTIiLCAiTm90OkEtQnJhbmQiO3Y9Ijk5IhoFIng4NiIiECIxMTIuMC41NjE1LjEzOCIqAj8wOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUlwiQ2hyb21pdW0iO3Y9IjExMi4wLjU2MTUuMTM4IiwiR29vZ2xlIENocm9tZSI7dj0iMTEyLjAuNTYxNS4xMzgiLCJOb3Q6QS1CcmFuZCI7dj0iOTkuMC4wLjAiIg==',
    'Referer': 'https://music.yandex.ru/chart',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Retpath-Y': 'https://music.yandex.ru/chart',
    'X-Yandex-Music-Client-Now': '2023-04-27T17:02:08+03:00',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.ru',
    'overembed': 'false',
    'ncrnd': '0.2854570782721719',
}

response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params, cookies=cookies, headers=headers)
print(response.status_code)
# pprint(response.json()['chartPositions'])
for track in response.json()['chartPositions']:
    position = track['chartPosition']['position']
    title = track['track']['title']
    author = track['track']['artists'][0]['name']
    artist = [artist['name'] for artist in track['track']['artists']]
    authors = ', '.join(artist)
    print(f"N-{position} - {title} - {authors}")
