import numpy as np
import pandas as pd

def sonarcloud_test4zzy_bonus(t):  
    a = 5 if t % 2 == 0 else 10
    b = 10

    if a != b:
        print("True")
    else:
        print("Wrong")


t = 100
sonarcloud_test4zzy_bonus(t)
