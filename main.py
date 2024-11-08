class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена на {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден.")


# Создание объектов класса Store
grocery_store = Store("Продукты", "Профсоюзная")
grocery_store.add_item("яблоки", 0.5)
grocery_store.add_item("бананы", 0.75)

shoe_store = Store("Обувь", "Красная")
shoe_store.add_item("кроссовки", 50.0)
shoe_store.add_item("ботинки", 70.0)

clothing_store = Store("Одежда", "Крыловка")
clothing_store.add_item("футболка", 15.0)
clothing_store.add_item("джинсы", 30.0)

# Тестирование методов на примере магазина продуктов
print("\nТестирование магазина продуктов:")
grocery_store.add_item("апельсины", 0.65)
print("Цена яблок:", grocery_store.get_price("яблоки"))
grocery_store.update_price("яблоки", 0.55)
print("Обновленная цена яблок:", grocery_store.get_price("яблоки"))
grocery_store.remove_item("бананы")
print("Цена бананов после удаления:", grocery_store.get_price("бананы"))