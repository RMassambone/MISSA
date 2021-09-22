#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 10:21:18 2021

@author: rmassambone
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['text.usetex'] = True
#plt.rcParams["figure.figsize"] = (6,3)

obj_MISSA_test1_df = pd.read_csv('objective_MISSA_test-1.txt', engine='python', header=None)
obj_MISSA_test2_df = pd.read_csv('objective_MISSA_test-2.txt', engine='python', header=None)
obj_MISSA_test3_df = pd.read_csv('objective_MISSA_test-3.txt', engine='python', header=None)
obj_MISSA_test4_df = pd.read_csv('objective_MISSA_test-4.txt', engine='python', header=None)
obj_MISSA_test5_df = pd.read_csv('objective_MISSA_test-5.txt', engine='python', header=None)
obj_MISSA_test6_df = pd.read_csv('objective_MISSA_test-6.txt', engine='python', header=None)
obj_MISSA_test7_df = pd.read_csv('objective_MISSA_test-7.txt', engine='python', header=None)
obj_MISSA_test8_df = pd.read_csv('objective_MISSA_test-8.txt', engine='python', header=None)

obj_Markov_Ram_test1_df = pd.read_csv('objective_Markov_Ram_test-1.txt', engine='python', header=None)
obj_Markov_Ram_test2_df = pd.read_csv('objective_Markov_Ram_test-2.txt', engine='python', header=None)
obj_Markov_Ram_test3_df = pd.read_csv('objective_Markov_Ram_test-3.txt', engine='python', header=None)
obj_Markov_Ram_test4_df = pd.read_csv('objective_Markov_Ram_test-4.txt', engine='python', header=None)
obj_Markov_Ram_test5_df = pd.read_csv('objective_Markov_Ram_test-5.txt', engine='python', header=None)
obj_Markov_Ram_test6_df = pd.read_csv('objective_Markov_Ram_test-6.txt', engine='python', header=None)
obj_Markov_Ram_test7_df = pd.read_csv('objective_Markov_Ram_test-7.txt', engine='python', header=None)
obj_Markov_Ram_test8_df = pd.read_csv('objective_Markov_Ram_test-8.txt', engine='python', header=None)

obj_cyclic_test1_df = pd.read_csv('objective_cyclic_test-1.txt', engine='python', header=None)
obj_cyclic_test2_df = pd.read_csv('objective_cyclic_test-2.txt', engine='python', header=None)
obj_cyclic_test3_df = pd.read_csv('objective_cyclic_test-3.txt', engine='python', header=None)
obj_cyclic_test4_df = pd.read_csv('objective_cyclic_test-4.txt', engine='python', header=None)
obj_cyclic_test5_df = pd.read_csv('objective_cyclic_test-5.txt', engine='python', header=None)
obj_cyclic_test6_df = pd.read_csv('objective_cyclic_test-6.txt', engine='python', header=None)
obj_cyclic_test7_df = pd.read_csv('objective_cyclic_test-7.txt', engine='python', header=None)
obj_cyclic_test8_df = pd.read_csv('objective_cyclic_test-8.txt', engine='python', header=None)

obj_randomized_test1_df = pd.read_csv('objective_randomized_test-1.txt', engine='python', header=None)
obj_randomized_test2_df = pd.read_csv('objective_randomized_test-2.txt', engine='python', header=None)
obj_randomized_test3_df = pd.read_csv('objective_randomized_test-3.txt', engine='python', header=None)
obj_randomized_test4_df = pd.read_csv('objective_randomized_test-4.txt', engine='python', header=None)
obj_randomized_test5_df = pd.read_csv('objective_randomized_test-5.txt', engine='python', header=None)
obj_randomized_test6_df = pd.read_csv('objective_randomized_test-6.txt', engine='python', header=None)
obj_randomized_test7_df = pd.read_csv('objective_randomized_test-7.txt', engine='python', header=None)
obj_randomized_test8_df = pd.read_csv('objective_randomized_test-8.txt', engine='python', header=None)

obj_MISSA = []
obj_best_MISSA = []
obj_Markov_Ram = []
obj_best_Markov_Ram = []
obj_cyclic = []
obj_best_cyclic = []
obj_randomized = []
obj_best_randomized = []

