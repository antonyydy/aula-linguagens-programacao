
# uso de if, elif e else 

idade = int(input())

if idade >= 0 and idade <= 12:
    print("kid")
elif idade >= 13 and idade <= 18:
    print("teen")
elif idade >= 19 and idade <= 60:
    print("adult")
else: 
    print("elderly")