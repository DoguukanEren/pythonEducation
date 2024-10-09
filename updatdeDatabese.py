# -*- coding: utf-8 -*-

import sqlite3

def updateCustomer():
    
    connection = sqlite3.connect("chinook.db")
    
    connection.execute("""
                       
                       update customers 
                       set city = 'Ankara'
                       where  city = 'Paris'
                       
                       """)
    connection.commit()
    connection.close()
    
updateCustomer()
