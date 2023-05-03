x = 10
y = 20
print(x, y)  # 10 20

z = x
x = y
y = z
print(x, y)  # 20 10
# OR
x, y = (y, x)
print(x, y)  # 10 20
