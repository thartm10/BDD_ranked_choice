import sys
import random

doctors, patients = int(sys.argv[1]), int(sys.argv[2])
outputfile = open("patient_preference_list.csv",'w')
doctorPatientMap = {}

for i in range(patients):
    doctorPatientMap[i] = random.sample(list(range(doctors)),doctors)
    outputfile.write(","+str(i))
outputfile.write("\n")

for j in range(doctors):
    outputfile.write(str(j))
    for k in range(patients):
        outputfile.write(","+str(doctorPatientMap[k].index(j)))
    outputfile.write("\n")
