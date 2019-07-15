# Ask the user for a string and print out whether this string is a palindrome or not.




print("/*************Palindrome*************/\n")


word = input("enter any word you like::\t")

# if word[::-1] == word:
#     print(word, "is a palindrome word")
#
# else:
#     print(word, "is not a palindrome word")

print('palindrome') if word==word[::-1] else print("not palindrome")


