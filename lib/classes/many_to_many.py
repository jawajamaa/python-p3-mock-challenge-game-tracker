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
        game_list = list()
        for result in Result.all:
            player = result.player
            if isinstance(player, Player) and player.username not in game_list:
                game_list.append(player)
                breakpoint()
        return game_list
        # print(game_list)

    def average_score(self, player):
        pass

class Player:
    def __init__(self, username):
        self.username = username

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
        pass
        # if isinstance(self.player, Player):
        #     breakpoint()
        #     return self.player

    def games_played(self):
        pass

    def played_game(self, game):
        pass

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

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <=5000:
            self._score = score
        else:
            raise ValueError ("Score needs to be an integer between 1 and 5000")
