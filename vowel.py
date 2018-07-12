li=['a','e','i','o','u']
li1=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
char=input()
if char in li:
    print("Vowel")
elif char in li1:
    print("Consonant")
else:
    print("invalid")
