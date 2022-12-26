
import matplotlib.pyplot as plt  # pip3 install matplotlib

# set initial values
p0 = 0.5  # initial population of plants
a0 = 0.2  # initial population of prey
h0 = 0.01  # initial population of predators

# set growth rates
r1 = 3.0  # plant growth rate
r2 = 4.0  # prey growth rate
r3 = 5.0  # predator growth rate

# set carrying capacities
k1 = 1.0  # plant carrying capacity
k2 = 1.0  # prey carrying capacity
k3 = 1.0  # predator carrying capacity

# set time steps
t = 30

# create empty lists to store population values
plants = []
prey = []
predators = []

# run logistic equation for each time step
for i in range(t):
    p = r1*p0*(1 - p0/k1)
    a = r2*a0*(p0/k1 - a0/k2)
    h = r3*h0*(a0/k2 - h0/k3)
    plants.append(p)
    prey.append(a)
    predators.append(h)
    p0 = p
    a0 = a
    h0 = h

# plot results
plt.plot(plants, label="Plants")
plt.plot(prey, label="Prey")
plt.plot(predators, label="Predators")
plt.legend()
plt.show()
