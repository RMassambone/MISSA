# MISSA
Código fonte para os experimentos numéricos do paper "A Markovian Incremental Stochastic Subgradient Algorithm", Rafael Massambone, Eduardo F. Costa e Elias S. Helou.

<p align="center">
  
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/RMassambone/MISSA">

  <a href="https://github.com/tgmarinho/README-ecoleta/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/RMassambone/MISSA">
  </a>
    
   <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">

<p align="center">
 <a href="#-paper">Paper</a>
 <a href="#-como-executar-o-projeto">Como executar</a>
 <a href="#user-content--licença">Licença</a>
</p>


## Paper

O paper "Markovian Incremental Stochastic Subgradient Algorithms" (MISSA) aborda um novo algoritmo para a tarefa de minimizar uma soma de funções convexas. O método usa informações parciais de subgradientes de forma sequencial com a escolha dos índices sendo realizada por uma cadeia de Markov geral. Sua formulação possibilita aplicação em redes de agentes tal que o caminho do fluxo de informações seja selecionado estocasticamente. Provamos a convergência do algoritmo para uma função objetivo ponderada onde os pesos são dados pela distribuição de probabilidade limite, no sentido de Cesàro. Ao contrário de trabalhos anteriores na literatura, a distribuição limite de Cesàro é geral (não necessariamente uniforme), permitindo funções objetivo gerais ponderadas e flexibilidade no método. O preprint pode ser encontrado em https://arxiv.org/abs/2108.07900.

## Como executar

Este projeto possui quatro métodos implementados:
1. MISSA (programa principal: missa.cpp)
2. Cyclic incremental stochastic subgradient algorithm (programa principal: cyclic.cpp)
3. Randomized incremental stochastic subgradient algorithm (programa principal: randomized.cpp)
4. Markov randomized incremental stochastic subgradient algorithm (programa principal: ram.cpp)

MISSA executa subiterações em paralelo através da biblioteca pthread https://en.cppreference.com/w/cpp/thread/thread. Nesse programa, implementamos duas cadeias de Markov tomando valores em uma matriz de transição P. Você pode alterar isso de acordo com sua necessidade em missa.cpp.

```bash

# Para compilar
$ g++ -O3 -Wl,--no-as-needed -std=c++11 -lpthread missa.cpp -o missa

# Para executar, pode usar por exemplo
$ ./missa <numero-iteracoes> <numero-cadeias=2> <numero-threads=2>

```

## Licença

Este projeto está sob a licença [MIT](./LICENSE).
