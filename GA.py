import random


def Print(generation):
    for chromosome in generation:
        print(chromosome, end=' ')
        print('fitness: {}'.format(Fitness(chromosome)))



def Fitness(chromosome: list) -> int:
    return sum(chromosome)


def Initialization(nums = 10, length = 8):
    generation = []
    for _ in range(nums):
        chromosome = []
        for _ in range(length):
            chromosome.append(random.randint(0, 1))
        generation.append(chromosome)
    generation.sort(key= lambda f: Fitness(f), reverse= True)
    return generation


def Selection(generation):
    #random selection
    parent_1_pos = random.randint(0, len(generation)-1)
    while True:
        parent_2_pos = random.randint(0, len(generation)-1)
        if parent_1_pos != parent_2_pos:
            break
    return [generation[parent_1_pos], generation[parent_2_pos]]


def Crossover(parents):
    #single-point crossover
    crossover_point = random.randint(1, len(parents[0])-1)
    offspring_0 = []
    offspring_1 = []
    offspring_0 += parents[0][0 : crossover_point]
    offspring_0 += parents[1][crossover_point : ]
    offspring_1 += parents[1][0 : crossover_point]
    offspring_1 += parents[0][crossover_point : ]
    return [offspring_0, offspring_1]


def Mutation(offsprings, probability = 0.1):
    for gene in offsprings[0]:
        gene = abs(gene-1) if random.random()<probability else gene
    for gene in offsprings[1]:
        gene = abs(gene-1) if random.random()<probability else gene
    return offsprings

def next_generation(generation, offsprings):
    next_generation = generation + offsprings
    next_generation.sort(key= lambda f: Fitness(f), reverse= True)
    return next_generation[0 : len(generation)]


#Initialization
ge = Initialization()

count = 0
while True:
    #Selection
    parents = Selection(ge)

    #Crossover
    offsprings = Crossover(parents)

    #Mutation
    offsprings = Mutation(offsprings, 0.1)

    #next-generation
    ge = next_generation(ge, offsprings)
    Print(ge)
    if Fitness(ge[0]) == 8:
        print(count)
        break
    print('----------------------------')
    count += 1