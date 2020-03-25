# Script to compute null-trajectories in a Schwarzchild background

import numpy as np
from scipy import integrate 
import matplotlib.pyplot as plt

# Differential Equation to Integrate
def f(phi,r,b):
    R = 1
    y = 1 / (r**2 * np.sqrt( 1/b**2 - (1-R/r)/r**2 ))
    return y

#Setting up the region of integration

r0 = float(input('Enter a initial radius: '))
rf = float(input('Enter a final radius: '))
r = np.linspace(r0, rf, 400)

#Trajectories to plot
impact_params = np.linspace(1,5,11)
sols = [integrate.solve_ivp(f, [r0,rf], [b], args=[2], dense_output=True) for b in impact_params]

#Plotting

x = []
y = []
for sol in sols:
    phi = sol.sol(r)
    x_temp, y_temp = r*np.cos(phi), r*np.sin(phi)
    x.append(x_temp[0])
    y.append(y_temp[0])

circle1 = plt.Circle((0, 0), 1, color='k')
fig, ax = plt.subplots()

for idx in range(len(impact_params)):
    plt.plot(x[idx],y[idx],label=str(round(impact_params[idx],2)))

ax.grid(linestyle='-', linewidth='0.5')
ax.set_aspect(1)
ax.add_artist(circle1)
plt.xlabel('x'), plt.ylabel('y')
plt.legend(labelspacing=0.5, title='Impact Parameters')

plt.title('Null Trajectories in a Schwarzchild Background', fontsize=12)

plt.show()