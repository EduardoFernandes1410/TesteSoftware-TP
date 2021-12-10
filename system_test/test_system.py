import sys
import locale
from subprocess import Popen, PIPE
from unittest import TestCase
import shutil

class SystemTest(TestCase):
    def setUp(self):
        self.process = Popen([sys.executable, "main.py"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    
    """
    Esse método auxiliar executa uma sequência de comandos dada como string na linha de comando,
    capturando os valores na saída padrão (STDOUT) e eventuais erros (STDERR), que são retornados
    como uma tupla de listas de strings na forma (saída, erros). Cada string na lista representa um
    segmento da saida (uma saída vazia é dada como uma lista vazia). Os segmentos são delimitados por
    sequências de "clear" na saída. Esse método assume que o processo da aplicação (self.process) está
    devidamente inicializado e em execução (o que é sempre verdade se executado dentro dos métodos de teste).
    Ao executar em métodos de teste, apenas uma chamada deve ser feita e, idealmente, essa chamada contém 
    toda a sequência de entradas para executar uma ação e terminar o programa
    """
    def run_commands(self, commands):
        # Obtendo a codificação e a sequência de limpeza utiliada pelo SO
        encoding = locale.getpreferredencoding()
        clear_sequence = b'\x1b[H\x1b[2J\x1b[3J' if encoding == "UTF-8" else b'\e[1;1H\e[2J'
        # Executando a sequência de comandos especificada e obtendo os valores de STDOUT e STDERR
        output, error = self.process.communicate(commands.encode(encoding))
        # Separando as saídas em sequências delimitadas pela sequência de "clear"
        output_sequences = output.split(clear_sequence)
        error_sequences = error.split(clear_sequence)
        # Decodificando as sequências das saídas, desconsiderando strings vazias
        decoded_output = []
        for sequence in output_sequences:
            decoded_sequence = sequence.decode(encoding)
            if decoded_sequence:
                decoded_output.append(decoded_sequence)
        decoded_error = []
        for sequence in error_sequences:
            decoded_sequence = sequence.decode(encoding)
            if decoded_sequence:
                decoded_error.append(decoded_sequence)
        # Retornando as saídas devidamente decodificadas
        return decoded_output, decoded_error

    def test_add_items_and_read_inventory(self):
        # Executando ações para adicionar itens e ler o relatório de estoque
        output, error = self.run_commands("2\n1\nBatata 20 10.90\n1\nCenoura 100 7.50\n5\n\n6\n4\n")
        # Verificando que nenhum erro é retornado
        self.assertEqual([], error)
        # Verificando a antepenúltima sequência da saída, que deve corresponder ao relatório
        report_sequence = output[len(output) - 3]
        valid_report = """=======================
Manager mode

1 - Register product
2 - Update price
3 - Remove product
4 - Update inventory
5 - Check Inventory
6 - Exit
=======================
Choice: |    | name    |   price |   quantity |
|---:|:--------|--------:|-----------:|
|  0 | Batata  |    10.9 |         20 |
|  1 | Cenoura |     7.5 |        100 |
Press any key to continue...
"""
        self.assertEqual(valid_report, report_sequence)
    
    def test_report_most_sold_with_no_sales(self):
        # Executando ações para adicionar itens e ler o relatório de estoque
        output, error = self.run_commands("3\n2\n\n6\n4")
        # Verificando que nenhum erro é retornado
        self.assertEqual([], error)
        # Verificando se a segunda sequência retornada exibe o relatório correto
        report_sequence = output[1]
        valid_report = """=======================
Report mode

1 - Sales on period
2 - Most sold items
3 - Revenue contributors
4 - Days with highest number of items sold
5 - Days with lowest number of items sold
6 - Exit
=======================
Choice: 2
| name   | quantity   |
|--------|------------|
Press any key to continue..."""

    def tearDown(self):
        # Matando o processo da aplicação, caso ele não tenha terminado
        self.process.kill()
        # Deletando o banco de dados de teste utilizado, se ele foi criado
        shutil.rmtree("test_db", ignore_errors=True)
