import filecmp
from unittest import TestCase
from shutil import rmtree
import os

from main import run_app

class SystemTest(TestCase):
    def setUp(self):
        current_dir = os.path.dirname(__file__)
        self.inputs = os.path.join(current_dir, 'inputs')
        self.outputs = os.path.join(current_dir, 'outputs')
        self.temp = os.path.join(current_dir, 'temp')
        if os.path.exists(self.temp):
            rmtree(self.temp)
        os.mkdir(self.temp)

    # def tearDown(self):
    #     rmtree(self.temp)

    def test_add_items_and_read_inventory2(self):
        run_app(
            'test_db', 
            from_file=True, 
            file_path=os.path.join(self.inputs, '1.in'), 
            to_file=True, 
            outfile_path=os.path.join(self.temp, 'test1.out')
        )
        self.assertTrue(
            filecmp.cmp(
                os.path.join(self.temp, 'test1.out') , 
                os.path.join(self.outputs, 'test1.out')
                )
        )
    