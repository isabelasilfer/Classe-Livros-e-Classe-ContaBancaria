class Livro:
    def __init__(self, titulo, autor, numero_paginas):  # corrigido __init__
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.pagina_actual = 0

    def abrir_livro(self):
        self.pagina_actual = 1
        print(f"Livro '{self.titulo}' aberto na página {self.pagina_actual}.")

    def ler_paginas(self, quantidade):
        if self.pagina_actual == 0:
            print("Abra o livro primeiro!")
        else:
            self.pagina_actual += quantidade
            if self.pagina_actual > self.numero_paginas:
                self.pagina_actual = self.numero_paginas
            print(f"Você leu mais {quantidade} páginas.")

    def exibir_progresso(self):
        lidas = self.pagina_actual
        faltam = self.numero_paginas - self.pagina_actual
        print(f"Páginas lidas: {lidas}")
        print(f"Páginas faltando: {faltam}")


livro1 = Livro("Jogos Vorazes", "Suzanne Collins", 397)
livro1.abrir_livro()
livro1.ler_paginas(60)
livro1.exibir_progresso()
