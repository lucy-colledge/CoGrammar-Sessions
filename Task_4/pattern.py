star="*"
x= int(1)
for i in range(0,10):
    print(star)
    x=x+1
    if x <= 5:
        star=star+"*"
    else:
        star=star[:-1]
