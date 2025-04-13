import pandas as pd
import matplotlib.pyplot as plt

file_path = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")

conteo_de_productos = df_pen_sales["Item"].value_counts()
plt.figure(figsize = (10, 5))
conteo_de_productos.plot(kind="barh", color = "red")
plt.title("Ranking de popularidad de Productos")
plt.xlabel("Cantidad de ventas")
plt.ylabel("Tipo de productos")
plt.gca().invert_yaxis()
plt.show()