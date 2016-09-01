#!/usr/bin/env python

#Useage: ./script.py <metadata.csv> <ctab_dir> <replicates>


import sys
import pandas as pd
import matplotlib.pyplot as plt

sample_file = pd.read_csv(sys.argv[1])
ctab_dir = sys.argv[2]
rep_file = pd.read_csv(sys.argv[3])

fem_Sxl = []
male_Sxl = []
fem_reps_Sxl = []
male_reps_Sxl = []

fem_samples = sample_file["sex"] == "female"
for sample in sample_file[fem_samples]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    sxl_samples = df["t_name"] == "FBtr0331261"
    fem_Sxl.append(df[sxl_samples]["FPKM"].values)
dev_stage = sample_file[fem_samples]["stage"].values

male_samples = sample_file["sex"] == "male"
for sample in sample_file[male_samples]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    sxl_samples = df["t_name"] == "FBtr0331261"
    male_Sxl.append(df[sxl_samples]["FPKM"].values)

fem_samples = rep_file["sex"] == "female"
for sample in rep_file[fem_samples]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    sxl_samples = df["t_name"] == "FBtr0331261"
    fem_reps_Sxl.append(df[sxl_samples]["FPKM"].values)

male_samples = rep_file["sex"] == "male"
for sample in rep_file[male_samples]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    sxl_samples = df["t_name"] == "FBtr0331261"
    male_reps_Sxl.append(df[sxl_samples]["FPKM"].values)

replica = [4, 5, 6, 7]
    


#print dev_stage

plt.figure()
plt.plot( fem_Sxl, color="r")
plt.plot( male_Sxl, color="b" )
plt.scatter( replica, fem_reps_Sxl, color="r")
plt.scatter( replica, male_reps_Sxl, color="b")
plt.title("Sxl abundance by developmental stage")
plt.xlabel("Developmental stage (days)")
plt.ylabel("FPKM")
plt.xticks(range(len(dev_stage)), dev_stage)
plt.savefig("Sxl_timecourse.png")
plt.close()