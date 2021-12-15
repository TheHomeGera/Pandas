import pandas as pd


def count_people_job_not_match_qualification(job_collum, qualification_collum, data):
    count = 0
    for (job, qualification) in zip(data[job_collum], data[qualification_collum]):
        if not find_match(job, qualification) and not find_match(qualification, job):
            count += 1
    return count


def find_match(field1, field2):
    mas = field1.lower().replace('-', ' ').split()
    for word in mas:
        if word in field2.lower():
            return True
    return False


works = pd.read_csv("works.csv").dropna()
count_people = count_people_job_not_match_qualification("jobTitle", "qualification", works)
print("у {} людей не совпадают профессия и должность".format(count_people))
