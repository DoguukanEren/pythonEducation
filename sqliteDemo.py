# -*- coding: utf-8 -*-


import sqlite3

connection = sqlite3.connect("chinook.db")


cursor = connection.execute("""select FirstName,LastName,City 
                            from customers 
                            order by FirstName desc
                            """)

for row in cursor:
    
    print( row)

connection.close()






                    