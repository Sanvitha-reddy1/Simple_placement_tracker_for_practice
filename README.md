#**Placement Readiness Tracker - Using simple NUMPY, PANDAS , DATA VISUALIZATION USING MATPLOTLIB**#

Generated a Dataset of Students

`python generate_placement_data.py`

You get placement_readiness.csv with these columns:


| Column Name | Meaning / Description |
| :--- | :--- |
| **Student_ID** | Anonymous ID |
| **Branch** | CSE / ECE / IT / MECH |
| **Python_Score** | Out of 100 |
| **SQL_Score** | Out of 100 |
| **Aptitude_Score** | Out of 100 |
| **Communication_Score** | Out of 100 |
| **Projects_Completed** | Count |
| **Mock_Interviews_Attended** | Count |

This is simulated data. It is not real students. Never do this analysis on real classmates.

**Calculated Readiness Band**

Add a column Readiness_Band:


| Condition | Band |
| :--- | :--- |
| Readiness Score ≥ 75 | Ready |
| 60 to 74 | Almost Ready |
| Below 60 | Needs Work |


**Charts** <br>
Bar chart: average score for each of the four skills<br>
Bar chart: how many students are in each readiness band<br>
Line or bar chart: average readiness score by branch<br>

**The report**

The weakest skill across the batch is ______ because ______. <br>
______ students are ready right now.<br>
The largest group is ______, which means ______.<br>
The single most useful training session would be ______ because ______.<br>
One thing that surprised me in this data was ______.<br>
If I only had time to help ten students, I would pick ______ because ______.<br>
