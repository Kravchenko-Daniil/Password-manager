from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from enum import Enum


class Characters(Enum):
    btn_lower = ascii_lowercase
    btn_upper = ascii_uppercase
    btn_numbers = digits
    btn_special = punctuation


GENERATE_PASSWORD = (
    'btn_refresh', 'btn_lower', 'btn_upper', 'btn_numbers', 'btn_special'
)
