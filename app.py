#LOJA ONLINE - SISTEMA DE DESCONTOS PROGRESSIVOS
#AUTOR: HENRIQUE MITUSAKI

#Entrada
valor_compra =float(input("Digite o valor total da sua compra: R$ "))
desconto_5 =float(valor_compra * 0.05)
desconto_10 =float(valor_compra * 0.1)
desconto_15 =float(valor_compra * 0.15)

#processamento

#Desconto 1 = 5%
if valor_compra <200:
    desconto_5
    valor_final_5= valor_compra-desconto_5
    print("Você recebeu um desconto de 5%")
    print(f"O valor total a pagar é de: R${valor_final_5:.2f}")

#Desconto 2 = 10%
elif valor_compra >=200 and valor_compra <300:
    desconto_10
    valor_final_10= valor_compra-desconto_10
    print("Você recebeu um desconto de 10%")
    print(f"O valor total a pagar é de: R${valor_final_10:.2f}")

#Desconto 3 = 15%
elif valor_compra >= 300:
    desconto_15
    valor_final_15= valor_compra-desconto_15
    print("Você recebeu um desconto de 15%")
    print(f"O valor total a pagar é de: R${valor_final_15:.2f}")
