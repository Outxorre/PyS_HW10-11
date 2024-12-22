import cv2
import requests
import numpy as np

url = "https://example.com/image.jpg"
response = requests.get(url)
image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
eyes = eye_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=10)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

for (x, y, w, h) in eyes:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Detected Patterns", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Я честно говоря щас в окно полечу, пусть и живу в частном доме
#Этот код который держится на божьей сопле написан самым криворуким способом, потом проверенным через чатгпт
#А всё потому, ЧТО МОЙ PyCharm НЕ ХОЧЕТ принимать существования пайтона в этом грешном мире, и просто
#ОТКАЗЫВАЕТСЯ запускать любой код. Та домашка сработала, которая с БД, НО ЭТО, это что то на уровне выше понимания человечества
#Думаю пофиксить эту чеченскую преграду можно одним способом, запустить микрофиксиков прям к транзисторам, пусть фиксят.
#Вкратце - не установились либы и не запустилась прога из за ошибки отсутсивия tempfile, А потом жалоба на либу за либой... и так, ничего на компе нету теперь.
#Переустановка, установка разных версий пайтона, создание папок, смена интерпритатора
#ничего не помогло этой квадратоплющеннойшмырогрызоплюхокошмаренной (только что придумал) тарантайке, ничего не помогло запустить пайтон на этом ПК
