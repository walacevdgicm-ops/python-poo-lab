# 🐍 Python POO Lab — Do Zero ao Sistema Bancário

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![POO](https://img.shields.io/badge/Paradigma-Orientação%20a%20Objetos-blueviolet)

Minha trilha de estudos de **Programação Orientada a Objetos em Python**, organizada em etapas: começa com entrada e saída de dados e termina em um **sistema bancário** com várias classes, herança, extrato e conta com limite.

Cada pasta é independente e pode ser executada sozinha.

## 🗺️ Trilha

| Etapa | Pasta | Conceitos |
|---|---|---|
| 01 | [`01-cadastro-streaming`](01-cadastro-streaming) | `input`, f-strings, validação de data, dicionários, laços |
| 02 | [`02-primeira-classe-conta`](02-primeira-classe-conta) | Classe, `__init__`, atributos e métodos, exceções (`ValueError`) |
| 03 | [`03-encapsulamento-e-heranca`](03-encapsulamento-e-heranca) | Atributos privados (`__saldo`), `@classmethod`, `@staticmethod`, herança |
| 04 | [`04-banco-com-multiplos-titulares`](04-banco-com-multiplos-titulares) | Composição: conta com vários clientes, transferência |
| 05 | [`05-sistema-bancario-completo`](05-sistema-bancario-completo) | Pacotes, `Banco` / `Cliente` / `Conta` / `Extrato`, **herança com `super()`** (`ContaEspecial` com cheque especial) |

## 🚀 Como executar

```bash
cd 05-sistema-bancario-completo
python main.py
```

Exemplo de saída da etapa 05:

```
Atenção: conta 557 usando R$ 300.00 do limite.
Não existe saldo suficiente na conta número 557
Extrato da Conta: 555
DEPÓSITO            500.00 08/11/2026
TRANSFERÊNCIA       200.00 08/11/2026
```

## 👨‍💻 Autor

**Walace Soares Vidigal Junior**, estudante de Análise e Desenvolvimento de Sistemas · [GitHub](https://github.com/walacevdgicm-ops)

Licença [MIT](LICENSE)
