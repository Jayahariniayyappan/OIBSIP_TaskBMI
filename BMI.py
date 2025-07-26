def calculate_bmi():
    print("Welcome to the BMI Calculator")
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))

    # Calculate BMI
    bmi = weight / (height ** 2)
    print(f"\nYour BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("Category: Underweight")
        print("Based on your category, small suggestions for your health:")
        print("You might be under your ideal weight." \
        "It's a good idea to include more nutritious, calorie-rich foods in your diet and maybe try strength-building exercises to gain healthy weight.")
    elif 18.5 <= bmi < 24.9:
        print("Category: Normal weight")
        print("Based on your category, small suggestions for your health:")
        print("Great!You're in the healthy weight range.Keeep doing what you're doing-stay active and eat balanced meals.")
    elif 25 <= bmi < 29.9:
        print("Category: Overweight")
        print("Based on your category, small suggestions for your health:")
        print("You're slightly over the ideal range.This could be a good time to look at your diet and a=daily activity." \
        "Small changes can make a big differences-like walking more, eating home-cooked food, or drinking more water.")
    else:
        print("Category: Obese")
        print("Based on your category, small suggestions for your health:")
        print("This means you're quite a bit above your healthy weight." \
        "It's important to start working on weight loss slowly and safely-maybe with the help of doctor or nutritionist." \
        "Even losing few kilos can boost your health")
calculate_bmi()
