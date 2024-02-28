
def create_student(name, korean, math, english, science) :
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }
def student_get_sum (student) :
    return student["korean"]+student["math"]+ \
           student["english"]+student["science"] 
           
def student_get_avg(student) :
    return (student_get_sum (student) / 4)

def student_to_string (student):
    return ("{}\t{}\t{}\t".format(student["name"], student_get_sum(student), student_get_avg(student)))

students = [
    create_student("yoon in sung", 65,73,73,94),
    create_student("go so tung", 65,23,98,97),
    create_student("kang in ho", 76,83,13,85),
    create_student("hansol gks", 78,98,99,31),
    create_student("jeng chul woong", 68,97,45,99),
    create_student("kim in ho", 56,87,99,33),
]

print("name","all sum","average",sep="\t")

for student in students:
    print(student_to_string(student))


