from collections import Counter
text = "Just waking up in the morning, gotta thank God I don't know, but today seems kinda odd No barking from the dog, no smog And momma cooked a breakfast with no hog I got my grub on, but didn't pig out"
freqs = Counter(text.split())
print(freqs)
