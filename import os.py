import os
import matplotlib.pyplot as plt

# Leer variables de entorno
datos_env = os.getenv("DATOS")
titulo = os.getenv("TITULO", "Gráfica sin título")

if not datos_env:
    raise ValueError("La variable de entorno DATOS no está definida")

# Convertir la cadena de texto a lista de números
datos = [float(x) for x in datos_env.split(",")]

# Crear la gráfica
plt.figure()
plt.plot(datos, marker="o")
plt.title(titulo)
plt.xlabel("Índice")
plt.ylabel("Valor")

# Crear carpeta de salida si no existe
os.makedirs("/salida", exist_ok=True)

# Guardar la gráfica
plt.savefig("/salida/grafica.png")
plt.close()
