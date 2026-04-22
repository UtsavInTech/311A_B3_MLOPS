📌 Project Overview

This project demonstrates basic dataset exploration (EDA) using the Scopus research paper dataset with Python and Pandas.
The goal is to understand dataset structure, statistics, missing values, and perform simple filtering and grouping operations.

⸻

🛠️ Technologies Used

* Python 🐍
* Pandas 📊
* CSV Dataset

⸻

📂 Dataset Description

The dataset (scopus.csv) contains research paper details such as:

* Title → Name of research paper
* Authors → Author name
* Year → Publication year
* Citations → Number of citations
* Journal → Publishing journal
* Field → Research domain
* Country → Author country

⸻

▶️ Steps Performed in the Code

The following operations are performed:

1. Load dataset using Pandas
2. Display first and last records
3. Check dataset shape
4. View column names
5. Show dataset information
6. Generate statistical summary
7. Detect missing values
8. Count unique values
9. Filter records based on year
10. Group data by research field
11. Sort papers based on citations

⸻

🚀 How to Run the Project

Step 1:
Install Pandas (if not installed)
pip install pandas
Step 2:
Place scopus.csv in the same folder as the Python file

Step 3:
Run the script
python explore_scopus.py


The program displays:

* Dataset structure
* Statistical summary
* Missing values
* Filtered records
* Grouped citation averages
* Top cited papers