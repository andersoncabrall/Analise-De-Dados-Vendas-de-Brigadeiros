import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print("Analisador de Lucro - Brigadeiros")
print("=" * 40)

dados = {
    'ingrediente': ['leite condensado', 'chocolate em po', 'granulado', 'leite em po', 'forminhas', 'manteiga'],
    'peso_total': [395, 1000, 500, 200, 100, 250],
    'custo_total': [3.89, 25.90, 14.00, 2.00, 2.50, 2.00],
    'custo_por_brigadeiro': [0.18, 0.04, 0.05, 0.00, 0.02, 0.02]
}

tabela = pd.DataFrame(dados)

preco_venda = 2.00
custo_total_brigadeiro = 0.31
lucro_por_brigadeiro = 1.69

print("\nResumo Financeiro:")
print(f"Preco de venda: R$ {preco_venda:.2f}")
print(f"Custo por brigadeiro: R$ {custo_total_brigadeiro:.2f}")
print(f"Lucro por brigadeiro: R$ {lucro_por_brigadeiro:.2f}")
print(f"Margem de lucro: {(lucro_por_brigadeiro/preco_venda)*100:.1f}%")

print("\n" + "=" * 40)
print("Projecao de Lucros:")
print("=" * 40)

quantidades = [50, 100, 200, 500]
print("Quantidade | Custo Total | Receita | Lucro")
print("-" * 45)

for qtd in quantidades:
    custo_total = custo_total_brigadeiro * qtd
    receita_total = preco_venda * qtd
    lucro_total = receita_total - custo_total
    print(f"{qtd:^10} | R$ {custo_total:6.2f} | R$ {receita_total:6.2f} | R$ {lucro_total:6.2f}")

sns.set_style("whitegrid")
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
ingredientes_com_custo = tabela[tabela['custo_por_brigadeiro'] > 0].sort_values('custo_por_brigadeiro', ascending=False)

sns.barplot(data=ingredientes_com_custo, 
            x='custo_por_brigadeiro', 
            y='ingrediente',
            palette='Blues_r',
            hue='ingrediente', 
            legend=False)

plt.title('Distribuição de Custos por Ingrediente (por brigadeiro)')
plt.xlabel('Custo (R$)')
plt.ylabel('Ingrediente')
for i, custo in enumerate(ingredientes_com_custo['custo_por_brigadeiro']):
    plt.text(custo + 0.005, i, f'R$ {custo:.2f}', va='center', fontsize=9)

plt.subplot(1, 2, 2)
projecao_df = pd.DataFrame({
    'Quantidade': quantidades,
    'Lucro': [lucro_por_brigadeiro * qtd for qtd in quantidades]
})

sns.barplot(data=projecao_df, 
            x='Quantidade', 
            y='Lucro',
            palette='Greens',
            hue='Quantidade',
            legend=False)

plt.title('Lucro por Quantidade Vendida')
plt.xlabel('Quantidade de Brigadeiros')
plt.ylabel('Lucro Total (R$)')

for i, lucro in enumerate(projecao_df['Lucro']):
    plt.text(i, lucro + 10, f'R$ {lucro:.0f}', ha='center', fontsize=10)

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))

comparacao_df = pd.DataFrame({
    'Quantidade': quantidades,
    'Custo Total': [custo_total_brigadeiro * qtd for qtd in quantidades],
    'Receita': [preco_venda * qtd for qtd in quantidades],
    'Lucro': [lucro_por_brigadeiro * qtd for qtd in quantidades]
})
comparacao_melted = comparacao_df.melt(id_vars='Quantidade', 
                                        value_vars=['Custo Total', 'Receita', 'Lucro'],
                                        var_name='Tipo', 
                                        value_name='Valor (R$)')
sns.barplot(data=comparacao_melted,
            x='Quantidade',
            y='Valor (R$)',
            hue='Tipo',
            palette='Set2')

plt.title('Comparação: Custo, Receita e Lucro por Quantidade')
plt.xlabel('Quantidade de Brigadeiros')
plt.ylabel('Valor (R$)')

for i, bar in enumerate(plt.gca().patches):
    height = bar.get_height()
    if height > 0:
        plt.text(bar.get_x() + bar.get_width()/2., height + 20,
                f'R$ {height:.0f}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()

print("\n" + "=" * 40)
print("Analise Final")
print("=" * 40)

ingrediente_mais_caro = tabela.loc[tabela['custo_por_brigadeiro'].idxmax()]
ingrediente_mais_barato = tabela.loc[tabela['custo_por_brigadeiro'].idxmin()]

print(f"Ingrediente com maior custo: {ingrediente_mais_caro['ingrediente']}")
print(f"Ingrediente com menor custo: {ingrediente_mais_barato['ingrediente']}")
print(f"- Cada brigadeiro da R$ {lucro_por_brigadeiro:.2f} de lucro")
print(f"- Para lucrar R$ 100,00: vender {100/lucro_por_brigadeiro:.0f} brigadeiros")
print(f"- Para lucrar R$ 500,00: vender {500/lucro_brigadeiro:.0f} brigadeiros")
