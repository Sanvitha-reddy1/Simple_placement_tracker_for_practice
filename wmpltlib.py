import pandas as pd
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

plt.figure(figsize = (10,6))

df = pd.read_csv("placement_readiness.csv")

skills_total = {
    "Python" : df["Python_Score"].mean(),
    "SQL" : df["SQL_Score"].mean(),
    "Communication" : df["Communication_Score"].mean(),
    "Aptitude" : df["Aptitude_Score"].mean()
}
 
plt.bar(skills_total.keys(), skills_total.values(), color = ["blue" , "orange" , "green" , "red"])

plt.title("Average Score of Students in each Skill")

plt.xlabel("Skills")

plt.ylabel("Average Score")

plt.xticks(rotation = 0)

plt.tight_layout()

plt.savefig("charts/average_score.png")

plt.close()

df2 = pd.read_csv("my_analysis.csv")

# print(df2["Readiness_Band"].value_counts().get("Ready"))

readiness = {
    "Need Work" : df2["Readiness_Band"].value_counts().get("Need Work"),
    "Almost Ready" : df2["Readiness_Band"].value_counts().get("Almost Ready"),
    "Ready" : df2["Readiness_Band"].value_counts().get("Ready"),
}

plt.figure(figsize = (10,6))

plt.bar(readiness.keys(), readiness.values(), color = ["blue" , "green" , "red"])

plt.title("Students in Readiness Band")

plt.xlabel("Readiness Band")

plt.ylabel("Number of Students")

plt.xticks(rotation = 0)

plt.tight_layout()

plt.savefig("charts/readiness_cnt.png")

plt.close()

# it_rs = df2.loc[df2["Branch"]=="IT","Readiness_score"]

# print(it_rs)

readiness_by_branch = {

    "CSE" : df2.loc[df2["Branch"]=="CSE","Readiness_score"].mean().round(2),
    "IT" :  df2.loc[df2["Branch"]=="IT","Readiness_score"].mean().round(2),
    "ECE" : df2.loc[df2["Branch"]=="ECE","Readiness_score"].mean().round(2),
    "MECH" : df2.loc[df2["Branch"]=="MECH","Readiness_score"].mean().round(2)
}

#print(readiness_by_branch.values())
plt.figure(figsize = (10,6))

plt.plot(readiness_by_branch.keys(), readiness_by_branch.values(), marker = "o" , label = "Average Readiness by branch", color = "purple")

plt.title("Average Readiness score by branch")

plt.xlabel("Branch")

plt.ylabel("Readiness Score")

plt.legend()

plt.xticks(rotation = 0)

plt.tight_layout()

plt.savefig("charts/avg_readiness_by_branch.png")

plt.close()