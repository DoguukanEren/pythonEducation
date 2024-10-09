# -*- coding: utf-8 -*-
import sqlite3

def deleteCustomers():
    
    connection = sqlite3.connect("chinook.db")
    
    connection.execute("""
                       
                            delete from customers
                            where city = 'Redmond' 
                                  
                       """)
                       
    connection.commit()
    connection.close()
    
deleteCustomers()
