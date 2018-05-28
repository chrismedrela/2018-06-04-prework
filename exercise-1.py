text = ['   tekst', 'z niepotrzebnymi    ', '  spacjami  ']

def mapped(string):
	return string.strip()

mapped = map(mapped, text)
print(list(mapped))  # ==> ['tekst', 'z niepotrzebnymi', 'spacjami']
