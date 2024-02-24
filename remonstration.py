fname = input("Enter file name: ")
if len(fname) < 1:
    fname = 'shakespeare.txt'
fh = open(fname)

word_freq = {}

for line in fh:
  words = line.split()
  for word in words:
    if word in word_freq:
      word_freq[word] += 1
    else:
      word_freq[word] = 1


for word, freq in word_freq.items():
  print(word, freq)
