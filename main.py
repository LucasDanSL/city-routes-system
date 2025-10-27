from arvore_avl import AVLTree, NoAVL
from grafo import Grafo

def main():
    avl = AVLTree()
    raiz = None
    cidades = {}

    while True:
        print("\n=== Sistema de Navegação ===")
        print("1 - Cadastrar cidade")
        print("2 - Remover cidade")
        print("3 - Mostrar percursos da AVL")
        print("4 - Criar/explorar grafo de uma cidade")
        print("0 - Sair")
        escolha = input("Escolha: ")

        if escolha == "1":
            nome = input("Nome da cidade: ")
            id_cidade = int(input("ID da cidade: "))
            grafo_cidade = Grafo()
            cidades[id_cidade] = grafo_cidade
            raiz = avl.insert(raiz, id_cidade, cidade=grafo_cidade)
            print(f"Cidade {nome} cadastrada com ID {id_cidade}. (AVL inserida)")
            print("Complexidade: Inserção AVL = O(log n)")

        elif escolha == "2":
            id_cidade = int(input("ID da cidade para remover: "))
            raiz = avl.remove(raiz, id_cidade)
            cidades.pop(id_cidade, None)
            print(f"Cidade {id_cidade} removida da AVL e do sistema.")
            print("Complexidade: Remoção AVL = O(log n)")

        elif escolha == "3":
            print("Pré-Ordem:", avl.preorder(raiz))
            print("Em-Ordem:", avl.inorder(raiz))
            print("Pós-Ordem:", avl.postorder(raiz))
            print("Complexidade: Percursos AVL = O(n)")

        elif escolha == "4":
            id_cidade = int(input("Escolha cidade por ID: "))
            grafo = cidades.get(id_cidade)
            if not grafo:
                print("Cidade não encontrada!")
                continue
            while True:
                print("\n--- Grafo da Cidade ---")
                print("1 - Adicionar aresta")
                print("2 - BFS")
                print("3 - DFS")
                print("4 - Dijkstra")
                print("0 - Voltar")
                g = input("Escolha: ")
                if g == "1":
                    u = input("Origem: ")
                    v = input("Destino: ")
                    p = int(input("Peso: "))
                    grafo.adicionar_aresta(u, v, p)
                    print(f"Aresta {u} -> {v} adicionada com peso {p}")
                elif g == "2":
                    start = input("BFS a partir de: ")
                    print("Ordem BFS:", grafo.bfs(start))
                    print("Complexidade: BFS = O(V + E)")
                elif g == "3":
                    start = input("DFS a partir de: ")
                    print("Ordem DFS:", grafo.dfs(start))
                    print("Complexidade: DFS = O(V + E)")
                elif g == "4":
                    start = input("Dijkstra a partir de: ")
                    dist = grafo.dijkstra(start)
                    print("Distâncias mínimas:", dist)
                    print("Complexidade: Dijkstra = O(E log V)")
                elif g == "0":
                    break
                else:
                    print("Opção inválida")

        elif escolha == "0":
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
