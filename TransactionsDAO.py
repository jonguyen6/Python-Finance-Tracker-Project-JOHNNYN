from DataBase import DataBase
import csv
import os

class TransactionsDAO:
    # The logic behind the app. This class should have the following methods:
    # 1. showAllCategories() = display the "Categories" table.
    # 2. showAllTransactions() = display the "Transactions" table.
    # 3. searchByCategoryID() = search the "Transactions" table via CategoryID.
    # 4. searchByTransactionID() = search the "Transactions" table via TransactionID.
    # 5. searchByType() = search the "Transactions" table via "type" (column)".
    # 6. searchByDate() = search the "Transactions" table via "date" (column)".
    # 7. printToCSV() = print both tables in their fullest into an output, CSV file for the user.

    # This function should grab the DB connection, execute the query, and return the results:
    def showAllCategories(self):
        # Creating an "instance" of the connection using the DataBase class as a blueprint for the object:
        db = DataBase()
        con = db.getConnection()
        cursor = con.cursor()
        res = cursor.execute("""SELECT * FROM Categories;""")
        # fetchall() = "returns all remaining rows of a query result as a list"
        result = res.fetchall()
        # Close the connection:
        con.close()
        return result

    # This function should grab the DB connection, execute the query, and return the results:
    def showAllTransactions(self):
        db = DataBase()
        con = db.getConnection()
        cursor = con.cursor()
        res = cursor.execute("""SELECT * FROM Transactions;""")
        result = res.fetchall()
        con.close()
        return result

    # Run the SQL query to obtain all rows from "Transaction" via user-specified categoryID; return results into an output list:
    def searchByCategoryID(self, categoryID):
        db = DataBase()
        con = db.getConnection()
        cursor = con.cursor()
        res = cursor.execute("""SELECT * FROM Transactions WHERE category_ID = ?;""", (categoryID,))
        result = res.fetchall()
        con.close()
        return result

    # Run the SQL query to obtain all rows from "Transaction" via user-specified transactionID; return results into an output list:
    def searchByTransactionID(self, transactionID):
        db = DataBase()
        con = db.getConnection()
        cursor = con.cursor()
        res = cursor.execute("""SELECT * FROM Transactions WHERE taID = ?;""", (transactionID,))
        result = res.fetchall()
        con.close()
        return result

    # Run the SQL query to obtain all rows from "Transaction" via user-specified type; return results into an output list:
    def searchByType(self, type):
        db = DataBase()
        con = db.getConnection()
        cursor = con.cursor()
        res = cursor.execute("""SELECT * FROM Transactions WHERE type = ?;""", (type,))
        result = res.fetchall()
        con.close()
        return result

    # Run the SQL query to obtain all rows from "Transaction" via user-specified date; return results into an output list:
    def searchByDate(self, date):
        db = DataBase()
        con = db.getConnection()
        cursor = con.cursor()
        res = cursor.execute("""SELECT * FROM Transactions WHERE date = ?;""", (date,))
        result = res.fetchall()
        con.close()
        return result

    # Return the "type" column from "Transactions":
    def showAllTypes(self):
        db = DataBase()
        con = db.getConnection()
        cursor = con.cursor()
        res = cursor.execute("""SELECT type FROM TRANSACTIONS;""")
        result = res.fetchall()
        con.close()
        return result

    # Add a category:
    def addCategory(self, categoryName):
        db = DataBase()
        con = db.getConnection()
        cursor = con.cursor()
        # Enclose in a try/catch block in case the action fails:
        try:
            cursor.execute("""INSERT INTO Categories (category) VALUES (?)""", (categoryName,))
            con.commit() # save/commit the changes made to the table
            con.close()
            return "Category added successfully."
        except Exception as e:
            con.close()
            return f"Failed to add the category, printing exception: {str(e)}."

    # Add a transaction:
    def addTransaction(self, categoryID, tDate, tAmount, tDescription, tType):
        db = DataBase()
        con = db.getConnection()
        cursor = con.cursor()
        # Enclose in a try/catch block in case the action fails:
        try:
            cursor.execute(
                "INSERT INTO Transactions (category_ID, date, amount, description, type) VALUES (?, ?, ?, ?, ?)",
                (categoryID, tDate, tAmount, tDescription, tType)
            )
            con.commit() # save/commit the changes made to the table
            con.close()
            return "Transaction added successfully."
        except Exception as e:
            con.close()
            return f"Failed to add the transaction, printing exception: {str(e)}"

    # Print everything into an output, CSV file for the user:
    def printToCSV(self):
        db = DataBase()
        con = db.getConnection()
        cursor = con.cursor()

        # Grabbing a list of contents from the "Categories" table:
        categories = self.showAllCategories()
        # Grabbing a list of contents from the "Transactions" table:
        transactions = self.showAllTransactions()

        # Write categories to CSV
        with open('financeTrackerData.csv', 'w', newline='') as file:
            # First, appending the "categories" table to the file:
            writer = csv.writer(file)
            writer.writerow(['-~-~ CATEGORIES ~-~-'])
            writer.writerow(['Category ID', 'Category Name'])  # Header
            writer.writerows(categories)

            # Empty row for spacing between the two tables:
            writer.writerow([])

            # Now it's time to append the "transactions" table data to the file:
            writer.writerow(['-~-~ TRANSACTIONS ~-~-'])
            writer.writerow(['Transaction ID', 'Category ID', 'Date', 'Amount', 'Description', 'Type'])
            writer.writerows(transactions)

        con.close()
        # Need to verify if the files were successfully created or not:
        if os.path.exists('financeTrackerData.csv'):
            return "CSV file successfully created: financeTrackerData.csv"
        else:
            return "Failed to create CSV files"