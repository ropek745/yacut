# Проект Yacut

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

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