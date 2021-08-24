# О проекте
Telegram-бот, работающий с API Яндекс.Практикум, для отслеживания статуса code-review.

## Стек технологий
* Python 3.9.1
* Git
## Установка проекта
Установить актуальную версию Python3 с официального сайта, если он не установлен:
https://www.python.org

Выполните команду:
```python
git clone https://github.com/ildarick93/Telegram_Bot_API
```
Перейдите в репозиторий:
```python
cd Telegram_Bot_API
```
В корневой папке проекта создайте виртуальную среду python:
```python
python -m venv venv
```
Активируйте виртуальную среду командой:
Windows:
```python
venv\Scripts\activate.bat
```
Linux или macOS:
```python
source venv/bin/activate
```
Установите необходимые зависимости с помощью pip:
```python
pip install -r requirements.txt
```
При необходимости обновления зависимостей используйте команду:
```python
python -m pip install —upgrade pip
```
Получение токенов:
* API Яндекс.Практикум:

https://oauth.yandex.ru/authorize?response_type=token&client_id=1d0b9dd4d652455a9eb710d450ff456a
* Telegram
  * Открываем телеграмм с аккаунта, к которому будет привязан бот
  * В строке поиска сверху вводим botfather и переходим в появившейся чат-бот (@BotFather)
  * Нажать кнопку: START (Если вы ранее уже создавали ботов — перейдите к следующему пункту)
  * Написать боту: /newbot
  * Далее нужно придумать и ввести ник бота, что бы он заканчивался нa слово bot
  * Скопируйте полученный API KEY

Примечание
Секретные данные необходимо добавить в файл .env
```python
PRAKTIKUM_TOKEN = type_here
TELEGRAM_TOKEN = type_here
CHAT_ID = type_chat_id_here
```
