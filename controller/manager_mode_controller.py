from view.output_manager import OutputManager


class ManagerModeController:

    def __init__(self,input_manager, db_controller):
        self._db_controller = db_controller
        self._input_man = input_manager

    def run(self):
        OutputManager.print_manager_menu()
        
        try:
            choice = self._input_man.manager_options()
        except:
            OutputManager.print_invalid_input()
            self.run()
            return

        if choice == 'register_product':
            self.insert_item()
            self.run()
        if choice == 'update_price':
            self.update_price()
            self.run()
        if choice == 'remove_product':
            self.remove_item()
            self.run()
        if choice == 'update_inventory':
            self.modify_inventory_qtd()
            self.run()
        elif choice == "check_inventory":
            self.check_stock()
            self.run()
        elif choice == 'exit':
            OutputManager.print_exiting_msg()
            return
        else:
            OutputManager.print_invalid_option()
            self.run()

    def insert_item(self):
        OutputManager.print_inserting_item()
        
        try:
            name, quantity, price = self._input_man.inserting_item_data()
        except Exception as e:
            OutputManager.print_invalid_input()
            self.insert_item()
            return
        
        try:
            self._db_controller.insert_new_product(name, price, quantity)
        except Exception as e:
            OutputManager.print_existent_product()

    def remove_item(self):
        OutputManager.print_removing_product()
        
        try:
            name = self._input_man.removing_product()
        except Exception as e:
            OutputManager.print_invalid_input()
            self.remove_item()
            return
        try:
            self._db_controller.remove_product(name)
        except Exception as e:
            OutputManager.not_in_inventory_error()

    def update_price(self):
        OutputManager.print_updating_price()
        
        try:
            name, price = self._input_man.updating_product_price()
        except Exception as e:
            OutputManager.print_invalid_input()
            self.update_price()
            return
        
        try:
            self._db_controller.update_inventory_price(name, price)
        except Exception as e:
            OutputManager.not_in_inventory_error()

    def modify_inventory_qtd(self):
        OutputManager.print_modifying_inventory_qtd()
        
        try:
            name, delta_quantity = self._input_man.adding_product_data()
        except Exception as e:
            OutputManager.print_invalid_input()
            self.modify_inventory_qtd()
            return
        
        try:
            self._db_controller.update_inventory_quantity(name, delta_quantity)
        except Exception as e:
            OutputManager.not_in_inventory_error()

    def check_stock(self):
        inventory = self._db_controller.read(None, 'products')
        OutputManager.print_dataframe(inventory)
        OutputManager.waiting_key_msg()
        self._input_man.waiting_any_key()
