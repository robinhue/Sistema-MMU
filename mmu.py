class MMU:
    
    # Método init que cria o dicionário tabela de partição e o seu endereco correspondente.
    def __init__(self):
        self.tabela_particao = {}
        self.particao_atual = 0

    # Método que adiciona uma nova partição à tabela de partições, recebendo os limites e a base da partição
    # e indexando na tabela de acordo com o valor da partição atual, além de encrementar o valor da partição atual
    def adicionar_particao(self, limite, base):
        self.tabela_particao[self.particao_atual] = {'limite': limite, 'base': base}
        self.particao_atual += 1
        
    # Método que este método converte um endereço lógico em um endereço físico,
    # recebendo o inteiro representado pela partição e o endereço a ser convertido.
    # Se a conversão não for possível, o método lança uma exceção.
    def converter_logico_fisico(self, particao, endereco):
        if particao not in self.tabela_particao:
            raise Exception('Partição inválida')
        if endereco > self.tabela_particao[particao]['limite']:
            raise Exception('Endereço inválido')
        return self.tabela_particao[particao]['base'] + endereco

# Arquivo Main
mmu = MMU()
mmu.adicionar_particao(100, 50) # Usando o método adicionar_particao foi estabelecido o limite de 100 e o numero base a ser convertido de 50.
mmu.adicionar_particao(200, 150) # Usando o método adicionar_particao foi estabelecido o limite de 200 e o numero base a ser convertido de 150.
print(mmu.tabela_particao)


try: # Código try que vai tentar rodar o código.
    print(mmu.converter_logico_fisico(0, 60)) # Já que o endereço(60) é menor que o limite(100) a saída do código será 110.
    print(mmu.converter_logico_fisico(1, 60)) # Já que o endereço(60) é menor que o limite(200) a saída do código será 210.
    print(mmu.converter_logico_fisico(2, 40)) # Já que essa partição não é existente isso vai trazer uma exceção.
except Exception as e: 
    print(e) # Um print para mostrar caso haja algun erro.