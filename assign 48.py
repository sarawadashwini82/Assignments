def count_vowels_consonants(s):
    vowels=0
    consonants=0
    for ch in s.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels+=1
            else:
                 consonants+=1
    print("vowels:",vowels)
    print("consonants:",consonants)
count_vowels_consonants("Python")     
       
    
