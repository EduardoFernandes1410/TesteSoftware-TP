from controller.cashier_mode_controller import CashierModeController
from controller.report_mode_controller import ReportModeController
from controller.manager_mode_controller import ManagerModeController
# from view.input_manager import InputManager
from view.output_manager import OutputManager


class MainController:
    def __init__(self, input_manager, db_controller):
        self._db_controller = db_controller
        self._input_man = input_manager

    def run(self):
        OutputManager.print_menu()
        choice = self._input_man.mode()

        options = {
            'cashier': CashierModeController,
            'manager': ManagerModeController,
            'report': ReportModeController
        }

        self._run_auxiliar(choice, options)

    def _run_auxiliar(self, choice, options):
        if choice in options.keys():
            mode_controller = options[choice](
                input_manager = self._input_man,
                db_controller = self._db_controller
                )
            mode_controller.run()

        elif choice == "exit":
            OutputManager.print_exiting_msg()
            return 
        
        else:
            OutputManager.print_invalid_option()
            self.run()


