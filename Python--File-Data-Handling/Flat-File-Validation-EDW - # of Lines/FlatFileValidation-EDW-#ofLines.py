source_file = open(r'Flat_File.txt', 'r')
lines = source_file.readlines()
count = 0
if lines[0].startswith('#', 0):
    for line in lines:
        count += 1
        line_count = count
    if (line_count - 1) == 0:
        print("File has only Header information")
    else:
        line_count -= 1
        print("The file has " + str(line_count) + " line(s), apart from the header")

source_file.close()

'''
Output#1
    File has only Header information

    Process finished with exit code 0

Output#2
    The file has 12 line(s), apart from the header

    Process finished with exit code 0
    
'''