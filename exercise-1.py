# encoding: utf-8
from timeit import Timer
"""
W Pythonie funkcje sa first-class citizens. Oznacza to, ze argumentami do
funkcji moga byc nie tylko dane (liczby, napisy, listy itd.), ale takze inne
funkcje. Tak samo funkcje moga zwracac funkcje.
Do czego to sie przydaje? Klasyczny przyklad to wbudowana funkcja filter.
Pozwala ona na wyrzucenie z kolekcji elementów, które nie spelniaja jakiegos
warunku. Warunkiem jest funkcja, która przyjmuje pojedynczy element i zwraca
True lub False, w zaleznosci od tego, czy dany element nalezy zostawic, czy go
wyrzucic.
"""

numbers = [1, 2, 3, 4, 5, 6]
def is_even(n):
    return n % 2 == 0

filtered = filter(is_even, numbers)
print(list(filtered))  # ==> [2, 4, 6]

"""
Jako cwiczenie, spróbuj wykorzystac podobna funkcje - wbudowana funkcje map.
Przeksztalca ona kazdy element jakiejs kolekcji w dowolny sposób. Pierwszym
argumentem jest funkcja, która przyjmuje element i powinna zwrócic
przeksztalcony element (np. pomnozony przez dwa). Drugim argumentem jest
kolekcja, której elementy chcemy przeksztalcic. Spróbuj przy pomocy tej funkcji
usunac poczatkowe i koncowe biale znaki (spacje) z listy stringów (zmienna
`text`). Hint: metoda .strip()
"""

text = ['   tekst', 'z niepotrzebnymi    ', '  spacjami  ']


def remove_spaces(s):
    return s.strip(' ')


mapped = map(remove_spaces, text)
print(mapped)

list_comprehension = [remove_spaces(x) for x in text]
print(list_comprehension)

"""
Ze wzgledu na to, ze list comprehension bedzie szybsze, dodalem je do rozwiazania.
List comprehension  - 0.868712902069
Map                 - 1.01444220543
"""
setup = "from __main__ import remove_spaces; text = ['   tekst', 'z niepotrzebnymi    ', '  spacjami  ']"
print(Timer("[remove_spaces(x) for x in text]", setup).timeit())
print(Timer("map(remove_spaces, text)", setup).timeit())
