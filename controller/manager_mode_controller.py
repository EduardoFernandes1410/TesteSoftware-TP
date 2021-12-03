from view.output_manager import OutputManager


class ManagerModeController:

    def __init__(self,input_manager, db_controller):
        self._db_controller = db_controller
        self.input_manager = input_manager

    def run(self):
        OutputManager.print_manager_menu()
        
        try:
            choice = self._input_man.cashier_options()
        except:
            OutputManager.print_invalid_input()
            self.run()
            return

        if choice == 'register_product':
            self.insert_item()
        if choice == 'update_price':
            self.update_price()
        if choice == 'remove_product':
            self.remove_item()
        if choice == 'update_inventory':
            self.modify_inventory_qtd()
        elif choice == 'exit':
            OutputManager.print_exiting_msg()
            return
        else:
            OutputManager.print_invalid_option()
            self.run()

    def insert_item(self, name, price, quantity):
        OutputManager.print_inserting_item()
        name, quantity, price = self._input_man.inserting_item_data()
        try:
            self.db_controller.insert_new_product(name, price, quantity)
        except Exception as e:
            OutputManager.print_existent_product()

    def remove_item(self, name):
        try:
            self.db_controller.remove_item(name)
        except Exception as e:
            OutputManager.not_in_inventory_error()

    def update_price(self, name, price):
        OutputManager.print_updating_price()
        name, price = self._input_man.updating_product_price()
        try:
            self.db_controller.update_price(name, price)
        except Exception as e:
            OutputManager.not_in_inventory_error()

    def modify_inventory_qtd(self, name, qtd):
        name, delta_quantity = self._input_man.adding_product_data()
        OutputManager.print_updating_price()
        try:
            self.db_controller.update_inventory_quantity(name, delta_quantity)
        except Exception as e:
            OutputManager.not_in_inventory_error()

