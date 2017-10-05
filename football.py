# coding: utf-8

import random
import numpy as np
import pandas as pd
from Mycup import Cup

a = Cup(["Team_1","Team_2","Team_3","Team_4","Team_5","Team_6","Team_7","Team_8","Team_9","Team_10"])
a.add_team("Team_11")
a.solve_cup()

data = a.return_all()
data = pd.DataFrame(data = data[1:,1:].astype(int),
                          index = data[1:,0],
                              columns = data[0,1:])
print ("The winner is %s with score %s"%(a.find_winner()[1],a.find_winner()[0]))
print (data.sort_values('points',ascending = False))


data.to_csv("./data")
print ('a.games[("Team_x","Team_y")]'+' to see results of match ')
