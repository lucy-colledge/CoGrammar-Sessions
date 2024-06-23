# to avoid error in calculations minutes and seconds must be treated seperatly
# swimming time = swimming_minutes : swimming_seconds
# cycling = cycling_minutes : cycling_seconds
# running = running_minutes : running_seconds
# ts round to nearest minute 
# triatholon total = tm : ts

# if t <= 100 : print (" Congratulations! You have achieved qualified for Provincial Colours")
# if t <= 105 : print (" Congratulations! You have achieved qualified for Provincial Half Colours")
# if t <= 110 : print (" Congratulations! You have achieved qualified for Provincial Scoll")
# else : print (" Unfortunatly you have not qualified for any awards in this competition, please try again.")

run_m , run_s = (input("Please enter you running time in the format Minutes:Seconds ")). split (":")
cyc_m , cyc_s = (input("Please enter you cycling time in the format Minutes:Seconds ")). split(":") 
swi_m , swi_s = (input("Please enter you swimming time in the format Minutes:Seconds ")). split(":") 
total_s = ( (int(run_s)) + (int(cyc_s)) + (int(swi_s)))
sec_m = round((total_s/int(60)),0)
total_m = ((int(run_m)) + (int(cyc_m)) + (int(swi_m)) + (int(sec_m)))
f = str(total_m)
print ( "Your total time to the nearest minute is: " + f)

if total_m <= 100 : 
    print (" Congratulations! You have achieved Provincial Colours")
elif total_m <= 105 :
    print (" Congratulations! You have achieved Provincial Half Colours")
elif total_m <= 110 :
    print (" Congratulations! You have achieved Provincial Scoll")
else : 
    print (" Unfortunatly you have not qualified for any awards in this competition.")
