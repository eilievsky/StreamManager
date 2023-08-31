import random

sequence = []
max_repetitions = 5

# Generate a random starting number
start_number = random.randint(1, 10)
sequence.append(start_number)

# Generate the remaining numbers
for _ in range(100):
    previous_number = sequence[-1]
    repetitions = random.randint(1, max_repetitions)
    
    # Generate the next number with a limit of 1000
    next_number = min(previous_number + random.randint(1, 10), 1000)
    
    # Append the next number to the sequence with repetitions
    sequence.extend([next_number] * repetitions)

# Print the sequence with each number on a separate line
for number in sequence:
    print(number)