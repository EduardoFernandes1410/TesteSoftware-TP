from unittest import TestCase
from unittest.mock import MagicMock, patch, Mock
from controller.manager_mode_controller import ManagerModeController

class TestManagerModeController(TestCase):
    def setUp(self):
        
        self.input_man = MagicMock()  
        self.db_cont = MagicMock()

    def test_insert_item(self):
        self.input_man.inserting_item_data.return_value = ('batata doce', 4.49, 12)
        manager_mode_controller = ManagerModeController(self.input_man, self.db_cont)
        manager_mode_controller.insert_item()
        self.db_cont.insert_new_product.assert_called_with('batata doce', 12, 4.49)

    @patch("controller.manager_mode_controller.OutputManager")
    def test_insert_item_invalid(self, mock_out):
        self.input_man.inserting_item_data.return_value = ('batata doce', 4.49, 12)
        manager_mode_controller = ManagerModeController(self.input_man, self.db_cont)
        self.db_cont.insert_new_product.side_effect = Exception()
        manager_mode_controller.insert_item()
        mock_out.print_existent_product.assert_called_once()
        
    def test_remove_item(self):
        self.input_man.removing_product.return_value = ('batata doce')
        manager_mode_controller = ManagerModeController(self.input_man, self.db_cont)
        manager_mode_controller.remove_item()
        self.db_cont.remove_product.assert_called_with('batata doce')

    @patch("controller.manager_mode_controller.OutputManager")
    def test_remove_item_invalid(self, mock_out):
        self.input_man.removing_product.return_value = ('batata doce')
        manager_mode_controller = ManagerModeController(self.input_man, self.db_cont)
        self.db_cont.remove_product.side_effect = Exception()
        manager_mode_controller.remove_item()
        mock_out.not_in_inventory_error.assert_called_once()
        
    def test_update_item(self):
        self.input_man.updating_product_price.return_value = ('batata doce', 4.49)
        manager_mode_controller = ManagerModeController(self.input_man, self.db_cont)
        manager_mode_controller.update_price()
        self.db_cont.update_price.assert_called_with('batata doce', 4.49)

    @patch("controller.manager_mode_controller.OutputManager")
    def test_update_item_invalid(self, mock_out):
        self.input_man.updating_product_price.return_value = ('batata doce', 4.49)
        manager_mode_controller = ManagerModeController(self.input_man, self.db_cont)
        self.db_cont.update_price.side_effect = Exception()
        manager_mode_controller.update_price()
        mock_out.not_in_inventory_error.assert_called_once()
        
    def test_modify_inventory_qtd(self):
        self.input_man.adding_product_data.return_value = ('batata doce', 12)
        manager_mode_controller = ManagerModeController(self.input_man, self.db_cont)
        manager_mode_controller.modify_inventory_qtd()
        self.db_cont.update_inventory_quantity.assert_called_with('batata doce', 12)

    @patch("controller.manager_mode_controller.OutputManager")
    def test_modify_inventory_qtd_invalid(self, mock_out):
        self.input_man.adding_product_data.return_value = ('batata doce', 12)
        manager_mode_controller = ManagerModeController(self.input_man, self.db_cont)
        self.db_cont.update_inventory_quantity.side_effect = Exception()
        manager_mode_controller.modify_inventory_qtd()
        mock_out.not_in_inventory_error.assert_called_once()
        
