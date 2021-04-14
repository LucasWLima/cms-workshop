#!/usr/bin/env python
# coding: utf-8

import os
import argparse
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":

    # Getting the arguments
    parser = argparse.ArgumentParser(description="This script parses amber mdout files to extract the total energy.")
    parser.add_argument("path", help="The filepath to the file to be analyzed.", nargs="*")
    parser.add_argument("-make_plots", help="Flag to create plots of the total energy along the dynamics.", action="store_true")

    args = parser.parse_args()
    filenames = args.path

    for filename in filenames:
    
        # Get the name of each parsed file
        fname = os.path.basename(filename).split('.')[0]

        with open (filename, 'r') as f:
            data = f.readlines()
            etot = []
            for line in data:
                split_line = line.split()
                if 'Etot  ' in line:
                    etot.append(float(split_line[2]))

            values = etot[:-2]

            # Opening the file filename_Etot.txt
            with open (F'{fname}_Etot.txt', 'w+') as Etot:

                for value in values:
                    # Writing the data in Etot.txt file
                    Etot.write(F'{value}\n')

            # Plotting the MD energies
            if args.make_plots == True:
                plt.figure()
                plt.xlabel("Simulation Frame")
                plt.ylabel("Total Energy")
                fig = plt.plot(values)
                plt.savefig(F'{fname}.png')
