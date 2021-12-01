from unittest import TestCase
from unittest.mock import patch, MagicMock
from view.input_manager import InputManager

@patch('view.input_manager.input')
class TestInputManager(TestCase):
    
    def test_choose_cashier_mode(self, mock_input):
        mock_input.return_value='1'
        input_manager = InputManager()
        self.assertEqual(input_manager.mode(), "cashier")

    
    def test_choose_manager_mode(self, mock_input):
        mock_input.return_value='2'
        input_manager = InputManager()
        self.assertEqual(input_manager.mode(), "manager")

    
    def test_choose_report_mode(self, mock_input):
        mock_input.return_value='3'
        input_manager = InputManager()
        self.assertEqual(input_manager.mode(), "report")

    
    def test_choose_main_exit(self, mock_input):
        mock_input.return_value='4'
        input_manager = InputManager()
        self.assertEqual(input_manager.mode(), "exit")

    
    def test_choose_invalid_mode(self, mock_input):
        mock_input.return_value='foo'
        self.assertRaises(ValueError, InputManager().mode)

    
    def test_choose_open_sale(self, mock_input):
        mock_input.return_value='1'
        input_manager = InputManager()
        self.assertEqual(input_manager.cashier_options(), "open_sale")

    
    def test_choose_exit_sale(self, mock_input):
        mock_input.return_value='2'
        input_manager = InputManager()
        self.assertEqual(input_manager.cashier_options(), "exit")

    
    def test_choose_sale_option(self, mock_input):
        mock_input.return_value='foo'
        self.assertRaises(ValueError, InputManager().cashier_options)

    def test_choose_add_product(self, mock_input):
        mock_input.return_value='1'
        input_manager = InputManager()
        self.assertEqual(input_manager.open_sale_options(), "add_product")

    def test_choose_remove_product(self, mock_input):
        mock_input.return_value='2'
        input_manager = InputManager()
        self.assertEqual(input_manager.open_sale_options(), "remove_product")

    def test_choose_close_sale(self, mock_input):
        mock_input.return_value='3'
        input_manager = InputManager()
        self.assertEqual(input_manager.open_sale_options(), "close_sale")

    def test_choose_exit_sale(self, mock_input):
        mock_input.return_value='4'
        input_manager = InputManager()
        self.assertEqual(input_manager.open_sale_options(), "exit")

    def test_adding_valid_product(self, mock_input):
        mock_input.return_value = 'test-item 1'
        input_manager = InputManager()
        self.assertEqual(input_manager.adding_product_data(), ("test-item", 1))

    def test_adding_valid_product_with_spaces(self, mock_input):
        mock_input.return_value = 'test item 1'
        input_manager = InputManager()
        self.assertEqual(input_manager.adding_product_data(), ("test item", 1))

    def test_adding_invalid_product(self, mock_input):
        mock_input.return_value = 'test-item not-number'
        input_manager = InputManager()
        self.assertRaises(Exception, input_manager.adding_product_data)

    def test_remove_product(self, mock_input):
        mock_input.return_value = "testing"
        input_manager = InputManager()
        self.assertEqual(input_manager.remove_product_data(), "testing")