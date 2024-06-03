import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageDraw, ImageFont

# Пример работы c "requests"
'''выводит на консоль список моих репозиториев на гитхаб'''

url = 'https://api.github.com/users/ChetinSergey/repos'
headers = {'Authorization': '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'}
response = requests.get(url, headers=headers)
repos = json.loads(response.content)

for repo in repos:
    print(repo['full_name'])


# Пример работы c "pandas"
''' Создание таблиц'''
df = pd.DataFrame(["точка_1", "точка_2", "точка_3"],
                  columns=['Name'],
                  index=["A", "B", "C"])
print(df)
''' Изменение столбцов и индексов'''
df.rename(columns={"Name": "Координаты"},
          index={"A": "x", "B": "y", "C": "z"}, inplace=True)
print(df)
print(f'{"":=^30}')

''' Создание таблиц при помощи словарей, где его ключи - это имена колонок'''
h_col = pd.Categorical(["Блондин", "Брюнет", "Рыжий"])
df1 = pd.DataFrame({"Name": ["Сергей", "Михаил", "Антон"],
                    "Age": [35, 33, 22],
                    "Hair_color": h_col},
                   index=[1, 2, 3])
print(df1)


# Пример работы с "Numpy" и "matplotlib" для отрисовки параболы:
'''задаём размер графика в дюймах'''
plt.figure(figsize=(8, 6))

'''задаём интервал, например, от -5 до 5 и сформируем на нем 5000 точек - это будут наши координаты по оси x'''
x = np.linspace(-5, 5, 5000)

'''по оси y откладываем квадрат этих точек'''
y = x ** 2

'''создаём сетку'''
plt.grid()

'''выводим кривую и подписи на графике'''
plt.plot(x, y)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)

'''результ ---> парабола'''
plt.show()

# Пример работы "pillow"
"""открываем картинку, применяем фильтр, добавляем текст на картинку"""

img = Image.open('Sprite.jpg')           # Открытие изображение
print(img.size)                          # Размер изображения
img = img.resize(size=(600, 600))        # Изменение размера изображения
img = img.rotate(-30)                     # Поворот по часовой стрелке на 30 градусов
img = img.filter(ImageFilter.GaussianBlur(radius=2))  # Применение фильтра размытия картинки
draw = ImageDraw.Draw(img)                            # Пишем на изображении что-либо...
font = ImageFont.truetype('arial.ttf', 48)
text = 'Hello, how are you?'
draw.text((100, 350), text=text, fill=(0, 0, 0), font=font)

img.show()
img.save('/Users/user/PycharmProjects/l7pakTuka/ChetinSergey/Classes_Urban/Modules_10-15/Sprite_new.png')

