# sudo pip install --upgrade pandas
# sudo pip3 install xlrd
# Pandas version 0.22.0
import pandas as pd
import numpy as np
import argparse
import pdb
class Map():
    def __init__(self, fileName):
        self.fileName = fileName
        self.goal = None
        self.pit = None
        self.epsilon = None
        self.giveUp = None
        self.trials = None
        self.moveCost = None

    def gridWorld(self):
        # By default pandas considers 1st row as a header, so need to mention header as none
        df = pd.read_excel(self.fileName,"Sheet1",header=None)
        gridworld = df.values # .values turns the dataframe into numpy array
        # print(gridworld)
        # print(np.select([gridworld == 'P', gridworld == 'G'],[-2,10],gridworld))
        # gridworld[np.isnan(gridworld)]
        # print(gridworld)
        # pdb.set_trace()
        # for i in range(gridworld.shape[0]):
        #     for j in range(gridworld.shape[1]):
        #         if gridworld[i,j] == 'nan':
        #             gridworld[i,j] = 0
        print(gridworld)

    def read_arguments(self):
        parser = argparse.ArgumentParser(prog = 'sarsa', description = "Program Name")
        parser.add_argument('Goal', type = float, help = "Goal Reward Value")
        parser.add_argument('Pit', type = float, help = "Pit Penalty Value")
        parser.add_argument('Epsilon', type = float, help = "Epsilon Value")
        parser.add_argument('Giveup', type = float, help = "Give up Costs Value")
        parser.add_argument('Iterations', type = int, help = "How many trials?")
        parser.add_argument('Move', type = float, help = "Move Costs Value")
        args = parser.parse_args()
        self.goal = args.Goal
        self.pit = args.Pit
        self.epsilon = args.Epsilon
        self.giveUp = args.Giveup
        self.trials = args.Iterations
        self.moveCost = args.Move

# class
def main():
    a = Map('CS 534 map for assignment 4 .xlsx')
    a.gridWorld()
    a.read_arguments()
    print(a.goal)

if __name__ == '__main__':
    main()







# # Q-learning Learn method
# def learn(self, state1, action1, reward, state2):
#     maxqnew = max([self.getQ(state2, a) for a in self.actions])
#     self.learnQ(state1, action1,
#                 reward, reward + self.gamma*maxqnew)
#
# # SARSA learn method
# def learn(self, state1, action1, reward, state2, action2):
#     qnext = self.getQ(state2, action2)
#     self.learnQ(state1, action1,
#                 reward, reward + self.gamma * qnext)
