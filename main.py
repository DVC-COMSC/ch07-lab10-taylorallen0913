# ******************************
# Make your Code
# ******************************

numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    # Find min index
    min_index = numbers.index(min(numbers[i:]))
    # Swap
    temp = numbers[i]
    numbers[i] = numbers[min_index]
    numbers[min_index] = temp

    print(numbers)
  