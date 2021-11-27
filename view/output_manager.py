import os
from time import sleep
class OutputManager:

    @staticmethod
    def print_menu():
        # os.system('clear')
        print("=======================")
        print("Welcome\n")
        print('1 - Cashier mode')
        print('2 - Manager mode')
        print('3 - Report mode')
        print('4 - Exit')
        print("=======================")
        print("Choice: ", end='')

    @staticmethod
    def print_cashier_menu():
        # os.system('clear')
        print("=======================")
        print("Cashier mode\n")
        print('1 - Init sale')
        print('2 - Exit')
        print("=======================")
        print("Choice: ", end='')

    @staticmethod
    def print_open_sale_menu(sale):
        # os.system('clear')
        print("=======================")
        print("SALE\n")
        for k,v in sale.items():
            print(k, ": ", v)
        if len(sale) > 0:
            print()
        print('1 - Add product')
        print('2 - Remove product')
        print('3 - Finish sale')
        print('4 - Exit')
        print("=======================")
        print("Choice: ", end='')
    
    @staticmethod
    def print_adding_product():
        print("Product name and quantity: ", end='')

    @staticmethod
    def print_removing_product():
        print("Product name: ", end='')

    @staticmethod
    def print_invalid_option():
        print("Invalid option.")
        sleep(1)

    @staticmethod
    def print_exiting_msg():
        print("Exiting...")
        sleep(1)

    @staticmethod
    def not_in_inventory_error():
        print("Fail. Product not in inventory.")
        sleep(1)

    @staticmethod
    def print_msg(msg):
        print(msg)
        sleep(1)