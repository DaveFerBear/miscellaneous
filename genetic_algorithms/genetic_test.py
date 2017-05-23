import string
import random
import sys

class Organism(object):

	def __init__(self, w, r):
		self.word = list(w)
		self.rate = r

	def mutate(self):
		i = 0
		for c in self.word:
			if random.random() < self.rate:
				self.word[i] = random.choice(string.letters)
			i+=1

	def printWord(self):
		print self.word

	# Cost Function #
	def evaluate(self, final_word):
		if len(self.word) != len(final_word):
			print "Word sizes do not match"
			return 0
		total_dist = 0
		for i in range(0, len(final_word)):
			total_dist += abs(ord(self.word[i]) - ord(final_word[i])) #int distance between chars
		self.value = total_dist

FINAL_WORD = "this is a sentence"
MUTATION_RATE = 0.01
ORG_NUMBER = 200
KILLOFF_NUMBER = 5
TOTAL_GENERATIONS = 1000


org_list = []

# Init
for i in range(0,ORG_NUMBER):
	seed = ""
	for j in range(0,len(FINAL_WORD)):
		seed += str(random.choice(string.letters))
	org_list.append(Organism(seed, MUTATION_RATE))
	org_list[i].evaluate(FINAL_WORD)

# Evolve
for gen in range(0,TOTAL_GENERATIONS):
	print ""
	org_list.sort(key=lambda x: x.value, reverse=False)
	org_list = org_list[KILLOFF_NUMBER:] # remove worst performing organisms
	org_list += org_list[len(org_list)-KILLOFF_NUMBER-1:len(org_list)-1] # duplicate best performing organisms (perhaps mutate?)
	for org in org_list:
		org.mutate()
		org.evaluate(FINAL_WORD)
		#sys.stdout.write(str(org.value) + " ")

