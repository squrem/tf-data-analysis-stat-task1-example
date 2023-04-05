import pandas as pd
import numpy as np

# task 1
chat_id = 434559054 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    N = 587
    y = np.log(x - N) 
    mu = y.mean()
    s = y.std(ddof=1)
    return mu - 0.5 * np.log(np.exp(s**2 /len(x) - 2 * mu) + 1)
    
