import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("3nodes.csv", header=None)
df[0] = df[0] - df[0].min()
median_vals = []
max_vals = []
min_vals = []
ninety_vals = []
for i in range(101):
    between = df[df[0].between(i, i + 1)]
    median_vals.append(between[1].median())
    max_vals.append(between[1].max())
    min_vals.append(between[1].min())
    ninety_vals.append(between[1].quantile(.9))

fig1 = plt.figure(1)
plt.rc('font', size=22)
plt.plot(range(0, 101), median_vals)
plt.plot(range(0, 101), max_vals)
plt.plot(range(0, 101), min_vals)
plt.plot(range(0, 101), ninety_vals)
plt.title("Analysis of Logging Delay")
plt.ylabel("Seconds")
plt.xlabel("Time in seconds since first connection")
plt.legend(["Median Delay", "Max Delay", "Min Delay", "90% Delay"])

df = pd.read_csv("3nodes.csv", header=None)
df[0] = df[0] - df[0].min()
kilobits_per_second = []
for i in range(101):
    between = df[df[0].between(i, i + 1)]
    kilobits_per_second.append(between[2].sum() * 8 / 1000)

fig2 = plt.figure(2)
plt.rc('font', size=22)
plt.title("Analysis of Logging Bandwidth Usage")
plt.ylabel("Kilobits per second")
plt.xlabel("Time in seconds since first connection")
plt.plot(range(0, 101), kilobits_per_second)
plt.show()
