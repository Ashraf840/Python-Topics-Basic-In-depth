n = int(input("Enter number: "))
orig = n
palindrome = 0
while (n>0):
    palindrome = (palindrome*10) + (n%10)
    n = n // 10

if orig == palindrome:
    print("Palindrome number")
else:
    print("Not palindrome number")

