# Import the following module so that we can use the child functions to get file attributes
import os
# Import the following module, since by default 'os.getctime' provides the output in seconds
import time
# May need to use complete path and file name, depending on the need.
source_file = 'Flat_file.txt'
# Get the size (in bytes) of the file
source_file_size = os.path.getsize((source_file))
# Get the creation time of the file
source_file_created = os.path.getctime(source_file)
# Get the modification time of the file
source_file_modified = os.path.getmtime(source_file)
print("The size of the file (in bytes) is : - " + str(source_file_size))
print("The file was created at : - " + str(time.ctime(source_file_created)))
print("The file was modified at : - " + str(time.ctime(source_file_modified)))