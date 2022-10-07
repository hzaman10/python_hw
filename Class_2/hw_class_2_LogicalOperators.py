                                #Python Operators

#---------------------------Python Logical Operators---------------------

'''
Operator 	    Description 	                                                Example 	
and  	        Returns True if both statements are true 	                    x < 5 and  x < 10 	
or 	            Returns True if one of the statements is true 	                x < 5 or x < 4 	
not 	        Reverse the result, returns False if the result is true         not(x < 5 and x < 10)
'''
#------------------------and operator------------
x=92

if x<60:
    print("Grade is : F")
elif x>=60 and x<70:
    print("Grade is : D")
elif x>=70 and x<80:
    print("Grade is : B")
elif x>=80 and x<90:
    print("Grade is : A")
elif x>=90 and x<=100:
    print("Grade is : A+")

#Grade is : A+

#------------------------or operator------------
y=90
print(y>50 or y>60)
#True

#------------------------not operator------------
y=90
print(not(y>50 or y>60))
#False



#---------------------------End of Logical Comparison Operators---------------------


