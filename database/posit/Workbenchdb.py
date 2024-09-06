#Import the SQLite3 package for SQLite3 manipulation.
import sqlite3
#Import shutil package for file operations.
import shutil

#Specify database file paths.
#This is hard-coded. In this instance, the Posit Workbench SQLite3 directory is listed as the source. The backup directory is in the same path, however, appended with .bak.
source_db_filename = '/var/lib/rstudio-server/rstudio.sqlite'
backup_db_filename = '/var/lib/rstudio-server/rstudio.sqlite.bk'

#Create a function that backs up the SQLite databases as specifed above.
def backup_database():
    #Try-catch exception.
    try:
        #copy2 allows us to preserve all file metadata. copy() would copy the file data and permissions.
        shutil.copy2(source_db_filename, backup_db_filename)
        #Print success if backup is successful.
        print("Backup successful.")
    #If the backup fails, let the user know.
    except Exception as e:
        print(f"Backup failed: {str(e)}")

#Function to restore the database above from a backup
def restore_database():
    #Try-catch exception
    try:
        #copy2 allows us to preserve all file metadata. copy() would copy the file data and permissions.
        shutil.copy2(backup_db_filename, source_db_filename)
        #Print success if restoration is successful.
        print("Restore successful.")
    #If the backup fails, let the user know.
    except Exception as e:
        print(f"Restore failed: {str(e)}")

#Allows the script to NOT be hard-coded. The user can select which options they would like.
#Display user options.
while True:
    print("Options:")
    print("1. Backup Database")
    print("2. Restore Database")
    print("3. Quit")
    userSelection = input("Enter your userSelection. Specify 1, 2 or 3: ")

    #Conditionals
    if userSelection == '1':
        backup_database()
    elif userSelection == '2':
        restore_database()
    elif userSelection == '3':
        break
    else:
        print("Invalid userSelection. Please enter 1, 2, or 3.")
