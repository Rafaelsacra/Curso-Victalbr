def adicionar():
    item=input("Adcione um item")
    with open("lista_compras.txt","a") as arquivo:
        arquivo.write(f"{item}\n")

def Exibir():
     with open("lista_compras.txt","r") as arquivo:
        arquivo.read()
    

def Menu():
    print('escolha uma opçao:')
    print("1=Adcionar um item")
    print("2=Exibir lista")
    print("3=Sair")
    
while True:
    Menu()
    opcao=input('digite uma opcao 1/2/3:  ')

    if opcao=="3":
        print('Até logo!')
        break

    if opcao in ('1','2','3'):
        
        if opcao=='1':
            adicionar()
        if opcao=='2':
            Exibir()
        else:
            print("Opção invalida")
        

