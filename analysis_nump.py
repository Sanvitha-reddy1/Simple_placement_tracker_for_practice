import numpy as np
import csv

python_score = []
aptitude = []
communication = []
gap = []

with open("placement_readiness.csv" , "r" ,encoding = "utf-8") as file : 
    reader = csv.DictReader(file)
    for row in reader : 
        python_score.append(int(row["Python_Score"]))
        aptitude.append(int(row["Aptitude_Score"]))
        communication.append(int(row["Communication_Score"]))
        gap.append(max(int(row["Aptitude_Score"]), int(row["Communication_Score"]), int(row["Python_Score"]),int(row["SQL_Score"])) - min(int(row["Aptitude_Score"]), int(row["Communication_Score"]), int(row["Python_Score"]),int(row["SQL_Score"])))

python_score = np.array(python_score);
aptitude = np.array(aptitude)
communication = np.array(communication)
gap = np.array(gap)

py_avg = python_score.mean()

apt_hi = aptitude.max()
apt_lo = aptitude.min()

comm_greater = (communication > 70).sum()

print(comm_greater)
print(gap)