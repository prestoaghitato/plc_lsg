#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 2019

@author: marcelruland
"""

import pandas as pd

def calculate_medians(filename):
    df = pd.read_csv(filename)
    df_medians = df.groupby("signals-interval").median()
    df_medians.to_csv("df_medians.csv")


def calculate_means(filename):
    df = pd.read_csv(filename)
    df_medians = df.groupby("signals-interval").mean()
    df_medians.to_csv("df_means.csv")


def simplify(filename, n):
    """
    keeps every n-th line in a file
    """
    input_file = open(filename, "r")
    output_file = open("output.dat", "w")
    for i, line in enumerate(input_file):
        if i % n == 0:
            output_file.write(line)
    input_file.close()
    output_file.close()


def eat_urns(filename):
    """
    import netlogo's urn output into python
    """
    out= []
    urn_file = open(filename, "r")
    for i, line in enumerate(urn_file):
        out.append([])
        for char in line:
            if char in "012":
                out[i].append(int(char))
    return out
            
def urn_frequency(urns):
    out = []
    for i, urn in enumerate(urns):
        out.append([0, 0, 0])
        for ball in urn:
            out[i][ball] += 1
    return out

if __name__ == "__main__":
    sender_urns = eat_urns("sender_urns.txt")
    sender_frequency = urn_frequency(sender_urns)
    sender_urns = 0
    receiver_urns = eat_urns("receiver_urns.txt")
    receiver_frequency = urn_frequency(receiver_urns)
    receiver_urns = 0
