# INTERVIEW QUESTION

The objective is to determine which students have failed the class and which have passed.  The rules are simple, if the student has ALL fail grades for their assignments then they fail the class.  If the student has one or more 'pass' grades, then they pass the class.

Create a report that gives us the list of students that have failed, and students that have passed.

Watch for:
* Students with no assignment data (maybe someone that was signed up for the class but never attended)
* Pass/Fail results data could be variants of the word 'pass' and 'fail'.
* An assignment was never submitted for that student - the grade is 'null'

## Data

You'll find the data in ./data folder named student_data.json.
There will be 300 students in the data with 0 or more assignments they have taken, each with a pass/fail/None (never submitted).

## Report Card

Read in the data and return a report with the following format:

    student name: PASS|FAIL (count) Passing Assignments, (count) Failing Assignments, (count) Unsubmitted

The final report should have 1 entry per student, so 300 entries.
Sort the above report by all students that have passed, followed by all of the failing students.

# Simple Example

## Inputs

```json
[
  {
    "student_name":"student1",
    "assignment": { "name":"Assignment1", "result":"pass" }
  },
  {
    "student_name":"student1",
    "assignment": {"name":"Assignment2", "result":"pass" }
  },
  {
    "student_name":"student2",
    "assignment": {"name":"Assignment1", "result":"fail" }
  },
  {
    "student_name":"student1",
    "assignment": {"name":"Assignment2", "result":"fail" }
  }
]
```

## Output

    student1: PASS (2) Passing Assignments, (0) Failing Assignments, (0) Unsubmitted
    student2: FAIL (0) Passing Assignments, (2) Failing Assignments, (0) Unsubmitted