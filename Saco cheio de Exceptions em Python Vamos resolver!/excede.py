from functools import wraps

def ignore_ex(f=None, value=None):
    def dec(func):
        @wraps(func)
        def wrapper(*args,
                    **kwargs):
            try:
                return func(*args,
                        **kwargs)
            except Exception:
                return value
        return wrapper
    return (dec(f) if callable(f)
            else dec)

@ignore_ex(value='não me enche')
def baba(x):
    return 5 / x


for no in [1, 2, 3, 0,
           1, 0, 3, 1, 0]:
    print(baba(no))













