KEY_SWITCH_CAMERA = 'c'
KEY_SWITCH_MODE = 'z'

KEY_FORWARD = 'w'
KEY_BACK = 's'
KEY_LEFT = 'a'
KEY_RIGHT = 'd'

KEY_TURN_LEFT = 'arrow_left'
KEY_TURN_RIGHT = 'arrow_right'

KEY_UP = 'e'
KEY_DOWN = 'q'

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
        self.mode = True
    
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

    def justMove(self, angle):
        pos = self.lookAt(angle)
        self.hero.setPos(pos)

    def moveTo(self, angle):
        if self.mode:
            self.justMove(angle)
        else:
            self.tryMove(angle)

    def forward(self):
        angle = (self.hero.getH()) % 360
        self.moveTo(angle)

    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.moveTo(angle)
    
    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.moveTo(angle)
    
    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.moveTo(angle)

    def turnLeft(self):
        angle = self.hero.getH()
        self.hero.setH((angle + 5) % 360)

    def turnRight(self):
        angle = self.hero.getH()
        self.hero.setH((angle - 5) % 360)

    def up(self):
        if self.mode:
            self.hero.setZ(self.hero.getZ() + 1)
 
    def down(self):
        if self.mode and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ() - 1)

    def changeMode(self):
        self.mode = not self.mode

    def tryMove(self, angle):
        pos = self.lookAt(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHighestBlock(pos)
            self.hero.setPos(pos)
        else:
            pos = (pos[0], pos[1], pos[2] + 1)
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)

    def acceptEvents(self):
        base.accept(KEY_FORWARD, self.forward)
        base.accept(KEY_FORWARD + '-repeat', self.forward)
        base.accept(KEY_BACK, self.back)
        base.accept(KEY_BACK + '-repeat', self.back)
        base.accept(KEY_LEFT, self.left)
        base.accept(KEY_LEFT + '-repeat', self.left)
        base.accept(KEY_RIGHT, self.right)
        base.accept(KEY_RIGHT + '-repeat', self.right)

        base.accept(KEY_TURN_LEFT, self.turnLeft)
        base.accept(KEY_TURN_LEFT + '-repeat', self.turnLeft)
        base.accept(KEY_TURN_RIGHT, self.turnRight)
        base.accept(KEY_TURN_RIGHT + '-repeat', self.turnRight)

        base.accept(KEY_UP, self.up)
        base.accept(KEY_UP + '-repeat', self.up)
        base.accept(KEY_DOWN, self.down)
        base.accept(KEY_DOWN + '-repeat', self.down)
        
        base.accept(KEY_SWITCH_MODE, self.changeMode)
        base.accept(KEY_SWITCH_CAMERA, self.changeView)