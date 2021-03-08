# =============================================================================

# =============================================================================
# import pprint
# =============================================================================
# main_dictionary = {}
# yeshivas = {}
# def student(yeshiva_name, student_name, school_set, age_set):
#          schools.setdefault(yeshiva_name)
#          student = {}
#          student['school'] = school_set
#          student['age'] = age_set
#          yeshiva_name[student_name]= student
# 
# student('Shraga', 'Dave', 'High', 18), student('Shraga', 'Yehuda', 'High', 18), 
# student('Reishit', 'Josh', 'prep', 18)
# 
# pprint.pprint(main_dictionary)
# # 
# 
# =============================================================================
import pprint
Shraga = {}
def student(student_name, school_set, age_set):
     student = {}
     student['school'] = school_set
     student['age'] = age_set
     Shraga[student_name]= student
student('Dave', 'High', 18), student('Yehuda', 'High', 18), 
student('Josh', 'prep', 18)

pprint.pprint(Shraga)

    