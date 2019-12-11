# this path here is for example only...

# what goes in this path?
        # - your csv file

# ex: path

path = "F:\data\google_stock_data.csv"
file = open(path)  # opening the csv file with the open method... then storing in variable of file

# loop construct used here of loop http://homepages.uc.edu/~thomam/Intro_OOP_Text/Loops.html

for line in file:  #will display each line in file till end
    print(line)

# Below is an example of parsing the csv file without using the csv module

path = "F:\data\google_stock_data.csv"

# reading the contents of file by using list comprehension;

lines = [line for line in open(path)] # this will assign each line to an index within an array of lines

# getting index 0 in array

lines[0]

# each line will be treated as an single string with a \n -- new line being placed at the end of each string

lines[1] # getting the second index in the array

# we can use the strip method to remove any leading or trailing white space off of each line/string

lines[2].strip()

# we can chain a few methods ( strip(), split() ) to do two actions on a single string ..
 # -- for example we can remove any white space around the lines and this chunk the string into smaller portions

 lines[3].strip().split(',')  # placing a  ' , ' between each word in array

 # we will remove white space and then split the string into separate values

 dataset =[line.strip().split(',') for line in open(path)]

 #  doing this will make each row will be a list of data.. though it will still be in string format /datatype

 dataset[0]


# importing csv module below
# -- when using a module for the first time it's always a good idea to print the directory as to find out the functions defined within and classes
import csv

print(dir(csv)) # -- will print the directory for the csv module

path = "F:\data\google_stock_data.csv"
file = open(path, newline='') # this will ensure that this csv module work across all platform(s)

# --above opening up the csv file , and specifying a newline keyword arg.. passed empty string
# --- this is because -depending on your system, your lines may end with a newline , carrot-return, or both

reader = csv.reader(file) # using the reader method on the csv -file to parse the data

# since the first line is a header and does not contain any data we will use the next function/method
# -- this remind's me of linked list.. [null]=>[value]->head(node)~

header = next(reader) # The first line is the header
data = [row for row in reader] # Read the remaining data

print(header)
print(data[0])
