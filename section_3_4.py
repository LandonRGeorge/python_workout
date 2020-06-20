#%%
from collections import Counter


#%%
words = ['this', 'is', 'an', 'elementary', 'example']
letter_counts = {word: Counter(word).most_common(1)[0][1] for word in words}
print(sorted(letter_counts.items(), key=lambda x: x[1], reverse=True))
