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

'''
:Output-

Navigate to the folder where you want to create the page.
In the Wiki web part, click Create a new wiki page.
If this link is not present, i.e. another wiki already exists in the folder, use the  menu for the wiki web part and select New.
If you don't see the web part, you can add it.
In the New Page form, make the following changes:
In the Name field, enter "projectx".
In the Title field, enter "Project X".
Click the Convert To... button on the right, select Markdown, then click Convert.
In the Body panel, enter the following text: "Project X data collection proceeds apace, we expect to have finished the first round of collection and quality control by...".
Notice a brief guide to additional Markdown formatting options appears at the bottom of the editing pane. For more information, see Markdown Syntax.
Click Save & Close.
The web part shows your new content. Notice that the Pages web part (the table of contents) in the right hand column shows a link to your new page.

 Reached - End of File. File is closed

Process finished with exit code 0


Process finished with exit code 0

'''