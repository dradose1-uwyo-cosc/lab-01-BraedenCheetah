# Braeden Kirby
# UWYO COSC 1010
# 10/15/2024
# HW 01
# Lab Section: 13
# Sources, people worked with, help given to:

# Homework Question:
#
# You are given a list of dictionaries where each dictionary represents a student
# and their scores
# in different subjects.
#
# Student Data:
# students = [
# {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
# {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
# {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
# {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
# ]
#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key 
# and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.
# Your task is to calculate the average scores for each student and print the names
# of students
# whose average score is greater than 80.
# Solution

#I will input the data for the students from the comments

students = [
 {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
 {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
 {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
 {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
]

#I will add a dictionary to hold the average scores so that they ar accessible

avg_scores = {}

#I will use a for/loop statement in order to calculate the average score for each student

for student in students:
    name = student["name"]
    scores = student["scores"]
    average = sum(scores.values()) / len(scores)
    avg_scores[name] = average

#I will use another for/loop statement to calculate if a student's score is above 80 so that it is printed

for name, average in avg_scores.items():
    if average > 80:
        print(name, "scored above an average of 80 on their exams.")