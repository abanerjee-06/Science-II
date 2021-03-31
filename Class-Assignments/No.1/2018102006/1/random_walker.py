from random import seed
from random import randint
import matplotlib.pyplot as plt
import math

def combination(N):											# For analytical calculation
  L1 = [i for i in range(2*N,N,-1)]						    # Based on the analytical solution arrived at
  L2 = [j for j in range(N,0,-1)]
  val = 1
  for k in range(len(L1)):
    val *= L1[k]/(4*L2[k])

  return val



seed(1)														# Seed for random number generation

N = int(input("Enter the total no.of steps: "))				# Accounting for user input
w1 = 0														# Initializing the different variables needed for 
w2 = 0														# the random walker experiment
c1 = 0
c2 = 0
x = []
y1 = []
a1 = []
y2 = []
w1_mean = [0 for m in range(N)]
w2_mean = [0 for m in range(N)]
w1_meansq = [0 for m in range(N)]
w2_meansq = [0 for m in range(N)]

for i in range(1,N+1):										# Performing the experiment for (i = 1 to N) steps
  x.append(i)
  c1 = 0
  c2 = 0
  for j in range(100):										# Repeating the experiment for each "i" 100 times
    w1 = 0
    w2 = 0
    for k in range(i):										# Performing the experiment for i-th step value 
      val1 = randint(-1,1)
      while (val1 == 0):
        val1 = randint(-1,1)
      w1 += val1
      val2 = randint(-1,1)
      while (val2 == 0):
        val2 = randint(-1,1)
      w2 += val2

    w1_meansq[i-1] += w1**2									# Calculating mean squared displacement for drunk 1
    w2_meansq[i-1] += w2**2									# Calculating mean squared displacement for drunk 2
    if (w1 == w2):											# Checking if two random walkers meet
      c1 += 1
    if (w1 == 0):											# Checking if random walker ends up at origin after "i" steps
      c2 += 1
    
    w1_mean[i-1] += w1 										# Calculating mean displacement for drunk 1
    w2_mean[i-1] += w2 										# Calculating mean displacement for drunk 2
    
  w1_mean[i-1] /= i*100										
  w2_mean[i-1] /= i*100  
  w1_meansq[i-1] /= 100
  w2_meansq[i-1] /= 100

  y1.append(c1/100)											# Calculating P(two drunks meet after "i" steps)
  y2.append(c2/100)											# Calculating P(drunk ending up at origin after "i" steps)	
  a1.append(combination(i))									# Calculating analytic solution for the meeting of two drunks
  																# after "i" steps


plt.plot(x,y1,'r', label='Computational Solution')			# Plotting the p_meeting graph
plt.plot(x,a1,'b', label='Analytical Solution')
plt.xlabel('N')
plt.ylabel('P(two drunks meet after N steps)')
plt.title('Two 1-D Random Walkers')
plt.legend()
plt.show()

plt.plot(x,y2,'r', label='Computational Solution')			# Plotting the p_origin graph
plt.xlabel('N')
plt.ylabel('P(Returning to origin after N steps)')
plt.title('P_Origin')
plt.legend()
plt.show()

plt.plot(w1_mean,'r', label='Computational Solution')		# Plotting the mean displacement graph for drunk 1
plt.plot([0 for i in range(200)],'b', label='Analytical Solution')
plt.xlabel('N')
plt.ylabel('Mean Displacement')
plt.title('Mean Displacement after N steps for Drunk 1')
plt.legend()
plt.show()

plt.plot(w2_mean,'r', label='Computational Solution')		# Plotting the mean displacement graph for drunk 2
plt.plot([0 for i in range(200)],'b', label='Analytical Solution')
plt.xlabel('N')
plt.ylabel('Mean Displacement')
plt.title('Mean Displacement after N steps for Drunk 2')
plt.legend()
plt.show()

plt.plot(w1_meansq,'r', label='Computational Solution')		# Plotting the mean squared displacement graph for drunk 1
plt.plot([i for i in range(200)],'b', label='Analytical Solution')
plt.xlabel('N')
plt.ylabel('Mean Squared Displacement')
plt.title('Mean Squared Displacement after N steps for Drunk 1')
plt.legend()
plt.show()

plt.plot(w2_meansq,'r', label='Analytical Solution')		# Plotting the mean squared displacement graph for drunk 2
plt.plot([i for i in range(200)],'b', label='Compuational Solution')
plt.xlabel('N')
plt.ylabel('Mean Squared Displacement')
plt.title('Mean Squared Displacement after N steps for Drunk 2')
plt.legend()
plt.show()


