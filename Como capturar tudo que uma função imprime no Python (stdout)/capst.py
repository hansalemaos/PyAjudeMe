import sys
from functools import wraps
from io import StringIO

def pcap(f=None, active=True):
    def _d(fu):
        @wraps(fu)
        def wrapper(*args,
                    **kwargs):
            if not active:
                return (
                    fu(*args,**kwargs)
                )
            stdout=sys.stdout
            sys.stdout=file= StringIO()
            try:
                vala = fu(*args, **kwargs)
            finally:
                sys.stdout = stdout
            rea = file.getvalue()
            return vala,rea
        return wrapper
    return (_d(f) if callable(f)
            else _d)

@pcap(active=False)
def test(x):
    print('Let me see' )
    result = x*x
    print(f'Result: {result}')
    return result

b=(test(20))
print(f'{b=}')
