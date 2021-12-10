from communication.database_controller import DatabaseController
from controller.main_controller import MainController
from view.input_manager import InputManager
import argparse
import sys, os

os.environ['DO_CLEAR'] = "True"
def run_app(database_name, from_file=False, file_path=None, to_file=False, outfile_path=None):
    """
    Runs the application.
    """
    if from_file:
        os.environ['DO_CLEAR'] = "False"
        sys.stdin = open(file_path)

    if to_file:
        os.environ['DO_CLEAR'] = "False"
        sys.stdout = open(outfile_path, 'w')
    
    input_man = InputManager()
    db_controller = DatabaseController(database_name)
    main_controller = MainController(input_manager=input_man,db_controller=db_controller)
    main_controller.run()

    db_controller.save_database()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sistema da Panificadora Alpha")

    parser.add_argument("-f", "--from_file", help="Usa um arquivo de entrada", action="store_true")
    parser.add_argument("-p", "--file_path", help="Caminho do arquivo de entrada", type=str, default='')
    parser.add_argument("-d", "--database_name", help="Nome do banco de dados", type=str, default='test_db')
    parser.add_argument("-o", "--to_file", help="Usa um arquivo de saída", action="store_true")
    parser.add_argument("-op", "--outfile_path", help="Caminho do arquivo de saída", type=str, default='')
    args = parser.parse_args()
    run_app(args.database_name, args.from_file, args.file_path, args.to_file, args.outfile_path)

