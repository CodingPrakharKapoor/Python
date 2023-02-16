c=str(input())

if (c>='a' and c<='z') or (c>='A' and c<='Z'):
        if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
            print("Vowel.")
        elif c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
            print("Vowel.")
        else:
            print("Consonant.")
else:
        print("Not an alphabet.")
