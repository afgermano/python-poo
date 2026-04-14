from modelos.avaliacao import Avaliacao

class Restaurante:
    """
    Representa um restaurante e suas características
    """
    restaurantes = []

    """ 
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
    """

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    """
        Retorna uma string com as informações dos restaurantes
    """
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """
            Exibe uma lista formatada de todos os restaurantes.
        """
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self):
        """Informa a situação do restaurante"""
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        """Muda o status do restaurante"""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante
         - Informa o nome do cliente 
         - Restringe a nota de 0 a 10
        """
        if 0 < nota <=10:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
            return
            

    @property
    def media_avaliacoes(self):
        """
            Calcula e retorna a média das avaliações do restaurante.
            Em caso de não existir aváliações, o sistema exibe um aviso    
        """
        if not self._avaliacao:
            return "Nenhuma avaliação"
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        #metodo round que aredonda sempre a nota
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media