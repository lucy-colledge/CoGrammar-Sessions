#Task is unclear if the string should be an input from user if so:
# string_ex=input("Please provide a sentence:")
string_ex = "This is a test sentence being used for string manipulation"

string_1 = ""
for x in range(len(string_ex)):
    if x % 2:
        string_1 = string_1 + string_ex[x].lower()
    else:
        string_1 = string_1 + string_ex[x].upper()
print (string_1)


word_list1=""
string_ex.split(' ') #will split into words
word_list = string_ex.split(' ')
for x in range (len(word_list)):
    if x % 2: 
        word_list1 = word_list1 +" "+ word_list[x].lower()
    else:
        word_list1 = word_list1 +" "+ word_list[x].upper()
string_2 = "".join(word_list1) 
print (string_2)
