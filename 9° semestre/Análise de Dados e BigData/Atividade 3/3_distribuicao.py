import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

total_cliques = 10000
total_conversoes = 850
dias = 30

# Probabilidade de conversão dado um clique
probabilidade_conversao = total_conversoes / total_cliques

media_conversoes_por_dia = total_conversoes / dias

desvio_padrao = np.sqrt(media_conversoes_por_dia)

# Simulação de distribuição normal para 30 dias
conversoes_simuladas = np.random.normal(media_conversoes_por_dia, desvio_padrao, dias)

# Probabilidade de obter mais de 30 conversões em um único dia
probabilidade_mais_de_30_conversoes = 1 - norm.cdf(30, loc=media_conversoes_por_dia, scale=desvio_padrao)

# Plot da distribuição simulada
plt.figure(figsize=(10, 6))
plt.hist(conversoes_simuladas, bins=10, density=True, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribuição Simulada de Conversões por Dia')
plt.axvline(x=30, color='red', linestyle='--', label='Limite de 30 conversões')
plt.xlabel('Conversões por Dia')
plt.ylabel('Densidade')
plt.grid(True)
plt.show()

print("Probabilidade de obter mais de 30 conversões em um único dia:", probabilidade_mais_de_30_conversoes)