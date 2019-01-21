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



if __name__ == "__main__":
    pass
