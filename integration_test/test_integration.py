from unittest import TestCase
from unittest.mock import patch, MagicMock
import pandas as pd
import os
import shutil
from communication.database_controller import DatabaseController
from view.input_manager import InputManager
from controller.cashier_mode_controller import CashierModeController
from controller.manager_mode_controller import ManagerModeController

class IntegrationTest(TestCase):
    def setUp(self):
        self.db_controller = DatabaseController("integration_db")
        self.input_manager = InputManager()

    def tearDown(self):
        shutil.rmtree("integration_db")


    def test_insert_save_and_verify(self):
        self.db_controller.insert_new_product("batata", 12.90, 12)
        self.db_controller.save_database()

        self.db_controller = DatabaseController("integration_db")
        df = self.db_controller.read("name == 'batata'", "products")
        self.assertEqual(len(df), 1)

    @patch("builtins.input")
    def test_insert_sell_and_remove(self, mock_input):
        self.db_controller.insert_new_product("batata_doce", 14.50, 20)
        cashier_controller = CashierModeController(self.input_manager, self.db_controller)
        mock_input.return_value = "batata_doce 10"
        cashier_controller.add_item()
        mock_input.return_value = "1"
        cashier_controller.finish_sale()
        self.db_controller.remove_product("batata_doce")
        sales_data = self.db_controller.read("name == 'batata_doce'", "sales")
        self.assertEqual(len(sales_data), 1)

    @patch("builtins.input")
    def test_insert_product_make_sale_check_quantity(self, mock_input):
        self.db_controller.insert_new_product("batata", 12.90, 12)
        cashier_controller = CashierModeController(self.input_manager, self.db_controller)
        mock_input.return_value = "batata 5"
        cashier_controller.add_item()
        mock_input.return_value = "1"
        cashier_controller.finish_sale()
        quantity = self.db_controller.get_product_quantity("batata")
        self.assertEqual(quantity, 7)


    def test_insert_product(self):
        self.db_controller.insert_new_product("batata", 12.90, 12)
        df = self.db_controller.read("name == 'batata'", "products")
        self.assertEqual(len(df), 1)


    def test_insert_and_remove_product(self):
        self.db_controller.insert_new_product("batata", 12.90, 12)
        self.db_controller.remove_product("batata")
        df = self.db_controller.read("name == 'batata'", "products")
        self.assertEqual(len(df), 0)

    @patch("builtins.input")
    def test_insert_remove_and_sell(self, mock_input):
        self.db_controller.insert_new_product("batata", 12.90, 12)
        self.db_controller.remove_product("batata")

        cashier_controller = CashierModeController(self.input_manager, self.db_controller)
        mock_input.return_value = "batata 1"
        cashier_controller.add_item()
        sale = cashier_controller.sale
        self.assertRaises(Exception, self.db_controller.validate_sale)
        
    @patch("builtins.input")
    def test_insert_change_sale_product(self, mock_input):
        self.db_controller.insert_new_product("batata", 12.90, 12)
        self.db_controller.update_inventory_price("batata", 10.50)
        cashier_controller = CashierModeController(self.input_manager, self.db_controller)
        mock_input.return_value = "batata 2"
        cashier_controller.add_item()
        sale = cashier_controller.sale
        self.assertEqual(21, self.db_controller.validate_sale, sale)