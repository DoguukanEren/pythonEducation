# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect("chinook.db")


cursor = connection.execute("""select city,count(*) 
                            
                            from Customers 
                            
                            group by city
                            
                            having count(*) > 1
                            
                            order by count(*) desc
                            
                            """)
                            
for row in cursor:
    
    print("City : " , row[0])
    print("Count : ", row[1])
    print("----------------")
    
connection.close()