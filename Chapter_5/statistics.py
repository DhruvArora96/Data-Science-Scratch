from __future__ import division
import sys
sys.path.append(r"C:\Users\dhruv\Documents\Learning\Data\Data-Science-Scratch\Chapter_3")
from linear_algebra import sum_of_squares
from collections import Counter 
import matplotlib.pyplot as plt
import random
import math

num_friends = random.choices(range(101),k=200)
friend_counts = Counter(num_friends)

""" xs=range(max(num_friends)+1)
ys=[friend_counts[x] for x in xs]

plt.bar(xs,ys)
plt.title("Histogram of Friend Counts")
plt.xlabel('# of friends')
plt.ylabel('# of people')
plt.show() """

def mean(x):
    return sum(x)/len(x)

def median(v):
    n=len(v)
    sorted_v=sorted(v)

    midpoint=n//2
    if n%2==1:
        return sorted_v[midpoint]
    else:
        lo=midpoint-1
        hi=midpoint
        return(sorted_v[lo]+sorted_v[hi])/2

def quantile(x,p):
    p_index = int(p*len(x))
    return sorted(x)[p_index]

def data_range(x):
    return max(x)-min(x)
def de_mean(x):
    x_bar=mean(x)
    return [x_i - x_bar for x_i in x]
def variance(x):
    n=len(x)
    deviatations = de_mean(x)
    return sum_of_squares(deviatations)/(n-1)

print(math.sqrt(variance(num_friends)))