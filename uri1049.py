animal = {"vertebrado":{"ave":{"carnivoro":"aguia","onivoro":"pomba"},"mamifero":{"onivoro":"homem","herbivoro":"vaca"}},"invertebrado":{"inseto":{"hematofago":"pulga","herbivoro":"lagarta"},"anelideo":{"hematofago":"sanguessuga","onivoro":"minhoca"}}}
w1 = raw_input()
w2 = raw_input()
w3 = raw_input()
print(animal[w1][w2][w3])
