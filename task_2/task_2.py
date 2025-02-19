from BTrees.OOBTree import OOBTree
from sortedcontainers import SortedDict
import timeit
import pandas as pd


df = pd.read_csv(r"D:\projects\Github\goit-algo2-hw-03\task_2\generated_items_data.csv")

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
sd = SortedDict()
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
def range_query_tree():
    pass

def range_query_dict():
    pass

add_item_to_tree("shirt", "Clothes", 100)



