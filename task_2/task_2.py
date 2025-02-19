from BTrees.OOBTree import OOBTree
import timeit
import pandas as pd



df = pd.read_csv(r"./task_2/generated_items_data.csv")

# Створення OOBTree
tree = OOBTree()
# Додавання з файлу
for _, row in df.iterrows():
    tree[row["ID"]] = {
        "Name": row["Name"],
        "Category": row["Category"],
        "Price": row["Price"]
    }

# Створення dict
sd = {}
# Додавання з файлу
for _, row in df.iterrows():
    sd[row["ID"]]= {
        "Name": row["Name"],
        "Category": row["Category"],
        "Price": row["Price"]
    }


# Додавання об'єктів 
def add_item_to_tree(name, category, price):
   
    
    id = max(tree.keys()) + 1 if tree else 1

    tree[id] = {"Name": name, "Category": category, "Price": price}
    print(f"Товар {id} добавлен: {tree[id]}")


def add_item_to_dict(name, category, price):

    id = max(sd.keys()) + 1 if sd else 1
    sd[id] = {"Name": name, "Category": category, "Price": price}
    print(f"Товар {id} добавлен: {sd[id]}")



# Пошук об'єктів
def range_query_tree(min_price, max_price):
    return list(tree.items(min_price, max_price))

def range_query_dict(min_price, max_price):
    return [
        (key, value) for key, value in sd.items()
        if min_price <= value["Price"] <= max_price
    ]

# Збереження результатів у файл
def save_results_to_txt(file_path, time_tree, time_dict):
    
    with open(file_path, 'a', encoding="utf-8") as file:
        file.write(f"Тест продуктивності:\n")
        file.write(f"OOBTree: {time_tree:.6f} секунд (100 запитів)\n")
        file.write(f"dict: {time_dict:.6f} секунд (100 запитів)\n")
        file.write("=" * 40 + "\n")


# Тестування
min_price, max_price = 10, 80

time_tree = timeit.timeit(lambda: range_query_tree(min_price, max_price), number=100)
time_dict = timeit.timeit(lambda: range_query_dict(min_price, max_price), number=100)

print(f"Час виконання для OOBTree: {time_tree:.6f} секунд (100 запитів)")
print(f"Час виконання для dict: {time_dict:.6f} секунд (100 запитів)")


save_results_to_txt("./task_2/performance_results.txt", time_tree, time_dict)

