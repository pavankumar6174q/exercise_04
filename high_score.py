student_scores = input("enter student scores with a space ").split()
for n in range(0 , len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)
high = 0
for scores in student_scores:
    if scores>high:
        high =scores
print(high)
    