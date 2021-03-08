de  atividade3  import Quadrilatero

class Teste(Quadrilatero):

    def __init__(self, x, y, p1x, p1y, p2x, p2y):

        super().__init__(x, y, p1x, p1y, p2x, p2y)

    def mostra(self):

        print('\nPonto: ({}, {})'.format(self.getX(), self.getY()))

        print('Quadrante: {}'.format(self.qualQuadrante()))

        if self.p1x < self.p2x and self.p1y > self.p2y:

            print('\nP1: {}'.format(self.p1))

            print('P2: {}'.format(self.p2))

        else:

            print('Quadrilatero error')

        print(self.contidoEmQ())

if __name__ == '__main__':

    x = input('X: ')

    y = input('Y: ')

    p1x = input('P1x: ')

    p1y = input('P1y: ')

    p2x = input('P2x: ')

    p2y = input('P2y: ')

    x = Teste(x, y, p1x, p1y, p2x, p2y)

    x.mostra()
