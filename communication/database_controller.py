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


    @staticmethod
    def check_product_existence_aux(name, table):
        product = table[table["name"] == name]
        if(len(product) == 0):
            return False
        return True


    def check_product_existence(self, name):
        return DatabaseController.check_product_existence_aux(name, self._products)


    def get_product_quantity_aux(name, table):
        if(not DatabaseController.check_product_existence_aux(name, table)):
            raise Exception("Item not found")

        product = table[table["name"] == name]
        return product.quantity.values[0]


    def get_product_quantity(self, name):
        return self.get_product_quantity_aux(name, self._products)


    def get_product_price_aux(name, table):
        if(not DatabaseController.check_product_existence_aux(name, table)):
            raise Exception("Item not found")

        product = table[table["name"] == name]
        return product.price.values[0]


    def get_product_price(self, name):
        return self.get_product_price_aux(name, self._products)

    
    def validate_sale_aux(sale, table):
        """ checa se as quantidades são possiveis e soma o valor total """
        total_price = 0
        for name, quantity in sale.items():
            if(DatabaseController.get_product_quantity_aux(name, table) < quantity):
                raise Exception("Not enough items in inventory")

            total_price += (DatabaseController.get_product_price_aux(name, table) * quantity)

        return total_price


    def validate_sale(self, sale):
        return self.validate(sale, self._products)


    def insert_new_product(self, name, price, quantity):
        if(self.check_product_existence(name)):
            raise Exception("Product already in database")

        self._products = self._products.append({
            'name': name,
            'price': price,
            'quantity': quantity
        }, ignore_index=True);


    def register_new_sale(self, products):
        timestamp = datetime.now().timestamp()
        datestring = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for name, quantity in products.items():
            price = self.get_product_price(name)
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
        if(not self.check_product_existence(name)):
            raise Exception("Product not found in database")

        self._products.loc[self._products["name"] == name, 'price'] = new_price


    def update_inventory_quantity(self, name, delta_quantity):
        if(not self.check_product_existence(name)):
            raise Exception("Product not found in database")

        self._products.loc[self._products["name"] == name, 'quantity'] += delta_quantity
        self._products.loc[self._products["name"] == name, 'quantity'] = max(
            0,  
            self._products.loc[self._products["name"] == name, 'quantity'][0]
        )


    def save_database(self):
        self._products.to_pickle(os.path.join(self._database_path, "products.pkl"))
        self._sales.to_pickle(os.path.join(self._database_path, "sales.pkl"))




# x = DatabaseController('test_db')
# x.insert_new_product('banana', price=10, quantity=100)
# x.insert_new_product('maca', price=5, quantity=100)
# x.insert_new_product('laranja', price=2, quantity=100)
# print(x._products)
# print(x._sales)
# del x