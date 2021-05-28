src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

print([x for v, x in zip(src, src[1:]) if v < x], end=' ')
