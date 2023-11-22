import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
import smtplib # Модуль для работы с почтой

# Основной класс
class Currency:
	# Ссылка на нужную страницу
	DOLLAR_EURO = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&sca_esv=584647371&sxsrf=AM9HkKkaMc57VbdQh04xiiHJNsw9s_0Qgg%3A1700678149985&ei=BUpeZZfbO7e9i-gP1I2vqAc&ved=0ahUKEwjX8Ybon9iCAxW33gIHHdTGC3UQ4dUDCBA&uact=5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&gs_lp=Egxnd3Mtd2l6LXNlcnAiGNC00L7Qu9C70LDRgCDQuiDQtdCy0YDQvjIKEAAYgAQYRhiCAjIFEAAYgAQyChAAGIAEGBQYhwIyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESLcTUABYsRBwAngBkAEAmAGcAaABiQiqAQMwLji4AQPIAQD4AQHCAgcQABiABBgKwgIMEC4YFhgeGMcBGNEDwgIGEAAYFhgewgIJEAAYgAQYChgqwgIIEAAYFhgeGArCAg4QLhgWGB4YxwEY0QMYCsICCxAAGBYYHhjxBBgKwgIKECMYgAQYigUYJ-IDBBgAIEGIBgE&sclient=gws-wiz-serp'
	# Заголовки для передачи вместе с URL
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

	current_converted_price = 0
	difference = 0 # Разница после которой будет отправлено сообщение на почту

	def __init__(self):
		# Установка курса валюты при создании объекта
		self.current_converted_price = float(self.get_currency_price().replace(",", "."))

	# Метод для получения курса валюты
	def get_currency_price(self):
		# Парсим всю страницу
		full_page = requests.get(self.DOLLAR_EURO, headers=self.headers)

		# Разбираем через BeautifulSoup
		soup = BeautifulSoup(full_page.content, 'html.parser')

		# Получаем нужное для нас значение и возвращаем его
		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
		return convert[0].text

	# Проверка изменения валюты
	def check_currency(self):
		currency = float(self.get_currency_price().replace(",", "."))
		if currency >= self.current_converted_price + self.difference:
			print("Курс сильно вырос, может пора что-то делать?")
		elif currency <= self.current_converted_price - self.difference:
			print("Курс сильно упал, может пора что-то делать?")

		print("Сейчас курс: 1 доллар = " + str(currency))



# Создание объекта и вызов метода
currency = Currency()
currency.check_currency()
