import random

# r_range = random.randrange(10, 20, 2)
# print(r_range)

# r_int = random.randint(10, 20)
# print(r_int)

# r_uniform = random.uniform(10, 20)
# print(r_uniform)
nome = ['luiz', 'maria', 'roberto']
random.shuffle(nome)
print(nome)
nomes = random.sample(nome, k=2)
print(nomes)
print()

nome_nopvos = random.choice(nome)
print(nome_nopvos)