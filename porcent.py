x=float(input(""))
p=float(input(""))

porc = x*p/100
acr = x+porc
des =  x-porc

acrescimo = round(acr, 2)
desconto = round(des, 2)

print(acrescimo)
print(desconto)
