# Problem Statement 5: Vowel Counter using Function
# -------------------------------------------------
# Function: count_vowels(text)
# • Accepts a string
# • Counts total vowels (a, e, i, o, u) irrespective of case
# • Returns total vowel count
# -------------------------------------------------

# User-defined Function
def count_vowels(text):
    vowels = "aeiouAEIOU"   # both lowercase and uppercase
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

# -------------------------------------------------
# Main Program
sentence = input("Enter a sentence: ")
total_vowels = count_vowels(sentence)
print("Total Vowels:", total_vowels)