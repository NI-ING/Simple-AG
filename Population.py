import random
import Chromosome


class Population:
    POPULATION_SIZE = 10
    NB_GENES = 10
    MUTATION_RATE = 0.2
    CROSSING_RATE = 0.7
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
