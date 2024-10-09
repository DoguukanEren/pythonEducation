# -*- coding: utf-8 -*-

import sqlite3

def joinOperation():
    
    connection = sqlite3.connect("chinook.db")
    
    cursor = connection.execute("""
                       
                       SELECT albums.Title, artists.Name FROM artists INNER JOIN albums
                       on artists.ArtistId = albums.ArtistId
                       
                       """)
    
    for row in cursor:
        print("Title = ", row[0])
        print("Artist Name = ", row[1])
        print("***********")
    
    connection.commit()
    connection.close()
    
joinOperation()