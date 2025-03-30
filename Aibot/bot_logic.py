import random
import os
from datetime import datetime

def gen_pass(pass_length):
    """Генерирует случайный пароль заданной длины."""
    elements = "+-/*!&$#?=@<>123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return "".join(random.choices(elements, k=pass_length))

def gen_emodji():
    """Возвращает случайный эмодзи."""
    emodji = ["😀", "🙂", "😂", "🤣", "😍", "😎", "🤩", "🤔", "🤯"]
    return random.choice(emodji)

def flip_coin():
    """Подбрасывает монетку (орел/решка)."""
    return random.choice(["ОРЕЛ", "РЕШКА"])