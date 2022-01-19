dia = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foi rodado? '))
diaPago = dia * 60
kmPago = km * 0.15
print('O custo pelo aluguel do carro é de R$ {:.2f} '.format(diaPago))
print('O custo por Km rodado é de R$ {:.2f} '.format(kmPago))
total = diaPago + kmPago
print('O valor total a se pagar é R$ {:.2f} '.format(total))
