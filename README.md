# DBSCAN Manual — Inteligência Artificial

Este projeto apresenta uma **implementação manual do algoritmo de agrupamento espacial baseado em densidade (DBSCAN)**, desenvolvida em Python como parte de um trabalho acadêmico da disciplina de **Inteligência Artificial**.

Diferentemente de abordagens prontas, **não foi utilizada nenhuma biblioteca que implemente DBSCAN**, como `sklearn.cluster.DBSCAN`. Toda a lógica do algoritmo foi construída do zero, incluindo a identificação explícita dos tipos de pontos.

---

## 🎯 Objetivos do Projeto

- Implementar o algoritmo **DBSCAN manualmente**
- Classificar explicitamente cada ponto em:
  - **Núcleo (Core)**
  - **Borda (Border)**
  - **Ruído (Noise)**
- Aplicar o algoritmo em três datasets distintos:
  - Two Moons
  - Two Circles
  - Iris Dataset
- Gerar visualizações 2D e 3D dos agrupamentos
- Comparar os clusters obtidos com as classes reais da base Iris

---

## 🧠 Conceitos Fundamentais

No DBSCAN, os pontos são classificados da seguinte forma:

- **Núcleo (Core)**  
  Possui pelo menos `min_samples` vizinhos dentro de um raio `eps`.

- **Borda (Border)**  
  Não possui vizinhos suficientes para ser núcleo, mas está dentro do raio `eps` de um ponto núcleo.

- **Ruído (Noise)**  
  Não é núcleo e não é alcançável por nenhum ponto núcleo.

Essa classificação é explicitamente implementada e armazenada durante a execução do algoritmo.

---

## 📁 Estrutura do Projeto

```text
dbscan-manual/
├── README.md
├── requirements.txt
├── main.py
│
├── src/
│   ├── algorithms/
│   │   └── dbscan_manual.py
│   ├── datasets/
│   │   └── load_datasets.py
│   ├── visualization/
│   │   └── plots.py
│   └── experiments/
│       ├── run_moons.py
│       ├── run_circles.py
│       └── run_iris.py
│
└── reports/
    ├── figures/
    └── results/
```
📌 Descrição das Pastas
```text
src/algorithms/
```
Contém a implementação manual do algoritmo DBSCAN.
```text
src/datasets/
```
Responsável pelo carregamento e geração dos datasets utilizados.
```text
src/visualization/
```
Funções para geração de gráficos 2D e 3D com identificação visual dos tipos de pontos.
```text
src/experiments/
```
Scripts independentes para execução dos experimentos em cada dataset.
```text
reports/
```
Armazena imagens, gráficos e resultados que podem ser utilizados no relatório final.

📊 Datasets Utilizados
🔹 Two Moons
Gerado com sklearn.datasets.make_moons

300 amostras

Ruído adicionado

Ideal para avaliar clusters não lineares

🔹 Two Circles
Gerado com sklearn.datasets.make_circles

Estrutura concêntrica

Desafio clássico para algoritmos baseados em distância

🔹 Iris Dataset
Dataset clássico da literatura

150 amostras

4 atributos

Classes reais:

Setosa

Versicolor

Virginica

Utilizada distância euclidiana

Visualização em 2D e 3D a partir de subconjuntos de atributos
```text
⚙️ Execução do Projeto
1️⃣ Instalação das dependências
pip install -r requirements.txt
2️⃣ Execução individual dos experimentos
(a partir da raiz do projeto)

python -m src.experiments.run_moons
python -m src.experiments.run_circles
python -m src.experiments.run_iris
3️⃣ Execução completa (opcional)
python main.py
```
📈 Visualizações
As visualizações utilizam cores distintas para cada tipo de ponto:

🔵 Azul — Núcleo (Core)

🟠 Laranja — Borda (Border)

🔴 Vermelho — Ruído (Noise)

Para a base Iris, são gerados:

Gráficos 2D (seleção de atributos)

Gráficos 3D para melhor análise espacial

As figuras são automaticamente salvas no diretório:

reports/figures/
em alta resolução (300 DPI), prontas para uso em relatórios e apresentações.

🔍 Análise da Base Iris
Os clusters gerados pelo DBSCAN são comparados com as classes reais do dataset Iris.

Observações típicas:

A classe Setosa tende a formar clusters densos e bem definidos

Versicolor e Virginica apresentam maior sobreposição

Pontos de borda aparecem nas regiões de transição

Pontos classificados como ruído indicam possíveis outliers

📝 Considerações Finais
Este projeto demonstra:

Implementação manual de um algoritmo de clustering não supervisionado

Classificação explícita de pontos em núcleo, borda e ruído

Separação clara entre lógica, visualização e experimentos

Organização adequada para trabalhos acadêmicos

Facilidade de extensão para novos datasets ou métricas

📚 Tecnologias Utilizadas
Python 3

NumPy

Matplotlib

Scikit-learn (utilizado apenas para geração/carregamento de datasets)

Pandas (análises auxiliares)
