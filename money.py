#!/bin/python
word = "$1.234.567,89 $1.234.234,232"
print word

wordlist = [ch for ch in word ]
print wordlist
for i in range(len(wordlist)):
    if wordlist[i] == '.':
        wordlist[i]=","
    elif wordlist[i] == ',':
        wordlist[i] = "."
print ''.join(wordlist)
