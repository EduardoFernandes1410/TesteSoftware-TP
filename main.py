from communication.database_controller import DatabaseController
from controller.main_controller import MainController
from view.input_manager import InputManager


input_man = InputManager()
db_controller = DatabaseController('test_db')

# db_controller.insert_new_product("batata", 5, 1.0)
# db_controller.insert_new_product("laranja", 10, 2.0)
# db_controller.insert_new_product("maca", 15, 3.0)
# db_controller.insert_new_product("abacaxi", 20, 4.0)
# db_controller.insert_new_product("melancia", 25, 5.0)

main_controller = MainController(input_manager=input_man,db_controller=db_controller)
main_controller.run()

db_controller.save_database()