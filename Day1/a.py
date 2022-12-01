input = open("input.txt", "r").readlines()
  
def sum_caloreies():
    
    temp = []
    calories = []

    for line in input:
        if line != "\n":
            temp.append(int(line))
        else:
            sum_of_calories = sum(temp)
            calories.append(sum_of_calories)
            temp = []
            
    calories = sorted(calories)
    print(calories[-1])
    print(sum(calories[-3:]))

if __name__ == "__main__":
    sum_caloreies()

