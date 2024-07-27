# Завдання 1
# Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі
# (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).

import networkx as nx
import matplotlib.pyplot as plt

# Створимо порожній граф
G = nx.Graph()

# Додамо вершини (туристичні місця)
tourist_sites = ["Києво-Печерська Лавра", "Софійський собор", "Золоті ворота", "Майдан Незалежності", "Андріївський узвіз"]

# Додамо вершини до графа
G.add_nodes_from(tourist_sites)

# Додамо ребра (маршрути між туристичними місцями)
# Відстані між туристичними місцями взяті умовно для прикладу
edges = [
    ("Києво-Печерська Лавра", "Софійський собор", 3),
    ("Софійський собор", "Золоті ворота", 1),
    ("Золоті ворота", "Майдан Незалежності", 1),
    ("Майдан Незалежності", "Андріївський узвіз", 2),
    ("Андріївський узвіз", "Києво-Печерська Лавра", 4),
    ("Києво-Печерська Лавра", "Майдан Незалежності", 2),  # Додаткове ребро
    ("Софійський собор", "Майдан Незалежності", 2)  # Додаткове ребро
]

# Додаємо ребра до графа з вагами
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Візуалізуємо граф
pos = nx.spring_layout(G)  # Розташування вершин
plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, edge_color='gray', font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа туристичних місць Києва")
plt.show()

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degrees.items():
    print(f"Вершина {node}: {degree}")

# Додатковий аналіз
degree_centrality = nx.degree_centrality(G)
print("Центральність за ступенем:")
for node, centrality in degree_centrality.items():
    print(f"Вершина {node}: {centrality:.2f}")
