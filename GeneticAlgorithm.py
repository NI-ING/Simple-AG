

@staticmethod
def select_tournament(pop):
    tournament_pop = Population(0)
    i = 0
    while i < TOURNAMENT_SELECTION_SIZE :
        tournament_pop.get_chromosomes().append(pop.get_chromosomes()[random.randrange(0,POPULATION_SIZE)])
        i += 1
    tournament_pop.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)
    return tournament_pop.get_chromosomes()[0]


@staticmethod
def crossover_chromosomes(parent1, parent2):
    if random.random() < CROSSING_RATE:
        child1 = Chromosome()
        child2 = Chromosome()

        '''One Point Cross Over'''
        index = random.randrange(1, NB_GENES)
        child1.genes = parent1.get_genes()[:index] + parent2.get_genes()[index:]
        child2.genes = parent2.get_genes()[:index] + parent1.get_genes()[index:]

        print("\nMaking a cross")
        print("Parent1: ", parent1.get_genes())
        print("Parent2: ", parent2.get_genes())
        print("Child1 : ", child1.get_genes())
        print("Child1 : ", child2.get_genes())

        return child1, child2
    else:
        return parent1, parent2


@staticmethod
def mutate_chromosome(chromosome):
    if random.random() < MUTATION_RATE:
        print("\nMaking a mutation")
        print("From: ", chromosome.get_genes())

        random_bit_position = random.randrange(0, NB_GENES)
        if chromosome.get_genes()[random_bit_position] == 0:
            chromosome.get_genes()[random_bit_position] = 1
        else:
            chromosome.get_genes()[random_bit_position] = 0

        print("To:   ", chromosome.get_genes())

