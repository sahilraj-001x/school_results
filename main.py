from total_student_marks import *
from students import *
from max_marks_subjects import *
from student_first_last_name import *

print('Type start to start the programme and stop to end the programme')
start = input().lower()
if start =='start':
    i = 1
    print('''PART 1
[1]. If you want to know your marks and others details press "h"
[2]. If you want to know minimum age to give exam press "a"
[3]. If you want to know the subjects press "s"
[4]. If you want to know highest marks in each subject press "e"
[5]. To exit type "stop"
    ''')
    while i<2:
        help = input('Choose anyone from PART 1 :').lower()
        if help== "h":
            print('''PART 2
    [1]. Enter your name to know your marks
    [2]. To know the person got the highest marks press "t"
    [3]. To know the person got the lowest marks press "l"
    [4]. To quit write "stop" 
            ''')
            while i < 2:
                help_loop = input('Choose anyone from PART 2 :').lower()
                if help_loop == "t":
                    print(student_seven['student_name'])
                    print(max(total_one,total_two,total_three,total_four,total_five,total_six,total_seven,total_eight,total_nine,total_ten,total_eleven,total_twelve))

                elif help_loop == "l":
                    print(student_six['student_name'])
                    print(min(total_one,total_two,total_three,total_four,total_five,total_six,total_seven,total_eight,total_nine,total_ten,total_eleven,total_twelve))

                elif help_loop==student1_first or help_loop==student1:
                    password_one = input("Enter your password :")
                    if password_one == student_one["student_password"]:
                        if student_one['student_age'] >= 20:
                            print(student_one['student_subject_marks'])
                            print("Total marks :",total_one)
                            print("Pass at 450")
                            if total_one>450:
                                print("Status : Pass")
                            else:
                                print("Status : Fail")
                        else:
                            print('Under age 20years are not eligible')
                    else:
                        print("wrong password !!!")

                elif help_loop==student2 or help_loop==student2_first:
                    password_two = input("Enter your password :")
                    if password_two == student_two["student_password"]:
                            if student_two['student_age'] >= 20:
                                print(student_two['student_subject_marks'])
                                print("Total marks :", total_two)
                                print("Pass at 450")
                                if total_two>450:
                                    print("Status : Pass")
                                else:
                                    print("Status : Fail")
                            else:
                                print('Under age 20years are not eligible')
                    else:
                        print("wrong password !!!")

                elif help_loop==student3 or help_loop==student3_first:
                    password_three = input("Enter your password :")
                    if password_three == student_three["student_password"]:
                        if student_three['student_age'] >= 20:
                            print(student_three['student_subject_marks'])
                            print("Total marks :", total_three)
                            print("Pass at 450")
                            if total_three>450:
                                print("Status : Pass")
                            else:
                                print("Status : Fail")
                        else:
                            print('Under age 20years are not eligible')
                    else:
                        print("wrong password !!!")

                elif help_loop==student4 or help_loop==student4_first:
                    password_four = input("Enter your password :")
                    if password_four == student_four["student_password"]:
                        if student_four['student_age'] >= 20:
                            print(student_four['student_subject_marks'])
                            print("Total marks :", total_four)
                            print("Pass at 450")
                            if total_four>450:
                                print("Status : Pass")
                            else:
                                print("Status : Fail")
                        else:
                            print('Under age 20years are not eligible')
                    else:
                        print("wrong password !!!")

                elif help_loop==student5 or help_loop==student5_first:
                    password_five = input("Enter your password :")
                    if password_five == student_five["student_password"]:
                        if student_five['student_age'] >= 20:
                            print(student_five['student_subject_marks'])
                            print("Total marks :", total_five)
                            print("Pass at 450")
                            if total_five>450:
                                print("Status : Pass")
                            else:
                                print("Status : Fail")
                        else:
                            print('Under age 20years are not eligible')
                    else:
                        print("wrong password !!!")

                elif help_loop==student6 or help_loop==student6_first:
                    password_six = input("Enter your password :")
                    if password_six == student_six["student_password"]:
                        if student_six['student_age'] >= 20:
                            print(student_six['student_subject_marks'])
                            print("Total marks :", total_six)
                            print("Pass at 450")
                            if total_six>450:
                                print("Status : Pass")
                            else:
                                print("Status : Fail")
                        else:
                            print('Under age 20years are not eligible')
                    else:
                        print("wrong password !!!")

                elif help_loop==student7 or help_loop==student7_first:
                    password_seven = input("Enter your password :")
                    if password_seven == student_seven["student_password"]:
                        if student_seven['student_age'] >= 20:
                            print(student_seven['student_subject_marks'])
                            print("Total marks :", total_seven)
                            print("Pass at 450")
                            if total_seven>450:
                                print("Status : Pass")
                            else:
                                print("Status : Fail")
                        else:
                            print('Under age 20years are not eligible')
                    else:
                        print("wrong password !!!")

                elif help_loop==student8 or help_loop==student8_first:
                    password_eight = input("Enter your password :")
                    if password_eight == student_eight["student_password"]:
                        if student_eight['student_age'] >= 20:
                            print(student_eight['student_subject_marks'])
                            print("Total marks :", total_eight)
                            print("Pass at 450")
                            if total_eight>450:
                                print("Status : Pass")
                            else:
                                print("Status : Fail")
                        else:
                            print('Under age 20years are not eligible')
                    else:
                        print("wrong password !!!")

                elif help_loop==student9 or help_loop==student9_first:
                    password_nine = input("Enter your password :")
                    if password_nine == student_nine["student_password"]:
                        if student_nine['student_age'] >= 20:
                            print(student_nine['student_subject_marks'])
                            print("Total marks :", total_nine)
                            print("Pass at 450")
                            if total_nine>450:
                                print("Status : Pass")
                            else:
                                print("Status : Fail")
                        else:
                            print('Under age 20years are not eligible')
                    else:
                        print("wrong password !!!")

                elif help_loop==student10 or help_loop==student10_first:
                    password_ten = input("Enter your password :")
                    if password_ten == student_ten["student_password"]:
                        if student_ten['student_age'] >= 20:
                            print(student_ten['student_subject_marks'])
                            print("Total marks :", total_ten)
                            print("Pass at 450")
                            if total_ten>450:
                                print("Status : Pass")
                            else:
                                print("Status : Fail")
                        else:
                            print('Under age 20years are not eligible')
                    else:
                        print("erong password !!!")

                elif help_loop==student11 or help_loop==student11_first:
                    password_eleven = input("Enter your password :")
                    if password_eleven == student_eleven["student_password"]:
                        if student_eleven['student_age'] >= 20:
                            print(student_eleven['student_subject_marks'])
                            print("Total marks :", total_eleven)
                            print("Pass at 450")
                            if total_eleven>450:
                                print("Status : Pass")
                            else:
                                print("Status : Fail")
                        else:
                            print('Under age 20years are not eligible')
                    else:
                        print("wrong password !!!")

                elif help_loop==student12 or help_loop==student12_first:
                    password_twelve = input("Enter your password :")
                    if password_twelve == student_twelve["student_password"]:
                        if student_twelve['student_age'] >= 20:
                            print(student_twelve['student_subject_marks'])
                            print("Total marks :", total_twelve)
                            print("Pass at 450")
                            if total_twelve>450:
                                print("Status : Pass")
                            else:
                                print("Status : Fail")
                        else:
                            print('Under age 20years are not eligible')
                    else:
                        print("wrong password !!!")

                elif help_loop=='stop':
                    print('back to part 1')
                    break
                else:
                    print("Error")
                    i+=1
        elif help == "a":
            print("Minimum age to qualify exam is : 20")
        elif help == "e":
            print(['English', 'Maths', 'Biology', 'Physics', 'Chemistry', 'Cse', 'Geography', 'History', 'Physical education', 'Civil', 'Political Science'])
            print("\nTo know the highest marks and student name write the name of the subject, when you want to exit press stop")
            while i<2:
                help_loop_one = input("Here :").lower()
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

                elif help_loop_one == 'stop':
                    print('back to part 1')
                    break
                else:
                    print("Error")
            else:
                print("No such subjects available")
                break
        elif help == "s":
            print(['English','Maths','Biology','Physics','Chemistry','Cse','Geography','History','Physical education','Civil','Political Science'])
        elif help == 'stop':
            print('... THANK YOU ...')
            break
        else:
            print("Error")
            i+=1
elif start == 'stop':
    print('... THANK YOU ...')
else:
    print('error ......required value not found')
