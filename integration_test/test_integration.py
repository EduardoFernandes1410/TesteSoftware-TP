from unittest import TestCase
import pandas as pd
import os
import shutil
from communication.database_controller import DatabaseController

class IntegrationTest(TestCase):
    def setUp(self):
        self.db_controller = DatabaseController("integration_db")

    def tearDown(self):
        shutil.rmtree("integration_db")


    def test_insert_product(self):
        self.db_controller.insert_new_product("batata", 12.90, 12)
        df = self.db_controller.read("name == 'batata'", "products")
        self.assertEqual(len(df), 1)



