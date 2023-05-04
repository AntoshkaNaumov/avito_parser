import csv

from lxml import html
import requests


def get_info(url, headers):
    res = requests.get(url, headers)
    tree = html.fromstring(res.content)

    titles = tree.xpath('//a[@class="Link ListingItemTitle__link"]//text()')
    # print(titles)
    prices = [price.replace(u'\xa0', ' ') for price in tree.xpath('//div[@class="ListingItemPrice__content"]//text()')]
    # print(prices)
    # print(len(prices))

    # prices_list = []
    # for price in prices:
    #    prices_list.append(price.replace(u'\xa0', ' '))
    # print(prices_list)
    params = [param.replace(u'\u2009', ' ').replace(u'\xa0', ' ')
            for param in tree.xpath(
            '//div[@class="ListingItemTechSummaryDesktop ListingItem__techSummary"][1]//text()')][::2]
    # print(params)

    with open('auto.csv', mode='w', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=':')
        writer.writerow(['Название авто', 'Характеристики', 'Цена'])
        for index in range(len(titles)):
            writer.writerow([titles[index], params[index], prices[index]])


if __name__ == '__main__':
    main_url = 'https://auto.ru/sankt-peterburg/cars/bmw/all/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
                "Accept-Language": 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
               'Cookie': 'sc_1681816313387=%D0%BD%D0%B5%20%D0%BF%D0%B0%D1%80%D1%81%D0%B8%D1%82%D1%81%D1%8F%20%D1%81%D0%B0%D0%B9%D1%82%20auto.ru:zennolab.com:%2Fsearch%2F:1681816309695257-12998715175177448281-balancer-l7leveler-kubr-yp-vla-17-BAL-8168; sc_1681816509432=%D0%BD%D0%B5%20%D0%BF%D0%B0%D1%80%D1%81%D0%B8%D1%82%D1%81%D1%8F%20%D1%81%D0%B0%D0%B9%D1%82%20auto.ru:www.cyberforum.ru:%2Fsearch%2F:1681816309695257-12998715175177448281-balancer-l7leveler-kubr-yp-vla-17-BAL-8168; gdpr=0; _ym_uid=1645464466702207110; amcuid=4972560311656757599; yabs-frequency=/5/DG0006FposC00000/swvnE0daUaQCIYVT_4lBOD0FPunAG_XztkPw8z93Z4eWc44EFE6kx6wCIY3L9HG9nvsNNunAG2FTgilyTwjQZ4fWGDlxQQ6MVdECIY2m8OCwW-74HunAW9VypjGn6h1UZ4eWlaSEXY_52M6DIk01hBPJbmeQbKQCIY0oszepqxP8LOnAOCTxRYUSzk98ZKeW0cb_gdMKKKv0ZKh00TbmYRSKiv9DZ4gWsfAap4CIwdACIe0QpcoU-EXqN8nA80On2LdlHRHtZ4f0bqyobYOQBagCIc1Zu8-izch6QOnAm57lnHVa9vzpZKe00Vk3U5LI8fvdZ4fWbUDqs4l_UKoCIg2LwjxeEKWnLenAe6DAzBnKAfvuZKgW0XtEUwKHQlDzZKf00G00/; yandexuid=7872100861644332491; yuidss=7872100861644332491; i=+ycTOVKvunUZtk0Z3w8LJc+Ag9MF+B/PVQw70ohZwC7pECuGCbm73EAwMcTA+gyD1SfAbExvekYv4Qr5mT9xMG7cfqM=; ymex=1681375022.oyu.1868299921678656871#1710192872.yrts.1678656872#1982923719.yrtsi.1667563719; yandex_gid=238; is_gdpr=1; is_gdpr_b=CIHuMRCosgEYASgC; _ym_isad=2; _ym_d=1681809619; yabs-sid=647063391681812736; ys=wprid.1681816309695257-12998715175177448281-balancer-l7leveler-kubr-yp-vla-17-BAL-8168#c_chck.438371436; yp=1712743624.p_cl.1681207623#1713345619.p_sw.1681809619#1713025880.p_undefined.1681489880#1997176309.pcs.0#1699295310.pgp.5_27795962#1699099655.stltp.serp_bk-map_1_1667563655#1683402702.ygu.1#1682840740.hdrc.0#1682074248.mcv.0#1682074249.szm.1:1920x1080:1920x937#1682414419.mcl.#1681896166.ln_tp.true; sync_cookie_csrf=2204355827fake; bh=EkEiQ2hyb21pdW0iO3Y9IjExMiIsICJHb29nbGUgQ2hyb21lIjt2PSIxMTIiLCAiTm90OkEtQnJhbmQiO3Y9Ijk5IhoFIng4NiIiDyIxMTIuMC41NjE1Ljg2IioCPzA6CSJXaW5kb3dzIkIIIjEwLjAuMCJKBCI2NCJSWiJDaHJvbWl1bSI7dj0iMTEyLjAuNTYxNS44NiIsIkdvb2dsZSBDaHJvbWUiO3Y9IjExMi4wLjU2MTUuODYiLCJOb3Q6QS1CcmFuZCI7dj0iOTkuMC4wLjAiIg=='}

    get_info(main_url, headers)
    #r = requests.get(main_url, headers=headers)
    #print(r.content)


