import matplotlib.pyplot as plt

# Given probabilities
P_A = 0.75  # Probability of solving the first problem
P_B_given_A = 0.80  # Probability of solving the second problem given the first problem is solved
P_B_given_not_A = 2/3  # Probability of solving the second problem given the first problem is not solved

# Calculate P(B), the probability of solving the second problem
P_not_A = 1 - P_A  # Probability of not solving the first problem
P_B = (P_B_given_A * P_A) + (P_B_given_not_A * P_not_A)

# Calculate conditional probabilities
P_A_given_B = (P_B_given_A * P_A) / P_B
P_B_given_not_A
P_not_B_given_not_A = 1 - P_B_given_not_A

# Labels for the chart
labels = ['P(FirstProblem | SecondProblem)', 'P(SecondProblem | ¬FirstProblem)', 'P(¬SecondProblem | ¬FirstProblem)']

# Corresponding probabilities
probabilities = [P_A_given_B, P_B_given_not_A, P_not_B_given_not_A]

# Create a bar chart
plt.bar(labels, probabilities)

# Add labels and title
plt.ylabel('Probability')
plt.title('Conditional Probabilities for AI Course Excercise Problems')

# Display the chart
plt.show()

