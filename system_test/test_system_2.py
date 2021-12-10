import filecmp
from unittest import TestCase
from shutil import rmtree
import sys, os

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

    def tearDown(self):
        # rmtree(self.temp)
        pass

    def run_test(self, in_file, out_file):
        run_app(
            'test_db', 
            from_file=True, 
            file_path=os.path.join(self.inputs, in_file), 
            to_file=True, 
            outfile_path=os.path.join(self.temp, out_file)
        )

        result = filecmp.cmp(
            os.path.join(self.temp, out_file) , 
            os.path.join(self.outputs, out_file)
        )

        return result

    def test_opening_manager_mode_and_exit(self):
        result = self.run_test('1.in', 'test1.out')
        self.assertTrue(result)


    # def test_add_items_and_read_inventory(self):
    #     result = self.run_test('2.in', 'test2.out')
    #     self.assertTrue(result)
    