import random
import matplotlib.pyplot as plt

N = int(input("Enter the total no.of marbles to be placed: "))		# Accounting for user input

circle_pts = 0									# Initializing different variables for the problem 
sqr_pts = 0										# of estimation of value of Pi 		
x = 0
y = 0
d = 0
L1 = []
L2 = []

for i in range(10,N+1):							# Putting a minimum of 10 marbles upto N
  L1.append(i)
  S = 0
  for j in range(50):							# Repeating the experiment for each such value 50 times
    circle_pts = 0
    sqr_pts = 0
    for k in range(i):							# Performing the experiment by using the Monte Carlo Method
      x = random.uniform(-1,1)					# Placing a point randomly in 2D square
      y = random.uniform(-1,1)
      d = x**2 + y**2							# Computing distance of marble placed from centre of circle
      if (d <= 1):								# If the marble falls inside the circle,
        circle_pts += 1							# incrementing appropriate counter
      sqr_pts += 1    
    S += 4*circle_pts/sqr_pts					# Calculating Pi value from known radius and formula for area
  S /= 50										# quadrant of a circle 
  L2.append(S)

  
plt.plot(L1,L2)									# Plotting the results obtained
plt.xlabel('N')
plt.ylabel('Pi value')
plt.title('Finding out value of Pi using Monte Carlo Simulation')
plt.show()