import warnings
_w=lambda *args,**kwargs:''

(
    warnings.warn,
    warnings.warn_explicit,
    warnings.showwarning
) = (
    [_w] * 3
)

import bs4

html='''
<span class="pl-s">''</span>
'''
soup = bs4.BeautifulSoup(html)
