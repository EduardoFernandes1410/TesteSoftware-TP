from view.output_manager import OutputManager
from datetime import datetime
import pandas as pd

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
        elif choice == "sold":
            self.most_sold_items()
        elif choice == "revenue":
            self.most_revenue_contributors_items()
        elif choice == "sales_highest":
            self.highest_sales_num_days()
        elif choice == "exit":
            OutputManager.print_exiting_msg()
            return
        else:
            OutputManager.print_invalid_option()
            self.run()

    def sales_on_period(self):
        OutputManager.print_dataframe(self.sales_on_period_aux())

    def sales_on_period_aux(self):
        try:
            OutputManager.print_sales_period("start")
            start_date = datetime.strptime(self._input_man.report_period_date(), "%Y-%m-%d").timestamp()
            OutputManager.print_sales_period("end")
            end_date = datetime.strptime(self._input_man.report_period_date(), "%Y-%m-%d").timestamp()
        except:
            OutputManager.print_invalid_option()
            self.sales_on_period_aux()
            return
        sales = self._db_controller.read("timestamp >= {0} and timestamp <= {1}".format(start_date, end_date), "sales")        
        return sales

    def most_sold_items(self, limit=10):
        pass

    def most_revenue_contributors_items(self):
        OutputManager.print_dataframe(self.revenue_contributors())
    
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
    @staticmethod
    def _most_sold_items_aux(table):
        table_grouped = table.groupby(["name"])
        table_grouped = table_grouped['quantity'].sum()
        table_grouped = table_grouped.sort_values(ascending=False)
        return table_grouped
        
    def most_revenue_contributors_items(self, limit=10):
        pass

    def highest_sales_num_days(self, limit=10):
        pass
    def export_report(self):
        pass
