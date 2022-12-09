serie = [2]
out = 0
for i in range(1, 10+1):
    serie.append(serie[-1] * i)
    out = serie[-1]
    print(str(i)+" * " + str(serie[-2]) + " = "+str(out))
print("##############")
print(serie)
