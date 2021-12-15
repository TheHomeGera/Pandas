import pandas as pd


def top(data, job_collum, qualification_collum, search_str):
    return data[data[job_collum].str.lower().str.contains(
        search_str[:-2])][qualification_collum].str.lower().value_counts().head(5)


works = pd.read_csv("works.csv").dropna()
print(top(works, "jobTitle", "qualification", "инженер"))
