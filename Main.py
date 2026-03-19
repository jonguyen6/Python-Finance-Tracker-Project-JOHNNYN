from TransactionsDAO import TransactionsDAO
from DataBase import DataBase
import sys

class Main:
    # Driver class and where to run the application. It should methods for the following options:
    def displayMenu(self):
        print("Welcome to Financial Tracker - Please select an option: ")
        print("1. Show All transactions and categories. ")
        print("2. Show the entire 'Categories' table. ")
        print("3. Show the entire 'Transactions' table. ")
        print("4. Show all transactional types in the 'Transactions' table. ")
        print("5. Search the 'Transactions' by a given transaction ID. ")
        print("6. Search the 'Transactions' by a given category ID. ")
        print("7. Search the 'Transactions' by a specific transaction type. ")
        print("8. Search the 'Transactions' by date. ")
        print("9. Add a category. ")
        print("10. Add a transaction. ")
        print("11. Print all to output CSV file. ")
        print("12. Exit the program. ")
        userInput = int(input("Enter your choice here: "))

        match userInput:
            # Note: since the DAO returns data, the switch/cases must display the data.
            case 1:
                print("\n")
                result = self.showAll()
                for item in result:
                    print(item)
                print("\n")
            case 2:
                print("\n")
                result = self.showCategoryTable()
                print("-~-~ CATEGORIES ~-~-")
                for item in result:
                    # Should print out both the ID and category name:
                    print(f"ID: {item[0]} | {item[1]}")
                print("\n")
            case 3:
                print("\n")
                result = self.showTransactionTable()
                print("-~-~ TRANSACTIONS ~-~-")
                # Print the entire row; all of its columns:
                for item in result:
                    print(f"ID: {item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]} | {item[5]}")
                print("\n")
            case 4:
                print("\n")
                result = self.showTransactionTypes()
                print("-~-~ TRANSACTION TYPES ~-~-")
                unique_types = set([item[0] for item in result])  # Get unique types
                for trans_type in unique_types:
                    print(f"• {trans_type}")
                print("\n")
            case 5:
                print("\n")
                searchTIDin = int(input("Please enter a transaction ID: "))
                result = self.searchByTransactionID(searchTIDin)
                for item in result:
                    print(item)
                print("\n")
            case 6:
                print("\n")
                searchCIDin = int(input("Please enter a category ID: "))
                result = self.searchByCategoryID(searchCIDin)
                for item in result:
                    print(item)
                print("\n")
            case 7:
                print("\n")
                searchTypeIn = input("Please enter a transaction type in lowercase (income/expense): ")
                result = self.searchByType(searchTypeIn)
                for item in result:
                    print(item)
                print("\n")
            case 8:
                print("\n")
                searchDateIn = input("Please enter a date (YYYY-MM-DD): ")
                result = self.searchByDate(searchDateIn)
                for item in result:
                    print(item)
                print("\n")
            case 9:
                print("\n")
                newCategoryName = input("Please enter a name for the new category you would like to add: ")
                result = self.addNewCategory(newCategoryName)
                print(result)
                print("\n")
            case 10:
                print("\n")
                print("User chose to add a new transaction, presenting available categories first...")
                # Show categories first so the user knows what they can choose from:
                transactionDAO = TransactionsDAO()
                categories = transactionDAO.showAllCategories()
                print("Available Categories:")
                for category in categories:
                    # print the category name and ID:
                    print(f"{category[0]}: {category[1]}")

                # Get inputs one by one from the user:
                categoryID = int(input("Enter category ID: "))
                date = input("Enter date (YYYY-MM-DD): ")
                amount = float(input("Enter amount (no dollar sign): "))
                description = input("Enter description: ")
                type = input("Enter type (income/expense): ")
                # pass the parameters into the defined method for adding a new transaction:
                result = self.addNewTransaction(categoryID, date, amount, description, type)
                print(result)
                print("\n")
            case 11:
                print("\n")
                result = self.printCSV()
                print(result)
                print("\n")
            case 12:
                print("\n")
                print("Exiting the program now...")
                sys.exit(0)
            case _:
                print("\n")
                print("Invalid input, please try again: ")

    def showAll(self):
        transactionsDAO = TransactionsDAO()
        output = transactionsDAO.showAllCategories()
        output.extend(transactionsDAO.showAllTransactions())
        return output

    def showCategoryTable(self):
        transactionsDAO = TransactionsDAO()
        return transactionsDAO.showAllCategories()

    def showTransactionTable(self):
        transactionsDAO = TransactionsDAO()
        return transactionsDAO.showAllTransactions()

    def showTransactionTypes(self):
        transactionsDAO = TransactionsDAO()
        return transactionsDAO.showAllTypes()

    def searchByTransactionID(self, searchTIDin):
        transactionsDAO = TransactionsDAO()
        return transactionsDAO.searchByTransactionID(searchTIDin)

    def searchByCategoryID(self, searchCIDin):
        transactionsDAO = TransactionsDAO()
        return transactionsDAO.searchByCategoryID(searchCIDin)

    def searchByType(self, searchTypeIn):
        transactionsDAO = TransactionsDAO()
        return transactionsDAO.searchByType(searchTypeIn)

    def searchByDate(self, searchDateIn):
        transactionsDAO = TransactionsDAO()
        return transactionsDAO.searchByDate(searchDateIn)

    def addNewCategory(self, newCategoryName):
        transactionsDAO = TransactionsDAO()
        return transactionsDAO.addCategory(newCategoryName)

    def addNewTransaction(self, categoryID, date, amount, description, type):
        transactionsDAO = TransactionsDAO()
        return transactionsDAO.addTransaction(categoryID, date, amount, description, type)

    def printCSV(self):
        transactionsDAO = TransactionsDAO()
        return transactionsDAO.printToCSV()

    def main(self):
        # Initialize the database:
        db = DataBase()
        db.createTables()
        transactionDAO = TransactionsDAO()
        # Aggregate tables w/ sample values, but ONLY if the tables are empty:
        if len(transactionDAO.showAllCategories()) == 0 and len(transactionDAO.showAllTransactions()) == 0:
            db.sampleValues()
        # Loop the menu display:
        while True:
            self.displayMenu()

if __name__ == "__main__":
    # create instance of "Main" class:
    app = Main()
    app.main()