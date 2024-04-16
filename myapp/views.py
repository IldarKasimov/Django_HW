from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

html_main = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Главная</title>
</head>
<body>
<header>
    <h1>Мой первый Django-сайт</h1>
</header>
<div>
    <ul>
        <li class="nav-item"><a href="/" class="nav-link">Главная</a></li>
        <li class="nav-item"><a href="/about_me/" class="nav-link">Обо мне</a></li>
    </ul>
    <h2> Привет! Это мой первый проект!</h2>
    <div>
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVxWdfrABjlR-f23BLU7GrbSNXg8emB3b334UwR9cmuA&s" 
        alt="Main foto">
    </div>
</body>
</html>
"""

html_me = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Обо мне</title>
</head>
<body>
<header>
    <h1>Обо мне:</h1>
</header>
<div>
    <ul>
        <li class="nav-item"><a href="/" class="nav-link">Главная</a></li>
        <li class="nav-item"><a href="/about_me/" class="nav-link">Обо мне</a></li>
    </ul>
    <h3> 
        Привет! Меня зовут Ильдар.</br>
        Мне 35 лет.</br>
        Живу в городе Магнитогорске!
    </h3>
    <div>
        <img src="https://sun9-27.userapi.com/impg/M49j6GkpQ0L8SMR1RWKygOusc5ln2CuSiqnYXA/5Y5X6O3Mwlw.jpg?size=755x935&quality=95&sign=c23571bc2866d1a1098e47e18c790fb5&c_uniq_tag=U-492yUVs2zO6xhpd6IGrWI0JsX8TLcne9uSECyJBjw&type=album" alt="Main foto">
    </div>
</body>
</html>
"""


def main(request):
    logger.info('Посетили главную страницу')
    return HttpResponse(html_main)


def about_me(request):
    logger.info('Посетили страницу обо мне')
    return HttpResponse(html_me)
