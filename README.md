<h1> Merge Sort Bidirecional Buiatti </h1>

O Merge Sort Bidirecional Buiatti é uma biblioteca que implementa uma versão otimizada do algoritmo merge sort, realizando ordenação bidirecional para melhorar a eficiência do processo de ordenação tradicional.

Descrição
O algoritmo Merge Sort Bidirecional é uma evolução do merge sort clássico, incorporando uma abordagem que processa os elementos simultaneamente a partir de ambas as extremidades da lista durante a fase de mesclagem. Esta técnica resulta em melhor aproveitamento da localidade de memória e potencial redução no número de comparações necessárias.

Requisitos
Python 3.x

Node.js 14.x ou superior (para versão JavaScript)

<h2>Instalação </h2>
Clone o repositório em seu ambiente local:

<pre>

git clone https://github.com/RobertoBuiatti/Merge-Sorte-Bidirecional-Buiatti.git

</pre>

Navegue até o diretório do projeto:

<pre>

cd Merge-Sorte-Bidirecional-Buiatti

</pre>

<h3>Para Python:</h3> 
<pre>

cd python

python setup.py install

</pre>

<h3>Para Node.js: </h3>
<pre>

cd node

npm install

</pre>

<h2>Uso</h2>
Python
<pre>

from merge_sort_bidirecional import merge_sort_bidirecional

# Lista exemplo para ordenação

lista = [64, 34, 25, 12, 22, 11, 90]

# Aplica o merge sort bidirecional

lista_ordenada = merge_sort_bidirecional(lista)

print(f"Lista original: {lista}")

print(f"Lista ordenada: {lista_ordenada}")

</pre>

Node.js
<pre>

const { mergeSortBidirecional } = require('./mergeSortBidirecional');

// Array exemplo para ordenação

const array = [64, 34, 25, 12, 22, 11, 90];

// Aplica o merge sort bidirecional

const arrayOrdenado = mergeSortBidirecional(array);

console.log(`Array original: ${array}`);

console.log(`Array ordenado: ${arrayOrdenado}`);

</pre>

Características Principais
Ordenação Bidirecional: Processa elementos de ambas as extremidades simultaneamente
Eficiência Melhorada: Otimiza o uso de cache e reduz movimentações de memória
Estabilidade: Mantém a ordem relativa de elementos iguais
Complexidade: O(n log n) no caso médio e pior caso
Versatilidade: Implementações disponíveis em Python e Node.js
Estrutura do Projeto
<pre>

.

├── python/ # Implementação Python

│ ├── merge_sort_bidirecional.py

│ └── setup.py

├── node/ # Implementação Node.js

│ ├── mergeSortBidirecional.js

│ └── package.json

├── tests/ # Testes unitários

│ ├── test_complete.py

│ ├── test_both.py

│ └── test_manual.py

├── README.md # Documentação

└── LICENSE # Licença do projeto

</pre>

Testes
Execute os testes para verificar o funcionamento correto do algoritmo:

<pre>

# Testes completos

python tests/test_complete.py

# Testes comparativos

python tests/test_both.py

# Testes manuais

python tests/test_manual.py

</pre>



Licença
Este projeto está licenciado sob os termos da licença MIT - veja o arquivo LICENSE para detalhes.

Autor
Roberto Buiatti
