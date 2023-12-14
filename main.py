from tkinter import *
from tkcalendar import Calendar
import datetime
import random
import csv

root = Tk()

root.geometry("400x500")
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day

cal = Calendar(root, selectmode='day',
               year=year, month=month,
               day=day)

cal.pack(pady=20)


# def last_day_of_month(year, month):
#     return calendar.monthrange(year, month)[1]


def get_tasty_treat(day, month, year):
    tasty_treats_4 = ['подорожник (2-3 ЛИСТИКА)', 'листья подорожника (2-3 ЛИСТИКА)', 'листья липы (1-2 ЛИСТИКА)', 'цветок календулы', 'геркулес (1Ч.Л.)', 'рис (10 ЗЕРЕН)', 'гречка (10 ЗЕРЕН)', 'листья березы (1-3 ЛИСТИКА)']
    tasty_treats_8 = ['клубника', 'морковь (1-2 ЛОМТИКА)', 'барбарис (1 ЯГОДА)', 'малина (1-2 ШТ)']
    tasty_treats_10 = ['каркаде']
    tasty_treats_12 = ['листья ивы', 'листья одуванчика (3-5 ЛИСТИКОВ)', 'яблоко (1 ДОЛЬКА)']
    tasty_treats_15 = ['листья крапивы (1/2 Ч.Л.)', 'листья малины (1-3 ЛИСТИКА)', 'корень одуванчика', 'топинамбур', 'шиповник (2-3 ШТ)', 'боярышник (2-3 ШТ)', 'роза (1 БУТОН)']
    tasty_treats_31 = ['листья яблони (1-3 ЛИСТИКА)']
    result = []
    result.append(tasty_treats_31[0])
    if day % 2 == 0:
        result.append(random.choice(tasty_treats_15))
    if datetime.datetime(year, month, day).weekday() in [1, 3, 5]:
        result.append(random.choice(tasty_treats_12))
    if day % 10 == 0:
        result.append(tasty_treats_10[0])
    if datetime.datetime(year, month, day).weekday() in [2, 4]:
        result.append(random.choice(tasty_treats_8))
    if datetime.datetime(year, month, day).weekday() in [6]:
        result.append(random.choice(tasty_treats_4))
    return ', '.join(['\n' + i for i in result])


def grad_date():
    selected_date = cal.get_date()
    day_only = datetime.datetime.strptime(selected_date, '%m/%d/%y')
    day = int(day_only.strftime('%d'))
    year = int(day_only.strftime('%y'))
    month = int(day_only.strftime('%m'))
    date.config(text='Вкусняшки на сегодня: ' + '\n\n' + get_tasty_treat(day, month, year))


Button(root, text="Вкусняшки на сегодня",
       command=grad_date).pack(pady=20)

dates = [['' for i in range(7)] for _ in range(5)]


def add_to_file():
    selected_date = cal.get_date()
    day_only = datetime.datetime.strptime(selected_date, '%m/%d/%y')
    day = int(day_only.strftime('%d'))
    year = int('20' + day_only.strftime('%y'))
    month = int(day_only.strftime('%m'))
    start_date = datetime.datetime(year, month, 1)
    str_start_date = datetime.datetime.strftime(start_date, '%Y-%m-%d')
    start_week = datetime.datetime.strptime(str_start_date, '%Y-%m-%d')
    week_num = start_week.date().isocalendar()[1]
    if day_only.date().isocalendar()[1] == week_num:
        dates[0][datetime.datetime(year, month, day).weekday()] = get_tasty_treat(day, month, year).replace('\n', '')
    if day_only.date().isocalendar()[1] == week_num + 1:
        dates[1][datetime.datetime(year, month, day).weekday()] = get_tasty_treat(day, month, year).replace('\n', '')
    if day_only.date().isocalendar()[1] == week_num + 2:
        dates[2][datetime.datetime(year, month, day).weekday()] = get_tasty_treat(day, month, year).replace('\n', '')
    if day_only.date().isocalendar()[1] == week_num + 3:
        dates[3][datetime.datetime(year, month, day).weekday()] = get_tasty_treat(day, month, year).replace('\n', '')
    if day_only.date().isocalendar()[1] == week_num + 4:
        dates[4][datetime.datetime(year, month, day).weekday()] = get_tasty_treat(day, month, year).replace('\n', '')
    with open('tasty_treats.csv', 'w', encoding='utf-8-sig', newline='') as file:
        selected_date = cal.get_date()
        day_only = datetime.datetime.strptime(selected_date, '%m/%d/%y')
        year = int(day_only.strftime('%Y'))
        month = day_only.strftime('%B')
        writer = csv.writer(file, delimiter=';')
        writer.writerow([month + ' ' + str(year)])
        writer.writerow(['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'])
        for row in dates:
            writer.writerow(row)


Button(root, text="Добавить в файл", command=add_to_file).pack(pady=10)


date = Label(root, text="")
date.pack(pady=20)

root.mainloop()