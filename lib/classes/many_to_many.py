class Freeze:
    # Freeze attributes to make immutable
    _frozen = False

    def __init__(self):
        self._frozen = True

    def __delattr__(self, *args, **kwargs):
        if self._frozen:
            raise AttributeError("This object is Frozen; ie immutable!")
        object.__delattr__(self, *args, **kwargs)

    def __setattr__(self, *args, **kwargs):
        if self._frozen:
            raise AttributeError("This object is Frozen; ie immutable!")   
        object.__setattr__(self, *args, **kwargs)


class Game(Freeze):
    def __init__(self, title):
        self.title = title
        super().__init__()

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise ValueError ("Title must be a string more than 0 characters in length")

    def results(self):
        if isinstance(self, Game):
            return [result for result in Result.all if result.game == self]
            # result_list = list()
            # for result in Result.all:
            #     if result.game == self:
            #         result_list.append(result)
            # return result_list

    def players(self):
        # return [result.player for result in Result.all if isinstance(result.player, Player) and result.player not in list()]
        username_list = list()
        player_list = list()
        for result in Result.all:
            if result.game == self:
                player = result.player
                if isinstance(player, Player) and player.username not in username_list:
                    username_list.append(player.username)
                    player_list.append(player)
        return player_list

    def average_score(self, player):
        total_score_list = list()
        for result in self.results():
            if player.username == result.player.username and result.game.title == self.title:
                total_score_list.append(result.score)
        avg_score = round(sum(total_score_list)/len(total_score_list), 1)
        return avg_score
        # return sum(result for result in self.results() if player.username == result.player.username and result.game.title == self.title)/len(list())
        # above commented possible can't work as need named list() to get len() for avg...

class Player:
    def __init__(self, username):
        self.username = username

    # def __repr__(self):
    #     return f"Username is: {self.username}"
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise ValueError ("Username must be a string between 2 and 16 characters in length")

    def results(self):
        # below validation wasn't requested and as a result could fail tests though in this case it doesn't, but wasn't needed...
        if isinstance(self, Player):
            return [result for result in Result.all if result.player == self]
            # player_results = list()
            # for result in Result.all:
            #     if result.player == self:
            #         player_results.append(result)    
            # return player_results

    def games_played(self):
        games_list = list()
        for result in Result.all:
            if result.player == self and result.game not in games_list:
                games_list.append(result.game)
        return games_list

    def played_game(self, game):
        return game in self.games_played()
    # below doesn't work, but should?
        # for game_played in self.games_played():
        #         print(game_played)
        #         print(game)
        #         if game_played != game:
        #             return False
        #         return True
                

    def num_times_played(self, game):
        pass

class Result(Freeze):
    all = list()

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
        super().__init__()

    # def __repr__(self):
    #     return f"Player's name is: {self.player}\nGame is: {self.game}\nScore is: {self.score}"
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <=5000:
            self._score = score
        else:
            raise ValueError ("Score needs to be an integer between 1 and 5000")

# player = Player("Saaammmm")
# print(player)
# player = Player("Paxton")
# print(player)
# player = Player("this_username_is_too_long")
