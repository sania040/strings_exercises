# Subject of the python script: Practice Questions of Python Strings
# Authored by: Sania Shakeel
# Where to contact: shakeelsania040@gmail.com   and   https://github.com/sania040

# Question 1: Concetinate two strings and print the Output

# Step 1: Get two sting inputs
str1 = "String one "
str2 = "String two "

#  Step 2: Concetenate and print the output
print(str1 + "and " + str2 + "are concetenated!")


# Question 2: Write script to print the reverse of string

# Step 1: Input String
str = "Hello world"
rev =""  # initiating an empty string
# Step 2: implementing logic
for c in str:  # initiating a for loop to be iterating the string
    rev = c + rev # the loop will iterate in a way that the 0 index will be retrived first and 
                    # will appended in string rev. on iteration the more characters from the string will be appended
                    # before the last iteration.  and at the end the character on last index will be at the 0 index of rev string.

# Step 3: Printing reveresed String
print(rev)

# Question 3: Write a program to check if a string is palidrome

# Step 1:  Input String 
str = "ohoo"

# Step 2: Implemenet logic
 # check if the str is equal to the reverse of string
if (str == str[:: -1]):  # str[::-1] will create a slice starting from end of string and end at 0 index and will iterate by -1.
# Step 3: Print output if pelindrome
    print("a pelindrome") 
# Step 4: If not pelindrome
else:  
    print("not a pelindrome") 
    
# Question 4: Write a script to count the number of vowels in a string

# Step 1: Input String and initiate vowel counter
str = "Want to count number of vowels"
vowels = 0

# Step 2: Implement logic
#initiate loop to iterate in string
for c in str:
    #check if c is vowel
    if(c =='a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
        vowels += 1 #increment vowel count
print(vowels)
# Question 5: Write a program to take user name as input and print its initials
# Step 1: Take name as input
name = input("Enter your Full name: ")
init= name[0]   # The first name's initial 
#Step 2: Take out initials
for c in range(len(name)):  # loop through the name
    if ( name[c]== " "): # Check for spaces in name
         init = name[c+1] + init    # if there is a space add the next character to init  String
print("Initials of your name are: ", init[:: -1])   # Print the reveresed version of that string
# Question 6: Write a program to delete the spaces from the string
# Step 1: Take String input and initialize a resultant string. 
str = input("Enter the string")
resultant = 

# Step 2: Iterate througth the string and remove spaces
# Iterate through the string
for char in str:
    if (char == ' '): #check if there is space
        continue            # skip that iteration and continue to next
    else:                      # if char is not space 
        resultant+= char    # add it in the resultant string
    
# Step 3: Print the resultant string  
print(resultant)

# What is slicing?
'''In Python, slicing is a way to extract a portion of a sequence (like a string, list, or tuple). 
It allows you to create a new sequence containing a subset of the original elements.
The basic syntax for slicing is as follows:

   '' sequence[start:stop:step]  ''
   
start: The index of the first element you want to include in the slice (inclusive).
stop: The index of the first element you don't want to include in the slice (exclusive).
step: An optional parameter that specifies the step size between elements. If omitted, it defaults to 1.'''

# Question 7: Write a program to input user's email and print the domain of the email.

# Step 1: Input email and initialize the domain string 
email = input("Enter your email:  ")
domain = ''

# Step 2: find @ and extract domain 
# find @ through string function .find()
index = email.find('@')

if (index != -1): # If index is not -1 or out of bound
    domain += email[index + 1:]   #slice email from the index of @ till end
    # PRint output
    print("Domain: ", domain)
else:  # if no @ found
    print("Error... Enter valid email")
    
# Question 8: Implement a program whcih counts the accurrances of specific character in a string
# Step 1: Input String and character to count, initialize count
sentence  = input("Enter you sentence: ")
char = input("Enter character to count")
count = 0
# Step 2: Iterate through the string for char
for c in sentence:
    if (c == char):   # if char found
        count +=1    # increment the count 
# Step 3: Print Output
print("The number of occurrances of", char, "in sentence are:  ", count)
# Question 9: Implement a program that capitalizes the first letter of each word in a sentence
# Step 1: Input string
sentence = input("Enter string:  ")
# Step 2: Split sentenceinto words
words = sentence.split()     #The split() method is used to split the input sentence into a list of words
# Step 3: Caplitalize the first letters of every word
capitalized = ' '.join(word.capitalize() for word in words)  #The capitalize() method is applied to each word to capitalize its first letter.
               #The join() method is used to join the capitalized words back into a sentence.
#Step 4: print Output
print(capitalized) 
# Question 10 : Write a program that checks if two given strings are anagrams of each other (contain the same characters with the same frequencies).
# Step 1: Input two Strings
str1 = "nothypstrings"
str2 =  'python stirngs'

# Step 2: remove spaces and case conflict
str1= str1.replace(' ', '').lower() # replace(' ','') will replace spaces with empty strings
str2 = str2.replace(' ','').lower() # lower() will convert upper case letter to lower
# step 3: sort strings and compare
if sorted(str1) == sorted(str2):    # sorted() returs the returned copy of string, which then will be compared
    print(f"{str1} and {str2} are anagrams!:)")  # if both sorted strings are equal 
else:
    print(f"{str1} and {str2} are not anagrams :(")
# Question 11: Write a program that checks if one string is a rotation of another.
# Step 1: input strings
str_1 = "python"
str_2 = 'onpyth'
# step 2: concatenate str_1 with itself
concetenated = str_1 + str_1 
# step 3: check if str_2 exists in concetenated
if len(str_1) != len(str_1) or str_1 == 0:
    print("not a rotation")
elif str_2 in concetenated != False:
    print("rotation :)")
# Question 12: Write a program for word frequency counter.
# Step 1: Input Sentence and initiate a dictionary for storing output
sentence = input("Enter the string:  ")
frequency_counter = {}
# Step 2: replace the . with space and remove case inequality and split sentence with respect to space
splitted_sentence = sentence.replace('.',  ' ').lower().split()
# print(splitted_sentence)
# Step 3: Iterate through the splitted sentence
for word in splitted_sentence:
    # step 3: if the word already exists in the dictionary frequency_counter than increase it by 1.
    if word in frequency_counter:
        frequency_counter[word] += 1
    # Step 4: in doesn't exist than initaite that word and it's count in dictionary
    else:
        frequency_counter[word] = 1
# Step 5: print the frequency_counter
print(frequency_counter)
# Question 13: String Compression
string = input("Enter String: ")
char = string[0]
count = 1
result = ""
for i in range (len(string)):
    if string[i] == char:
        count+=1
    else:
        result += str(count) + char
        char = string[i]
        count = 1
result += str(count) + char 
print(result)
# Question 14: Camel case to underscore
camel_case = input("Enter string in camel case: ")
underscore_case = ""
for c in camel_case:
    if c != c.lower():
        underscore_case += "_" + c.lower()
    else:
        underscore_case += c

print(underscore_case)
