import numpy as np                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               #YMC98 #YMC98
import math                                                                                                                                                                                                                                                                                                                                                                                                                                                   #YMC98     #YMC98
import matplotlib.pyplot as plt                                                                                                                                                                                                                                                                                                                                                                                                                                     #YMC98                   #YMC98
#import pdb                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         #YMC98   #YMC98
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     #YMC98    #YMC98               #YMC98
#Holder table                                                                                                                                                                                                                                                                                                                                                                                                                                             #YMC98           #YMC98
pop_size = 150                                                                                                                                                                                                                                                                                                                                                                                                                                      #YMC98                  #YMC98
gens = 650                                                                                                                                                                                                                                                                                                                                                                                                                                                #YMC98      #YMC98
cross_prob = .8                                                                                                                                                                                                                                                                                                                                                                                                                                                    #YMC98    #YMC98
K = .5                                                                                                                                                                                                                                                                                                                                                                                                                                                 #YMC98       #YMC98
F = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                      #YMC98  #YMC98
limitsHolder = [-10,10]                                                                                                                                                                                                                                                                                                                                                                                                                                                  #YMC98      #YMC98
limitsEgg = [-1,1]                                                                                                                                                                                                                                                                                                                                                                                                                                               #YMC98#YMC98
bestsol = []                                                                                                                                                                                                                                                                                                                                                                                                                                                     #YMC98   #YMC98
                                                                                                                                                                                                                                                                                                                                                                                                                                                        #YMC98#YMC98
def criteria_check(sol,mode="Holder"):
    x = sol[0]
    y = sol[1]
    if mode!="Holder":                                                                                                                                                                                                                                                                                                                                                                                                                                                   #YMC98     #YMC98
        return limitsEgg[0] <= x <= limitsEgg[1] and limitsEgg[0] <= y <= limitsEgg[1]                                                                                                                                                                                                                                                                                                                                                                                                                                                     #YMC98    #YMC98
    else:                                                                                                                                                                                                                                                                                                                                                                                                                                                     #YMC98   #YMC98
        return limitsHolder[0] <= x <= limitsHolder[1] and limitsHolder[0] <= y <= limitsHolder[1]                                                                                                                                                                                                                                                                                                                                                           #YMC98     #YMC98
                                                                                                                                                                                                                                                                                                                                                                                                                                                        #YMC98#YMC98
def fitfunc(sol, mode):#Egg,None for egg holder                                                                                                                                                                                                                                                                                                                                                                                                                                                        #YMC98#YMC98
    x = sol[0]
    y = sol[1]
    if mode=="Egg":
         return -(512*y+47)*math.sin(math.sqrt(np.abs((x*256)+y*512+47)))-x*512*math.sin(math.sqrt(np.abs(x*512-y*512-47)))                                                                                                                                                                                                                                                                                                                                                                                                                                                        #YMC98#YMC98
    else: #YMC98     #YMC98
        return -np.abs(math.sin(x)*math.cos(y)*np.exp(np.abs(1-(math.sqrt(x**2+y**2)/math.pi))))                                                                                                                                                                                                                                                                                                                                                                                                                                                      #YMC98  #YMC98
                                                                                                                                                                                                                                                                                                                                                                                                                                                             #YMC98   #YMC98
def iscross():                                                                                                                                                                                                                                                                                                                                                                                                                                                     #YMC98   #YMC98
    return np.random.uniform(0,1) > cross_prob                                                                                                                                                                                                                                                                                                                                                                                                                                                      #YMC98  #YMC98
                                                                                                                                                                                                                                                                                                                                                                                                                                                     #YMC98   #YMC98
