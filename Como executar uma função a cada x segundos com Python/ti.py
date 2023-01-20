from threading import Timer
from time import time

def f(x,y):
    print(f'Rep: {x}')
    print(f'Hora: {time()}')
    print(f'Var: {y}')
    t = Timer(
        1, #intervalo
        f, #funcao
        args=(x+1,), # adicionar 1
        kwargs={
            'y': 'abobrinha'
        }

    )
    t.start()

f(x=0, y='bobao')