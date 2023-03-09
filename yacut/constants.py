import re
from string import ascii_letters, digits


SYMBOLS = ascii_letters + digits
REGEX = fr"^[{re.escape(SYMBOLS)}]*$"
ITERATION_COUNT = 10

INVALID_SYMBOLS = 'Присутствуют недопустимые символы'
NOT_UNIQUE_ID = 'Имя {custom_id} уже занято!'
INVALID_NAME = 'Указано недопустимое имя для короткой ссылки'
URL_REQUIRED = '"url" является обязательным полем!'
NO_BODY = 'Отсутствует тело запроса'
NAME_ALREADY_TAKEN = 'Имя "{custom_id}" уже занято.'
NO_ID = 'Указанный id не найден'

LENGTH_SHORT_ID = 6
LENGTH_CUSTOM_ID = 16

ORIGINAL_LINK_DESC = 'Ссылка для укорачивания'
ORIGINAL_LINK_LEN = 2048
DATA_REQUIRED = 'Обязательное поле!'
CUSTOM_ID_DESC = 'Введите свою ссылку (опционально)'
URL_MESSAGE = 'Должна быть ссылка!'
BUTTON_DESC = 'Укоротить'