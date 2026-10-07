import pandas as pd
import numpy as np 

df = pd.read_csv("placement_readiness.csv")

print(df.head())
print(df.shape)

print("Students with python above 75 : \n",df[df['Python_Score'] > 75].head())

df = df.sort_values('Aptitude_Score', ascending = False)
print("Apptitude Marks from highest : \n",df.head())

py_top = df.sort_values('Python_Score',ascending= False)

print("Top 10 Python Scores of Students : \n",py_top['Python_Score'].head())

pyvscom = df[(df['Python_Score'] > 65) & (df['Communication_Score'] < 45)]

print("students who are strong in Python but weak in Communication : \n",pyvscom.head(10))

df['Total_Score'] = df['Python_Score'] + df['Communication_Score'] + df['Aptitude_Score'] + df['SQL_Score']

print("Total Score \n", df['Total_Score'].head())

df['Average_Score'] = df['Total_Score']/4

print("Average Score \n",df['Average_Score'].head())

# List the columns you want to compare and use .min(axis=1)
skill_columns = ['Python_Score', 'Aptitude_Score', 'SQL_Score', 'Communication_Score']

df['Lowest_Skill_Score'] = df[skill_columns].min(axis=1)

# print(df['Lowest_Skill_Score'].head())

total_score = df["Average_Score"] + (df["Projects_Completed"] * 2) + df["Mock_Interviews_Attended"]

# Apply the cap at 100 using .clip()
df["Readiness_score"] = total_score.clip(upper=100)

df["Readiness_Band"] = "Almost Ready"

df.loc[df["Readiness_score"] >= 75 , "Readiness_Band"] = "Ready"

df.loc[df["Readiness_score"] < 60  , "Readiness_Band"] = "Need Work"

print(df['Readiness_Band'].head(10))

df.to_csv("my_analysis.csv")

print(df['Readiness_Band'].value_counts())

py_avg = df['Python_Score'].mean()

sql_avg = df['SQL_Score'].mean()

com_avg = df['Communication_Score'].mean()

apt_avg = df['Aptitude_Score'].mean()

label = ["Python" , "SQL" , "Communication" , "Aptitude"]

weakest_skill = np.array([py_avg, sql_avg, com_avg, apt_avg]).argmin()

print("Weakest Skill : ",label[weakest_skill])