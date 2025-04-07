# Program to determine what clothes Rohan should wear based on temperature

# Input: Get the current temperature from the user
temperature = float(input("Enter the current temperature in Celsius: "))

# Condition to check the temperature and suggest clothes
if temperature >= 25:
    print("The weather is warm. You can wear light and soft clothes.")
elif 15 <= temperature < 25:
    print("The weather is mild. A light jacket or sweater should be fine.")
else:
    print("The weather is cold. It's best to wear a warm jacket or coat.")



