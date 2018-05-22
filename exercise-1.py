# encoding: utf-8

"""
W Pythonie funkcje są first-class citizens. Oznacza to, że argumentami do
funkcji mogą być nie tylko dane (liczby, napisy, listy itd.), ale także inne
funkcje. Tak samo funkcje mogą zwracać funkcje.

Do czego to się przydaje? Klasyczny przykład to wbudowana funkcja filter.
Pozwala ona na wyrzucenie z kolekcji elementów, które nie spełniają jakiegoś
warunku. Warunkiem jest funkcja, która przyjmuje pojedynczy element i zwraca
True lub False, w zależności od tego, czy dany element należy zostawić, czy go
wyrzucić.
"""

numbers = [1, 2, 3, 4, 5, 6]
def is_even(n):
    return n % 2 == 0

filtered = filter(is_even, numbers)
print(list(filtered))  # ==> [2, 4, 6]

"""
Jako ćwiczenie, spróbuj wykorzystać podobną funkcję - wbudowaną funkcję map.
Przekształca ona każdy element jakiejś kolekcji w dowolny sposób. Pierwszym
argumentem jest funkcja, która przyjmuje element i powinna zwrócić
przekształcony element (np. pomnożony przez dwa). Drugim argumentem jest
kolekcja, której elementy chcemy przekształcić. Spróbuj przy pomocy tej funkcji
usunąć początkowe i końcowe białe znaki (spacje) z listy stringów (zmienna
`text`). Hint: metoda .strip()
"""

text = ['   tekst', 'z niepotrzebnymi    ', '  spacjami  ']


def remove_white_characters(input_text):    
    assert isinstance(input_text, str)    
    return input_text.strip()

mapped = map(remove_white_characters, text)
print(list(mapped))  # ==> ['tekst', 'z niepotrzebnymi', 'spacjami']
