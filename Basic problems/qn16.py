#Write a Python program to print without a newline or space.

#The problem is,when you use the print() function in Python, by default it moves to a new line after printing.But here, you’re asked to print several outputs on the same line, without spaces or line breaks between them.

# The end="" tells Python don't move to the next line after printing.

for i in range(0,10):
    print("HI",end="") #without the 'end=' the outputs will be in newlines,can insert anything between the end="(can be anything)".
