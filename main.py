from controller.main_controller import MainController
from view.input_manager import InputManager


input_man = InputManager()
main_controller = MainController(input_manager=input_man,db_controller= None)
main_controller.run()

    