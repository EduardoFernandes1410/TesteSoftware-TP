from unittest import TestCase
from unittest.mock import patch, MagicMock
from view.input_manager import InputManager

@patch('view.input_manager.input')
class TestInputManager(TestCase):
    def setUp(self):
        self.input_manager = InputManager()

    def test_choose_cashier_mode(self, mock_input):
        mock_input.return_value='1'
        self.assertEqual(self.input_manager.mode(), "cashier")

    
    def test_choose_manager_mode(self, mock_input):
        mock_input.return_value='2'
        self.assertEqual(self.input_manager.mode(), "manager")

    
    def test_choose_report_mode(self, mock_input):
        mock_input.return_value='3'
        self.assertEqual(self.input_manager.mode(), "report")

    
    def test_choose_main_exit(self, mock_input):
        mock_input.return_value='4'
        self.assertEqual(self.input_manager.mode(), "exit")

    
    def test_choose_invalid_mode(self, mock_input):
        mock_input.return_value='foo'
        self.assertRaises(ValueError, InputManager().mode)

    
    def test_choose_open_sale(self, mock_input):
        mock_input.return_value='1'
        self.assertEqual(self.input_manager.cashier_options(), "open_sale")

    
    def test_choose_exit_cashier_mode(self, mock_input):
        print("+"*300)
        mock_input.return_value='2'
        self.assertEqual(self.input_manager.cashier_options(), "exit")

    
    def test_choose_sale_option(self, mock_input):
        mock_input.return_value='foo'
        self.assertRaises(ValueError, InputManager().cashier_options)

    def test_choose_add_product(self, mock_input):
        mock_input.return_value='1'
        self.assertEqual(self.input_manager.open_sale_options(), "add_product")

    def test_choose_remove_product(self, mock_input):
        mock_input.return_value='2'
        self.assertEqual(self.input_manager.open_sale_options(), "remove_product")

    def test_choose_close_sale(self, mock_input):
        mock_input.return_value='3'
        self.assertEqual(self.input_manager.open_sale_options(), "close_sale")

    def test_choose_exit_sale(self, mock_input):
        mock_input.return_value='4'
        self.assertEqual(self.input_manager.open_sale_options(), "exit")

    def test_adding_valid_product(self, mock_input):
        mock_input.return_value = 'test-item 1'
        self.assertEqual(self.input_manager.adding_product_data(), ("test-item", 1))

    def test_adding_valid_product_with_spaces(self, mock_input):
        mock_input.return_value = 'test item 1'
        self.assertEqual(self.input_manager.adding_product_data(), ("test item", 1))

    def test_adding_invalid_product(self, mock_input):
        mock_input.return_value = 'test-item not-number'
        self.assertRaises(Exception, self.input_manager.adding_product_data)

    def test_remove_product(self, mock_input):
        mock_input.return_value = "testing"
        self.assertEqual(self.input_manager.remove_product_data(), "testing")

    def test_sale_finished_ok(self, mock_input):
        mock_input.return_value = "1"
        self.assertEqual(self.input_manager.sale_finished(), "ok")

    def test_sale_finished_nok(self, mock_input):
        mock_input.return_value = "2"
        self.assertEqual(self.input_manager.sale_finished(), "nok")

    def test_inserting_item_data(self, mock_input):
        mock_input.return_value = "pao de batata 5 1.5"
        name, qtd, price = self.input_manager.inserting_item_data()
        self.assertEqual(name, "pao de batata")
        self.assertEqual(qtd, 5)
        self.assertEqual(price, 1.5)
        
    def test_updating_item_data(self, mock_input):
        mock_input.return_value = "pao de batata 1.5"
        name, price = self.input_manager.updating_product_price()
        self.assertEqual(name, "pao de batata")
        self.assertEqual(price, 1.5)
        
    def test_removing_item_data(self, mock_input):
        mock_input.return_value = "pao de batata"
        name = self.input_manager.removing_product()
        self.assertEqual(name, "pao de batata")

    def test_report_options(self, mock_input):
        mock_input.return_value = "3"
        self.assertEqual(self.input_manager.report_options(), "revenue")

    def test_manager_options(self, mock_input):
        mock_input.return_value = "3"
        self.assertEqual(self.input_manager.manager_options(), "remove_product")

    def test_report_output_limit(self, mock_input):
        mock_input.return_value = "5"
        self.assertEqual(self.input_manager.report_output_limit(), 5)

    def test_report_output_limit_none(self, mock_input):
        mock_input.return_value = None
        self.assertEqual(self.input_manager.report_output_limit(), None)