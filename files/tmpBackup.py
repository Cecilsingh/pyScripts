#Import shutil package for file operations
import shutil

#Specify source directory. In this case, tmp
source_dest_folder = '/tmp'

#Specify destination directory.
#This cannot exist on the host already
backup_dest_folder = '/home/$USER/tmpbk'

#Use the shutil package to copy the source folder 
shutil.copytree(source_dest_folder, backup_dest_folder)
