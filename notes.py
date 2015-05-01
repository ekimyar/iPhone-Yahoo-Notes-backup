#!/bin/python
### Pull in the file data
file = open('/var/mail/pi', 'r')
## Turn the file into a string
data = file.read()

## Creat function to write desired list item to a new file
def create_notefile(note):
    newfile = open("Note"+str(note)+".html", "w")
    newfile.write(datalist[note])
    newfile.close()
    print(newfile.name)

## Split the string on two new lines and turn it into a list
datalist = data.split("\n\n")

## Debug thing to see if the list is in there
## howmanytimes = len(datalist)
## print for debug- datalist has the emails
## print(howmanytimes)

## the main effort-- iterate through list, write every other item to file 
number = 1
for item in datalist:
    if "div" in item:
        number = number + 2
        create_notefile(number)
        

#print(datalist[number])
