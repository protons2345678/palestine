def calculate_bread_prices():
    regular_price = 3.49
    discount_rate = 0.06

    try:
        num_loaves = int(input("Enter the number of loaves of day-old bread being purchased: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    total_regular_price = num_loaves * regular_price
    discount_amount = total_regular_price * discount_rate
    total_price = total_regular_price - discount_amount


    print(f"Regular price for {num_loaves} loaves: ${total_regular_price:.2f}")
    print(f"Discount amount: ${discount_amount:.2f}")
    print(f"Total price after discount: ${total_price:.2f}")


calculate_bread_prices()