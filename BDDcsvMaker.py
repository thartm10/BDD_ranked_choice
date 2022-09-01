import sys
import random

doctors, patients = int(sys.argv[1]), int(sys.argv[2])
outputfile = open("patient_preference_list.csv",'w')
doctorPatientMap = {}
notFirst = False

for i in range(patients):
    if notFirst:outputfile.write(",")
    doctorPatientMap[i] = random.sample(list(range(doctors)),doctors)
    outputfile.write(str(i))
    notFirst = True
outputfile.write("\n")

for j in range(doctors):
    notFirst2 = False
    for k in range(patients):
        if notFirst2:outputfile.write(",")
        outputfile.write(str(doctorPatientMap[k].index(j)))
        notFirst2 = True
    outputfile.write("\n")
