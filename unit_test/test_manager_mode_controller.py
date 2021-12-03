from unittest import TestCase
from unittest.mock import MagicMock, patch, Mock
from controller.manager_mode_controller import ManagerModeController

class TestManagerModeController(TestCase):
    def setUp(self):
        
        self.input_man = MagicMock()  
        self.db_cont = MagicMock()

    # def test_insert_item(self):
    #     self.input_man.open_sale_options.return_value = 'exit'
    #     cashier_mode_controller = CashierModeController(self.input_man, self.db_cont)
    #     cashier_mode_controller.open_sale()
    #     self.assertEqual(cashier_mode_controller.sale, {})

    
    # def test_remove_item(self):
    #     self.input_man.adding_product_data.return_value = 'test-item', 10
    #     self.input_man.open_sale_options.return_value = 'exit'
    #     cashier_mode_controller = CashierModeController(self.input_man, self.db_cont)
    #     cashier_mode_controller.add_item()
    #     self.assertEqual(cashier_mode_controller.sale, {'test-item': 10})

    
    # def test_update_price(self):
    #     self.input_man.adding_product_data.return_value = 'test-item', 10
    #     self.input_man.open_sale_options.side_effect = ['remove_product', 'exit']
    #     self.input_man.remove_product_data.return_value = 'test-item'
    #     cashier_mode_controller = CashierModeController(self.input_man, self.db_cont)
    #     cashier_mode_controller.add_item()
    #     self.assertEqual(cashier_mode_controller.sale, {})

    def test_modify_inventory_qtd(self):
        self.input_man.adding_product_data.return_value = ('batata doce', 12)
        manager_mode_controller = ManagerModeController(self.input_man, self.db_cont)
        self.db_cont.update_inventory_quantity.return_value = True
        manager_mode_controller.modify_inventory_qtd()
        self.db_cont.update_inventory_quantity.assert_called_with('batata doce', 12)