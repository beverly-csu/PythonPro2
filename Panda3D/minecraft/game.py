# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        mapmanager = MapManager()
        mapmanager.loadLand('map.txt')
        hero = Hero((0, 1, 1), mapmanager)
        base.camLens.setFov(90)


game = Game()
game.run()