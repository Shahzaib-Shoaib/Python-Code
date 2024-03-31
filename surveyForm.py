original = 2.2

question = input("Would you like to have a more personalised experience? [y/n]: ")
if question.lower() == 'y':

    mode = input("Which applies to you: \n 1. You would like to drink more water \n 2. You have an illness that requires a larger intake of water \n 3. Other \n[1/2/3] ")

    if mode == '1':
        new_amount = int(input("How much would you like to drink? "))

    elif mode == '2':
        severity = int(input("What is the severity [1-5]: "))
        if severity == 1:
            new_amount = original + 0.5
        elif severity == 2:
            new_amount = original + 0.9
        elif severity == 3:
            new_amount = original + 1.1
        elif severity == 4:
            new_amount = original + 1.5
        elif severity == 5:
            new_amount = original + 1.9

    else:
        age = int(input("How old are you? "))
        gender = input("Are you male or female? [m/f]: ")
        if age >= 45 and age <= 70 and gender == 'f':
            new_amount = 2.5
        elif age >= 45 and age <= 70 and gender == 'm':
            new_amount = 3.5
        elif age >= 70 and gender == 'f':
            new_amount = 2.9
        elif age >= 70 and gender == 'm':
            new_amount = 3.9
        elif age >= 19 and age < 45 and gender == 'f':
            new_amount = 2.2
        elif age >= 19 and age < 45 and gender == 'm':
            new_amount = 3.3
        elif age >= 18 and age > 12 and gender == 'f':
            new_amount = 1.6
        elif age >= 18 and age > 12 and gender == 'm':
            new_amount = 1.9
        elif age <= 12:
            new_amount = 1.2

else:
    print("Thank you for your day. Enjoy your Hydration product.")
    
def calculate_water_intake(weight_kg, exercise_intensity, climate_factor):
    # Calculate baseline water intake based on weight
    baseline_intake_ml = weight_kg * 30  # Assuming 30ml per kg of body weight

# Adjust water intake based on exercise intensity
    if exercise_intensity == 'low':
        exercise_factor = 0.5
    elif exercise_intensity == 'moderate':
        exercise_factor = 0.7
    elif exercise_intensity == 'high':
        exercise_factor = 1.0
    else:
        print("Invalid exercise intensity provided.")
        return None

# Adjust water intake based on climate
    if climate_factor == 'hot':
        climate_adjustment = 0.2
    elif climate_factor == 'cold':
        climate_adjustment = -0.1
    else:
        print("Invalid climate factor provided.")
        return None

# Calculate total recommended water intake
    total_intake_ml = baseline_intake_ml * exercise_factor + baseline_intake_ml * climate_adjustment

    return total_intake_ml

def main():
    # Collect fitness inputs from the user
    weight_kg = float(input("Enter your weight in kilograms: "))
    exercise_intensity = input("Enter your exercise intensity (low/moderate/high): ").lower()
    climate_factor = input("Enter your climate factor (hot/cold): ").lower()

# Calculate personalized water intake
    water_intake_ml = calculate_water_intake(weight_kg, exercise_intensity, climate_factor)

# Display personalized recommendation
    if water_intake_ml:
        print("You should drink {:.2f} milliliters of water per day.".format(water_intake_ml))
        
        
main()