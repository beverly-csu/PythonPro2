# напиши здесь код создания и управления картой
class MapManager:
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.color = (0.57, 1, 0.55, 1)
        self.startNew()
        self.addBlock((0, 0, 0))

    def startNew(self):
        self.land = render.attachNewNode('land')

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        texture = loader.loadTexture(self.texture)
        self.block.setTexture(texture)
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)