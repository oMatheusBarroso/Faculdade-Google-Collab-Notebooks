import math
import numpy as np
import matplotlib.pyplot as plt

total_conversoes = 850
dias = 30

media_conversoes_por_dia = total_conversoes / dias

desvio_padrao = math.sqrt(media_conversoes_por_dia)

# Simulação de distribuição normal para 30 dias
conversoes_simuladas = np.random.normal(media_conversoes_por_dia, desvio_padrao, dias)

dias_periodo = np.arange(1, dias + 1)

# Plot do número de conversões por dia
plt.figure(figsize=(10, 6))
plt.bar(dias_periodo, conversoes_simuladas, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Número de Conversões por Dia')
plt.xlabel('Dia')
plt.ylabel('Número de Conversões')
plt.grid(True)
plt.xticks(dias_periodo)
plt.show()