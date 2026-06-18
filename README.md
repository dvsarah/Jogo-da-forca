# 🎮 Jogo da Forca em Python (Projeto Acadêmico)

**Trabalho desenvolvido em grupo** para a disciplina de **Programação I**.

Este projeto consiste em um **Jogo da Forca** interativo desenvolvido em ambiente de terminal utilizando **Python 3**. O software foi construído como um trabalho acadêmico em equipe, com o objetivo de consolidar conceitos estruturais de lógica de programação, manipulação de arquivos e controle de fluxo.

---

## 🚀 Funcionalidades e Destaques Técnicos

O projeto vai além de uma lógica de jogo convencional, integrando recursos avançados para o terminal:

* **Persistência e Leitura de Dados:** O jogo consome os dados dinamicamente de um arquivo externo (`Jogo.txt`). Ele processa e estrutura as palavras e suas respectivas dicas em uma matriz bidimensional.
* **Sorteio de Dicas e Palavras:** Sistema inteligente que sorteia aleatoriamente a palavra da rodada e gerencia as dicas associadas a ela sem repeti-las em sequência, utilizando controle de estados globais.
* **Controle de Tempo (Milissegundos):** Implementação de um timer regressivo utilizando a biblioteca `time` (`perf_counter()`), limitando o tempo total de resposta do usuário em 1 minuto (60.000 ms) por partida.
* **Interface Visual em ASCII Art:** Atualização dinâmica do estado do boneco na forca diretamente no terminal de acordo com os erros cometidos pelo jogador.
* **Tratamento de Exceções e Validações:** O código valida se o arquivo de dados existe antes de iniciar, impede que o usuário repita letras já tentadas e pune o abuso de pedidos de dicas diminuindo as vidas restantes.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 
* **Bibliotecas Nativas:** `os` (manipulação de caminhos e comandos do sistema), `random` (aleatorização de palavras/dicas) e `time` (controle fino do cronômetro).

---

