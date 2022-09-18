
y = [x for x in range(-7,7) ]
z = [ _ for _ in range(0,7,3)] + [ _*-1 for _ in range(0, 7, 3)][1:]
z.remove(0)
# y[0]
print(z, y)

