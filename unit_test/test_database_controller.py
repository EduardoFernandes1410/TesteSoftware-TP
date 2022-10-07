from unittest import TestCase
from xml.dom import minicompat
import pandas as pd
import os
from communication.database_controller import DatabaseController
from hypothesis import given
from hypothesis.strategies import fixed_dictionaries, text, floats, integers, data

class DatabaseControllerTest(TestCase):
    def setUp(self):
        self.df = pd.DataFrame([["batata", 10.90, 95]], columns=['name', 'price', 'quantity'])


    def test_get_product_quantity_success(self):
        qtd = DatabaseController.get_product_quantity_aux("batata", self.df)
        self.assertEqual(qtd, 95)


    @given(text(min_size=1).filter(lambda x: x != "batata"))
    def test_get_product_quantity_not_found_exception(self, product_name):
        with self.assertRaises(Exception):
            qtd = DatabaseController.get_product_quantity_aux(product_name, self.df)


    def test_get_product_price_success(self):
        price = DatabaseController.get_product_price_aux("batata", self.df)
        self.assertEqual(price, 10.90)


    @given(text(min_size=1).filter(lambda x: x != "batata"))
    def test_get_product_price_not_found_exception(self, product_name):
        with self.assertRaises(Exception):
            price = DatabaseController.get_product_price_aux(product_name, self.df)


    def test_check_product_existence_true(self):
        exists = DatabaseController.check_product_existence_aux("batata", self.df)
        self.assertTrue(exists)


    @given(text(min_size=1).filter(lambda x: x != "batata"))
    def test_check_product_existence_false(self, product_name):
        exists = DatabaseController.check_product_existence_aux(product_name, self.df)
        self.assertFalse(exists)


    @given(fixed_dictionaries({
        "name": text(min_size=1).filter(lambda x: x != "batata"),
        "price": floats(min_value=0.01, max_value=10000.),
        "quantity": integers(min_value=1, max_value=10000)
    }))
    def test_validate_sale_aux_correct_total_price(self, product_dict):
        new_df = pd.concat([self.df, pd.DataFrame(product_dict, index=[0])], ignore_index=True)
        sale = {"batata": 2, product_dict["name"]: product_dict["quantity"]}
        price = DatabaseController.validate_sale_aux(sale, new_df)
        self.assertEqual(price, 21.80 + (product_dict["price"] * product_dict["quantity"]))


    @given(
        fixed_dictionaries({
            "name": text(min_size=1).filter(lambda x: x != "batata"),
            "price": floats(min_value=0.01, max_value=10000.),
            "quantity": integers(min_value=1, max_value=10000)
        }),
        data()
    )
    def test_validate_sale_aux_not_enough_items_exception(self, product_dict, data):
        new_df = pd.concat([self.df, pd.DataFrame(product_dict, index=[0])], ignore_index=True)
        qtd = data.draw(integers(min_value=product_dict["quantity"]+1))
        sale = {"batata": 2, "arroz": qtd}
        with self.assertRaises(Exception):
            price = DatabaseController.validate_sale_aux(sale, new_df)


    @given(text(min_size=1).filter(lambda x: x != "batata"))
    def test_validate_sale_aux_item_not_found_exception(self, product_name):
        sale = {"batata": 2, product_name: 10}
        with self.assertRaises(Exception):
            price = DatabaseController.validate_sale_aux(sale, self.df)