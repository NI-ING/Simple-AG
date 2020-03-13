import random


POPULATION_SIZE = 10
NB_GENES = 10
MUTATION_RATE = 0.2
CROSSING_RATE = 0.7
TARGET_CHROMOSOME = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0]
TOURNAMENT_SELECTION_SIZE = 4




class Chromosome:
    POPULATION_SIZE = 10
    '''NB_GENES = 10'''
    '''TARGET_CHROMOSOME = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0]'''


    '''Chromosome Init'''
    def __init__(self):
        nb_genes = 10
        self.genes = []
        self.fitness = 0
        i = 0
        while i < nb_genes:
            self.genes.append(random.randint(0, 1))
            i += 1

    '''Chromosome Get Value'''
    def get_genes(self):
        return self.genes

    '''Chromosome Fitness'''
    def get_fitness(self):
        nb_genes = 10
        target_chromosome = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0]
        # this init is very important
        self.fitness = 0
        for i in range(nb_genes):
            if self.genes[i] == target_chromosome[i]:
                self.fitness += 1
        return self.fitness

    def __str__(self):
        return self.genes.__str__()


class Population:
    '''Population Init'''
    def __init__(self, size):
        self.chromosomes = []
        i = 0
        while i < size:
            self.chromosomes.append(Chromosome())
            i += 1
        self.chromosomes.sort(key=lambda x: x.get_fitness(), reverse=True)

    '''Get All Population Chromosomes'''
    def get_chromosomes(self):
        return self.chromosomes

    def print_population(self, gen_number):
        target_chromosome = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0]

        print("\n-----------------------Generation Summary---------------------------")
        print("--------------------------------------------------------------------")
        print("Generation #", gen_number, "| Fittest chromosome fitness:", self.get_chromosomes()[0].get_fitness())
        print("Target chromosome", target_chromosome)
        print("--------------------------------------------------------------------")
        i = 0
        for x in self.get_chromosomes():
            print("Chromosome #", i, " :", x, "| Fitness", x.get_fitness())
            i += 1


class GeneticAlgorithm:

    @staticmethod
    def select_tournament(pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_chromosomes().append(pop.get_chromosomes()[random.randrange(0, POPULATION_SIZE)])
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

    '''Population evolution Cross Over --> Mutation'''

    @staticmethod
    def evolve(pop):
        new_pop = Population(0)

        # '''Keep The Fittests Chromosomes'''
        # for i in range(NUMBER_OF_ELITE_CHROMOSOMES):
        #    new_pop.get_chromosomes().append(pop.get_chromosomes()[i])

        print("\nCrossover and Mutation Trace:")
        while new_pop.get_chromosomes().__len__() < POPULATION_SIZE:
            parent1 = GeneticAlgorithm.select_tournament(pop)
            parent2 = GeneticAlgorithm.select_tournament(pop)

            child1, child2 = GeneticAlgorithm.crossover_chromosomes(parent1, parent2)

            GeneticAlgorithm.mutate_chromosome(child1)
            GeneticAlgorithm.mutate_chromosome(child2)

            new_pop.get_chromosomes().append(child1)

            # make sure to not depass the population size if we keep the elite
            if len(new_pop.get_chromosomes()) < POPULATION_SIZE:
                new_pop.get_chromosomes().append(child2)

        new_pop.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)
        return new_pop


generation_number = 0
MAX_FITNESS = TARGET_CHROMOSOME.__len__()
population = Population(POPULATION_SIZE)
population.print_population(generation_number)

while population.get_chromosomes()[0].get_fitness() < MAX_FITNESS :
    generation_number += 1
    population = GeneticAlgorithm.evolve(population)
    population.print_population(generation_number)
