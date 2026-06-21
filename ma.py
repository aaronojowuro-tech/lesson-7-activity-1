medical_cause = input("do you have your medical cause? (y/n): ").strip().upper()
if medical_cause == "Y":
    print("you are allowed ")
else:
    a=int(input("enter your attetendance"))
    if a>=75:
        print("you are allowed")