# Projeto de conclusão da disciplina de Metodologia Científica 2017.1 do curso de Ciência da Computação da Universidade Federal de Campina Grande.

Para executar o projeto basta rodar o shell script usando o comando "./run_all" dentro da pasta "/code" do projeto e o mesmo realizará as seguintes ações:

1 - Executar o arquivo createLoads.py na pasta /load para criar os inputs com base nos nossos fatores que são:
Tamanho da entrada: small, medium, large.
Ordenação da entrada: r(random), p(parcialmente ordenado) e o(ordenado).

2 - Rodar os algoritmos (quick sort, merge sort e bucket sort) para todas as combinações possíveis de fatores(fatorial completo). Serão realizados 5 experimentos para cada combinação de fatores para eliminar possíveis variações aleatórias.

3 - Escrever na pasta /output o intervalo de tempo em milissegundos (pretendemos utilizar como métrica o tempo de execução do algoritmo) que cada algoritmo(com uma certa combinação de fatores) levou para executar.
