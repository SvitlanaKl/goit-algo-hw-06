# Завдання 2

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

# Додаємо вершини та ребра для кожної лінії метро
for line, stops in stations.items():
    G.add_nodes_from(stops)
    G.add_edges_from([(stops[i], stops[i+1]) for i in range(len(stops) - 1)])

# Візуалізуємо граф
pos = nx.spring_layout(G)  # Розташування вершин
plt.figure(figsize=(15, 10))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=10)
plt.title("Карта метро міста Київ")
plt.show()

# DFS (Depth-First Search)
def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    path.append(start)
    visited.add(start)
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path.copy(), visited)
            if result is not None:
                return result
    return None

# BFS (Breadth-First Search)
def bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                queue.append((neighbor, path + [neighbor]))
    return None

# Знаходимо шляхи за допомогою DFS та BFS
start, goal = "Академмістечко", "Червоний хутір"
path_dfs = dfs(G, start, goal)
path_bfs = bfs(G, start, goal)

print(f"Шлях від {start} до {goal} за допомогою DFS: {path_dfs}")
print(f"Шлях від {start} до {goal} за допомогою BFS: {path_bfs}")

# Пояснення результатів
print("\nПояснення результатів:")
print("DFS (глибини пошуку) йде по глибоких шляхах до тих пір, поки не досягне цілі або не повернеться назад.")
print("BFS (ширини пошуку) йде по всіх сусідніх вершинах, перш ніж перейти на наступний рівень глибини, тому знаходить найкоротший шлях у графі.")
