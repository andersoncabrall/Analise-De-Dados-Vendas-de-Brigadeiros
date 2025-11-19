# 📊 Analisador de Lucro - Produção de Brigadeiros

Um projeto simples em Python para analisar a rentabilidade na produção e venda de brigadeiros.

## 🎯 Objetivo

Calcular custos, lucros e fazer projeções financeiras para a produção de brigadeiros, ajudando na tomada de decisões sobre preços e quantidades.

## 📋 Funcionalidades

- **Análise de custos** por ingrediente
- **Cálculo de margem de lucro** por unidade
- **Projeções** para diferentes quantidades de produção
- **Gráficos visuais** para melhor compreensão dos dados

## 🛠️ Pré-requisitos

- Python 3.6 ou superior
- Bibliotecas: pandas e matplotlib

## 📦 Instalação

### 1. Instalar o Python
[Download Python](https://www.python.org/downloads/)

### 2. Instalar as bibliotecas necessárias
```bash
pip install pandas matplotlib
```

## 🚀 Como usar

1. **Baixe o arquivo** `analisador_lucros.py`
2. **Execute no terminal:**
```bash
python analisador_lucros.py
```

## 📊 Saída do Programa

### 1. Resumo Financeiro no Terminal
```
Analisador de Lucro - Brigadeiros
========================================

Resumo Financeiro:
Preco de venda: R$ 2.00
Custo por brigadeiro: R$ 0.31
Lucro por brigadeiro: R$ 1.69
Margem de lucro: 84.5%

========================================
Projecao de Lucros:
========================================
Quantidade | Custo Total | Receita | Lucro
--------------------------------------------
    50     | R$  15.50 | R$ 100.00 | R$  84.50
   100     | R$  31.00 | R$ 200.00 | R$ 169.00
   200     | R$  62.00 | R$ 400.00 | R$ 338.00
   500     | R$ 155.00 | R$ 1000.00 | R$ 845.00
```

### 2. Gráficos Gerados

*Mostra a porcentagem que cada ingrediente representa no custo total de um brigadeiro*
*Mostra o lucro total esperado para diferentes quantidades vendidas*

### 3. Análise Final
```
========================================
Analise Final
========================================
Ingrediente com maior custo: leite condensado
Ingrediente com menor custo: leite em po
- Cada brigadeiro da R$ 1.69 de lucro
- Para lucrar R$ 100,00: vender 59 brigadeiros
- Para lucrar R$ 500,00: vender 296 brigadeiros
```

## 💡 Personalização

Para adaptar aos seus custos, edite o dicionário `dados` no código:

```python
dados = {
    'ingrediente': ['seus ingredientes...'],
    'peso_total': [seus pesos...],
    'custo_total': [seus custos...],
    'custo_por_brigadeiro': [seus custos unitários...]
}
```

## 📈 Insights do Projeto

- **Margem excelente** de 84.5% por unidade
- **Escala é fundamental** - quanto mais produzir, maior o lucro total
- **Ingrediente crítico**: leite condensado (maior custo unitário)

## 🎓 Tecnologias Utilizadas

- **Pandas**: Para manipulação e análise de dados tabulares
- **Matplotlib**: Para criação de visualizações e gráficos
- **Python**: Linguagem de programação principal

**💡 Dica**: Feche a janela dos gráficos para ver a análise completa no terminal!
