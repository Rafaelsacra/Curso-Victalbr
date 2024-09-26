def soma(a,b):
    return(a+b)
def multiplicar(a,b):
    return(a*b)
def subtrair(a,b):
    return(a-b)
def dividir(a,b):
    if b==0:
        return("Erro:Divisao por zero!")
    return(a/b)

def Menu():
    print('escolha uma opçao:')
    print("1=soma")
    print("2=subtrai")
    print("3=multiplica")
    print("4=divide")
    print("5=sair")

while True:
    Menu()
    opcao=input('digite uma opcao 1/2/3/4/5:  ')
    if opcao=="5":
        print('Até logo!')
        break
    if opcao in ['1','2','3','4']:
        try:
            num1=float(input('digite o primeiro numero'))
            num2=float(input('digite o segundo numero'))
        except:ValueError
        print('Digite numeros válidos')
        continue
    if opcao=='1':
        
