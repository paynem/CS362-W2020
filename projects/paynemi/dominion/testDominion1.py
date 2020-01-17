# -*- coding: utf-8 -*-
"""
Worked on:Thurs Jan 16 3:48pm 2020

@author: paynemi
"""

import Dominion
import testUtility
import random
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
nV = testUtility.SetVictoryCards(player_names)
nC = -10 + 10 * len(player_names)

#Define box
box = testUtility.GetBoxes(nV)

#Define supply_order
supply_order = testUtility.GetSupplyOrder()
#supply_order[6].remove('Gold')
#supply_order[2].insert(0,'Gold')
#Define supply
supply = testUtility.GetSupply(nC, nV, box, player_names)
supply["Gold"] = [Dominion.Gold()]*0
supply["Silver"] = [Dominion.Silver()]*0

#initialize the trash
trash = []

#Construct the Player objects
players = testUtility.GetPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
