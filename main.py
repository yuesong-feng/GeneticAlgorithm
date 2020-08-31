import random
    
class Chromosome:
    def __init__(self):
        self.value = []
        self.length = 8
        for _ in range(self.length):
            self.value.append(random.randint(0, 1))
        self.fitness = Fitness(self)

class Generation:
    def __init__(self, n: int):
        self.chromosome = []
        for _ in range(n):
            self.chromosome.append(Chromosome())
            self.nums = n

def Fitness(Chromosome) -> int:
    res = 0
    for each in Chromosome.value:
        res += each
    return res

def Selection(generation: Generation) -> list:
    parent_1_pos = random.randint(0, generation.nums-1)
    while True:
        parent_2_pos = random.randint(0, generation.nums-1)
        if parent_1_pos != parent_2_pos:
            break
    parent_1 = generation.chromosome[parent_1_pos]
    parent_2 = generation.chromosome[parent_2_pos]
    return [parent_1, parent_2]



# Initialization
generation = Generation(10)

# Selection
parents = Selection(generation)
parent_1 = parents[0]
parent_2 = parents[1]

#Crossover
#single-point
crossover_point = random.randint(0, parent_1.length)
# offspring_1 = 
# offspring_1.append(parent_1.)


print(parent_1)