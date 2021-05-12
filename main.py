from total_student_marks import *
from students import *
from max_marks_subjects import *


i = 1
print('''If you want to know your marks and others details press "h"
If you want to know minimum age to give exam press "a"
If you want to know highest marks in each subject press "e"
If you want to know the subjects press "s"
''')
while i<2:
    help = input()
    if help== "h":
        print('''Enter your name to know your marks
To know the person got the highest marks press "t"
To know the person got the lowest marks press "l"
To quit write "stop" 
        ''')
        while i < 2:
            help_loop = input('What do u want to know :')
            if help_loop == "t":
                print(student_seven['student_name'])
                print(max(total_one,total_two,total_three,total_four,total_five,total_six,total_seven,total_eight,total_nine,total_ten,total_eleven,total_twelve))
            elif help_loop == "l":
                print(student_six['student_name'])
                print(min(total_one,total_two,total_three,total_four,total_five,total_six,total_seven,total_eight,total_nine,total_ten,total_eleven,total_twelve))
            elif help_loop == student_one['student_name']:
                print(student_one['student_subject_marks'])
                print("Total marks :",total_one)
                if total_one>450:
                    print("Status : Pass")
                else:
                    print("Status : Fail")
            elif help_loop==student_two['student_name']:
                print(student_two['student_subject_marks'])
                print("Total marks :", total_two)
                if total_two>450:
                    print("Status : Pass")
                else:
                    print("Status : Fail")
            elif help_loop==student_three['student_name']:
                print(student_three['student_subject_marks'])
                print("Total marks :", total_three)
                if total_three>450:
                    print("Status : Pass")
                else:
                    print("Status : Fail")
            elif help_loop==student_four['student_name']:
                print(student_four['student_subject_marks'])
                print("Total marks :", total_four)
                if total_four>450:
                    print("Status : Pass")
                else:
                    print("Status : Fail")
            elif help_loop==student_five['student_name']:
                print(student_five['student_subject_marks'])
                print("Total marks :", total_five)
                if total_five>450:
                    print("Status : Pass")
                else:
                    print("Status : Fail")
            elif help_loop==student_six['student_name']:
                print(student_six['student_subject_marks'])
                print("Total marks :", total_six)
                if total_six>450:
                    print("Status : Pass")
                else:
                    print("Status : Fail")
            elif help_loop==student_seven['student_name']:
                print(student_seven['student_subject_marks'])
                print("Total marks :", total_seven)
                if total_seven>450:
                    print("Status : Pass")
                else:
                    print("Status : Fail")
            elif help_loop==student_eight['student_name']:
                print(student_eight['student_subject_marks'])
                print("Total marks :", total_eight)
                if total_eight>450:
                    print("Status : Pass")
                else:
                    print("Status : Fail")
            elif help_loop==student_nine['student_name']:
                print(student_nine['student_subject_marks'])
                print("Total marks :", total_nine)
                if total_nine>450:
                    print("Status : Pass")
                else:
                    print("Status : Fail")
            elif help_loop==student_ten['student_name']:
                print(student_ten['student_subject_marks'])
                print("Total marks :", total_ten)
                if total_ten>450:
                    print("Status : Pass")
                else:
                    print("Status : Fail")
            elif help_loop==student_eleven['student_name']:
                print(student_eleven['student_subject_marks'])
                print("Total marks :", total_eleven)
                if total_eleven>450:
                    print("Status : Pass")
                else:
                    print("Status : Fail")
            elif help_loop==student_twelve['student_name']:
                print(student_twelve['student_subject_marks'])
                print("Total marks :", total_twelve)
                if total_twelve>450:
                    print("Status : Pass")
                else:
                    print("Status : Fail")
            else:
                print("Error")
                break
    elif help == "a":
        print("Minimum age to qualify exam is : 20")
    elif help == "e":
        print("To know the highest marks and student name write the name of the subject, when you want to exit press stop")
        while i<2:
            help_loop_one = input("Here :")
            if help_loop_one == 'english':
                print(student_four['student_name'],"got the highest marks in english :",max(a_english,b_english,c_english,d_english,e_english,f_english,g_english,i_english,j_english,k_english,l_english,))
            elif help_loop_one == 'maths':
                print(student_seven['student_name'],"got the highst marks in maths :",max(a_maths,c_maths,e_maths,g_maths,j_maths,k_maths,l_maths))
            elif help_loop_one == 'biology':
                print(student_eight['student_name'],"got the highest marks in biology :",max(b_biology,d_biology,h_biology,i_biology))
            elif help_loop_one == 'physics':
                print(student_seven['student_name'],"got the highest marks in physics :",max(a_physics,b_physics,c_physics,e_physics,g_physics,j_physics,l_physics))
            elif help_loop_one == 'chemistry':
                print(student_nine['student_name'],"got the highest marks in chemisty :",max(a_chemistry,b_chemistry,c_chemistry,e_chemistry,f_chemistry,g_chemistry,i_chemistry,j_chemistry,l_chemistry))
            elif help_loop_one == 'cse':
                print(student_seven['student_name'],"got the highest marks in cse :",max(a_cse,e_cse,f_cse,g_cse,k_cse,l_cse))
            elif help_loop_one == 'geography':
                print(student_four['student_name'],"got the highest marks in geography :",max(d_geography,h_geography))
            elif help_loop_one == 'history':
                print(student_four['student_name'],"got the highest marks in history :",max(d_history,h_history))
            elif help_loop_one == 'physical education':
                print(student_two['student_name'],"got the highest marks in physical education :",max(b_phed,c_phed,h_phed,i_phed))
            elif help_loop_one == 'civil':
                print(student_nine['student_name'],"got the highest marks in civil :",max(f_civil,i_civil,k_civil))
            elif help_loop_one == 'political science':
                print(student_ten['student_name'],"got the highest marks in political science :",max(d_ps,f_ps,h_ps,j_ps,k_ps))
            else:
                print("Error")
                break
        else:
            print("No such subjects available")
            break
    elif help == "s":
        print(['English','Maths','Biology','Physics','Chemistry','Cse','Geography','History','Physical education','Civil','Political Science'])
    else:
        print("Error")
        break

