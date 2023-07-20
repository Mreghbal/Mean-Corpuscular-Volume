def calculate_mcv(red_blood_cells, hematocrit):
    mcv = (hematocrit / red_blood_cells) * 10
    return mcv

# Get user input for red blood cell count and hematocrit
red_blood_cells = float(input("Enter the number of red blood cells: "))
hematocrit = float(input("Enter the hematocrit value: "))

# Calculate MCV
mcv = calculate_mcv(red_blood_cells, hematocrit)

# Print the result
print(f"The Mean Corpuscular Volume (MCV) is {mcv:.2f} femtoliters.")
