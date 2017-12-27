# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import datetime
import requests


def get_html(url):  # получаем объект soup по переданной ссылке
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    return soup


def li_processing(li):  # получаем и сохраняем изображение из переданного <li>
    month_now = str((datetime.date.today()).strftime("%b"))  # текущий месяц
    day_now = (str((datetime.date.today()).strftime("%d"))).lstrip("0")  # отрезаем ведущий ноль, как у Google
    year_now = str((datetime.date.today()).strftime("%Y"))  # текущий год
    date_str = month_now + " " + day_now + ", " + year_now  # преобразуем текущую дату к формату Google
    doodle_date = str((li.find('input', class_='tag')).get('value'))  # получаем дату дудла
    if doodle_date == date_str:  # если дата дудла равна текущей
        doodle_img = li.find('img')  # находим тег img
        src = str(doodle_img.get('src')).lstrip('/')  # получаем ссылку на изображение вырезаем начальные слеши
        img_link = 'https://' + src  # добавляем https и окончательную ссылку на изображение
        doodle_link = str((li.find('input', class_='name')).get('value'))
        doodle_link = 'https://www.google.com/doodles/' + doodle_link
        file_format = src.split('.')[-1]
        doodle_arr = [img_link, doodle_link, file_format]
        return doodle_arr


def get_doodles_img():  # получаем из объекта soup теги <li>, содержащие изображения с
    doodles_array = []  # массив дудлов
    url_all_doodles = 'https://www.google.com/doodles?hl=en'  # страница с дудлами
    doods_soup = get_html(url_all_doodles)  # парсим страницу

    first_li = doods_soup.find('li', class_='latest-doodle on')  # последний по времени дудл, который отображается первым
    latest_doodle = li_processing(first_li)  # вытаскиваем массив со ссылкой на изо, названием и ссылкой на страницу
    if latest_doodle is not None:  # если он не пустой - тогда добавляем его к массиву всех дудлов
        doodles_array = [latest_doodle]  # создаем список путей к файлам

    another_latest_li = doods_soup.find_all('li', class_="latest-doodle ")  # массив с остальными дудлами
    for i in another_latest_li:  # проходим по массиву
        another_doodle = li_processing(i)  # обрабатываем li
        if another_doodle is not None:  # если не пустой, т.е. дата дудла - сегодня
            doodles_array.append(another_doodle)  # то добавляем к возвращаемому массиву

    if doodles_array:
        return doodles_array
    else:  # если никаких дудлов не найдено
        return None
