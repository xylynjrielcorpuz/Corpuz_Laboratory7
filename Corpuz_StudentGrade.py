#pROFILE
User_Name = input("Please enter the name of the student: ")
User_Section = input("Please enter the section of the Student (e.g., BSIT-103): ")

#Prelims
User_Prelim_Grade = float(input("Input the preliminary grade (40 to 100 only): "))
if User_Prelim_Grade <= 100 and User_Prelim_Grade >= 40: 
    User_Compute_Prelim = 33.33*(User_Prelim_Grade/100)
    #Midterms
    User_Midterm_Grade = float(input("Input the midterm grade (40 to 100 only): "))
    if User_Midterm_Grade <= 100 and User_Midterm_Grade >= 40: 
        User_Compute_Midterm = 33.33*(User_Midterm_Grade/100)
        User_Final_Grade = float(input("Input the final grade (40 to 100 only): "))
        
    #Finals
        if User_Final_Grade <=100 and User_Final_Grade >= 40:
            User_Compute_Finals = 33.34*(User_Final_Grade/100)
            User_GWA = User_Compute_Prelim + User_Compute_Midterm + User_Compute_Finals
            User_GWA_final = round(User_GWA)
        
            print(f"The Final Grade of {User_Name} of {User_Section} is: {User_GWA_final}")
            
            #Computation of GPA
            if User_GWA_final >= 99 and User_GWA_final <=100:
                GPA_1 = 1.00
                print(f"The GPA of {User_Name} is {GPA_1:.2f}")
                print("Thank you!")
                
            elif User_GWA_final >= 96 and User_GWA_final <=98:
                GPA_2 = 1.25
                print(f"The GPA of {User_Name} is {GPA_2:.2f}")
                print("Thank you!")
                
            elif User_GWA_final >= 93 and User_GWA_final <=95:
                GPA_3 = 1.50
                print(f"The GPA of {User_Name} is {GPA_3:.2f}")
                print("Thank you!")
            
            elif User_GWA_final >= 90 and User_GWA_final <=92:
                GPA_4 = 1.75
                print(f"The GPA of {User_Name} is {GPA_4:.2f}")   
                print("Thank you!")
            
            elif User_GWA_final >= 87 and User_GWA_final <=89:
                GPA_5 = 2.00
                print(f"The GPA of {User_Name} is {GPA_5:.2f}")  
                print("Thank you!") 
            
            elif User_GWA_final >= 84 and User_GWA_final <=86:
                GPA_6 = 2.25
                print(f"The GPA of {User_Name} is {GPA_6:.2f}")  
                print("Thank you!") 
            
            elif User_GWA_final >= 81 and User_GWA_final <=83:
                GPA_7 = 2.50
                print(f"The GPA of {User_Name} is {GPA_7:.2f}")
                print("Thank you!")   
                
            elif User_GWA_final >= 78 and User_GWA_final <=80:
                GPA_8 = 2.75
                print(f"The GPA of {User_Name} is {GPA_8:.2f}") 
                print("Thank you!")    
                
            elif User_GWA_final >= 75 and User_GWA_final <=77:
                GPA_9 = 3.00
                print(f"The GPA of {User_Name} is {GPA_9:.2f}")  
                print("Thank you!") 
                
            elif User_GWA_final < 75:
                GPA_9 = 5.00
                print(f"The GPA of {User_Name} is {GPA_9:.2f}")  
                print("Thank you!") 
            
            else:
                print("Retry. There must be an error.")
                print("Thank you!")
            
        else:
            print("Invalid. Input grade must be 40 to 100 only.")
            print("Thank you!")
    else:
        print("Invalid. Input grade must be 40 to 100 only.")
        print("Thank you!")
        
else:
    print("Invalid. Input grade must be 40 to 100 only.")
    print("Thank you!")
    
    






    


