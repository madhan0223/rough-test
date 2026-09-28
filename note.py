

"""
df = pd.read_csv("shop_sales_sql.csv")

print(df.head())"""

import mysql.connector
from tabulate import tabulate

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2005"
)
mycursor = connection.cursor()
mycursor.execute("USE hospital")
mycursor.execute("show tables")
for c in mycursor:
    print(c)
mycursor.execute("SELECT * FROM bills")
rows=mycursor.fetchall()
# Get column names
columns = [i[0] for i in mycursor.description]

print(tabulate(rows, headers=columns, tablefmt="grid"))