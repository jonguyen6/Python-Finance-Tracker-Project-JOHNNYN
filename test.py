from DataBase import DataBase
from TransactionsDAO import TransactionsDAO

print("=== Testing Database ===")

# Test 1: Create database
db = DataBase()
db.createTables()
print("✅ Tables created")

# Test 2: Add sample data
db.sampleValues()
print("✅ Sample data added")

# Test 3: Query categories
dao = TransactionsDAO()
categories = dao.showAllCategories()
print(f"\nCategories found: {len(categories)}")
for cat in categories:
    print(f"  {cat}")

# Test 4: Query transactions
transactions = dao.showAllTransactions()
print(f"\nTransactions found: {len(transactions)}")
for trans in transactions:
    print(f"  {trans}")