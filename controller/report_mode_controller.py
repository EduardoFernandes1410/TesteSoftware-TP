from view.output_manager import OutputManager

class ReportModeController:
    def __init__(self, input_manager, db_controller):
        self._input_man = input_manager
        self._db_controller = db_controller

    def run(self):
        OutputManager.print_report_menu()
        choice = self._input_man.report_options()
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
        pass

    def most_sold_items(self, limit=10):
        pass

    def most_revenue_contributors_items(self, limit=10):
        pass

    def highest_sales_num_days(self, limit=10):
        pass

    def export_report(self):
        pass
