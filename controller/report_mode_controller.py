from view.output_manager import OutputManager
from datetime import datetime
import pandas as pd
import numpy as np

class ReportModeController:
    def __init__(self, input_manager, db_controller):
        self._input_man = input_manager
        self._db_controller = db_controller

    def run(self):
        OutputManager.print_report_menu()
        try:
            choice = self._input_man.report_options()
        except:
            OutputManager.print_invalid_option()
            self.run()
            return

        if choice == "sales_period":
            self.sales_on_period()
            self.run()

        elif choice == "sold":
            self.most_sold_items()
            self.run()

        elif choice == "revenue":
            self.most_revenue_contributors_items()
            self.run()

        elif choice == "sales_highest":
            self.highest_sales_num_days()
            self.run()

        elif choice == "exit":
            OutputManager.print_exiting_msg()
            return

        else:
            OutputManager.print_invalid_option()
            self.run()


    def sales_on_period(self):
        OutputManager.print_dataframe(self.sales_on_period_aux())
        OutputManager.waiting_key_msg()
        self._input_man.waiting_any_key()


    def sales_on_period_aux(self):
        try:
            OutputManager.print_sales_period("start")
            start_date = datetime.strptime(self._input_man.report_period_date(), "%Y-%m-%d").timestamp()
            OutputManager.print_sales_period("end")
            end_date = datetime.strptime(self._input_man.report_period_date() + " 23:59:59", "%Y-%m-%d %H:%M:%S").timestamp()
        except:
            OutputManager.print_invalid_option()
            self.sales_on_period_aux()
            return
        sales = self._db_controller.read("timestamp >= {0} and timestamp <= {1}".format(start_date, end_date), "sales")
        return sales


    def most_sold_items(self):
        sales_table = self._db_controller.read(None, "sales")
        most_sold_items = self._most_sold_items_aux(sales_table, 10)
        OutputManager.print_dataframe(most_sold_items)
        OutputManager.waiting_key_msg()
        self._input_man.waiting_any_key()


    @staticmethod
    def _most_sold_items_aux(table, limit=10):
        table_grouped = table.groupby(["name"])
        table_grouped = table_grouped['quantity'].sum()
        table_grouped = table_grouped.sort_values(ascending=False)
        return table_grouped.head(limit)


    def most_revenue_contributors_items(self):
        OutputManager.print_dataframe(self.revenue_contributors())
        OutputManager.waiting_key_msg()
        self._input_man.waiting_any_key()

    
    def revenue_contributors(self):
        try:
            OutputManager.print_output_limit()
            limit = self._input_man.report_output_limit()
        except:
            OutputManager.print_invalid_option()

        sales = self._db_controller.read(None, "sales")
        revenue = pd.DataFrame({"name": sales["name"], "revenue": sales["quantity"] * sales["price"]})
        best_revenues = revenue.groupby("name").sum().sort_values(by="revenue", ascending=False)

        if limit is None:
            return best_revenues

        return best_revenues.head(limit)


    def highest_sales_num_days(self):
        sales_table = self._db_controller.read(None, "sales")
        highest_sales_num_days = self._highest_sales_num_days_aux(sales_table, 10)
        OutputManager.print_dataframe(highest_sales_num_days)
        OutputManager.waiting_key_msg()
        self._input_man.waiting_any_key()


    @staticmethod
    def _highest_sales_num_days_aux(table, limit=10):
        days = table['datestring'].str.slice(0, 10)
        days, count = np.unique(days, return_counts=True)
        df = pd.DataFrame({"day": days, "sales num": count}).set_index('day')
        df = df['sales num'].sort_values(ascending=False).head(limit)
        return df


    def export_report(self):
        pass
