def calculate_bmi(weight, height):
    """Calculate BMI using the formula: BMI = weight (kg) / height (m)^2."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI into standard categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    try:
        # Get user inputs
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Display results
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {classify_bmi(bmi)}")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if _name_ == "_main_":
    main()
