# encoding: utf-8

"""
Python pozwala na zagnieżdżanie funkcji. Przedstawiono to na przykładzie funkcji
new_counter. Funkcja inc ma dostęp do wszystkich zmiennych lokalnych
zdefiniowanych w new_counter - jest to tzw. domknięcie (closure). Jeśli jednak
chcemy je nadpisać, konieczne jest użycie `nonlocal counter`, w przeciwnym razie
Python zakłada, że chodzi o zmienną lokalną dla inc. Zwróć też uwagę, że funkcja
new_counter zwraca funkcję inc.
"""

def new_counter():
    counter = 0
    def inc():
        nonlocal counter
        counter += 1
        return counter
    return inc

counter = new_counter()
counter_2 = new_counter()
print(counter())  # ==> 1
print(counter())  # ==> 2
print(counter_2())  # ==> 1
print(counter())  # ==> 3

"""
Jako ćwiczenie, spróbuj zaimplementować funkcję generate_adder(a), która zwraca
funkcję zagnieżdżoną adder(b) zwracającą sumę liczb a i b. 
"""

def generate_adder(a):    
    def adder(b):        
        nonlocal a        
        return a + b    
    return adder
    
add_5 = generate_adder(5)
add_10 = generate_adder(10)
print(add_5(7))  # ==> 12
print(add_5(15))  # ==> 20
print(add_10(33))  # ==> 43
