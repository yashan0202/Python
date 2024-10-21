def calculate_bmi(weight, height, system='metric'):
    """Function to calculate BMI based on system type: metric or imperial"""
    if system == 'metric':
        # BMI calculation for metric system (kg, meters)
        bmi = weight / (height ** 2)
    elif system == 'imperial':
        # BMI calculation for imperial system (lbs, inches)
        bmi = 703 * (weight / (height ** 2))
    else:
        raise ValueError("Invalid measurement system. Use 'metric' or 'imperial'.")
    
    return round(bmi, 2)


def bmi_category(bmi):
    """Function to return BMI category and health advice"""
    if bmi < 18.5:
        category = 'Underweight'
        advice = "It's important to eat a balanced diet and maintain a healthy weight."
    elif 18.5 <= bmi < 24.9:
        category = 'Normal weight'
        advice = "Great job! Continue maintaining a healthy lifestyle."
    elif 25 <= bmi < 29.9:
        category = 'Overweight'
        advice = "You might want to consider a balanced diet and regular exercise."
    elif 30 <= bmi < 34.9:
        category = 'Obesity Class I (Moderate)'
        advice = "You may need to consult a healthcare provider for a healthy weight management plan."
    elif 35 <= bmi < 39.9:
        category = 'Obesity Class II (Severe)'
        advice = "A more focused intervention is recommended. Consult a healthcare professional."
    else:
        category = 'Obesity Class III (Very Severe or Morbid)'
        advice = "It is critical to work closely with healthcare providers to reduce health risks."
    
    return category, advice


def get_input():
    """Function to get user input and return weight, height, and measurement system"""
    system = input("Choose measurement system (metric/imperial): ").lower()
    
    if system == 'metric':
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    elif system == 'imperial':
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in inches: "))
    else:
        raise ValueError("Invalid input. Please choose 'metric' or 'imperial'.")
    
    return weight, height, system


def main():
    print("Welcome to the Advanced BMI Calculator!")
    
    try:
        # Get user input
        weight, height, system = get_input()
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height, system)
        
        # Determine BMI category and health advice
        category, advice = bmi_category(bmi)
        
        # Print results
        print(f"\nYour BMI is: {bmi}")
        print(f"BMI Category: {category}")
        print(f"Health Advice: {advice}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()
