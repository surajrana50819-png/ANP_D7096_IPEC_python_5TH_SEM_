# Lab 2: Word Frequency Counter
# Problem: Accept a sentence and count word frequency

sentence = input("Enter a sentence: ")
words = sentence.split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

# ---- Display frequency dictionary
print("Word Frequency:", freq)

# ---- Most frequent word
most_freq = max(freq, key=freq.get)
print("Most Frequent Word:", most_freq)

# ---- Display words in alphabetical order
print("Words in Alphabetical Order:", sorted(freq.keys()))
