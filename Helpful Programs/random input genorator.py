import random

categorys = ["Caring for others and the environment", "Participation", "Excellence (in any area)", "Correct uniform", "Attitude towards attendance", "Commitment to Tutor Group", "Courtesy"]

outFile = open("dataset.csv", "w")

for i in range(100):
    output = ""
    person = ""
    catNum = random.randint(0, len(categorys)-1)
    
    if catNum > 0 and catNum < 3: person = "Peer {0}".format(random.randint(1, 100))
    elif catNum > 2 and catNum < 5: person = "Tutor {0}".format(random.randint(1, 25))
    else:
        if random.randint(0, 1) == 0: person = "Peer {0}".format(random.randint(1, 100))
        else: person = "Tutor {0}".format(random.randint(1, 25))

    output += "Person {0},{1},{2}\n".format(i+1, categorys[catNum], person)
    outFile.write(output)

outFile.close()
