score = [99,97,96,75,93,23,0,75,84,34,50,66,92]
s_score = sorted(score, reverse = True)
print(s_score)
#score is 20% - A, 30% - B, 30% - C, 20% - D
A = round(s_score.__len__()/10*2)
B = round(s_score.__len__()/10*3)
C = round(s_score.__len__()/10*3)
D = round(s_score.__len__()/10*2)
print("A Score is :")
print(s_score[0:A])
print("B Score is :")
print(s_score[A:A+B])
print("C Score is :")
print(s_score[A+B:A+B+C])
print("D Score is :")
print(s_score[A+B+C:A+B+C+D])


