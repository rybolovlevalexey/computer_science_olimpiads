class FootballTeam:
    def __init__(self, name, city, team):
        self.name = name
        self.city = city
        self.team = team

    def delete_player(self, footballer):
        if footballer in self.team:
            del self.team[self.team.index(footballer)]
            return True
        return False

    def new_player(self, footballer):
        self.team.append(footballer)

    def team_ready(self):
        if len(self.team) >= 5:
            return True
        return False

    def __str__(self):
        return self.name + self.city + ','.join(self.team)


class FootballPlayer:
    def __init__(self, team_name, player_name):
        self.team_name = team_name
        self.player_name = player_name


n, m = map(int, input().split())
teams = dict()
footballers = dict()
for i in range(n):
    name, city, *team = input().split()
    teams[name] = FootballTeam(name, city, team)
    for player in team:
        footballers[player] = FootballPlayer(name, player)
for i in range(m):
    st = input().split()
    if len(st) == 1:
        st = st[0]
        teams[footballers[st].team_name].delete_player(st)
        del footballers[st]
    elif len(st) == 2:
        footballer_name, team_name = st
        teams[team_name].new_player(footballer_name)
        footballers[footballer_name] = FootballPlayer(team_name, footballer_name)
    elif len(st) == 3:
        footballer_name, team_name1, team_name2 = st
        teams[footballers[footballer_name].team_name].delete_player(footballer_name)
        teams[team_name2].new_player(footballer_name)
        footballers[footballer_name].team_name = team_name2
ans_sp = set()
for key, value in teams.items():
    if value.team_ready():
        ans_sp.add(value.city)
for elem in sorted(ans_sp):
    print(elem)
