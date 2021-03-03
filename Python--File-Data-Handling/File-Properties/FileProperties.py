import os
import time
source_file = 'Flat_file.txt'
source_file_size = os.path.getsize((source_file))
source_file_created = os.path.getctime(source_file)
source_file_modified = os.path.getmtime(source_file)
print("The size of the file (in bytes) is : - " + str(source_file_size))
print("The file was created at : - " + str(time.ctime(source_file_created)))
print("The file was modified at : - " + str(time.ctime(source_file_modified)))