#Initialize population                                                                                                                                                                                                                                                                                                                                                                                                                                                       #YMC98 #YMC98
def gencandidate(mode):                                                                                                                                                                                                                                                                                                                                                                                                                                                        #YMC98#YMC98
    if mode=='Holder':                                                                                                                                                                                                                                                                                                                                                                                                                                                      #YMC98  #YMC98
        candidates = [list(np.random.uniform(-10,10,2)) for i in range(pop_size)]                                                                                                                                                                                                                                                                                                                                                                                                                                                    #YMC98    #YMC98
    else:                                                                                                                                                                                                                                                                                                                                                                                                                                                      #YMC98  #YMC98
        candidates = [list(np.random.uniform(-1,1,2)) for i in range(pop_size)]                                                                                                                                                                                                                                                                                                                                                                                                                                                      #YMC98  #YMC98
    return candidates                                                                                                                                                                                                                                                                                                                                                                                                                                                        #YMC98#YMC98
                                                                                                                                                                                                                                                                                                                                                                                                                                                                #YMC98                                            #YMC98                                                                                                                                                                                                                                                                                                                                                                                                                                                        #YMC98#YMC98                                                                                                                                                                                                                            #YMC98                                                                                                                                                                                                                            #YMC98                                                                                                                                                                                                                            #YMC98
candidates = gencandidate("Egg")                                                                                                                                                                                                                                                                                                                                                                                                                                                       #YMC98 #YMC98
#pdb.set_trace()                                                                                                                                                                                                                                                                                                                                                                                                                                                       #YMC98 #YMC98
best_sol_gen = 10000
for j in range(gens):                                                                                                                                                                                                                                                                                                                                                                                                                                                        #YMC98#YMC98                                                                                                                                                                                                                                                                                                                                                                                                                                                        #YMC98                                                                                                                                                                                                                                                                                                           #YMC98     #YMC98
    F = np.random.uniform(-2,2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                #YMC98#YMC98          
    for i in range(pop_size):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           #YMC98     #YMC98
        check = False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           #YMC98     #YMC98
        temp = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 #YMC98        #YMC98
        while not check:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     #YMC98   #YMC98
            #Mutation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         #YMC98       #YMC98
            xr1 = candidates[np.random.randint(0,pop_size)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             #YMC98   #YMC98
            xr2 = candidates[np.random.randint(0,pop_size)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #YMC98    #YMC98
            xr3 = candidates[np.random.randint(0,pop_size)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         #YMC98       #YMC98
            temp = candidates[i]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     #YMC98           #YMC98
            candidates[i][0] += K*(xr1[0] - candidates[i][0]) + F*(xr2[0] - xr3[0])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             #YMC98   #YMC98
            candidates[i][1] += K*(xr1[1] - candidates[i][1]) + F*(xr2[1] - xr3[1])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    #YMC98            #YMC98
            #CrossOver                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #YMC98    #YMC98
            if iscross():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          #YMC98    #YMC98
                candidates[i][0] = temp[0]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       #YMC98    #YMC98
            if iscross():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         #YMC98     #YMC98                                                                                                                                                                                                                                                                                      #YMC98                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #YMC98    #YMC98
                candidates[i][1] = temp[1]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           #YMC98     #YMC98
            #Check Criteria                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #YMC98    #YMC98
            check = criteria_check(candidates[i],"Egg")            
        parent_val = fitfunc(temp, "Egg")
        trial_val = fitfunc(candidates[i], "Egg")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              #YMC98    #YMC98
        if parent_val < trial_val:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            #YMC98    #YMC98
            candidates[i] = temp[:]
            if parent_val < best_sol_gen:
                best_sol_gen = parent_val
        else:
            if trial_val < best_sol_gen:
                best_sol_gen = trial_val
                
    bestsol.append(best_sol_gen)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 #YMC98      #YMC98
x = [i for i in range(gens)]
plt.plot(x, bestsol)
print('last best sol : ',bestsol[-1])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        #YMC98        #YMC98
plt.ylabel("Best solution generation-wise")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        #YMC98        #YMC98
print('Best sol fit val',fitfunc([1,404.2319/512],"Egg"))