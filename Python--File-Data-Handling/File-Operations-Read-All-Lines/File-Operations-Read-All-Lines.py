# The location of the file and file name need to be mentioned explicitly
# 'r' as a prefix to filepath-name is added to get read of unicode errors with file path
# Following line opens the file in "read" only mode
source_file = open(r'Flat_File.txt', 'r')
# Following line reads the line
lines = source_file.readlines()
# Iterate with the number of lines in the file using the for loop
for line in lines:
    # Print the content line by line and remove the new-line character
    print(line.rstrip('\n'))
# Always remember to close the file
source_file.close()
print("\n Reached - End of File. File is closed")