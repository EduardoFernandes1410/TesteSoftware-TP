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

