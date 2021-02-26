# question working with files

"""
open the file in read
copy the contents somehow
open the file in write
write some new contents (this will overwrite the previous file)
append the old contents to the file

starting file looks like this:
first line
second line
third line
fourth line

I would like your file to look like this at the end:
new line 1
new line 2
first line
second line
third line
fourth line
"""

if __name__ == '__main__':

    # open original file and copy contents to list using readlines()
    with open('generic_text_file.txt', 'r') as f:
        lines_list = [line.strip() for line in f.readlines()]

    # write in two new lines (to new file for debug), overwriting old contents of file
    with open('generic_text_file2.txt', 'w') as f:
        f.write("new line 1\n")
        f.write("new line 2\n")

    # append old content from list into file (new file for debug) 
    with open('generic_text_file2.txt', 'a') as f:
        for line in lines_list:
            f.write(line + "\n")


    #----------------------------------------------------
    # challenge to get str.strip() working with map
    with open('generic_text_file.txt', 'r') as f:
        map_lines_list = list(map(lambda x:x.strip(), f.readlines()))      
        print("map:", map_lines_list)