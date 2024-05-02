from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def main(request):
    html_main = """
    <title>Обо мне</title>
    <h1>Мой первый Django-сайт</h1>
    <ul>
        <li class="nav-item"><a href="/about/" class="nav-link">Обо мне</a></li>
        <li class="nav-item"><a href="/less2/" class="nav-link">Домашняя работа №2</a></li>
        <li class="nav-item"><a href="/less3/" class="nav-link">Домашняя работа №3</a></li>
        <li class="nav-item"><a href="/less4/" class="nav-link">Домашняя работа №4</a></li>
        <li class="nav-item"><a href="/admin/" class="nav-link">Админка / Домашняя работа №5</a></li>
    </ul>
    <h2> Привет! Это мой первый проект!</h2>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVxWdfrABjlR-f23BLU7GrbSNXg8emB3b334UwR9cmuA&s" 
    alt="Main foto">
    """
    logger.info('Постелили главную страницу')
    return HttpResponse(html_main)


def about_me(request):
    html_me = """
    <title>Обо мне</title>
    <h1>Обо мне:</h1>
    <ul>
        <li class="nav-item"><a href="/" class="nav-link">Главная</a></li>
    </ul>
    <h3> 
        Привет! Меня зовут Ильдар.</br>
        Мне 35 лет.</br>
        Живу в городе Магнитогорске!
    </h3>
    <div>
        <img src="https://sun9-27.userapi.com/impg/M49j6GkpQ0L8SMR1RWKygOusc5ln2CuSiqnYXA/5Y5X6O3Mwlw.jpg?size=755x935&quality=95&sign=c23571bc2866d1a1098e47e18c790fb5&c_uniq_tag=U-492yUVs2zO6xhpd6IGrWI0JsX8TLcne9uSECyJBjw&type=album" alt="Main foto">
    </div>
    """
    logger.info('Посетили страницу обо мне')
    return HttpResponse(html_me)
