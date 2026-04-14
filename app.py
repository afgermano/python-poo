#importando a classe
#da(from) pasta modelos e no arquivo restaurante e classe restaurante
from modelos.restaurante import Restaurante

restaurante1 = Restaurante('Villa Gourmet', 'Comida Gourmet')
restaurante1.receber_avaliacao('Gui', 10)
restaurante1.receber_avaliacao('Lais', 20)

rastaurante2 = Restaurante('GoCoffee', 'Cafeteria')

def main():
    # mandando a classe restaurante listar todos os restaurantes cadastrados
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()