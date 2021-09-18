class Body:
    def __init__(self, name, m, initial_pos, initial_vel, color):
        """
        New body object
        """
        self.name = name
        self.initial_pos, self.initial_vel = initial_pos, initial_vel
        self.posX, self.posY = initial_pos
        self.velX, self.velY = initial_vel
        self.color = color
        self.mass = m
        
    def changeVel(self, dvx, dvy):
        self.velX += dvx
        self.velY += dvy

    def move(self, dt):
        self.posX += self.velX * dt
        self.posY += self.velY * dt
    
    def getPos(self):
        return (self.posX, self.posY)
    
    def reset(self):
        self.posX, self.posY = self.initial_pos
        self.velX, self.velY = self.initial_vel
        