# 📊 Analisador de Lucro - Brigadeiros

Ferramenta Python para análise de rentabilidade na produção de brigadeiros com gráficos profissionais.

## 🎯 Funcionalidades

- **Análise de custos** por ingrediente
- **Cálculo de margem de lucro** (84.5% por unidade)
- **Projeções financeiras** para diferentes quantidades
- **3 gráficos visuais** com Seaborn
- **Insights estratégicos** para tomada de decisão

## 🚀 Como Usar

```bash
# Instalar dependências
pip install pandas seaborn matplotlib

# Executar análise
python analisador_lucros.py
```

## 📊 Resultados

### Dados Financeiros
- Preço de venda: R$ 2,00
- Custo por unidade: R$ 0,31
- Lucro por unidade: R$ 1,69
- Margem: 84.5%

### Projeções
| Quantidade | Custo Total | Receita | Lucro |
|------------|-------------|---------|-------|
| 50         | R$ 15,50    | R$ 100,00 | R$ 84,50 |
| 100        | R$ 31,00    | R$ 200,00 | R$ 169,00 |
| 200        | R$ 62,00    | R$ 400,00 | R$ 338,00 |
| 500        | R$ 155,00   | R$ 1000,00 | R$ 845,00 |

### Gráficos Gerados
1. **Distribuição de Custos** - Custo por ingrediente
2. **Projeção de Lucros** - Lucro por quantidade
3. **Comparação Completa** - Custo × Receita × Lucro

## 🔧 Personalização

Edite os dados no código:
```python
dados = {
    'ingrediente': ['leite condensado', 'chocolate...'],
    'custo_total': [3.89, 25.90, ...],  # Seus custos
    'custo_por_brigadeiro': [0.18, 0.04, ...]  # Custos unitários
}
```

## 🛠️ Tecnologias
- Python 3
- Pandas (análise de dados)
- Seaborn (visualização)
- Matplotlib (gráficos)

---

*Projeto educacional para análise financeira com Python*
