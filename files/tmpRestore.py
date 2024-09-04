#Import shutil package for file operations
import shutil

#Specify backup file
source_recovery_folder = '/home/$USER/backup.txt'

#Specify destination file to restore.
backup_recovery_folder = '/home/$USER/initial.txt'

#Use the shutil package to copy the source folder 
shutil.copytree(backup_recovery_folder, source_recovery_folder)
