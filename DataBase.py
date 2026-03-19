import sqlite3

class DataBase:
    # this class should have the following methods:
    # 1. getConnection() to connect/establish the database.
    # 2. getCursor() for the cursor to navigate the database.
    # 3. createTables() to create the database tables.
    # 4. sampleValues() to aggregate the tables w/ sample values.

    def getConnection(self):
        # Create the DB connection and cursor:
        con = sqlite3.connect("FinanceTrackerDB.db")
        return con

    def getCursor(self):
        # Create the DB cursor:
        connection = self.getConnection()
        cursor = connection.cursor()
        return cursor

    def createTables(self):
        con = self.getConnection()
        cursor = self.getCursor()
        # Create the DB table using the following line w/ SQL inside:
        cursor.execute("CREATE TABLE IF NOT EXISTS Categories (catID INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT);")
        cursor.execute("CREATE TABLE IF NOT EXISTS Transactions (taID INTEGER PRIMARY KEY AUTOINCREMENT, category_ID INT, date TEXT, amount REAL, description TEXT, type TEXT, "
                       "FOREIGN KEY(category_ID) REFERENCES Categories(catID));")
        # this should create two tables: one for categories to categorize the transactions, and another table for the actual transactions.
        con.commit()
        con.close()

    def sampleValues(self):
        connection = self.getConnection()
        cursor = connection.cursor()

        # The following will aggregate the "Categories" with sample values to work with:
        cursor.execute("""
            INSERT INTO Categories (category) VALUES
                ('Food'), ('Utilities'), ('Bills'), ('Income'), ('Other');
        """)

        # Information aggregation for "Transactions":
        transactionData = [
            (1, "2026-03-01", 50.00, "groceries", "expense"),
            (5, "2026-03-05", 2000.00, "paycheck", "income"),
            (2, "2026-03-10", 150.00, "electric bill", "expense"),
            (5, "2026-03-15", 500.00, "freelance work", "income"),
        ]
        cursor.executemany("INSERT INTO Transactions (category_ID, date, amount, description, type) VALUES (?, ?, ?, ?, ?)", transactionData)

        # commit the action to the DB and close connection:
        connection.commit()
        connection.close()