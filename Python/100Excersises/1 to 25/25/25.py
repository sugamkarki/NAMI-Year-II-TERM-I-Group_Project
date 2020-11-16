alphabet=[]
for letters in range(97,123):
    alphabet.append(chr(letters))
d=dict(a=alphabet)
for item in d.values():
    for alpha in item:
        print(alpha)
