
# coding: utf-8

import random
import numpy as np
import pandas as pd

class Team():
    name = ''
    points = wins = loses = draws = goals = skips = 0

    def Play(self,enemy):
        score = (random.randint(0,5),random.randint(0,5))
        self.goals += score[0]
        self.skips += score[1]

        enemy.goals += score[1]
        enemy.skips += score[0]

        if score[0] < score[1]:
            self.loses += 1

            enemy.wins += 1
            enemy.points += 3

        elif score[0] == score[1]:
            self.points += 1
            self.draws += 1

            enemy.points += 1
            enemy.draws += 1

        else:
            self.wins += 1
            self.points += 3

            enemy.loses += 1

        return (self.name,enemy.name),score ,(enemy.name,self.name),(score[1],score[0])

    def return_one(self):
        return np.array([[self.name,self.points,self.wins,self.loses,self.draws,self.goals,self.skips]])

class Cup:
    random.seed()
    teams = []
    games = {}
    solved = False
    def __init__(self, teams):
        for i in range(len(teams)):
            new_team = Team()
            new_team.name = teams[i]
            self.teams.append(new_team)

    def add_team(self,team):
        new_team = Team()
        new_team.name = team
        self.teams.append(new_team)

    def solve_cup(self):
        if self.solved == True:
            return "already solved"
        else:
            for i in range(len(self.teams)):
                for j in range(i,len(self.teams)):
                    if i == j:
                        self.games[(self.teams[i].name,self.teams[i].name)] = "Do not try to make me fail"
                        continue

                    game1,score1,game2,score2 = Team.Play(self.teams[i],self.teams[j])
                    self.games[game1]=score1
                    self.games[game2]=score2
            self.solved = True

    def find_winner(self):
        max = (self.teams[0].points,self.teams[0].name,0)

        for i in range(1,len(self.teams)):
            if self.teams[i].points > max[0]:
                max = (self.teams[i].points,self.teams[i].name,i)

        return max

    def return_all(self):
        to_ret = np.array([["name","points","wins","loses","draws","goals","skips"]])

        for i in range(len(self.teams)):
            to_ret = np.append(arr = to_ret,values = Team.return_one(self.teams[i]),axis = 0)

        return to_ret


if __name__ == "__main__":
    _main()
