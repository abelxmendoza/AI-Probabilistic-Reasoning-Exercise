# Given probabilities
P_positive_given_disease = 0.97  # Probability of a positive result given the patient has the disease
P_positive_given_no_disease = 0.02  # Probability of a positive result given the patient does not have the disease
P_disease = 1 / 400  # Base rate of the disease in the population

# Calculate P(PositiveResult)
P_positive = (P_positive_given_disease * P_disease) + (P_positive_given_no_disease * (1 - P_disease))

# Calculate P(HasDisease | PositiveResult) using Bayes' theorem
P_disease_given_positive = (P_positive_given_disease * P_disease) / P_positive

# Convert probabilities to percentages rounded to 2 decimal places
P_positive_percentage = round(P_positive * 100, 2)
P_disease_given_positive_percentage = round(P_disease_given_positive * 100, 2)

# Print the results as both decimals and rounded percentages
print("P(PositiveResult) as a decimal:", P_positive)
print("P(PositiveResult) as a percentage:", P_positive_percentage, "%")
print("P(HasDisease | PositiveResult) as a decimal:", P_disease_given_positive)
print("P(HasDisease | PositiveResult) as a percentage:", P_disease_given_positive_percentage, "%")
