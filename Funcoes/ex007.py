'''Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.'''

def valorPagamento(vPrest, dAtraso):
  """
  Função valorPagamento
  Calcula o valor da prestação acrescido de juros e multa, de acordo com os dias de atraso
  param1 = vPrest
  param2 = dAtraso
  Retorna o valor da prestação
  """
  jDia = vPrest*(0.1/100) #Calcula os juros diário
  vMulta = 3/100 #Multa de 3%
  tJuros = dAtraso * jDia #Calcula o total dos juros
  tMulta = vMulta * vPrest #Calcula o valor da multa
  if dAtraso == 0: #Se a prestação estiver no vencimento
    return vPrest #Retorna o valor da prestação
  else: #Se estiver vencida
    return vPrest + tJuros + tMulta #Retorna com multa e juros

#Função que imprime cabeçalho
def imprimeLinha(msg):
  tam=len(msg)+4
  print("-"*tam)
  print(f"  {msg}")
  print("-"*tam)


imprimeLinha("Cálculo de Prestações")
parcelas = []
vFinal = 0
vTotal = 0
while True:
  prestacao = float(input("Valor da prestação: (0=Fim) "))
  if prestacao == 0:
    break
  else:
    atraso = int(input("Atraso em dias: "))
    
    vFinal = valorPagamento(prestacao, atraso)
    parcelas.append(vFinal)
  vTotal += vFinal
print("-"*20)
for i in parcelas:
  print(f"Parcela recebida: {i:>11.2f}")
print("-"*20)
print(f"Valor total recebido: {vTotal:.2f}")
print("-"*20)
  