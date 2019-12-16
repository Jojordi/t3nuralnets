import random as rn
from AST import *
class FindNumberAGA:
    @staticmethod
    def fitness(individual, goal_number):
        return abs(individual.eval()-goal_number)*-1

    @staticmethod
    def generate_individual(args):
        return AST(args[0], args[1])()

    @staticmethod
    def end_state(args,given_sequence,max_score,iterations):
        if iterations>args["iterations"] or given_sequence.eval()==args["goal"]:
            if given_sequence.eval()==args["goal"]:
                print("SUCCESS!")
            return True
        else:
            return False
