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
