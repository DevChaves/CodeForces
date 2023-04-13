#A fórmula para calcular a área de uma circunferência é: area = π × raio2 Considerando para este problema que π = 3.14159:

#- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

#Input
#A entrada contém um valor de ponto flutuante de precisão dupla.

#Output
#Apresentar a mensagem "A=" seguido pelo valor calculado da área, conforme exemplo, com 4 casas após o ponto decimal
#Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

π = 3.14159
raio = float(input())
area = π * raio**2
print("A={:.4f}".format(area))