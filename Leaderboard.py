class Player:
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name

class Score:
    def __init__(self, player, score):
        self.player = player
        self.score = score

class LeaderBoard:
    def __init__(self):
        self.score = {}

    def addScore(self, player, score):
        if player.player_id not in self.score:
            self.score[player.player_id] = score
        else:
            self.score[player.player_id] = self.score[player.player_id] + score

    def getScore(self):
        return self.score

    def getTopK (self, k):
        topk = sorted(self.score.items(), key=lambda item: item[1], reverse=True)
        print(topk)
        return topk[:k]

    def getRank(self, player_id):
        if player_id not in self.score:
            return -1
        ranks = sorted(self.score.items(), key=lambda item: item[1], reverse=True)
        for idx, player in enumerate(ranks):
            if player[0] == player_id:
                return idx


p1 = Player(1, "Alice")
p2 = Player(2, "Bob")
p3 = Player(3, "Charlie")

# Leaderboard
lb = LeaderBoard()
lb.addScore(p1, 50)
lb.addScore(p2, 70)
lb.addScore(p3, 60)
print(lb.getScore())
print(lb.getTopK(2))
print(lb.getRank(1))


