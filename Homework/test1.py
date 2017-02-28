wordCounter = {}
with open(r'C:\Users\Aliwka\Desktop\ДЗ-курсы\Homework6\first.txt') as fh:
  for line in fh:
    word_list = line.replace(',','').replace('\'','').replace('.','').lower().split()
    for word in word_list:
      if word not in wordCounter:
        wordCounter[word] = 1
      else:
                wordCounter[word] = wordCounter[word] + 1
print('{:15}{:3}'.format('Слова','Число'))
print('-' * 18)
for  (word,occurance)  in wordCounter.items(): 
  print('{:15}{:3}'.format(word,occurance))
