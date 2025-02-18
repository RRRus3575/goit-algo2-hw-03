import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.DiGraph()

edges = [
    ("Термінал 1",	"Склад 1", 25),
    ("Термінал 1",	"Склад 2",	20),
    ("Термінал 1", "Склад 3", 15),
("Термінал 2", "Склад 3", 15),
("Термінал 2", "Склад 4", 30),
("Термінал 2", "Склад 2", 10),
("Склад 1", "Магазин 1", 15),
("Склад 1", "Магазин 2", 10),
("Склад 1", "Магазин 3", 20),
("Склад 2", "Магазин 4", 15),
("Склад 2", "Магазин 5", 10),
("Склад 2", "Магазин 6", 25),
("Склад 3", "Магазин 7", 20),
("Склад 3", "Магазин 8", 15),
("Склад 3", "Магазин 9", 10),
("Склад 4", "Магазин 10", 20),
("Склад 4", "Магазин 11", 10),
("Склад 4", "Магазин 12", 15),
("Склад 4", "Магазин 13", 5),
("Склад 4", "Магазин 14", 10),
]

G.add_weighted_edges_from(edges)

G.add_node("Джерело")
G.add_node("Сток")

cap_terminal_1 = sum(weight for u, v, weight in edges if u == "Термінал 1")
cap_terminal_2 = sum(weight for u, v, weight in edges if u == "Термінал 2")

#Додаємо віртуальне джерело
G.add_edge("Джерело", "Термінал 1", capacity=cap_terminal_1)
G.add_edge("Джерело", "Термінал 2", capacity=cap_terminal_2)

cap_shops = {f"Магазин {i}": 0 for i in range(1, 15)}
for u, v, weight in edges:
    if "Магазин" in v:
        cap_shops[v] += weight

for shop, cap in cap_shops.items():
    G.add_edge(shop, "Сток", capacity=cap)

# Викотристовуємо алгоритм Едмондса-Карпа
flow_value, flow_dict = nx.maximum_flow(G, "Джерело", "Сток", flow_func=nx.algorithms.flow.edmonds_karp)

# Вивід результатів
print(f"Максимальний потік у системі: {flow_value}")
print("Розподіл потоку:")
for u, v_flow in flow_dict.items():
    for v, flow in v_flow.items():
        if flow > 0:  # Показываем только потоки > 0
            print(f"{u} → {v}: {flow}")

pos = {
    "Термінал 1": (-3, 0),
    "Термінал 2": (3, 0),
    "Склад 1": (-1, 3),
    "Склад 2": (1, 3),
    "Склад 3": (-1, -3),
    "Склад 4": (1, -3),
    "Магазин 1": (-7, 7),
    "Магазин 2": (-4, 7),
    "Магазин 3": (-1, 7),
    "Магазин 4": (1, 7),
    "Магазин 5": (4, 7),
    "Магазин 6": (7, 7),
    "Магазин 7": (-7, -7),
    "Магазин 8": (-4, -7),
    "Магазин 9": (-1, -7),
    "Магазин 10": (1, -7),
    "Магазин 11": (3, -7),
    "Магазин 12": (5, -7),
    "Магазин 13": (7, -7),
    "Магазин 14": (9, -7),
    "Джерело": (-5, 0),
    "Сток": (11, 0),
}

# Малюємо граф
plt.figure(figsize=(12, 7))
nx.draw(G, pos, with_labels=True, node_size=2500, node_color="skyblue", font_size=8, font_weight="bold", arrows=True)
labels = {edge: "" for edge in G.edges()} 
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Відображаємо граф
plt.title("Логістична мережа")
plt.show()