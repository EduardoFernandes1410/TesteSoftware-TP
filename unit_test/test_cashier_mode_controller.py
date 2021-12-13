from unittest import TestCase
from unittest.mock import MagicMock, patch, Mock
from controller.cashier_mode_controller import CashierModeController


class TestCashierModeController(TestCase):
    def setUp(self):
        self.input_man = MagicMock()  
        self.db_cont = MagicMock()

    def test_empty_sale_at_begining(self):
        self.input_man.open_sale_options.return_value = 'exit'
        cashier_mode_controller = CashierModeController(self.input_man, self.db_cont)
        cashier_mode_controller.open_sale()
        self.assertEqual(cashier_mode_controller.sale, {})

    
    def test_add_item_to_sale(self):
        self.input_man.adding_product_data.return_value = 'test-item', 10
        self.input_man.open_sale_options.return_value = 'exit'
        cashier_mode_controller = CashierModeController(self.input_man, self.db_cont)
        cashier_mode_controller.add_item()
        self.assertEqual(cashier_mode_controller.sale, {'test-item': 10})

    
    def test_remove_item_from_sale(self):
        self.input_man.adding_product_data.return_value = 'test-item', 10
        self.input_man.open_sale_options.side_effect = ['add_product', 'remove_product', 'exit']
        self.input_man.remove_product_data.return_value = 'test-item'
        self.db_cont.check_product_existence.return_value=True
        cashier_mode_controller = CashierModeController(self.input_man, self.db_cont)
        cashier_mode_controller.open_sale()
        self.assertEqual(cashier_mode_controller.sale, {})

    @patch('controller.cashier_mode_controller.OutputManager')
    def test_finish_sale_ok(self, mock_output):
        self.db_cont.validate_sale.return_value = 15
        cashier_mode_controller = CashierModeController(self.input_man, self.db_cont)
        cashier_mode_controller.finish_sale()
        mock_output.print_sale_total.assert_called_with(15)

    @patch('controller.cashier_mode_controller.OutputManager')
    def test_finish_sale_nok(self, output_man):
        self.db_cont.validate_sale.side_effect = Exception()
        cashier_mode_controller = CashierModeController(self.input_man, self.db_cont)
        cashier_mode_controller.finish_sale()
        output_man.print_msg.assert_called()