import requests
import time
import json
import datetime
weather_config = "f95fcd713a9214b4acf02420ff552db4"
city = "Astana"

while True:
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_config}&units=metric"
        )
        data = r.json()
        cityN = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        humid = data["main"]["humidity"]
        currentT = datetime.datetime.now()

        print(f"{cityN} \n {cur_weather}\n{humid}\n{currentT}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    time.sleep(1800)

#Ну, я тут слегка по другому сделал, но по сути одно и тоже.
#Просто вместо того что бы создать файл json, я обращаюсь к достоверным данным через API ключ
#Файл я не создаю, но в любом случае работаю с его массивами и с самим файлом.
#Пара отличий -
#я обращаюсь к интернет базе, в которой инфы больше и лучше
#всё так же работаю с json БД, просто уже созданной.
#как указано - повторяется каждые 30 минут для обновления данных