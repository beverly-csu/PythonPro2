KEY_SWITCH_CAMERA = 'c'

KEY_FORWARD = 'w'
KEY_BACK = 's'
KEY_LEFT = 'a'
KEY_RIGHT = 'd'


class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.acceptEvents()
    
    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def checkDir(self, angle):
        '''угол 0 (от 0 до 20)      ->        Y - 1
           угол 45 (от 25 до 65)    -> X + 1, Y - 1
           угол 90 (от 70 до 110)   -> X + 1
           от 115 до 155            -> X + 1, Y + 1
           от 160 до 200            ->        Y + 1
           от 205 до 245            -> X - 1, Y + 1
           от 250 до 290            -> X - 1
           от 290 до 335            -> X - 1, Y - 1
           от 340                   ->        Y - 1'''
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (+1, -1)
        elif angle <= 110:
            return (+1, 0)
        elif angle <= 155:
            return (+1, +1)
        elif angle <= 200:
            return (0, +1)
        elif angle <= 245:
            return (-1, +1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)

    def lookAt(self, angle):
        x_from = int(self.hero.getX())
        y_from = int(self.hero.getY())
        z_from = int(self.hero.getZ())

        dx, dy = self.checkDir(angle)
        
        x_to = x_from + dx
        y_to = y_from + dy
        return (x_to, y_to, z_from)

    def acceptEvents(self):
        base.accept(KEY_SWITCH_CAMERA, self.changeView)