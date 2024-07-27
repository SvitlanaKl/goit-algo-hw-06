# Завдання 2
# Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.

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
plt.savefig("graph.png")  # Збереження зображення графа
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
markdown_content = f"""
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

# Збереження документа markdown
with open("readme.md", "w", encoding="utf-8") as md_file:
    md_file.write(markdown_content)

print("Документ збережено як readme.md")


