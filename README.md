# 🏙️ City Routes System 🗺️

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Status](https://img.shields.io/badge/Status-Completo-brightgreen)

**Descrição curta:**  
Sistema em Python para gestão de cidades e rotas, usando Árvores AVL para armazenar cidades e Grafos para modelar bairros e conexões viárias. Permite inserção, remoção, percursos (pré/in/pós), BFS, DFS e cálculo de caminhos mínimos com Dijkstra.

---

## 📌 Sumário
- [🎯 Objetivo](#-objetivo)  
- [🏗 Estrutura do Projeto](#-estrutura-do-projeto)  
- [⚙️ Como Executar](#-como-executar)  
- [📝 Exemplos de Uso](#-exemplos-de-uso)  
- [📊 Complexidade das Operações](#-complexidade-das-operações)  
- [🧠 Aprendizados](#-aprendizados)  
- [🛠️ Requisitos](#-requisitos)  

---

## 🎯 Objetivo
Simular uma plataforma de navegação urbana, integrando **estruturas hierárquicas e de rede**:

- 🏛️ AVL para cidades (balanceamento automático)  
- 🛣️ Grafos para bairros e rotas  
- 🔍 Busca, percursos e cálculo de caminhos mínimos  

---

## 🏗 Estrutura do Projeto

sistema_rotas/
├── arvore_binaria.py # BST com percursos e operações básicas
├── arvore_avl.py # AVL com inserção, remoção e rebalanceamento
├── grafo.py # Grafos com BFS, DFS e Dijkstra
├── main.py # Interface de linha de comando
└── README.md # Este arquivo

yaml
Copiar código

---

## ⚙️ Como Executar

1. Certifique-se de ter Python 3 instalado.  
2. Abra o terminal ou VS Code na pasta do projeto.  
3. Execute:

```bash
python main.py
Use o menu interativo para:

🏙️ Cadastrar ou remover cidades

🌳 Visualizar percursos da AVL (pré/in/pós)

🗺️ Criar e explorar grafos de bairros (BFS, DFS, Dijkstra)

📝 Exemplos de Uso
Cadastrar cidades
text
Copiar código
Nome da cidade: Recife
ID da cidade: 1
Cidade Recife cadastrada com ID 1. (AVL inserida)
Complexidade: Inserção AVL = O(log n)
Mostrar percursos da AVL
text
Copiar código
Pré-Ordem: [1]
Em-Ordem: [1]
Pós-Ordem: [1]
Complexidade: Percursos AVL = O(n)
Criar grafo da cidade
text
Copiar código
Escolha cidade por ID: 1
1 - Adicionar aresta
2 - BFS
3 - DFS
4 - Dijkstra
0 - Voltar

Origem: BairroA
Destino: BairroB
Peso: 5
Aresta BairroA -> BairroB adicionada com peso 5
Executar algoritmos de grafos
text
Copiar código
BFS a partir de BairroA: ['BairroA', 'BairroB']
Complexidade: BFS = O(V + E)

DFS a partir de BairroA: ['BairroA', 'BairroB']
Complexidade: DFS = O(V + E)

Dijkstra a partir de BairroA: {'BairroA': 0, 'BairroB': 5}
Complexidade: Dijkstra = O(E log V)
📊 Complexidade das Operações
Operação	Estrutura	Complexidade
Inserção	AVL	O(log n)
Remoção	AVL	O(log n)
Percursos (pré/in/pós)	AVL	O(n)
BFS	Grafo	O(V + E)
DFS	Grafo	O(V + E)
Dijkstra (caminho mínimo)	Grafo	O(E log V)

🧠 Aprendizados
🌳 Estruturas hierárquicas (BST, AVL)

🔄 Balanceamento automático de árvores (rotações AVL)

🛣️ Algoritmos de grafos (BFS, DFS, Dijkstra)

🧩 Recursividade e percursos

📊 Análise de complexidade (Big O)

🔗 Integração de diferentes estruturas em um sistema realista

🛠️ Requisitos
Python 3.x

Bibliotecas padrão (heapq, collections)

Nenhuma instalação externa necessária
