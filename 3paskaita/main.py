print(len('Laura'))    
print(len('Žiemelytė'))

print(len('Žiniasklaida: po susitikimo su lenkų diplomatu Zelenskis liko įsiutęs'))


vardas = 'Laura'
print(vardas.lower())
print(vardas.upper())

delfi = 'Žiniasklaida: po susitikimo su lenkų diplomatu Zelenskis liko įsiutęs'
print(delfi[0:10])
print(delfi[-11:])
print(delfi[1::2])
print(delfi[9:19])

print(delfi.count('a'))
print(delfi.find('a'))

txt = 'Labas rytas!'
print(txt[1:])
print(txt[:-1])
print(txt[1:-1])

#5 uzduotis
text = 'An American in Paris'
print(text.replace('a','*').replace('A','*'))
#6 uzduotis
s=text.count('a')
a=text.count('A')
print(a+s)
#7 uzduotis
textKitas = 'Breakfast at Tiffany\'s'
textDarKitas = '2001: A Space Odyssey'
textVelKitas = 'It\'s a Wonderful Life'

vowels = 'AEIOUaeiou'
mytable = str.maketrans('','',vowels)
print(text.translate(mytable))

mytable = str.maketrans('','',vowels)
print(textKitas.translate(mytable))

mytable = str.maketrans('','',vowels)
print(textDarKitas.translate(mytable))

mytable = str.maketrans('','',vowels)
print(textVelKitas.translate(mytable))

