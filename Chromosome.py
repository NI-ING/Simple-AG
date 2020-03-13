import random


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
