# MISSA
Código fonte para os experimentos numéricos do paper "A Markovian Incremental Stochastic Subgradient Algorithm", Rafael Massambone, Eduardo F. Costa e Elias S. Helou.

<p align="center">
  
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/RMassambone/MISSA">

  <a href="https://github.com/tgmarinho/README-ecoleta/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/RMassambone/MISSA">
  </a>
    
   <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">

## Paper

O paper "Markovian Incremental Stochastic Subgradient Algorithms" (MISSA) aborda um novo algoritmo para a tarefa de minimizar uma soma de funções convexas. O método usa informações parciais de subgradientes de forma sequencial com a escolha dos índices sendo realizada por uma cadeia de Markov geral. Sua formulação possibilita aplicação em redes de agentes tal que o caminho do fluxo de informações seja selecionado estocasticamente. Provamos a convergência do algoritmo para uma função objetivo ponderada onde os pesos são dados pela distribuição de probabilidade limite, no sentido de Cesàro. Ao contrário de trabalhos anteriores na literatura, a distribuição limite de Cesàro é geral (não necessariamente uniforme), permitindo funções objetivo gerais ponderadas e flexibilidade no método. O preprint pode ser encontrado em https://arxiv.org/abs/2108.07900.

## Como executar

Este projeto possui quatro métodos implementados:
1. MISSA (programa principal: missa.cpp)
2. Cyclic incremental stochastic subgradient algorithm (programa principal: cyclic.cpp)
3. Randomized incremental stochastic subgradient algorithm (programa principal: randomized.cpp)
4. Markov randomized incremental stochastic subgradient algorithm (programa principal: ram.cpp)

MISSA executa subiterações em paralelo através da biblioteca `std::thread` https://en.cppreference.com/w/cpp/thread/thread. Nesse programa, implementamos duas cadeias de Markov <img src="https://render.githubusercontent.com/render/math?math=s_1(k), \, s_2(k)"> tomando valores em uma matriz de transição <img src="https://render.githubusercontent.com/render/math?math=P">. Você pode alterar isso de acordo com sua necessidade em missa.cpp.

```bash

# Para compilar
$ g++ -O3 -Wl,--no-as-needed -std=c++11 -lpthread missa.cpp -o missa

# Para executar
$ ./missa <numero-iteracoes> <numero-cadeias=2> <numero-threads=2>

```
Como resultado, o programa imprimirá na tela o CPU time para MISSA em cada um dos oito testes realizados. Além disso, arquivos "/home/objective_MISSA_test-1.txt", ..., "/home/objective_MISSA_test-8.txt" serão gerados em $HOME com os valores de <img src="https://render.githubusercontent.com/render/math?math=f(\mathbf{x}^k)"> para cada teste. Altere o diretório de destino para os arquivos de acordo com sua preferência.
  
Os demais métodos utilizam apenas uma cadeia de Markov. Eles podem ser compilados e executados com

```bash

# Para compilar
$ g++ -O3 -Wl,--no-as-needed -std=c++11 -lpthread cyclic.cpp -o cyclic
$ g++ -O3 -Wl,--no-as-needed -std=c++11 -lpthread ram.cpp -o ram
$ g++ -O3 -Wl,--no-as-needed -std=c++11 -lpthread randomized.cpp -o randomized

# Para executar
$ ./cyclic <numero-iteracoes> <numero-cadeias=1> <numero-threads=1>
$ ./ram <numero-iteracoes> <numero-cadeias=1> <numero-threads=1>
$ ./randomized <numero-iteracoes> <numero-cadeias=1> <numero-threads=1>

```

Após executar todos os métodos, você pode desejar visualizar um gráfico com os resultados. Digitando
  
```bash
  
  $ python3 graphs_diminishing_all_best.py
  
```
será gerado como saída o arquivo "teste1-fig.svg". Você pode alterar o código para visualizar o gráfico para os demais testes.
  
<img src="./teste1-fig.svg">
  
## Licença

Este projeto está sob a licença [MIT](./LICENSE).
