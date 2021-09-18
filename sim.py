import math, body, pygame, sys, vpython
import matplotlib.pyplot as plt

class Simulation:
    def __init__(self, G, bodies):
        self.bodies = bodies
        self.n = len(bodies)
        self.G = G
        self.totalMass = 0
        self.comX, self.comY = 0, 0
        for body in bodies:
            self.totalMass += body.mass
            self.comX += body.mass * body.posX
            self.comY += body.mass * body.posY
        self.comX /= self.totalMass
        self.comY /= self.totalMass
        last_calculated_points = None

    def move(self, dt):
        self.comX = self.comY = 0
        for i in range(self.n):
            body1 = self.bodies[i]
            for j in range(i+1, self.n):
                body2 = self.bodies[j]
                dx, dy = body2.posX - body1.posX, body2.posY - body1.posY
                r2 = dx**2 + dy**2
                fx = self.G*body1.mass*body2.mass*dx/(r2**1.5)
                fy = self.G*body1.mass*body2.mass*dy/(r2**1.5)
                body1.changeVel(fx*dt/body1.mass, fy*dt/body1.mass)
                body2.changeVel(-fx*dt/body2.mass, -fy*dt/body2.mass)
            body1.move(dt)
            self.comX += body1.mass * body1.posX
            self.comY += body1.mass * body1.posY
        self.comX /= self.totalMass
        self.comY /= self.totalMass

    def draw_all(self, screen):
        for b in self.bodies:
            b.draw(screen)
        pygame.draw.circle(screen, (128, 128, 128), (int(self.comX), int(self.comY)), 10)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.comX), int(self.comY)), 5)

    def createPoints(self, duration, dt):
        points = [[] for _ in self.bodies]
        for i, body in enumerate(self.bodies):
            points[i].append(body.getPos())
        t = 0
        while t < duration:
            self.move(dt)
            for i, body in enumerate(self.bodies):
                points[i].append(body.getPos())
            t += dt
        self.last_calculated_points = points

    def plot(self):
        if not self.last_calculated_points:
            print("Please calculate points before plotting.")
            pass
        for i, ps in enumerate(self.last_calculated_points):
            x, y = list(zip(*ps))
            plt.plot(x, y, self.bodies[i].color, label=self.bodies[i].name)
        plt.show()

    def reset(self):
        for body in self.bodies:
            body.reset()
