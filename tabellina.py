                       #tabellina del numero inserito
print('********* LE TABELLINE **********') 
scelta=-1
while(scelta !=0):
    print('===================')
    user =int(input("digita un numero: "))
    print('===================')
    print("tabellina:")
    for indice in range(20):
        print("{} per {} = {} ".format(user,(indice+1),(indice+1)*user))


