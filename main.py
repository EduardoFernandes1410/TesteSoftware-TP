from communication.database_controller import DatabaseController
from controller.main_controller import MainController
from view.input_manager import InputManager


input_man = InputManager()
db_controller = DatabaseController('test_db')
db_controller.insert_new_product('banana', price=10, quantity=100)

main_controller = MainController(input_manager=input_man,db_controller=db_controller)
main_controller.run()

db_controller.save_database()