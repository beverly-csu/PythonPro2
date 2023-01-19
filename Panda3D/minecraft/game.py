# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        mapmanager = MapManager()       ## NEED
        mapmanager.loadLand('map.txt')
        base.camLens.setFov(90)


game = Game()
game.run()