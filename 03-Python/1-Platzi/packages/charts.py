import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    

    # Crear gráfico de barras horizontal para mejor visualización de nombres de países
    plt.figure(figsize=(12, 8))
    bars = plt.barh(labels, values, color='skyblue')

    # Añadir etiquetas y título
    plt.xlabel('Porcentaje de la Población Mundial (%)')
    plt.title('Top 15 Países por Porcentaje de Población Mundial')
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    # Añadir los valores en las barras
    for i, bar in enumerate(bars):
        plt.text(values[i] + 0.1, bar.get_y() + bar.get_height()/2, f'{values[i]}%', 
                va='center', fontweight='bold')
        
    # Ajustar el diseño
    plt.tight_layout()
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    generate_bar_chart()
    generate_pie_chart()