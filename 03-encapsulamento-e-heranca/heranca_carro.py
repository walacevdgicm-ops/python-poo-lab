class Carro(object):
    def fale_comigo(self):
        print("Sou um Carro")


class Fusca(Carro):
    def fale_com_um_fusca(self):
        print("Sou um Fusca")


x = Carro()
y = Fusca()

x.fale_comigo()
y.fale_com_um_fusca()