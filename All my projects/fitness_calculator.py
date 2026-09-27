"""

This program represents a health calculator that allows users to enter personal information and receive health recommendations based on their data. The calculator can include functions to calculate Body Mass Index (BMI), Basal Metabolic Rate (BMR), and other relevant health indicators. It can also provide advice on nutrition, exercise, and healthy habits based on the results obtained.

"""

#======================================================================================================================================
# PERSONAL FITNESS AND HEALTH CALCULATOR
#======================================================================================================================================

def calculate_bmi(weight_kg, height_m):
    """
    Calculates the Body Mass Index (BMI).

    Formula: BMI = weight / (height^2)

    Parameters:
    weight_kg (float): Weight in kilograms
    height_m (float): Height in meters

    Returns:
    float: The calculated BMI
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

def is_healthy_weight(bmi):
    """
    Determines whether the BMI is within the healthy range (18.5 - 24.9).

    Parameter:
    bmi (float): Body Mass Index

    Returns:
    bool: True if within the healthy range, False if not
    """
    # Comparison and logical operators
    return bmi >= 18.5 and bmi <= 24.9

def is_overweight(bmi):
    """Description: Determines whether a person is overweight based on their BMI.

Medical criterion: A person is considered overweight when BMI is greater than or equal to 25.

Parameter:

bmi (float): The calculated Body Mass Index

Must return:

True if overweight (BMI >= 25)

False if not overweight (BMI < 25)"""

    return bmi >= 25

def is_underweight(bmi):

    """Description: Determines whether a person is underweight based on their BMI.

Medical criterion: A person is considered underweight when BMI is less than 18.5.

Parameter:

bmi (float): The calculated Body Mass Index

Must return:

True if underweight (BMI < 18.5)

False if not underweight (BMI >= 18.5)"""

    return bmi < 18.5

def calculate_daily_calories(weight_kg, height_cm, age, is_male):

    """Calculates the recommended daily calories using the Harris-Benedict formula.

Medical formulas:

For men: 88.362 + (13.397 x weight) + (4.799 x height) - (5.677 x age)

For women: 447.593 + (9.247 x weight) + (3.098 x height) - (4.330 x age)

Parameters:

weight_kg (float): Weight in kilograms

height_cm (float): Height in centimeters

age (int): Age in years

is_male (bool): True if male, False if female

Must return:

(float): The daily calories calculated based on sex"""

    # Arithmetic and boolean operators

    calories_male = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)

    calories_female = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)

    return is_male * calories_male + (1 - is_male) * calories_female

def calculate_daily_water(weight_kg):
    """Must return:

(float): Recommended liters of water

Steps to follow:

Calculate how many milliliters of water are needed: weight_kg * 35

Convert the milliliters to liters by dividing by 1000

Return the result"""

    ml_water = weight_kg * 35
    liters_water = ml_water / 1000

    return liters_water



def calculate_max_heart_rate(age):
    """Description: Calculates the recommended maximum heart rate during exercise.

Medical formula: 220 - age

Parameter:

age (int): Age in years

Must return:

(int): Maximum recommended beats per minute"""

    return 220 - age

def generate_full_report(name, weight, height, age, is_male):
    """"
    Generates a complete health and fitness report

    """

    print("="*60)
    print(f"📊 FITNESS AND HEALTH REPORT - {name}")
    print("="*60)

    # Calculations
    bmi = calculate_bmi(weight, height)
    calories = calculate_daily_calories(weight, height, age, is_male)
    water = calculate_daily_water(weight)
    max_hr = calculate_max_heart_rate(age)

    # Basic Information
    print("\n👤 Personal Data:")
    print(f"   Weight: {weight} kg")
    print(f"   Height: {height} m")
    print(f"   Age: {age}")
    print(f"   Male?: {is_male}")

    # BMI and evaluation
    print(f"\n💪 Body Mass Index (BMI):")
    print(f"     Your BMI: {round(bmi, 2)}")
    print(f"     Is it a healthy weight? {is_healthy_weight(bmi)}")
    print(f"     Is it underweight? {is_underweight(bmi)}")
    print(f"     Overweight? {is_overweight(bmi)}")

    # Calories
    print(f"\n🍽️  Nutrition:")
    print(f"    Recommended daily calories: {round(calories, 0)} kcal")
    print(f"    Recommended daily water: {round(water, 2)} liters")

    # Cardio
    print(f"\n❤️  Heart Rate Zone:")
    print(f"    Maximum heart rate: {max_hr} bpm")
    print(f"    Optimal cardio zone: {round(max_hr*0.6, 0)} - {round(max_hr*0.8, 0)} bpm")

    print("\n" + "="*60)

# ============================================
# MAIN PROGRAM
# ============================================

header = """
╔════════════════════════════════════════════════════════════╗
║        💪 PERSONAL FITNESS AND HEALTH CALCULATOR 💪         ║
║                                                            ║
║          Discover your optimal health metrics!              ║
╚════════════════════════════════════════════════════════════╝
"""
print(header)

# Request data from the user
name = input("\n👤 What is your name? ")
weight = float(input("⚖️  How much do you weigh? (kg): "))
height = float(input("📏 How tall are you? (meters, e.g.: 1.75): "))
age = int(input("🎂 How old are you? "))
sex = input("⚤  Are you male or female? (M/F): ")

# Convert sex to boolean
is_male = sex == "M" or sex == "m" or sex == "male"

# Generate report
generate_full_report(name, weight, height, age, is_male)

print("\n✨ Take care of your health! ✨\n")
