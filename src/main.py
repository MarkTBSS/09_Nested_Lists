aiyaArray = [ 
                ['Harry', 37.21], 
                ['Berry', 37.21], 
                ['Tina', 37.2], 
                ['Akriti', 41.0], 
                ['Harsh', 39.0]
            ]

aiyaArray.sort(key=lambda x: x[1])
lowestScore = aiyaArray[0][1]

""" secondScoreArray = []
for student in aiyaArray:
    name, score = student[0], student[1]
    if score != lowestScore:
        secondScoreArray.append(student)
print(secondScoreArray) """

secondScoreArray = [student for student in aiyaArray if student[1] != lowestScore]

lowestScore = secondScoreArray[0][1]

""" thirdScoreArray = []
for student in secondScoreArray:
    name, score = student[0], student[1]
    if score == lowestScore:
        thirdScoreArray.append(student) """

thirdScoreArray = [student for student in secondScoreArray if student[1] == lowestScore]
thirdScoreArray.sort()

for student in thirdScoreArray:
    name = student[0]
    print(name)
