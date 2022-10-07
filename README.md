# TesteSoftware-TP
Software Test TP - DCC - UFMG

## Group members
- Augusto Maillo Queiroga de Figueiredo - 2019006450
- Eduardo Augusto Militao Fernandes - 2019006540
- Pedro Dias Pires - 2019007040
- Arthur de Brito Bonifacio - 2019006370

## System Explanation
In this work, we developed a command-line trade management system. This system has 3 operating modes availaible: cashier mode, manager mode and report mode. Each of them will be detailed below:

### Cashier Mode
In this operating mode, the system user can open a new purchase and then add the products being purchased together with their quantities, remove added products, close the purchase, validating it in the system (checking if the added quantities are available in the inventory) and then record the purchase in the system, updating the quantities in the inventory and storing the purchase in the database.

### Manager Mode
In manager mode, the user has the ability to register new products in the trade inventory, informing the name, price and available quantity of the product, update the price of a product, remove a product from the system and change the stock of a product, informing both a positive (stock replenishment) and negative (stock loss) amount of variation.

### Report Mode
In this mode, the user can generate different reports on all the data in the system, in order to consult information about its use and that of its customers. Some of the reports available to be generated are: displaying all purchases made in a given period, displaying the best-selling items, displaying the most profitable items, displaying the days with the most sales volume, etc.

## Technologies Used
- Programming language: Python3
- Test framework: unittest
- Mock tool: MagicMock - this framework is used to generate "mocks" of system classes, in order to facilitate the creation of unit tests. In this way, it is possible to guarantee that all tests will have no external dependencies and are deterministic.
- Database: Pandas - all system information is stored in two Panda DataFrames, which are saved in "pickle" files on the user's machine. When starting the program, these files are read and the DataFrames are reconstructed. When you close it, the files are updated with the new information from the DataFrames.
- Test automation: GitHub Actions - when performing each "commit" on GitHub, a new "build" is built and all system tests are executed automatically. That way, if the "commit" leads to a regression in the system, the "build" will fail and the developer will be warned, preventing "bugs" from reaching the end user.