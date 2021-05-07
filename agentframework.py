import random

class Agent:
    # Set variables
    def __init__(self, environment, agents, neighbourhood):
        self._x = random.randint(0, 99)
        self._y = random.randint(0, 99)
        self.environment = environment
        self.agents = agents
        self.neighbourhood = neighbourhood
        self.store = 0

        
    # Create privacy for x and y variables
    def getx(self):
        return self._x
    
    def gety(self):
        return self._y
    
    def setx(self, value):
        self._x = value
        
    def sety(self, value):
        self._y = value
        
            
    # Model movement of sheep
    def move(self):
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._y = (self._y - 1) % 100
   
    
    # Consume environment as they move
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:
            self.environment[self._y][self._x] -= self.environment[self._y][self._x]
            self.store += self.environment[self._y][self._x]
            
        if self.store >= 100: # Throw up food if more than limit
            self.environment[self._y][self._x] += self.store
            self.store -= self.store
            
            
    # If another agent nearby, share out food stores
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                average = (self.store + agent.store) / 2
                agent.store = average
                self.store = average
                """print("sharing " + agent.store + " " + self.store)"""
                
                
    # Claculate distance between agent and surrounding agents
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
                
                