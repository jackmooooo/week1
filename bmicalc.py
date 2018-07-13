print('weclome to my bmi calculator')
def helper(kgorlb, morin):
    if kborlb == "kb":
        if morin == "m":
            def calckgm(YourWeightInKilograms, YourHeightInMeters):
                height = float(YourHeightInMeters)
                weight = float(YourWeightInKilograms)
                bmi = weight/(height**2)
                if bmi >= 40:
                    print("you are morbidly obese")
                elif bmi < 40 & bmi >= 30:
                    print("you are obese")
                elif bmi < 30 & bmi >= 25:
                    print("you are overweight")
                elif bmi < 25 & bmi >= 18.5:
                    print("you are normal")
                elif bmi < 18.5 & bmi >= 2:
                    print("you are underweight")
                elif bmi < 2:
                    print("what are you?")
                calckgm(input("Your Weight In Kilograms>>"), input("Your Height In Meters>>"))
helper(input("kb or lb>>"), input("m or in>>"))
