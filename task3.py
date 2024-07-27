# Завдання 3
# Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: 
# додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.

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
plt.savefig("graph1.png")  # Збереження зображення графа
plt.show()

# Реалізація DFS (Depth-First Search)
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

# Реалізація BFS (Breadth-First Search)
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
start, goal = "Києво-Печерська Лавра", "Андріївський узвіз"
path_dfs = dfs(G, start, goal)
path_bfs = bfs(G, start, goal)

print(f"Шлях від {start} до {goal} за допомогою DFS: {path_dfs}")
print(f"Шлях від {start} до {goal} за допомогою BFS: {path_bfs}")

# Пояснення результатів
explanation = """
Пояснення результатів:
DFS (глибини пошуку) йде по глибоких шляхах до тих пір, поки не досягне цілі або не повернеться назад. 
Це означає, що DFS може знайти шлях, який не є найкоротшим, особливо якщо в графі є кілька шляхів до цілі.
BFS (ширини пошуку) йде по всіх сусідніх вершинах, перш ніж перейти на наступний рівень глибини, тому знаходить найкоротший шлях у графі.
"""
print(explanation)

# Створення документа markdown
readme_content = f"""
# Порівняння алгоритмів DFS та BFS для знаходження шляхів у графі

## Опис
Цей документ містить порівняння алгоритмів DFS (глибини пошуку) та BFS (ширини пошуку) для знаходження шляхів у графі, що моделює транспортну мережу туристичних місць Києва.

## Граф
Мережа включає такі туристичні місця:
1. Києво-Печерська Лавра
2. Софійський собор
3. Золоті ворота
4. Майдан Незалежності
5. Андріївський узвіз

Графічне представлення мережі:

![Граф](graph.png)

## Результати пошуку

### Шлях від "Києво-Печерська Лавра" до "Андріївський узвіз"

#### DFS (глибини пошуку)
- Шлях: {path_dfs}

#### BFS (ширини пошуку)
- Шлях: {path_bfs}

## Пояснення результатів
DFS (глибини пошуку) йде по глибоких шляхах до тих пір, поки не досягне цілі або не повернеться назад. Це означає, що DFS може знайти шлях, який не є найкоротшим, особливо якщо в графі є кілька шляхів до цілі.

BFS (ширини пошуку) йде по всіх сусідніх вершинах, перш ніж перейти на наступний рівень глибини, тому знаходить найкоротший шлях у графі.

## Висновки
- **DFS** може знайти будь-який шлях до цілі, але не завжди найкоротший.
- **BFS** завжди знаходить найкоротший шлях, якщо всі ребра мають однакову вагу.

На основі отриманих результатів, алгоритм BFS краще підходить для знаходження найкоротшого шляху в графах з рівними вагами ребер.
"""

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node is not None:
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph[current_node][next_node]['weight'] + weight_to_current_node
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

# Знаходження найкоротших шляхів від кожної вершини до кожної іншої вершини
shortest_paths_all = {}
for node in G.nodes:
    shortest_paths_all[node] = dijkstra(G, node)

# Оновлення markdown документа з результатами алгоритму Дейкстри
readme_content += "\n## Найкоротші шляхи за алгоритмом Дейкстри\n"

for start_node, paths in shortest_paths_all.items():
    readme_content += f"\n### Найкоротші шляхи від {start_node}:\n"
    for end_node in paths:
        path = []
        current_node = end_node
        while current_node is not None:
            path.append(current_node)
            next_node = paths[current_node][0]
            current_node = next_node
        path = path[::-1]
        readme_content += f"- до {end_node}: {path} з вагою {paths[end_node][1]}\n"

# Збереження оновленого документа markdown
with open("README.md", "w", encoding="utf-8") as md_file:
    md_file.write(readme_content)

print("Документ README.md оновлено з результатами алгоритму Дейкстри")
