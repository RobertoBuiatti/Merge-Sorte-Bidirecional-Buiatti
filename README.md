# Merge Sort Bidirecional Buiatti

Este projeto implementa o algoritmo de ordenação  **Merge Sort Bidirecional** , desenvolvido por Roberto Buiatti. O Merge Sort Bidirecional é uma variação do Merge Sort tradicional que realiza a ordenação de forma bidirecional, potencialmente otimizando o desempenho em determinados cenários.

## Descrição

O Merge Sort Bidirecional funciona dividindo a lista de elementos em duas sublistas, ordenando cada uma delas e, em seguida, mesclando-as de maneira bidirecional para produzir a lista final ordenada. Esta abordagem pode oferecer vantagens em relação ao Merge Sort tradicional, especialmente em conjuntos de dados específicos.

## Estrutura do Projeto

O repositório está organizado da seguinte forma:

* `merge/`: Contém a implementação principal do algoritmo em diferentes linguagens.
  * `node/`: Implementação em JavaScript/Node.js.
  * `python/`: Implementação em Python.
* `test/`: Inclui scripts de teste para validar o funcionamento do algoritmo.
  * `test_both.py`: Testes que comparam as implementações em ambas as linguagens.
  * `test_complete.py`: Testes abrangentes para a implementação em Python.
  * `test_manual.py`: Testes manuais e casos de uso específicos.
* `README.md`: Este arquivo, contendo informações gerais sobre o projeto.
* `.gitignore`: Arquivos e diretórios ignorados pelo Git.
* `LICENSE`: Informações sobre a licença do projeto.

## Requisitos

Para executar as implementações deste projeto, você precisará ter instalados:

* **Node.js** : Para a versão em JavaScript/Node.js.
* **Python 3** : Para a versão em Python.

## Instalação e Uso

### Node.js

1. Navegue até o diretório `merge/node`:
   <pre class="!overflow-visible" data-start="1670" data-end="1701"><span>cd merge/node
   </span></code></div></div></pre>
2. Instale as dependências necessárias (se houver):
   <pre class="!overflow-visible" data-start="1760" data-end="1789"><span>npm install
   </span></code></div></div></pre>
3. Execute o script de ordenação:
   <pre class="!overflow-visible" data-start="1830" data-end="1877"><span>node mergeSortBidirecional.js
   </span></code></div></div></pre>

### Python

1. Navegue até o diretório `merge/python`:
   <pre class="!overflow-visible" data-start="1939" data-end="1972"><span>cd merge/python
   </span></code></div></div></pre>
2. Execute o script de ordenação:
   <pre class="!overflow-visible" data-start="2013" data-end="2064"><span>python merge_sort_bidirecional.py
   </span></code></div></div></pre>

## Testes

Para garantir que as implementações funcionem corretamente, você pode executar os testes incluídos no projeto.

1. Navegue até o diretório `test`:
   <pre class="!overflow-visible" data-start="2229" data-end="2254"><span>cd test
   </span></code></div></div></pre>
2. Execute os testes desejados. Por exemplo, para executar os testes completos em Python:
   <pre class="!overflow-visible" data-start="2351" data-end="2392"><span>python test_complete.py
   </span></code></div></div></pre>

