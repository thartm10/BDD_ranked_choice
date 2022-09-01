import sys
import random

doctors, patients = int(sys.argv[1]), int(sys.argv[2])
outputfile = open("patient_preference_list.csv",'w')

doctorList = list(range(doctors))

for i in doctorList:
    outputfile.write(","+str(i))
outputfile.write("\n")

for j in range(patients):
    outputfile.write(str(j))
    [outputfile.write(","+str(k)) for k in random.sample(doctorList,doctors)]
    outputfile.write("\n")
