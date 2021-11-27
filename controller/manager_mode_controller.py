from view.output_manager import OutputManager


class ManagerModeController:

    def __init__(self,input_manager, db_controller):
        self._db_controller = db_controller
        self.input_manager = input_manager

    def run(self):
        """ 
        cadastrar produto
            add item e quantidade
        remover produto
            remove item e quantidade         
        recarregar estoque
        atualizar preco

        sair
        """
        pass

    def insert_item(self, name, price, quantity):
        try:
            self.db_controller.insert_new_item(name, price, quantity)
        except Exception as e:
            print("cannot insert, already in inventory")

    def remove_item(self, name):
        try:
            self.db_controller.remove_item(name)
        except Exception as e:
            OutputManager.not_in_inventory_error()

    def update_price(self, name, price):
        try:
            self.db_controller.update_price(name, price)
        except Exception as e:
            OutputManager.not_in_inventory_error()

    def modify_inventory_qtd(self, name, qtd):
        try:
            self.db_controller.reload_inventory()
        except Exception as e:
            OutputManager.not_in_inventory_error()

