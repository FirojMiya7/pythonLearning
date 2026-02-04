# Vowel Counter using function
"""
Input: string
Output: number of vowels
"""


def vowelCounter(word):
    count = 0
    for m in word.lower():
        if m in 'aeiou':
            count += 1
    return count

word = input("Enter any word or something: ")

print("There are", vowelCounter(word) ,f"vowel letters present in your \nword: {word}")



# Logic
# Easy but long 
        # if m == 'a' or m == 'e' or m == 'i' or m == 'o' or m == 'u':
        #     count += 1