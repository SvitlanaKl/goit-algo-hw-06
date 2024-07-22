# Завдання 3

import networkx as nx
import matplotlib.pyplot as plt

# Створимо порожній граф
G = nx.Graph()

# Додамо вершини (станції метро)
stations = {
    "Червона лінія": ["Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська", "Шулявська", "Політехнічний інститут", "Вокзальна", "Університет", "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Лівобережна", "Дарниця", "Чернігівська", "Лісова"],
    "Синя лінія": ["Героїв Дніпра", "Мінська", "Оболонь", "Почайна", "Тараса Шевченка", "Контрактова площа", "Поштова площа", "Майдан Незалежності", "Площа Льва Толстого", "Олімпійська", "Палац Україна", "Либідська", "Деміївська", "Голосіївська", "Васильківська", "Виставковий центр", "Іподром", "Теремки"],
    "Зелена лінія": ["Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота", "Палац спорту", "Кловська", "Печерська", "Дружби народів", "Видубичі", "Славутич", "Осокорки", "Позняки", "Харківська", "Вирлиця", "Бориспільська", "Червоний хутір"]
}

# Додамо вершини та ребра для кожної лінії метро з вагами
for line, stops in stations.items():
    G.add_nodes_from(stops)
    G.add_edges_from([(stops[i], stops[i+1], {'weight': 1}) for i in range(len(stops) - 1)])

# Додамо декілька перехідних ребер з вагами
transfer_edges = [
    ("Театральна", "Золоті ворота", 1),
    ("Хрещатик", "Майдан Незалежності", 1),
    ("Палац спорту", "Площа Льва Толстого", 1)
]
for u, v, w in transfer_edges:
    G.add_edge(u, v, weight=w)

# Візуалізуємо граф
pos = nx.spring_layout(G)  # Розташування вершин
plt.figure(figsize=(15, 10))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Карта метро міста Київ з вагами ребер")
plt.show()

# Алгоритм Дейкстри
def dijkstra(graph, start):
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node is not None:
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node, data in destinations.items():
            weight = data['weight'] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return shortest_paths
        
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    return shortest_paths

# Знаходимо найкоротші шляхи від Академмістечка до всіх інших станцій
start_station = "Академмістечко"
shortest_paths = dijkstra(G, start_station)

# Виводимо найкоротші шляхи та відстані
for destination in shortest_paths:
    path = []
    node = destination
    while node is not None:
        path.append(node)
        node = shortest_paths[node][0]
    path = path[::-1]
    print(f"Найкоротший шлях від {start_station} до {destination}: {' -> '.join(path)} з відстанню {shortest_paths[destination][1]}")

# Візуалізація графа з найкоротшими шляхами від Академмістечка
plt.figure(figsize=(15, 10))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=10)
nx.draw_networkx_nodes(G, pos, nodelist=[start_station], node_color='green', node_size=3000)
nx.draw_networkx_edges(G, pos, edgelist=[(shortest_paths[node][0], node) for node in shortest_paths if shortest_paths[node][0] is not None], edge_color='red')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Найкоротші шляхи від Академмістечка")
plt.show()
