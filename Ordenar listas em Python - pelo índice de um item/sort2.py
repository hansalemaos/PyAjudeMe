l = ["hallo",
     "12hal33",
     "42ha004942r",
     "4204h213",
     "hall000",
     "h",
     "cvwsA"]

sort_by_letter_pos = (
     lambda v,pos:
     (sorted(v,key=lambda x:x[pos]
     if len(x) > pos else ''))
)
for _ in reversed(
     sort_by_letter_pos(l,0)):
     print(_)	