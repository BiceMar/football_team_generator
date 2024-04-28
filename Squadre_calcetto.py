import numpy as np
import mip


players = []

def addplayer(name,points):
    player = {"name":name,"points":points}
    players.append(player)

    return players

def playerviz(players):
    for player in players:
        print(player["name"] + " " + str(player["points"]) + " points")

def sortplayers(players):
    n = len(players)
    m = mip.Model()
    x = [m.add_var(var_type=mip.BINARY) for i in range(n)]
    y = [m.add_var(var_type=mip.BINARY) for i in range(n)]
    p = np.array([player["points"] for player in players])
    names = np.array([player["name"] for player in players])
    m.objective = mip.minimize(mip.xsum(p[i] * x[i] for i in range(n))-mip.xsum(p[i] * y[i] for i in range(n)))
    m.add_constr(mip.xsum(x[i] for i in range(n)) >= n/2)
    m.add_constr(mip.xsum(y[i] for i in range(n)) >= n/2)
    m.add_constr((mip.xsum(p[i] * x[i] for i in range(n))-mip.xsum(p[i] * y[i] for i in range(n)))>= 0)
    for i in range(n):
        m += x[i] + y[i] <= 1
    m.optimize()
    selected_players = [(names[i], x[i].x, y[i].x) for i in range(n)]

    return selected_players
    #print("Team A: ",[name[i]*x[i].x for i in range(10)])
    #print("Team B: ",[name[i]*x[i].x for i in range(10)])

if __name__ == "__main__":
    teamA = []
    teamB = []
    addplayer("Lil",10)
    addplayer("Elio",8)
    addplayer("Lorezo",8)
    addplayer("Pat",8)
    addplayer("Aleverz",9)
    addplayer("Ele",6)
    addplayer("Michi",5)
    addplayer("Nico",7)
    addplayer("AmicaAleverz",6)
    addplayer("Franco",9)
    #addplayer("Alemiu",3)
    print("Players:")
    playerviz(players)
    teams = sortplayers(players)
    print(teams)
    teams = np.array(teams)
    for i in range(len(teams)):
        if teams[i, 1] == 1:
            teamA.append(teams[i])
        else:
            teamB.append(teams[i])

    print("Team A: ", teamA)
    print("Team B: ", teamB)




    
   