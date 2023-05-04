import json

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


class AvitoParse:

    def __init__(self,
                 url: str,
                 items: list,
                 count: int = 100,
                 version_main=None
                 ):
        self.url = url
        self.items = items
        self.count = count
        self.version_main = version_main
        self.data = []


    def __set_up(self):
        self.driver = uc.Chrome(version_main=self.version_main)


    def __get_url(self):
        self.driver.get(self.url)


    def __paginator(self):
        while self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='pagination-button']") and self.count > 0:
            self.__parse_page()
            self.driver.find_element(By.CSS_SELECTOR, "[data-marker='pagination-button']").click()
            self.count -= 1


    def __parse_page(self):
        titles = self.driver.find_elements(By.CSS_SELECTOR, "[data-marker='item']")
        for title in titles:
            name = title.find_element(By.CSS_SELECTOR, "[itemprop='name']").text
            description = title.find_element(By.CSS_SELECTOR, "[class*='item-description']").text
            url = title.find_element(By.CSS_SELECTOR, "[data-marker='item-title']").get_attribute("href")
            price = title.find_element(By.CSS_SELECTOR, "[itemprop='price']").get_attribute("content")
            data = {
                'name': name,
                'description': description,
                'url': url,
                'price': price
            }
            if any([item.lower() in description.lower() for item in self.items]): # and int(price) == 0:
                self.data.append(data)
                print(data)
            # print(name, description, url, price)
        self.__save_data()


    def __save_data(self):
        with open("items.json", 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)


    def parse(self):
        self.__set_up()
        self.__get_url()
        self.__paginator()


if __name__ == '__main__':
    url = 'https://www.avito.ru/sankt-peterburg?q=%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE'
    url2 = 'https://www.avito.ru/sankt-peterburg/bytovaya_elektronika?cd=1&p=100&q=%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE'
    AvitoParse(url=url,
               items=["iphone", "телевизор", "чехол", "пульт", "диван", "холодильник"],
               count=10,
               version_main=112
               ).parse()
