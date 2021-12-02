from unittest import TestCase
import pandas as pd
import os
from communication.database_controller import DatabaseController

class DatabaseControllerTest(TestCase):
    def setUp(self):
        self.df = pd.DataFrame([["batata", 10.90, 95]], columns=['name', 'price', 'quantity'])


    def test_get_product_quantity_success(self):
        qtd = DatabaseController.get_product_quantity_aux("batata", self.df)
        self.assertEqual(qtd, 95)


    def test_get_product_quantity_not_found_exception(self):
        with self.assertRaises(Exception):
            qtd = DatabaseController.get_product_quantity_aux("arroz", self.df)


    def test_get_product_price_success(self):
        price = DatabaseController.get_product_price_aux("batata", self.df)
        self.assertEqual(price, 10.90)


    def test_get_product_price_not_found_exception(self):
        with self.assertRaises(Exception):
            price = DatabaseController.get_product_price_aux("arroz", self.df)


    def test_check_product_existence_true(self):
        exists = DatabaseController.check_product_existence_aux("batata", self.df)
        self.assertTrue(exists)


    def test_check_product_existence_false(self):
        exists = DatabaseController.check_product_existence_aux("arroz", self.df)
        self.assertFalse(exists)


    def test_validate_sale_aux_correct_total_price(self):
        self.df = self.df.append({
                'name': "arroz",
                'price': 5.99,
                'quantity': 2
        }, ignore_index=True)

        sale = {"batata": 2, "arroz": 1}
        price = DatabaseController.validate_sale_aux(sale, self.df)
        self.assertEqual(price, 27.79)


    def test_validate_sale_aux_not_enough_items_exception(self):
        self.df = self.df.append({
                'name': "arroz",
                'price': 5.99,
                'quantity': 2
        }, ignore_index=True)

        sale = {"batata": 2, "arroz": 10}
        with self.assertRaises(Exception):
            price = DatabaseController.validate_sale_aux(sale, self.df)


    def test_validate_sale_aux_item_not_found_exception(self):
        self.df = self.df.append({
                'name': "arroz",
                'price': 5.99,
                'quantity': 2
        }, ignore_index=True)

        sale = {"batata": 2, "tomate": 10}
        with self.assertRaises(Exception):
            price = DatabaseController.validate_sale_aux(sale, self.df)