import pandas as pd

class DatabaseController:
    def __init__(self, database_path):
        pass
        # if nao existe -> create else read

    def create_database(self):
        # pd.DataFrame(columns=['product', 'price', 'quantity'])
        # pd.to_pickle(arquivo)
        pass

    def read_database(self):
        pass
    
    def validate(self, sale):
        # checa se as quantitades são possiveis e soma o valor total
        pass

    def write(self, product, price, quantity):
        pass

    def read(self, query):
        pass

    def update_database(self, product, price, quantity):
        pass