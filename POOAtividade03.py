class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    #   @x.setter
    def setX(self, x):
        self.__x = x

    #  @y.setter
    def setY(self, y):
        self.__y = y



    def Quadrante(self, x, y):
        if (x > 0 and y > 0):
            return 1
        if (x < 0 and y > 0):
            return 2
        if (y < 0 and x < 0):
            return 3
        if (y < 0 and x > 0):
            return 4
        if (y == 0 and x == 0):
            return O




# Quadrante = Retângulo
class Quad():
    def __init__(self, Ponto1, Ponto2):
        self.Ponto1 = Ponto1
        self.Ponto2 = Ponto2

    def contidoEmQuadrante(a):
        if (a.getX() <= a.Ponto2.getX()
                and a.getX() >= a.Ponto1.getX()
                and a.getY() <= a.Ponto1.getY()
                and a.getY() >= a.Ponto2.getY()):
            return True
        else:
            return False



