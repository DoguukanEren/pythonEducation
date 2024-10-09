# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect("chinook.db")


cursor = connection.execute("""select FirstName,Lastname 
                            
                            from Customers 
                            
                            where FirstName like '%ja'
                            
                            """)
                            
for row in cursor:
    
    print("FirstName = " , row[0])
    print("LastName  =", row[1])
    print("----------------")        
    
connection.close()