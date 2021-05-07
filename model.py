import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import random

# Set parameter limits
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

# Create empty environment & agent arrays
environment = []
agents = []

# Set size of figure for animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Read in.txt to create environment
f = open('in.txt', newline='')
dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in dataset:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()   


# Starting positions
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, neighbourhood))
"""print(agents)"""

ax.set_autoscale_on(False),

# Move the sheep
def update(frame_number):
    fig.clear() # Clear each time so no build up of points  
    matplotlib.pyplot.xlim(0, 99) # Environment needs to be set after clearing
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for j in range(num_of_iterations):
        random.shuffle(agents) # Sheep move in random order each time
        for i in range(num_of_agents):
            agents[i].move() 
            agents[i].eat()
            agents[i].share_with_neighbours(20)
    """print(agents)"""

    
    for i in range(num_of_agents): # Plot points
        matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
        """print(agents[i]._x, agents[i]._y)"""


# Set animation
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False)
    canvas.show()
    
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop() # Wait for interactions.