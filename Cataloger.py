"""
Main Program
Author: Dennis Santos-Sanchez
"""
import sqlalchemy as al
import sqlite3 as lt

def new_catalog():
    return

def load_catalog():
    return

def interpret(cmd):
    while cmd != "":
        if cmd =="New":
            new_catalog()
        if cmd =="Load":
            load_catalog()
    return

def main():
    print("Welcome to the GameCataloger!")
    print("If you would like to start a new catalog enter the command: New")
    print("If you would like to use an existing catalog enter the command: Load")
    #create Title Table
    #create Played Table
    #create completed Table
    #create Genre Table
    #create Release Date Table
    #create Systems Table
    cmd = input("Enter Command:")

if __name__ == "__main__":
    main()
