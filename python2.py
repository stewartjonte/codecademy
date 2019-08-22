#So unit two is all about strings and commenting. So far it's been a little repetitive, but there's been some interesting updates too.

#standard strings can be printed like this
print "a string"

#Integers and floats can be printed too
num = 2
numfloat = 3.4
print "A number can be printed " + str(num) + " and floats can be printed too! " + str(numfloat)

#methods that can be used with a string: len() upper() lower() str()<converts a different data type into a string for printing
name = "Jack"
print len(name)
print name.lower()
print name.upper()
print str(numfloat)

#Formatting with % is a little odd. Say you have a sentence that reads off three names, you can use a %s as a placeholder, at the end of the second " you use % with the number
#of place holder variables. That probably doesn't make any sense how i explained it
name1 = "Juan"
name2 = "Janet"
name3 = "Ryan"
print "The three names are %s, %s, and %s" % (name1, name2, name3)

# dont get this: If you’d like to print a variable that is an integer, you can “pad” it with zeros using %02d. 
# The 0 means “pad with zeros”, the 2 means to pad to 2 characters wide, and the d means the number is a signed integer (can be positive or negative).

#indexing is done with a variable name and []. Counting starts at zero. so Juan index is J-0, u-1, a-2, n-3
print name1[2]

