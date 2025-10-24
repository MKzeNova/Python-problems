# program to test whether a passed letter is a vowel or not which is entered by user
def isvowel(letter):
    vowels="aeiou"
    if letter in vowels:
        print(letter, "is vowel")
    else:
        print(letter, "is not vowel")
cha=str(input("Enter your character: "))
isvowel(cha)