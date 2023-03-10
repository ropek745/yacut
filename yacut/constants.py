import re
from string import ascii_letters, digits


SYMBOLS = ascii_letters + digits
PATTERN_FOR_SHORT = fr"^[{re.escape(SYMBOLS)}]*$"
ITERATION_COUNT = 10
LENGTH_SHORT_ID = 6
LENGTH_CUSTOM_ID = 16
ORIGINAL_LINK_LEN = 2048