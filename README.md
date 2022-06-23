## Execução
    `python server.py [-h] [-d delay] [-p pace]  [-o output-file] [-l log-history] advsearch.player1 advsearch.player2`

Onde 'player(1 ou 2)' são os diretórios dentro de `advsearch` onde estão implementados os módulos dos jogadores (dentro do arquivo agent).

Os argumentos entre colchetes são opcionais, seu significado é descrito a seguir:
-h, --help                                  Mensagem de ajuda
-d delay, --delay delay                     Tempo alocado para os jogadores realizarem a jogada (default=5s)
-p pace, --pace pace                        Tempo mínimo que o servidor espera para processar a jogada (para poder ver partidas muito rápidas sem se perder no terminal)
-l log-history, --log-history log-history   Arquivo para o log do jogo (default=history.txt)
-o output-file, --output-file output-file   Arquivo de saida com os detalhes do jogo (inclui historico)

Exemplo:
    `python server.py advsearch.randomplayer advsearch.randomplayer -d 1 -p 0.3`


## Funcionamento

Iniciando pelo primeiro jogador, que jogará com as peças pretas, o servidor chama a função `make_move(board, color)` do seu `agent.py`. A função recebe `board`, um objeto da classe `Board` e `color`, um caractere indicando a cor com a qual a jogada deve ser feita (‘B’ para as pretas ou ‘W’ para as brancas). Veja no `othello/board.py`.

O servidor então espera o delay e recebe a tupla (x,y) com coluna e linha com a jogada do jogador. O servidor processa a jogada, exibe o novo estado no terminal e passa a vez pro oponente, repetindo esse ciclo até o fim do jogo.

No fim do jogo, o servidor exibe a pontuação de cada jogador e cria um arquivo history.txt
com todas as jogadas tentadas pelos jogadores (inclusive as ilegais).

Em um objeto da classe `Board`, o atributo `tiles` contém a representação do tabuleiro como uma matriz de caracteres (ou lista de strings ;). `W` representa uma peça branca (white), `B` uma peça preta (black) e `.` (ponto) representa um espaço livre. No exemplo a seguir, temos a representação do estado inicial de Othello. 

```text
[
“........”,
“........”,
“........”,
“...WB...”,
“...BW...”,
“........”,
“........”,
“........”,
]
```

O eixo x cresce da esquerda para a direita e o eixo y cresce de cima para baixo. O exemplo a seguir mostra o sistema de coordenadas para o estado inicial. 

```text
  01234567 --> eixo x
0 ........
1 ........
2 ........
3 ...WB...
4 ...BW...
5 ........
6 ........
7 ........
|
|
v
eixo y
```
## Algoritmo Utilizado para desenvolvimento do Agente que compete com o RandomAgent
#### MiniMax com poda alpha beta
A partir do retorno de possiveis proximas jogadas do nosso agente  é gerado uma arvore de pesquisa 
onde utilizamos a estratégia do minimax onde ele simula essas possíveis jogadas maximizando a nossa jogada,
e a jogada do adversario minimiza o nosso ganho,assim nos retornando qual caminho o nosso agente realmente
deve jogar. Para melhorar o minimax foi aplicado uma técnica que no caso  é um algoritmo de pesquisa que busca diminuir o número 
de nós que são avaliados pelo algoritmo minimax em sua árvore de pesquisa conhecido com Poda Alpa-Beta

### Simulação de 30 jogos entre minmax_agent versus ramdomplyer
Caso o minmax_agent não conseguir encontrar uma melhor jogada das disponíveis
em 5 segundos, ele escolhe uma jogada aleatória.

| Agente |  Vitórias   | Média de peças total |
|:-------|:-----------:|---------------------:|
| MinMaxAgent     | 19 vitórias |                 35,3 |
|     RandomPlayer   | 11 vitórias |                 28,7 |


### Melhorias possíveis:

Definir uma melhor regra para a utilidade por exeplo: levar em consideração a posição das peças que valem mais pontos por exemplo,
pois foi utilizada somente o número de peças da cor do jogador.

### Particularidades

