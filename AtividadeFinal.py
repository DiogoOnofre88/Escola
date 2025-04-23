class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - {self.preco:.2f}€"

class Cliente:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        return f"Cliente: {self.nome}, Saldo: {self.saldo:.2f}€"

class Loja:
    def __init__(self, cliente):
        self.produtos = []
        self.carrinho = {}
        self.cliente = cliente

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        if not self.produtos:
            print("Não há produtos disponíveis.")
        else:
            print("\n--- Produtos Disponíveis ---")
            contador = 1
            for produto in self.produtos:
                print(f"[{contador}] {produto}")
                contador += 1

    def adicionar_ao_carrinho(self):
        self.listar_produtos()
        try:
            escolha = int(input("\nDigite o número do produto que deseja adicionar ao carrinho: "))
            if 1 <= escolha <= len(self.produtos):
                produto_escolhido = self.produtos[escolha - 1]
                quantidade = int(input(f"Quantas unidades de '{produto_escolhido.nome}' deseja adicionar? "))
                if quantidade <= 0:
                    print("A quantidade deve ser maior que 0.")
                    return
                if produto_escolhido in self.carrinho:
                    self.carrinho[produto_escolhido] += quantidade
                else:
                    self.carrinho[produto_escolhido] = quantidade
                print(f"{quantidade} unidade(s) de '{produto_escolhido.nome}' adicionadas ao carrinho.")
            else:
                print("Produto inválido.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

    def calcular_total(self):
        return sum(produto.preco * qtd for produto, qtd in self.carrinho.items())

    def ver_carrinho(self):
        if not self.carrinho:
            print("\nO carrinho está vazio.")
            return

        print("\n--- Carrinho de Compras ---")
        total = 0
        for produto, quantidade in self.carrinho.items():
            subtotal = produto.preco * quantidade
            print(f"{produto.nome} x {quantidade} = {subtotal:.2f}€")
            total += subtotal
        print(f"\nTotal: {total:.2f}€")

    def simular_pagamento(self):
        if not self.carrinho:
            print("Carrinho vazio. Não é possível finalizar a compra.")
            return

        total = self.calcular_total()
        self.ver_carrinho()

        print(f"\nSaldo disponível: {self.cliente.saldo:.2f}€")
        if self.cliente.saldo >= total:
            self.cliente.saldo -= total
            print(f"Pagamento realizado com sucesso! Novo saldo: {self.cliente.saldo:.2f}€")
            self.carrinho.clear()
        else:
            faltando = total - self.cliente.saldo
            print(f"Saldo insuficiente. Faltam {faltando:.2f}€.")

def menu():
    print("\n--- Menu da Loja ---")
    print("[1] Ver produtos disponíveis")
    print("[2] Adicionar produto ao carrinho")
    print("[3] Ver carrinho de compras")
    print("[4] Finalizar compra")
    print("[0] Sair")

cliente = Cliente("Diogo", 100.00)

loja = Loja(cliente)
loja.adicionar_produto(Produto("T-shirt", 15.90))
loja.adicionar_produto(Produto("Calças", 49.90))
loja.adicionar_produto(Produto("Tênis", 89.90))

while True:
    menu()
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        loja.listar_produtos()
    elif escolha == "2":
        loja.adicionar_ao_carrinho()
    elif escolha == "3":
        loja.ver_carrinho()
    elif escolha == "4":
        loja.simular_pagamento()
    elif escolha == "0":
        print("Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
