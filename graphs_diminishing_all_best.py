#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 10:21:18 2021

@author: rmassambone
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['text.usetex'] = True

obj_MISSA_test1_df = pd.read_csv('objective_MISSA_test-1.txt', engine='python', header=None)
obj_Markov_Ram_test1_df = pd.read_csv('objective_Markov_Ram_test-1.txt', engine='python', header=None)
obj_cyclic_test1_df = pd.read_csv('objective_cyclic_test-1.txt', engine='python', header=None)
obj_randomized_test1_df = pd.read_csv('objective_randomized_test-1.txt', engine='python', header=None)

obj_MISSA = []
obj_best_MISSA = []
obj_Markov_Ram = []
obj_best_Markov_Ram = []
obj_cyclic = []
obj_best_cyclic = []
obj_randomized = []
obj_best_randomized = []

best_obj = 1e+08
for i in range(len(obj_MISSA_test1_df.index)):
    obj = obj_MISSA_test1_df[0][i]
    if obj < best_obj:
        best_obj = obj
    obj_MISSA.append(obj)
    obj_best_MISSA.append(best_obj)

best_obj = 1e+08
for i in range(len(obj_Markov_Ram_test1_df.index)):
    obj = obj_Markov_Ram_test1_df[0][i]
    if obj < best_obj:
        best_obj = obj
    obj_Markov_Ram.append(obj)
    obj_best_Markov_Ram.append(best_obj)

best_obj = 1e+08
for i in range(len(obj_cyclic_test1_df.index)):
    obj = obj_cyclic_test1_df[0][i]
    if obj < best_obj:
        best_obj = obj
    obj_cyclic.append(obj)
    obj_best_cyclic.append(best_obj)

best_obj = 1e+08
for i in range(len(obj_randomized_test1_df.index)):
    obj = obj_randomized_test1_df[0][i]
    if obj < best_obj:
        best_obj = obj
    obj_randomized.append(obj)
    obj_best_randomized.append(best_obj)

fig1 = plt.figure()

plt.plot(range(0,len(obj_MISSA)), obj_MISSA, color = (0.0, 0, 0.9, 0.8), linewidth = 0.5, label = r'$M1$')
plt.plot(range(0,len(obj_best_MISSA)), obj_best_MISSA, color = 'blue', linewidth = 1.5)

plt.plot(range(0,len(obj_Markov_Ram)), obj_Markov_Ram, color = (0, 0, 0, 0.6), linewidth = 0.5, label = r'$M2$')
plt.plot(range(0,len(obj_best_Markov_Ram)), obj_best_Markov_Ram, color = 'black', linewidth = 1.5)

plt.plot(range(0,len(obj_cyclic)), obj_cyclic, color = (0.9, 0, 0, 0.4), linewidth = 0.5, label = r'$M3$')
plt.plot(range(0,len(obj_best_cyclic)), obj_best_cyclic, color = 'red', linewidth = 1.5)

plt.plot(range(0,len(obj_randomized)), obj_randomized, color = (0, 0.9, 0, 0.2), linewidth = 0.5, label = r'$M4$')
plt.plot(range(0,len(obj_best_randomized)), obj_best_randomized, color = 'green', linewidth = 1.5)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$k$', fontsize=20)
plt.ylabel(r'$f(\mathbf{x}^k)$', fontsize=20)
plt.legend(loc="lower left", fontsize=20)
fig1.savefig('teste1-fig.svg', bbox_inches="tight")
