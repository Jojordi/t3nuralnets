import random as rn
from AST import *
class FindNumberRestrictedAGA:
    @staticmethod
    def fitness(individual, goal_number):
        node_list = individual.serialize()
        checked_terminals={}
        repetitions = 0
        for node in node_list:
            if isinstance(node,TerminalNode):
                if node.eval() in checked_terminals:
                    repetitions+=1
                else:
                    checked_terminals[node.eval()]=""

        return abs(individual.eval()-goal_number)*-1 - repetitions*1000

    @staticmethod
    def generate_individual(args):
        return AST(args[0], args[1])()

    @staticmethod
    def end_state(args,given_sequence,max_score,iterations):
        print(iterations)
        print(given_sequence)
        if iterations>args["iterations"] or given_sequence.eval()==args["goal"]:
            if given_sequence.eval()==args["goal"]:
                print("SUCCESS!")
            return True
        else:
            return False