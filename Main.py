from AST import *
from AdaptedGeneticAlgorithm import *
from FindNumberAGA import *
from FindNumberLimitedAGA import *
from FindNumberRestrictedAGA import *
import random as rn
import matplotlib.pyplot as plt

# FINDNUMBER_GOAL = 10
# FINDNUMBER_INITIAL_POPULATION = 50
# FINDNUMBER_MUTATION_RATE = 0.8
# FINDNUMBER_ARGS = {'goal':FINDNUMBER_GOAL,'iterations':1000}
# FINDNUMBER = AdaptedGeneticAlgorithm(FINDNUMBER_INITIAL_POPULATION,
#                                      FindNumberAGA.fitness,
#                                   FINDNUMBER_MUTATION_RATE,
#                                   FindNumberAGA.end_state,
#                                   FINDNUMBER_ARGS,
#                                   FindNumberAGA.generate_individual,
#                                   [[AddNode,SubNode,MultNode],[2,3,5]],
#                                   FINDNUMBER_ARGS['goal'])
# results = FINDNUMBER.run()
# f1 = plt.figure(1)
# ax1 = f1.add_subplot(111)
# ax1.set_title("Fitness Evolution of BitSequence")
# ax1.set_xlabel('Generations')
# ax1.set_ylabel('Number of Accurate Characters')
# ax1.plot(results[0], c='r')
# ax1.plot(results[1], c='b')
# ax1.plot(results[2], c='g')
# f1.show()
# print("FINDNUMBER")
# print("Goal value: " + str(FINDNUMBER_GOAL))
# print("Obtained Sequence: "+ str(results[3])+"\n")

# FINDNUMBER2_GOAL = 65346
# FINDNUMBER2_INITIAL_POPULATION = 50
# FINDNUMBER2_MUTATION_RATE = 0.8
# FINDNUMBER2_ARGS = {'goal':FINDNUMBER2_GOAL,'iterations':1000}
# FINDNUMBER2 = AdaptedGeneticAlgorithm(FINDNUMBER2_INITIAL_POPULATION,
#                                      FindNumberAGA.fitness,
#                                   FINDNUMBER2_MUTATION_RATE,
#                                   FindNumberAGA.end_state,
#                                   FINDNUMBER2_ARGS,
#                                   FindNumberAGA.generate_individual,
#                                   [[AddNode,SubNode,MultNode,MaxNode],[25,7,8,100,4,2]],
#                                   FINDNUMBER2_ARGS['goal'])
# results = FINDNUMBER2.run()
# f1 = plt.figure(1)
# ax1 = f1.add_subplot(111)
# ax1.set_title("Fitness Evolution of BitSequence")
# ax1.set_xlabel('Generations')
# ax1.set_ylabel('Negative Distance To Goal Number')
# results[2].pop(0)
# ax1.plot(results[2], c='r')
# f1.show()
# print("FINDNUMBER")
# print("Goal value: " + str(FINDNUMBER2_GOAL))
# print("Obtained Sequence: "+ str(results[3])+"\n")


# FINDNUMBER3_GOAL = 65346
# FINDNUMBER3_INITIAL_POPULATION = 50
# FINDNUMBER3_MUTATION_RATE = 0.8
# FINDNUMBER3_ARGS = {'goal':FINDNUMBER3_GOAL,'iterations':300}
# FINDNUMBER3 = AdaptedGeneticAlgorithm(FINDNUMBER3_INITIAL_POPULATION,
#                                      FindNumberLimitedAGA.fitness,
#                                   FINDNUMBER3_MUTATION_RATE,
#                                   FindNumberLimitedAGA.end_state,
#                                   FINDNUMBER3_ARGS,
#                                   FindNumberLimitedAGA.generate_individual,
#                                   [[AddNode,SubNode,MultNode,MaxNode],[25,7,8,100,4,2]],
#                                   FINDNUMBER3_ARGS['goal'])
# results = FINDNUMBER3.run()
# f1 = plt.figure(1)
# ax1 = f1.add_subplot(111)
# ax1.set_title("Fitness Evolution of BitSequence")
# ax1.set_xlabel('Generations')
# ax1.set_ylabel('Negative Distance To Goal Number')
# results[2].pop(0)
# ax1.plot(results[2], c='r')
# f1.show()
# print("FINDNUMBER")
# print("Goal value: " + str(FINDNUMBER3_GOAL))
# print("Obtained Sequence: "+ str(results[3])+"\n")
# print("Obtained Value:"+str(results[3].eval()))


# FINDNUMBER4_GOAL = 65346
# FINDNUMBER4_INITIAL_POPULATION = 50
# FINDNUMBER4_MUTATION_RATE = 0.8
# FINDNUMBER4_ARGS = {'goal':FINDNUMBER4_GOAL,'iterations':100}
# FINDNUMBER4 = AdaptedGeneticAlgorithm(FINDNUMBER4_INITIAL_POPULATION,
#                                      FindNumberRestrictedAGA.fitness,
#                                   FINDNUMBER4_MUTATION_RATE,
#                                   FindNumberRestrictedAGA.end_state,
#                                   FINDNUMBER4_ARGS,
#                                   FindNumberRestrictedAGA.generate_individual,
#                                   [[AddNode,SubNode,MultNode],[25,7,8,100,4,2]],
#                                   FINDNUMBER4_ARGS['goal'])
# results = FINDNUMBER4.run()
# f1 = plt.figure(1)
# ax1 = f1.add_subplot(111)
# ax1.set_title("Fitness Evolution of BitSequence")
# ax1.set_xlabel('Generations')
# ax1.set_ylabel('Negative Distance To Goal Number')
# results[2].pop(0)
# ax1.plot(results[2], c='r')
# f1.show()
# print("FINDNUMBER")
# print("Goal value: " + str(FINDNUMBER4_GOAL))
# print("Obtained Sequence: "+ str(results[3])+"\n")
# print("Obtained Value:"+str(results[3].eval()))