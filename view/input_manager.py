class InputManager:
    def __init__(self):
        pass

    def mode(self):
        x = int(input())

        if x == 1:
            return "cashier"
        elif x == 2:
            return "manager"
        elif x == 3:
            return "report"
        elif x == 4:
            return "exit"

    def cashier_options(self):
        x = int(input())

        if x == 1:
            return "open_sale"
        elif x == 2:
            return "exit"

    def open_sale_options(self):
        x = int(input())
        if x == 1:
            return "add_product"
        elif x == 2:
            return "remove_product"
        elif x == 3:
            return "close_sale"
        elif x == 4:
            return "exit"

    def sale_finished(self):
        x = int(input())
        if x == 1:
            return "ok"
        elif x == 2:
            return "nok"
    
    def adding_product_data(self):
        raw_input = input().split(' ')
        qtd = int(raw_input[-1])
        product = ' '.join(raw_input[:-1])
        return product, int(qtd)

    def remove_product_data(self):
        product = input()
        return product

        