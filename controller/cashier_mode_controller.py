from view.output_manager import OutputManager


class CashierModeController:
    def __init__(self, input_manager, db_controller):
        self._input_man = input_manager
        self._db_controller = db_controller
        self._sale = dict()

    def run(self):
        OutputManager.print_cashier_menu()
        try:
            choice = self._input_man.cashier_options()
        except:
            OutputManager.print_invalid_option()
            self.run()
            return

        if choice == 'open_sale':
            self.open_sale()
        elif choice == 'exit':
            OutputManager.print_exiting_msg()
            return
        else:
            OutputManager.print_invalid_option()
            self.run()

    def open_sale(self):
        OutputManager.print_open_sale_menu(self.sale)
        try:
            option = self._input_man.open_sale_options()
        except:
            OutputManager.print_invalid_option()
            self.open_sale()
            return
        if option == "add_product":
            self.add_item()
            self.open_sale()
            
        elif option == "remove_product":
            self.remove_item()
            self.open_sale()

        elif option == "close_sale":
            self.finish_sale()
            self.open_sale()

        elif option == "exit":
            return
        else:
            OutputManager.print_invalid_option()
            self.open_sale()

    def add_item(self):
        OutputManager.print_adding_product()
        product, qtd = self._input_man.adding_product_data()
        if self._db_controller.check_product_existence(product):
            self._sale[product] = qtd
        else:
            OutputManager.print_not_existent_product()

    def remove_item(self):
        OutputManager.print_removing_product()
        product = self._input_man.remove_product_data()
        del self._sale[product]

    def finish_sale(self):
        try:
            total_price = self._db_controller.validate_sale(self.sale)
            OutputManager.print_sale_total(total_price)
            status = self._input_man.sale_finished()
            if status == "ok":
                self.register_sale()
        except Exception as e:
            OutputManager.print_msg(e)
        self._sale = dict()

    def register_sale(self):
        self._db_controller.register_new_sale(self.sale)

    @property
    def sale(self):
        return self._sale


    

