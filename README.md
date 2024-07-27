
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
- Шлях: ['Києво-Печерська Лавра', 'Софійський собор', 'Золоті ворота', 'Майдан Незалежності', 'Андріївський узвіз']

#### BFS (ширини пошуку)
- Шлях: ['Києво-Печерська Лавра', 'Андріївський узвіз']

## Пояснення результатів
DFS (глибини пошуку) йде по глибоких шляхах до тих пір, поки не досягне цілі або не повернеться назад. Це означає, що DFS може знайти шлях, який не є найкоротшим, особливо якщо в графі є кілька шляхів до цілі.

BFS (ширини пошуку) йде по всіх сусідніх вершинах, перш ніж перейти на наступний рівень глибини, тому знаходить найкоротший шлях у графі.

## Висновки
- **DFS** може знайти будь-який шлях до цілі, але не завжди найкоротший.
- **BFS** завжди знаходить найкоротший шлях, якщо всі ребра мають однакову вагу.

На основі отриманих результатів, алгоритм BFS краще підходить для знаходження найкоротшого шляху в графах з рівними вагами ребер.

## Найкоротші шляхи за алгоритмом Дейкстри

### Найкоротші шляхи від Києво-Печерська Лавра:
- до Києво-Печерська Лавра: ['Києво-Печерська Лавра'] з вагою 0
- до Софійський собор: ['Києво-Печерська Лавра', 'Софійський собор'] з вагою 3
- до Андріївський узвіз: ['Києво-Печерська Лавра', 'Андріївський узвіз'] з вагою 4
- до Майдан Незалежності: ['Києво-Печерська Лавра', 'Майдан Незалежності'] з вагою 2
- до Золоті ворота: ['Києво-Печерська Лавра', 'Майдан Незалежності', 'Золоті ворота'] з вагою 3

### Найкоротші шляхи від Софійський собор:
- до Софійський собор: ['Софійський собор'] з вагою 0
- до Києво-Печерська Лавра: ['Софійський собор', 'Києво-Печерська Лавра'] з вагою 3
- до Золоті ворота: ['Софійський собор', 'Золоті ворота'] з вагою 1
- до Майдан Незалежності: ['Софійський собор', 'Майдан Незалежності'] з вагою 2
- до Андріївський узвіз: ['Софійський собор', 'Майдан Незалежності', 'Андріївський узвіз'] з вагою 4

### Найкоротші шляхи від Золоті ворота:
- до Золоті ворота: ['Золоті ворота'] з вагою 0
- до Софійський собор: ['Золоті ворота', 'Софійський собор'] з вагою 1
- до Майдан Незалежності: ['Золоті ворота', 'Майдан Незалежності'] з вагою 1
- до Києво-Печерська Лавра: ['Золоті ворота', 'Майдан Незалежності', 'Києво-Печерська Лавра'] з вагою 3
- до Андріївський узвіз: ['Золоті ворота', 'Майдан Незалежності', 'Андріївський узвіз'] з вагою 3

### Найкоротші шляхи від Майдан Незалежності:
- до Майдан Незалежності: ['Майдан Незалежності'] з вагою 0
- до Золоті ворота: ['Майдан Незалежності', 'Золоті ворота'] з вагою 1
- до Андріївський узвіз: ['Майдан Незалежності', 'Андріївський узвіз'] з вагою 2
- до Києво-Печерська Лавра: ['Майдан Незалежності', 'Києво-Печерська Лавра'] з вагою 2
- до Софійський собор: ['Майдан Незалежності', 'Софійський собор'] з вагою 2

### Найкоротші шляхи від Андріївський узвіз:
- до Андріївський узвіз: ['Андріївський узвіз'] з вагою 0
- до Майдан Незалежності: ['Андріївський узвіз', 'Майдан Незалежності'] з вагою 2
- до Києво-Печерська Лавра: ['Андріївський узвіз', 'Києво-Печерська Лавра'] з вагою 4
- до Золоті ворота: ['Андріївський узвіз', 'Майдан Незалежності', 'Золоті ворота'] з вагою 3
- до Софійський собор: ['Андріївський узвіз', 'Майдан Незалежності', 'Софійський собор'] з вагою 4
