import matplotlib.pyplot as plt

# Definir los puntos en el eje X y el eje Y
x = [1, 2, 5, 6,  7]  # Los puntos en el eje X
y = [2, 6, 3, 6, 3]  # Los valores correspondientes en el eje Y

# Crear la gráfica
plt.plot(x, y, marker='o')  # 'o' para marcar los puntos en la gráfica

# Configurar los ejes y el título
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Gráfica de valores subiendo y bajando')

# Mostrar la gráfica
plt.grid(True)
plt.show()

