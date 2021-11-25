import os
from time import sleep
class OutputManager:

    @staticmethod
    def print_menu():
        os.system('clear')
        print("=======================")
        print("Welcome\n")
        print('1 - Cashier mode')
        print('2 - Manager mode')
        print('3 - Report mode')
        print('4 - Exit')
        print("=======================")
        print("Choice: ", end='')

    @staticmethod
    def print_invalid_option():
        print("Invalid option.")
        sleep(1)

    @staticmethod
    def print_exiting_msg():
        pass