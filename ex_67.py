import random

hanguls = list("abcdefghijkmnlopqrstu")

with open("info.txt","w") as file :
    for i in range(1000) :
        name =  random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40,100)
        height = random.randrange(140,200)
        
        
        file.write("{},{},{}\n".format(name, weight,height))

