# -*- coding: utf-8 -*-

import sqlite3

def insertCustomer():
    
    connection = sqlite3.connect("chinook.db")
    connection.execute("""
                       
                       insert into customers
                       (FirstName,LastName,city,email)
                       values('Doğukan','Özer','Eregli','dogukanerenozer@gmailcom')
                       
                       """)
                       
    connection.commit()
    connection.close()
    
insertCustomer()