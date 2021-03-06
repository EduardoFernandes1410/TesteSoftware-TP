import os
from time import sleep
import settings
class OutputManager:

    @staticmethod
    def print_menu():
        OutputManager._clear()
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
        OutputManager._clear()
        print("=======================")
        print("Cashier mode\n")
        print('1 - Init sale')
        print('2 - Exit')
        print("=======================")
        print("Choice: ", end='')

    @staticmethod
    def print_open_sale_menu(sale):
        OutputManager._clear()
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
    def print_sale_total(total):
        print("Total: R$ %.2f\n" % total)
        print("(1) Ok | (2) Not ok")
        print("Choice: ", end='')
        
    @staticmethod
    def print_exiting_msg():
        print("Exiting...")
        sleep(1)

    @staticmethod
    def not_in_inventory_error():
        print("Fail. Product not in inventory.")
        sleep(1)
    
    @staticmethod
    def not_in_sell_items_error():
        print("Error: the product is not in the current sell's item list.")
        sleep(1)

    @staticmethod
    def print_report_menu():
        OutputManager._clear()
        print("=======================")
        print("Report mode\n")
        print('1 - Sales on period')
        print('2 - Most sold items')
        print('3 - Revenue contributors')
        print('4 - Days with highest number of items sold')
        print('5 - Days with lowest number of items sold')
        print('6 - Exit')
        print("=======================")
        print("Choice: ", end='')
    
    @staticmethod
    def print_sales_period(limit):
        print("Enter period {} date in yyyy-mm-dd format: ".format(limit), end='')
    
    @staticmethod
    def print_output_limit():
        print("Enter the number of lines to show (press enter to show all lines): ", end='')

    @staticmethod
    def print_dataframe(df):
        print(df.to_markdown())

    @staticmethod
    def print_msg(msg):
        print(msg)
        sleep(1)

    @staticmethod
    def print_not_existent_product():
        print("Error. Not existent product.")
        sleep(1)

    @staticmethod
    def print_invalid_input():
        print("Fail. Input invalid.")
        sleep(1)
        
    @staticmethod
    def print_manager_menu():
        OutputManager._clear()
        print("=======================")
        print("Manager mode\n")
        print('1 - Register product')
        print('2 - Update price')
        print('3 - Remove product')
        print('4 - Update inventory')
        print('5 - Check Inventory')
        print('6 - Exit')
        print("=======================")
        print("Choice: ", end='')
        
    @staticmethod
    def print_inserting_item():
        print("Item name / quantity / price: ", end='')
        
    @staticmethod
    def print_existent_product():
        print("Cannot insert, product already in inventory")
        sleep(1)

    @staticmethod
    def print_updating_price():
        print("Product name and new price: ", end='')
        
    @staticmethod
    def print_modifying_inventory_qtd():
        print("Product name and new quantity: ", end='')

    @staticmethod
    def waiting_key_msg():
        print("Press any key to continue...")

    @staticmethod
    def _clear():
        if os.environ['DO_CLEAR'] == "True":
            os.system('cls' if os.name == 'nt' else 'clear')