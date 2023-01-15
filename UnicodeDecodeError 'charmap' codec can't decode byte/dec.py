# pip install group-and-iter-everything
from group_and_iter_everything import groupby_decoding_result

with open("c:\\portugues.txt", mode="rb") as f:
    data = f.read()


resultados = groupby_decoding_result(
    bytes_=data,
    mode="strict",
    continue_on_exceptions=True,
    withindex=False,
    withvalue=True,
)