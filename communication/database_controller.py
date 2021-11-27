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
        df.to_pickle(os.path.join(self._database_path, "products.pkl"))


    def create_sales_table(self):
        df = pd.DataFrame(columns=['timestamp', 'datestring', 'name', 'quantity', 'price'])
        df.to_pickle(os.path.join(self._database_path, "sales.pkl"))

    
    def validate(self, sale):
        # checa se as quantitades são possiveis e soma o valor total
        pass


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


    def read(self, query, table):
        if(table == "products"):
            return self._products.query(query)
        if(table == "sales"):
            return self._sales.query(query)


    def update_database(self, product, price, quantity):
        pass