## Given 
## transport cost matrix
## Supply values 
## Demand values
## Finding minimum cost

###Input 
supply_size=int(input("Enter the number of supply centers "))
demand_size=int(input("Enter the number of demand centers "))
demand = []
supply = []
for i in range(1,supply_size+1):
    supply.append(int(input("Enter the supply for "+str(i)+"th centre: ")))
    
for j in range(1,demand_size+1):
    demand.append(int(input("Enter the demand for "+str(j)+"th centre: ")))
import numpy as np

### Handling unbalanced problems
if np.sum(np.array(supply)) == np.sum(np.array(demand)):
  flag=-1
elif np.sum(np.array(supply)) > np.sum(np.array(demand)):
  flag= 0       ## Supply more
else:
  flag= 1        ## Demand more
  
if flag==0:
  cost=[[0]*(demand_size+2) for i in range(supply_size+1)]
  alloc=[[0]*(demand_size+1) for i in range(supply_size+1)]
  for i in range(supply_size):
    cost[i][demand_size+1]=supply[i]
  for j in range(demand_size):
    cost[supply_size][j]=demand[j]
  cost[supply_size][demand_size]=abs(np.sum(np.array(supply)) - np.sum(np.array(demand)))
elif flag==1:
  cost=[[0]*(demand_size+1) for i in range(supply_size+2)]
  alloc=[[0]*(demand_size) for i in range(supply_size+2)]
  for i in range(supply_size):
    cost[i][demand_size]=supply[i]
  for j in range(demand_size):
    cost[supply_size+1][j]=demand[j]
  cost[supply_size][demand_size]=abs(np.sum(np.array(supply)) - np.sum(np.array(demand)))
else:
  cost=[[0]*(demand_size+1) for i in range(supply_size+1)]
  alloc=[[0]*(demand_size) for i in range(supply_size+1)]
  for i in range(supply_size):
    cost[i][demand_size]=supply[i]
  for j in range(demand_size):
    cost[supply_size][j]=demand[j]

## Input cost matrix
for i in range(supply_size):
  for j in range(demand_size):
    cost[i][j]=int(input("Enter the cost between demand centre "+str(i)+" and supply centre "+str(j)+": "))

print("The cost matrix is ")
print(np.matrix(cost))
### Finding allocation matrix
import sys
MAX_INT = sys.maxsize
No_of_allocations=0
cost=np.array(cost)
total_cost=0
while (True):
  cost_without_sd=np.array(cost)[:len(cost)-1,:len(cost[0])-1]
  minc = np.min(cost_without_sd)
  if minc==MAX_INT:
    break
  ind=np.where(cost_without_sd==minc)
  indices=list(zip(ind[0],ind[1]))
  possible_allocations=[min(cost[len(cost)-1][indices[i][1]],cost[indices[i][0]][len(cost[0])-1]) for i in range(len(indices))]
  max_allocations=indices[np.argmax(possible_allocations)]
  allocated_value=possible_allocations[np.argmax(possible_allocations)]
  cost[len(cost)-1][max_allocations[1]]-=allocated_value
  cost[max_allocations[0]][len(cost[0])-1]-=allocated_value
  total_cost+=allocated_value*cost[max_allocations[0]][max_allocations[1]]
  alloc[max_allocations[0]][max_allocations[1]]=allocated_value
  if cost[len(cost)-1][max_allocations[1]]<cost[max_allocations[0]][len(cost[0])-1]:
    cost[:,max_allocations[1]]=MAX_INT
  elif cost[len(cost)-1][max_allocations[1]]>cost[max_allocations[0]][len(cost[0])-1]:
    cost[max_allocations[0],:]=MAX_INT
  else:
    cost[:,max_allocations[1]]=MAX_INT
    cost[max_allocations[0],:]=MAX_INT
       
print("The allocation matrix is ")
print(np.matrix(np.array(alloc)[:-1,:]))
print("The minimal cost is ")
print(total_cost)
