students = [
    {"name" : "yoon in seng", "korean" : 87, "math" : 98, "english" : 79, "science" : 14},
    {"name" : "ji sung", "korean" : 23, "math" : 12, "english" : 32, "science" : 67},
    {"name" : "hansil hem", "korean" : 33, "math" : 45, "english" : 68, "science" : 85},
    {"name" : "jeong han sol", "korean" : 45, "math" : 58, "english" : 56, "science" : 58},
    {"name" : "park jun gu", "korean" : 67, "math" : 95, "english" : 86, "science" : 95},
    {"name" : "han nam i", "korean" : 67, "math" : 75, "english" : 53, "science" : 57},
]

print("이름","총점","평균",sep="\t")

for student in students:
    score_sum=student["korean"]+student["math"]+ \
               student["english"]+student["science"]
    score_average=score_sum/4
    print(student["name"],score_sum,score_average,sep="\t")