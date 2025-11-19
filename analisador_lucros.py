import pandas as pd
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

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)

ingredientes_com_custo = tabela[tabela['custo_por_brigadeiro'] > 0]
plt.pie(ingredientes_com_custo['custo_por_brigadeiro'], 
        labels=ingredientes_com_custo['ingrediente'], 
        autopct='%1.1f%%')

plt.title('Porcentagem de Custos por Unidade de Brigadeiro')
plt.subplot(1, 2, 2)

lucros = [lucro_por_brigadeiro * qtd for qtd in quantidades]
plt.bar([str(qtd) for qtd in quantidades], lucros, color='green')

plt.title('Lucro por Quantidade')
plt.xlabel('Quantidade de Brigadeiros')
plt.ylabel('Lucro Total (R$)')

for i, lucro in enumerate(lucros):
    plt.text(i, lucro + 10, f'R$ {lucro:.0f}', ha='center')

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
print(f"- Para lucrar R$ 500,00: vender {500/lucro_por_brigadeiro:.0f} brigadeiros")
