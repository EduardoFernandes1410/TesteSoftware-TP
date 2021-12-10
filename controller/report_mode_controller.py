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

        elif choice == "sales_lowest":
            self.lowest_sales_num_days()
            self.run()
        
        elif choice == "exit":
            OutputManager.print_exiting_msg()
            return

        else:
            OutputManager.print_invalid_option()
            self.run()


    def sales_on_period(self):
        OutputManager.print_sales_period("start")
        start_date = self._input_man.report_period_date()
        OutputManager.print_sales_period("end")
        end_date = self._input_man.report_period_date()

        try:
            sales_table = self._db_controller.read(None, "sales")
            information = self.sales_on_period_aux(sales_table, start_date, end_date)
        except:
            OutputManager.print_invalid_option()
            return

        OutputManager.print_dataframe(information)
        OutputManager.waiting_key_msg()
        self._input_man.waiting_any_key()


    @staticmethod
    def sales_on_period_aux(table, start_date_string, end_date_string):
        try:
            start_date = datetime.strptime(start_date_string, "%Y-%m-%d").timestamp()
            end_date = datetime.strptime(end_date_string + " 23:59:59", "%Y-%m-%d %H:%M:%S").timestamp()
        except:
            raise Exception()

        sales = table.query("timestamp >= {0} and timestamp <= {1}".format(start_date, end_date))
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
        try:
            OutputManager.print_output_limit()
            limit = self._input_man.report_output_limit()
        except:
            OutputManager.print_invalid_option()
            self.most_revenue_contributors_items()
            return

        OutputManager.print_dataframe(self.most_revenue_contributors_items_aux(sales = self._db_controller.read(None, "sales"), limit = limit))
        OutputManager.waiting_key_msg()
        self._input_man.waiting_any_key()

    
    @staticmethod
    def most_revenue_contributors_items_aux(sales, limit):
        revenue = pd.DataFrame({"name": sales["name"], "revenue": sales["quantity"] * sales["price"]})
        if revenue.empty:
            return revenue
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


    def lowest_sales_num_days(self):
        sales_table = self._db_controller.read(None, "sales")
        lowest_sales_num_days = self._lowest_sales_num_days_aux(sales_table, 10)
        OutputManager.print_dataframe(lowest_sales_num_days)
        OutputManager.waiting_key_msg()
        self._input_man.waiting_any_key()


    @staticmethod
    def _highest_sales_num_days_aux(table, limit=10):
        days = table['datestring'].str.slice(0, 10)
        days, count = np.unique(days, return_counts=True)
        df = pd.DataFrame({"day": days, "sales num": count}).set_index('day')
        df = df['sales num'].sort_values(ascending=False).head(limit)
        return df

    @staticmethod
    def _lowest_sales_num_days_aux(table, limit=10):
        days = table['datestring'].str.slice(0, 10)
        days, count = np.unique(days, return_counts=True)
        df = pd.DataFrame({"day": days, "sales num": count}).set_index('day')
        df = df['sales num'].sort_values(ascending=True).head(limit)
        return df

    
