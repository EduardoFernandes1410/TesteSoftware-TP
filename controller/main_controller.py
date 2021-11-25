from controller.cashier_mode_controller import CashierModeController
from view.input_manager import InputManager
from view.output_manager import OutputManager


class MainController:
    def __init__(self, input_manager):
        self._input_man = input_manager

    def run(self):
        OutputManager.print_menu()
        choice = self._input_man.mode()

        if choice == "cashier":
            cashier_mode = CashierModeController(input_manager = self._input_man)
            cashier_mode.run()

        elif choice == "manager":
            pass

        elif choice == "report":
            pass

        elif choice == "exit":
            return 
        
        else:
            OutputManager.print_invalid_option()
            self.run()


