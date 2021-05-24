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
alloc=[[0]*(demand_size) for i in range(supply_size+1)]
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
  for i in range(supply_size):
    cost[i][demand_size+1]=supply[i]
  for j in range(demand_size):
    cost[supply_size][j]=demand[j]
  cost[supply_size][demand_size]=abs(np.sum(np.array(supply)) - np.sum(np.array(demand)))
elif flag==1:
  cost=[[0]*(demand_size+1) for i in range(supply_size+2)]
  for i in range(supply_size):
    cost[i][demand_size]=supply[i]
  for j in range(demand_size):
    cost[supply_size+1][j]=demand[j]
  cost[supply_size][demand_size]=abs(np.sum(np.array(supply)) - np.sum(np.array(demand)))
else:
  cost=[[0]*(demand_size+1) for i in range(supply_size+1)]
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

No_of_allocations=0
Total_cost=0
supply_size_corr=len(cost)-1
demand_size_corr=len(cost[0])-1
i=0
j=0
### Finding allocation matrix
while (i < supply_size_corr and j < demand_size_corr):
  x=min(cost[supply_size_corr][j],cost[i][demand_size_corr])
  #print(x)
  cost[supply_size_corr][j]-=x
  cost[i][demand_size_corr]-=x
  No_of_allocations+=1
  Total_cost+=x*cost[i][j]
  alloc[i][j]=x

  if cost[supply_size_corr][j]<cost[i][demand_size_corr]:
    j+=1
  elif cost[supply_size_corr][j]>cost[i][demand_size_corr]:
    i+=1
  else:
    i+=1
    j+=1
print("The allocation Matrix is ")
print(np.matrix(alloc))
print("The minimum cost found is: "+ str(Total_cost))
