source_file = open(r'Flat_File.txt', 'r')
lines = source_file.readlines()
for line in lines:
    print(line)
source_file.close()
print("\n Reached - End of File. File is closed")
