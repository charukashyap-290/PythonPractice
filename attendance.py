p_days=int(input())

if p_days<=210:
    # calculate percentage
    per_cent = (p_days/210)*100 #percentage of the student
    print(per_cent)

    if per_cent>=70:# if the percentage is greater or less then 70
        print("You are allowed in the examination.")# then the student is allowed
    elif per_cent<70:
        print("Allowed ONLY IF you have a medical certificate")

        #'''check if the student have th eemdical cerificate or not'''
        med_certi=input("do you have a medical certificate ?\n yes/no ").lower() in ['yes','y','true']

        if med_certi==True:
            print("Allowed, as you have the medical certificate") 
        else:
            print("You do not have the medical cerificate, \nThus you are NOT ALLOWED")      
        
else:
    print("Invalid")