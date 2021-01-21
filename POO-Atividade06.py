import csv
import matplotlib.pyplot as plt

while True:
    op = input(' 1- Criar arquivo\n 2- Ler arquivo\n 3- Exibir gráfico\n 4- Sair do Programa\n Selecione uma opção:' )

    if op == '1':
        x = int(input('Digite o número de profissões: '))
        y = open('tabela.csv', 'w')
        try:
            writer = csv.writer(y)
            writer.writerow(('ocupaçao', 'salario'))
            for c in range(0, x):
                ocup = input('escreva uma ocupação: ')
                sal = float(input('digite o salário desta ocupação: '))
                writer.writerow((ocup, sal))
        finally:
            y.close()

    elif op == '2':
        print('\n')
        try:
            print(open('Tabela.csv', 'r').read())
        except:
            print('NÃO FOI POSSÍVEL ENCOTRAR O ARQUIVO!')

    elif op == '3':
        try:
            ocup = []
            sal = []
            y = open('tabela.csv', 'r')
            r = csv.DictReader(y)
            for z in r:
                ocup.append(z['profissao'])
                sal.append(float(z['salario']))
            try:
                plt.figure(figsize=(6, 6))
                plt.plot(ocup, sal)
                plt.show()
                plt.bar(ocup, sal)
                plt.show()
                fig1, x1 = plt.subplots(figsize=(6, 6))
                x1.pie(sal, labels=ocup, autopct='%1.1f%%', shadow=True, startangle=90)
                x1.axis('equal')
                plt.show()
            finally:
                y.close()

        except:
            print('NÃO FOI POSSÍVEL ENCOTRAR O ARQUIVO!')

    elif op == '4':
        break