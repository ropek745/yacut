# Проект Yacut

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

Ключевые возможности сервиса:

 - генерация коротких ссылок и связь их с исходными длинными ссылками
 - переадресация на исходный адрес при обращении к коротким ссылкам
 
Пользовательский интерфейс сервиса — одна страница с формой. Эта форма состоит из двух полей:

 - обязательного для длинной исходной ссылки
 - необязательного для пользовательского варианта короткой ссылки (не должен превышать 16 символов)
 
Если пользователь предложит вариант короткой ссылки, который уже занят, то появляется соответствующее уведомление. Существующая в базе данных ссылка должна остаться неизменной.

Если пользователь не заполнит поле со своим вариантом короткой ссылки, то сервис должен сгенерировать её автоматически. Формат для ссылки по умолчанию — шесть случайных символов, в качестве которых можно использовать:

большие латинские буквы,
маленькие латинские буквы,
цифры в диапазоне от 0 до 9.
Автоматически сгенерированная короткая ссылка добавляется в базу данных, но только если в ней уже нет такого же идентификатора. В противном случае идентификатор генерируется заново.

## Технологии:
* Python 3.10
* Flask 2.0.2
* SQLAlchemy 1.4.29

## Порядок запуска:
1. Клонировать репозиторий и перейти в него в командной строке:

      ```
      git clone git@github.com:ropek745/yacut.git
      ```
      
      ```
      cd yacut
      ```

2. Cоздать и активировать виртуальное окружение:

    ```
    python3 -m venv venv
    ```

  * Если у вас Linux/macOS
  
      ```
      source venv/bin/activate
      ```

  * Если у вас Windows

      ```
      source venv/scripts/activate
      ```

3. Установить зависимости из файла requirements.txt:

    ```
    python3 -m pip install --upgrade pip
    ```
    
    ```
    pip install -r requirements.txt
    ```

4. Создать файл ```.env``` в корне проекта и установить параметры
   ```
    FLASK_APP=yacut
    FLASK_ENV=production
    DATABASE_URI=sqlite:///db.sqlite3
    SECRET_KEY=YOUR_SECRET_KEY
   ```
5. Запустить проект
    ```
   flask run
   ```
    Проект будет доступен по адресу http://localhost/

## Разработчик - [Роман Пекарев](https://github.com/ropek745) ##
