from sortedcontainers import SortedList
class leaderboard:
    def __init__(self):
        # player_id, name
        self.player_scores = {}
        # team_id -> [player_id]
        self.team_map = {}
        # team score: team_id -> score
        self.team_score = {}
        # Leaderboard: sorted list of tuples(team_id, score)
        self.leaderboard = SortedList(key=lambda x: -x[1])
        # reverse mapping player_id -> set of team_id
        self.player_to_user = {}

    def add_user(self, team_id, player_ids):

        self.team_map[team_id] = set(player_ids)

        for p_id in player_ids:
            if p_id not in self.player_to_user:
                self.player_to_user[p_id] = set()
            self.player_to_user[p_id].add(team_id)

        # calculate team score:
        score = 0
        for p_id in player_ids:
            score += self.player_scores[p_id]
        self.team_score[team_id] = score
        self.leaderboard.add((team_id,score))

    def get_top_k(self, k):
        return self.leaderboard[:k]

    def update_player_score(self, player_id, delta):
        old_score = self.player_scores.get(player_id, 0)
        new_score = old_score + delta
        self.player_scores[player_id] = new_score

        for team_id in self.player_to_user[player_id]:
            old_team_score = self.team_score[team_id]
            new_team_score = old_team_score + delta
            self.team_score[team_id] = new_team_score

            #update leader board
            self.leaderboard.discard((team_id, old_team_score))
            self.leaderboard.add((team_id,new_team_score))


if __name__ == "__main__":
    lb = leaderboard()

    lb.player_scores = {
        'p1': 10,
        'p2': 5,
        'p3': 0,
        'p4': 7
    }
    print(lb.player_scores)

    lb.add_user('t1', ['p1','p2'])
    lb.add_user('t2', ['p3', 'p4'])

    print(lb.leaderboard)
    print(lb.get_top_k(2))

    lb.update_player_score('p2', 10)
    lb.update_player_score('p3', 20)

    print(lb.get_top_k(2))











