import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
import smtplib # Модуль для работы с почтой

# Основной класс
class Currency:
	# Ссылка на нужную страницу
	DOLLAR_EURO = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&sca_esv=584647371&sxsrf=AM9HkKkQXe9-1NHHGGmT31ravcTwd6hn5w%3A1700679294568&ei=fk5eZfKEIqXQi-gP_a-40AE&oq=%D0%B5%D0%B2%D1%80%D0%BE+&gs_lp=Egxnd3Mtd2l6LXNlcnAiCdC10LLRgNC-ICoCCAAyDxAAGIAEGIoFGEMYRhiCAjIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQ0iBGlAAWKIPcAJ4AZABAJgBnAGgAawHqgEDMC43uAEDyAEA-AEBqAIQwgIKECMYgAQYigUYJ8ICBRAAGIAEwgILEC4YgAQYxwEY0QPCAhAQABgBGIAEGIoFGAoYQxgqwgILEC4YrwEYxwEYgATCAgsQLhiABBjHARivAcICBxAjGOoCGCfCAhQQABiABBjjBBjpBBjqAhi0AtgBAcICBBAjGCfiAwQYACBBiAYBugYGCAEQARgB&sclient=gws-wiz-serp'
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
		#print("Сейчас разница евродоллар " + str(currency))
		message = ("Сейчас разница евродоллар " + str(currency))
		return message



# Создание объекта и вызов метода
currency = Currency()
currency.check_currency()
