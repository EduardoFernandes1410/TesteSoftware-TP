from datetime import datetime
import pandas as pd
import os

class DatabaseController:
    def __init__(self, database_path):
        self._database_path = database_path

        # if nao existe -> create else read
        if(not os.path.isdir(database_path)):
            os.mkdir(database_path)

        if(not os.path.exists(os.path.join(database_path, "products.pkl"))):
            self.create_product_table()

        if(not os.path.exists(os.path.join(database_path, "sales.pkl"))):
            self.create_sales_table()

        self._products = pd.read_pickle(os.path.join(database_path, "products.pkl"))
        self._sales = pd.read_pickle(os.path.join(database_path, "sales.pkl"))


    def create_product_table(self):
        df = pd.DataFrame(columns=['name', 'price', 'quantity'])
        print(df)
        df.to_pickle(os.path.join(self._database_path, "products.pkl"))


    def create_sales_table(self):
        df = pd.DataFrame(columns=['timestamp', 'datestring', 'name', 'quantity', 'price'])
        print(df)

        df.to_pickle(os.path.join(self._database_path, "sales.pkl"))

    
    def validate(self, sale):
        """ checa se as quantidades são possiveis e soma o valor total """
        total_price = 0
        for name, quantity in self._products.items():
            if(self._products[self._products["name"] == name].quantity.values[0] < quantity):
                raise Exception("Not enough items in inventory")

            total_price += self._products[self._products["name"] == name].price.values[0]

        return total_price


    def insert_new_product(self, name, price, quantity):
        if(not name in self._products.name.values):
            self._products = self._products.append({
                'name': name,
                'price': price,
                'quantity': quantity
            }, ignore_index=True);
        else:
            raise Exception("Product already in database")


    def register_new_sale(self, products):
        timestamp = datetime.now().timestamp()
        datestring = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for name, quantity in products.items():
            price = self.read("name == '%s'" % name, "products").price.values[0]
            self._sales = self._sales.append({
                'timestamp': timestamp,
                'datestring': datestring,
                'name': name,
                'quantity': quantity,
                'price': price
            }, ignore_index=True)
            self.update_inventory_quantity(name, -quantity)


    def read(self, query, table):
        if(table == "products"):
            return self._products.query(query)
        if(table == "sales"):
            return self._sales.query(query)


    def update_inventory_price(self, name, new_price):
        if(name in self._products.name.values):
            self._products.loc[self._products["name"] == name, 'price'] = new_price
        else:
            raise Exception("Product not found in database")


    def update_inventory_quantity(self, name, delta_quantity):
        if(name in self._products.name.values):
            self._products.loc[self._products["name"] == name, 'quantity'] += delta_quantity
            self._products.loc[self._products["name"] == name, 'quantity'] = max(0,  self._products.loc[self._products["name"] == name, 'quantity'][0])
        else:
            raise Exception("Product not found in database")


    def __del__(self):
        self._products.to_pickle(os.path.join(self._database_path, "products.pkl"))
        self._sales.to_pickle(os.path.join(self._database_path, "sales.pkl"))
