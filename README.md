# TDE
Todas as informações e aprendizagem foram retiradas da página ificial do python: https://docs.python.org/3/

Para trocar o arquivo de entrada, basta alterar a linha 3 do código para o nome do arquivo desejado (por exemplo, "arqtxt1.txt", "arqtxt2.txt", ou "arqtxt3.txt"). 

Primeiro, o código irá abrir o arquivo e pegar a quantidade de operações.

O código entra em um loop while que continua enquanto houver operações a serem realizadas.

Para o código eliminar os espaços utilizei o .strip(), e no conjunto utilizei também o .split(,) para tirar a ",". Quando tinha testado, os elementos estavam com um espaço dentro das aspas então foi necessário utilizar o for para retirá-los.

para verificar a operação a ser realizada fiz uma comparação, usando o if.
O python já tinha uma função para união, intersecção e diferença, apenas pesquisei como utilizar. Já para o produto do plano cartesiano, pesquisando encontrei uma biblioteca que tinha essa função, a itertools, e a importei.

No fim do looping, diminui um da quantidade de operações, para que o looping encerre ao terminar a leitura e operações. Já que a função .readline() lê linha por linha, a cada repetição ele irá continuar a leitura de onde parou.

Ao fim fechei o arquivo com o .close para finalizar a leitura daquele arquivo.
