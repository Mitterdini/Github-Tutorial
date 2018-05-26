class Steam(object):

    def __init__(self, games):                                                  #'magic' function that initializes a new empty object
        self.games = games

    def steam_library(self):                                                    #'self' turns into whatever the object name is
        for game in self.games:
            print(game)

doctorS = Steam(["Rocket League", "Sky Noon", "PUBG"])                          #Creating an object named 'doctorS'
protech = Steam(["DBZ Fighterz", "Rumble Fighter", "Battlefield One"])

doctorS.steam_library()                                                         #'doctorS' has all the base functions of the class Steam()
protech.steam_library()                                                         #'protech' does too
