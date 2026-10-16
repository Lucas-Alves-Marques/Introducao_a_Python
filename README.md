# 🐍 Introdução a Python

Projeto de estudos com pequenos programas em Python, organizados por módulos. Os exemplos percorrem conceitos básicos da linguagem: exibição de informações, variáveis e tipos, entrada de dados, operadores, condições, laços, funções e leitura de arquivos de texto.

Os arquivos são exercícios independentes. Não há um aplicativo único para iniciar: escolha um exemplo e execute-o individualmente.

## 📋 Requisitos

- Python 3 instalado.
- Um terminal aberto na pasta `Introducao_a_Python`.

Os exemplos usam apenas recursos da biblioteca padrão do Python; não é necessário instalar pacotes adicionais.

Para conferir se o Python está disponível:

```powershell
python --version
```

Em algumas instalações do Windows, o comando pode ser:

```powershell
py --version
```

## ▶️ Como executar

Se o PowerShell estiver aberto na pasta que contém `Introducao_a_Python`, entre na pasta do projeto e execute o arquivo desejado:

```powershell
cd .\Introducao_a_Python
python .\modulo_2\hello_word.py
```

Se `python` não for reconhecido, tente `py` no lugar:

```powershell
py .\modulo_2\hello_word.py
```

Os exercícios que usam `input()` solicitarão informações no terminal. Execute um programa de cada vez e siga as mensagens exibidas.

## 📚 Conteúdo do projeto

### 👋 Módulo 2 — Primeiro programa

- [`modulo_2/hello_word.py`](modulo_2/hello_word.py): exibe a mensagem `Hello, World!`.

### 🔤 Módulo 3 — Variáveis, tipos e entrada e saída

- [`modulo_3/entrada_dados.py`](modulo_3/entrada_dados.py): solicita código, salário e nome, converte os valores numéricos e exibe os dados, incluindo uma variável booleana.
- [`modulo_3/exibir_variavel.py`](modulo_3/exibir_variavel.py): demonstra a exibição de valores armazenados em variáveis e a formatação com `%d`, `%s`, `%.2f` e `%r`.
- [`modulo_3/tipo_variavel.py`](modulo_3/tipo_variavel.py): usa `type()` para consultar o tipo de um valor e mostra conversões para texto com `str()`.

### 🔁 Módulo 4 — Operadores, condições e repetição

- [`modulo_4/operadores.py`](modulo_4/operadores.py): apresenta os operadores lógicos `and`, `or` e `not`.
- [`modulo_4/media.py`](modulo_4/media.py): lê duas notas, calcula a média e informa aprovação para média maior ou igual a 7.
- [`modulo_4/estrutura_repeticao.py`](modulo_4/estrutura_repeticao.py): contém exemplos comentados de `range()` e executa um laço `while` para exibir números de 1 a 15.
- [`modulo_4/estrutura_simples.py`](modulo_4/estrutura_simples.py): mostra, em comentários, como gravar texto e lê o conteúdo de `arqText.txt`.
- [`modulo_4/media_valores.py`](modulo_4/media_valores.py): soma valores positivos digitados, conta quantos foram informados e calcula a média. Um valor menor ou igual a zero encerra a entrada.

### 🧩 Módulo 5 — Funções e organização do programa

- [`modulo_5/media.py`](modulo_5/media.py): separa a leitura de notas e o cálculo/exibição do resultado em duas funções (`lernotas()` e `resultado()`).

### 📄 Módulo 6 — Arquivos de texto

- [`modulo_6/gravar.py`](modulo_6/gravar.py): solicita duas notas, calcula a média e informa se o resultado é aprovado ou reprovado.
- [`modulo_6/arqText.txt`](modulo_6/arqText.txt): arquivo de texto de exemplo, com as linhas `Curso Python` e `Aula Pratica`.

## 💻 Exemplos de execução

Execute estes comandos a partir da pasta raiz do projeto:

```powershell
python .\modulo_3\entrada_dados.py
python .\modulo_4\media.py
python .\modulo_5\media.py
python .\modulo_6\gravar.py
```

Para testar a leitura de texto, execute `estrutura_simples.py` com `modulo_6` como pasta atual, pois o programa procura `arqText.txt` relativamente à pasta atual:

```powershell
Push-Location .\modulo_6
python ..\modulo_4\estrutura_simples.py
Pop-Location
```

Esse programa está configurado para leitura. O trecho que grava texto está comentado no próprio arquivo.

## 💡 Observações sobre os exercícios

- Em `media_valores.py`, informe pelo menos um valor positivo antes de encerrar a entrada. Se o primeiro valor for zero ou negativo, a quantidade de valores será zero e o cálculo da média não poderá ser realizado.
- Os arquivos são exemplos didáticos e mantêm a lógica apresentada em cada exercício; não formam um pacote e não têm testes automatizados configurados.
- Alguns nomes de arquivos e mensagens foram mantidos como estão no projeto para facilitar a correspondência com os exercícios.
