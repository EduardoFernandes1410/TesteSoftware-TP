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

    
    def test_most_sold_items(self):
        most_sold_item = ReportModeController._most_sold_items_aux(self.sales)
        items = ['melancia', 'abacaxi', 'maca', 'laranja', 'batata']
        self.assertEqual(list(most_sold_item.index), items)

    def test_most_sold_items_with_limit(self):
        most_sold_item = ReportModeController._most_sold_items_aux(self.sales, 2)
        self.assertEqual(most_sold_item.index[0], 'melancia')
        self.assertEqual(most_sold_item.index[1], 'abacaxi')
        self.assertEqual(len(most_sold_item),2)

    def test_highest_sales_num_days(self):
        highest_sales_num_days = ReportModeController._highest_sales_num_days_aux(self.sales)
        self.assertEqual(highest_sales_num_days.index[0], '02/01/2021')

    def test_lowest_sales_num_days(self):
        lowest_sales_num_days = ReportModeController._lowest_sales_num_days_aux(self.sales)
        self.assertEqual(lowest_sales_num_days.index[0], '01/01/2021')
    
    def test_most_revenue_contributor_items(self):
        revenue_contributor = ReportModeController.most_revenue_contributors_items_aux(self.sales, limit=None)
        indexes_ans = ['melancia', 'abacaxi', 'maca', 'laranja', 'batata']
        values_ans = [125.0, 80.0, 45.0, 20.0, 5.0]
        values_received = [x[0] for x in list(revenue_contributor.values)]
        self.assertEqual(list(revenue_contributor.index), indexes_ans)
        self.assertEqual(values_received, values_ans)

    def test_most_revenue_contributor_items_with_limit(self):
        revenue_contributor = ReportModeController.most_revenue_contributors_items_aux(self.sales, limit=2)
        indexes_ans = ['melancia', 'abacaxi']
        values_ans = [125.0, 80.0]
        values_received = [x[0] for x in list(revenue_contributor.values)]
        self.assertEqual(list(revenue_contributor.index), indexes_ans)
        self.assertEqual(values_received, values_ans)