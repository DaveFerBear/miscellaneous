import random, string

def fitness(final_word, word):
	fitness = 0
	for i in range(0, len(final_word)):
		if (final_word[i] != word[i]):
			fitness+=1
	return fitness

POP_SIZE = 10
NUM_MUTATIONS = 
target = "popcorn"

# Initialize Population
pop = []
for i in range(0,POP_SIZE):
	s = ""
	for j in range(0, len(target)):
		s += random.choice(string.letters)
	pop.append(s)

print pop
print fitness(target, pop[0])

