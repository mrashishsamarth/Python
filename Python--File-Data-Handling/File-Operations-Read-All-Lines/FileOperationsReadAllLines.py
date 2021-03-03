source_file = open(r'Flat_File.txt', 'r')
lines = source_file.readlines()
for line in lines:
    print(line)
source_file.close()
print("\n Reached - End of File. File is closed")

'''
:Output-

#CustomerID|SubscriptionID|ProductModel

 Reached - End of File. File is closed

Process finished with exit code 0

'''