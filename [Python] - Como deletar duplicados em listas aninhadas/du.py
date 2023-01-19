
l2 = [[1, 2], [1, 2], 7,
      [3, 8], [3, 8]]

result = list(

      i[1] for i in
      {f'{k}{repr(k)}':k
      for k in l2}.items()

)
print(result)
