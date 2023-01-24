l = ["hallo", "12hal33", "42ha004", "4204h213", "hall000", "cvwsA"]

sort_len = (
lambda v: (
     sorted(v,
     key=lambda x:len(x))
))
for _ in reversed(sort_len(l)):
     print(_)
	 