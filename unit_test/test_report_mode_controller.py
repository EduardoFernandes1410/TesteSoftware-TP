from unittest import TestCase
from unittest.mock import patch, MagicMock
import pandas as pd
from controller.report_mode_controller import ReportModeController

class TestReportModeController(TestCase):
    def setUp(self):
        self.sales = pd.DataFrame(
            data = [
                [1, '01/01/2021 00:00:00', 'batata', 5, 1.0],
                [2, '01/01/2021 00:00:00', 'laranja', 10, 2.0],
                [3, '02/01/2021 00:00:00', 'maca', 15, 3.0],
                [4, '02/01/2021 00:00:00', 'abacaxi', 20, 4.0],
                [5, '02/01/2021 00:00:00', 'melancia', 25, 5.0],
                ],
            columns=['timestamp', 'datestring', 'name', 'quantity', 'price']
        )

    def test_most_sold_items_aux(self):
        most_sold_item = ReportModeController._most_sold_items_aux(self.sales, 3)
        self.assertEqual(most_sold_item.index[0], 'melancia')
        self.assertEqual(most_sold_item.index[1], 'abacaxi')
        self.assertEqual(most_sold_item.index[2], 'maca')

    def test_highest_sales_num_days(self):
        highest_sales_num_days = ReportModeController._highest_sales_num_days(self.sales)
        self.assertEqual(highest_sales_num_days.index[0], '02/01/2021')

    
