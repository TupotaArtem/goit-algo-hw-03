import random

def get_numbers_ticket(min_value, max_value, quantity):
  
    if not (1 <= min_value <= max_value <= 1000) or not (min_value <= quantity <= max_value):
        return []
    
    numbers = random.sample(range(min_value, max_value + 1), quantity)    
   
    return sorted(numbers)

def main():
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)


if __name__=="__main__":
    main()
