import json

import matplotlib.pyplot as plt
import pandas as pd


class Product:
    def __init__(self, category, name, price, unit, manufacturer, article):
        self.category = category
        self.name = name
        self.price = price
        self.unit = unit
        self.manufacturer = manufacturer
        self.article = article
        self.quantity_received = 0
        self.quantity_shipped = 0

    def receive(self, quantity):
        self.quantity_received += quantity

    def ship(self, quantity):
        if quantity <= self.quantity_received - self.quantity_shipped:
            self.quantity_shipped += quantity
        else:
            print("Not enough quantity available for shipment.")

    def get_stock(self):
        return self.quantity_received - self.quantity_shipped

    def display_info(self):
        print(f"Category: {self.category}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Unit: {self.unit}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Article: {self.article}")
        print(f"Stock: {self.get_stock()}")
        print("--------------------")

    def to_dict(self):
        return {
            "Category": self.category,
            "Name": self.name,
            "Price": self.price,
            "Unit": self.unit,
            "Manufacturer": self.manufacturer,
            "Article": self.article,
            "QuantityReceived": self.quantity_received,
            "QuantityShipped": self.quantity_shipped,
        }


class Inventory:
    def __init__(self, filename="inventory_data.json"):
        self.products = []
        self.filename = filename
        self.load_data()

    def add_product(self, product):
        self.products.append(product)
        self.save_data()

    def receive_product(self, article, quantity):
        for product in self.products:
            if product.article == article:
                product.receive(quantity)
                self.save_data()
                return
        print(f"Product with article {article} not found.")

    def ship_product(self, article, quantity):
        for product in self.products:
            if product.article == article:
                product.ship(quantity)
                self.save_data()
                return
        print(f"Product with article {article} not found.")

    def display_stock(self):
        for product in self.products:
            product.display_info()

    def display_all_products(self):
        data = [product.to_dict() for product in self.products]
        df = pd.DataFrame(data)
        print(df)

    def plot_demand_supply_ratio(self):
        data = {"Name": [], "Demand/Supply Ratio": []}
        for product in self.products:
            data["Name"].append(product.name)
            data["Demand/Supply Ratio"].append(
                product.quantity_shipped / product.quantity_received
            )

        df = pd.DataFrame(data)
        df.plot(x="Name", y="Demand/Supply Ratio", kind="bar")
        plt.title("Demand/Supply Ratio for Products")
        plt.show()

    def save_data(self):
        data = [product.to_dict() for product in self.products]
        with open(self.filename, "w") as file:
            json.dump(data, file)

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                for item in data:
                    product = Product(
                        item["Category"],
                        item["Name"],
                        item["Price"],
                        item["Unit"],
                        item["Manufacturer"],
                        item["Article"],
                    )
                    product.quantity_received = item["QuantityReceived"]
                    product.quantity_shipped = item["QuantityShipped"]
                    self.products.append(product)
        except FileNotFoundError:
            pass


def main():
    inventory = Inventory()

    while True:
        print("\n1. Add Product")
        print("2. Receive Product")
        print("3. Ship Product")
        print("4. Display Stock")
        print("5. Display All Products")
        print("6. Plot Demand/Supply Ratio")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            category = input("Enter category: ")
            name = input("Enter name: ")
            price = float(input("Enter price: "))
            unit = input("Enter unit: ")
            manufacturer = input("Enter manufacturer: ")
            article = input("Enter article: ")

            product = Product(category, name, price, unit, manufacturer, article)
            inventory.add_product(product)

        elif choice == "2":
            article = input("Enter article: ")
            quantity = int(input("Enter quantity received: "))
            inventory.receive_product(article, quantity)

        elif choice == "3":
            article = input("Enter article: ")
            quantity = int(input("Enter quantity shipped: "))
            inventory.ship_product(article, quantity)

        elif choice == "4":
            inventory.display_stock()

        elif choice == "5":
            inventory.display_all_products()

        elif choice == "6":
            inventory.plot_demand_supply_ratio()

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
