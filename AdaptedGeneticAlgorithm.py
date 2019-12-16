import random as rn
import sys
class AdaptedGeneticAlgorithm:
    def __init__(self,population,
                 fitness_function,
                 mutation_rate,end_state,
                 end_state_args = None,
                 individual_generation_function=None,
                 individual_generation_function_args=None,
                 fitness_function_args = None):

        self.original_population=population
        self.fitness_function = fitness_function
        self.mutation_rate_args = mutation_rate
        self.end_state = end_state
        self.end_state_args = end_state_args
        self.individual_generation_function = individual_generation_function
        self.individual_generation_function_args = individual_generation_function_args
        self.fitness_function_args = fitness_function_args
        self.individuals = {}
        self.start_population(self.original_population)
        self.chosen = []
        self.current_max = rn.choice(list(self.individuals))
        self.max_history = [0]
        self.min_history = [0]
        self.avg = [0]

    def start_population(self,initial_number):
        n = 0
        i = 0
        while n < initial_number and i < 1000000:
            i += 1
            new_individual = self.generate_random()
            if str(new_individual).replace(" ", "") not in self.individuals:
                self.individuals[str(new_individual).replace(" ", "")] = [new_individual, None]
                n += 1

    def evaluate(self):
        totalSum = 0
        to_delete = []
        maximum_of_generation = -1000000
        minimum_of_generation = sys.maxsize
        for individual in self.individuals:

            if self.individuals[individual][1] is None:
                self.individuals[individual][1]=self.fitness_function(self.individuals[individual][0], self.fitness_function_args)

            if len(self.individuals)>self.original_population*3:
                if self.individuals[individual][1]<self.avg[-1]:
                    to_delete=to_delete+[individual]

            if self.individuals[self.current_max][1] is None or self.individuals[individual][1]>self.individuals[self.current_max][1]:
                self.current_max=individual

            if self.individuals[individual][1]>maximum_of_generation:
                maximum_of_generation = self.individuals[individual][1]

            if self.individuals[individual][1]<minimum_of_generation:
                minimum_of_generation = self.individuals[individual][1]

            totalSum+=self.fitness_function(self.individuals[individual][0],self.fitness_function_args)
        self.avg = self.avg + [totalSum / len(self.individuals)]
        self.max_history = self.max_history + [maximum_of_generation]
        self.min_history = self.min_history + [minimum_of_generation]
        for i in to_delete:
            del self.individuals[i]

    def tourney_select(self):
        max = -1000000
        max_key = ""
        selected = rn.choices(list(self.individuals),k=int(len(self.individuals)/5))
        for individual in selected:
            if self.individuals[individual][1] >= max:
                max = self.individuals[individual][1]
                max_key = individual
        return max_key

    def selection(self):
        selected =[]
        while len(selected) < len(self.individuals)/5:
            selection = self.tourney_select()
            selected.append(selection)
        n = 0
        iterations = 0
        while n < len(self.individuals)/10 and iterations <1000:
            sire_1 = self.individuals[rn.choice(selected)][0].copy()
            selected_sire_2 = self.individuals[rn.choice(selected)][0]
            selected_sire_2_length=len(selected_sire_2.serialize())
            selected_node = selected_sire_2.serialize()[rn.randint(0,selected_sire_2_length-1)]
            sire_2=selected_node.copy()
            crossover_index = rn.randint(1,len(sire_1.serialize())-1)
            sire_1.serialize()[crossover_index].replace(sire_2)
            if (rn.randint(0, 101) > self.mutation_rate_args * 100):
                 sire_1.serialize()[0].replace(self.generate_random())
            for node in sire_1.serialize():
                if(rn.randint(0,101) > self.mutation_rate_args * 100):
                    node.replace(self.generate_random())
            self.individuals[str(sire_1).replace(" ","")] = [sire_1, None]
            n+=1
            iterations+=1

    def generate_random(self):
        return self.individual_generation_function(self.individual_generation_function_args)

    def run(self):
        n=0
        self.evaluate()
        while True:
            if self.check_end_state(n):
                break
            self.selection()
            self.evaluate()
            n+=1
        return self.get_data()

    def print(self):
        print(self.individuals)

    def get_data(self):
        return [self.min_history]+[self.avg]+[self.max_history]+[self.individuals[self.current_max][0]]

    def check_end_state(self,iterations):
        return self.end_state(self.end_state_args,self.individuals[self.current_max][0],self.max_history[-1],iterations)