for test in range(1,9):
    
    best_obj = 1e+08
    
    if (test == 1):
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
        
    if (test == 2):
        for i in range(len(obj_MISSA_test2_df.index)):
            obj = obj_MISSA_test2_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_MISSA.append(obj)
            obj_best_MISSA.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_Markov_Ram_test2_df.index)):
            obj = obj_Markov_Ram_test2_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_Markov_Ram.append(obj)
            obj_best_Markov_Ram.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_cyclic_test2_df.index)):
            obj = obj_cyclic_test2_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_cyclic.append(obj)
            obj_best_cyclic.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_randomized_test2_df.index)):
            obj = obj_randomized_test2_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_randomized.append(obj)
            obj_best_randomized.append(best_obj)
        
        fig2 = plt.figure()
        
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
        fig2.savefig('teste2-fig.svg', bbox_inches="tight")
    
    if (test == 3):
        for i in range(len(obj_MISSA_test3_df.index)):
            obj = obj_MISSA_test3_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_MISSA.append(obj)
            obj_best_MISSA.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_Markov_Ram_test3_df.index)):
            obj = obj_Markov_Ram_test3_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_Markov_Ram.append(obj)
            obj_best_Markov_Ram.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_cyclic_test3_df.index)):
            obj = obj_cyclic_test3_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_cyclic.append(obj)
            obj_best_cyclic.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_randomized_test3_df.index)):
            obj = obj_randomized_test3_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_randomized.append(obj)
            obj_best_randomized.append(best_obj)
        
        fig3 = plt.figure()
        
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
        plt.legend(loc="lower right", fontsize=20, ncol=1, handleheight=0.05, labelspacing=0.05)
        fig3.savefig('teste3-fig.svg', bbox_inches="tight")
    
    if (test == 4):
        for i in range(len(obj_MISSA_test4_df.index)):
            obj = obj_MISSA_test4_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_MISSA.append(obj)
            obj_best_MISSA.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_Markov_Ram_test4_df.index)):
            obj = obj_Markov_Ram_test4_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_Markov_Ram.append(obj)
            obj_best_Markov_Ram.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_cyclic_test4_df.index)):
            obj = obj_cyclic_test4_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_cyclic.append(obj)
            obj_best_cyclic.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_randomized_test4_df.index)):
            obj = obj_randomized_test4_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_randomized.append(obj)
            obj_best_randomized.append(best_obj)
        
        fig4 = plt.figure()
        
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
        fig4.savefig('teste4-fig.svg', bbox_inches="tight")
    
    if (test == 5):
        for i in range(len(obj_MISSA_test5_df.index)):
            obj = obj_MISSA_test5_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_MISSA.append(obj)
            obj_best_MISSA.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_Markov_Ram_test5_df.index)):
            obj = obj_Markov_Ram_test5_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_Markov_Ram.append(obj)
            obj_best_Markov_Ram.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_cyclic_test5_df.index)):
            obj = obj_cyclic_test5_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_cyclic.append(obj)
            obj_best_cyclic.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_randomized_test5_df.index)):
            obj = obj_randomized_test5_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_randomized.append(obj)
            obj_best_randomized.append(best_obj)
        
        fig5 = plt.figure()
        
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
        fig5.savefig('teste5-fig.svg', bbox_inches="tight")
    
    if (test == 6):
        for i in range(len(obj_MISSA_test6_df.index)):
            obj = obj_MISSA_test6_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_MISSA.append(obj)
            obj_best_MISSA.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_Markov_Ram_test6_df.index)):
            obj = obj_Markov_Ram_test6_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_Markov_Ram.append(obj)
            obj_best_Markov_Ram.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_cyclic_test6_df.index)):
            obj = obj_cyclic_test6_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_cyclic.append(obj)
            obj_best_cyclic.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_randomized_test6_df.index)):
            obj = obj_randomized_test6_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_randomized.append(obj)
            obj_best_randomized.append(best_obj)
        
        fig6 = plt.figure()
        
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
        fig6.savefig('teste6-fig.svg', bbox_inches="tight")
    
    if (test == 7):
        for i in range(len(obj_MISSA_test7_df.index)):
            obj = obj_MISSA_test7_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_MISSA.append(obj)
            obj_best_MISSA.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_Markov_Ram_test7_df.index)):
            obj = obj_Markov_Ram_test7_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_Markov_Ram.append(obj)
            obj_best_Markov_Ram.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_cyclic_test7_df.index)):
            obj = obj_cyclic_test7_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_cyclic.append(obj)
            obj_best_cyclic.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_randomized_test7_df.index)):
            obj = obj_randomized_test7_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_randomized.append(obj)
            obj_best_randomized.append(best_obj)
        
        fig7 = plt.figure()
        
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
        fig7.savefig('teste7-fig.svg', bbox_inches="tight")
    
    if (test == 8):
        for i in range(len(obj_MISSA_test8_df.index)):
            obj = obj_MISSA_test8_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_MISSA.append(obj)
            obj_best_MISSA.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_Markov_Ram_test8_df.index)):
            obj = obj_Markov_Ram_test8_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_Markov_Ram.append(obj)
            obj_best_Markov_Ram.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_cyclic_test8_df.index)):
            obj = obj_cyclic_test8_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_cyclic.append(obj)
            obj_best_cyclic.append(best_obj)
        
        best_obj = 1e+08
        for i in range(len(obj_randomized_test8_df.index)):
            obj = obj_randomized_test8_df[0][i]
            if obj < best_obj:
                best_obj = obj
            obj_randomized.append(obj)
            obj_best_randomized.append(best_obj)
        
        fig8 = plt.figure()
        
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
        fig8.savefig('teste8-fig.svg', bbox_inches="tight")
    
    obj_MISSA.clear()
    obj_best_MISSA.clear()

    obj_Markov_Ram.clear()
    obj_best_Markov_Ram.clear()
    
    obj_cyclic.clear()
    obj_best_cyclic.clear()
    
    obj_randomized.clear()
    obj_best_randomized.clear()
    
#plt.axvline(100, color='0.8', linestyle='--')
