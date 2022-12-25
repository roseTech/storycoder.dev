
import matplotlib.pyplot as plt  # pip3 install matplotlib
import math

P0 = 200  # initial population
K = 400  # carrying capacity
R = 0.4  # growing capacity

T = 29  # maximum time
T_STEP = 0.1  # time step

ps1 = []  # population calculated via differential equation
ps2 = []  # population calculated via solution of the differential equation
ts = []

p1 = P0
t = 0.0

while t < T:
    ts.append(t)

    # via differential equation (forward euler scheme)
    ps1.append(p1)
    p1 += T_STEP * (R * p1 * (1 - p1 / K))

    # via solution of the differential equation
    p2 = (P0 * K * math.exp(R * t)) / ((K - P0) + (P0 * math.exp(R * t)))
    ps2.append(p2)

    t += T_STEP

plt.plot(ts, ps1, label="ps1")
plt.plot(ts, ps2, label="ps2")
plt.legend()
plt.show()
