num = input("Enter a number or word: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")