#Faça um Programa que peça as 4 notas bimestrais e mostre a média

nota_1 = input('Digite a primeira nota: ')
nota_2 = input('Digite a segunda nota: ')
nota_3 = input('Digite a terceira nota: ')
nota_4 = input('Digite a quarta nota: ')

int_nota1 = int(nota_1)
int_nota2 = int(nota_2)
int_nota3 = int(nota_3)
int_nota4 = int(nota_4)

resultado_soma = int_nota1 + int_nota2 + int_nota3 + int_nota4
media = resultado_soma / 4

print('O resultado da media das 4 notas bimestrais é: ', media)