def convert_currency():
    while True:
        amount = input("Enter the amount: ")
        try:
            amount = float(amount)
            if amount <= 0:
                print("invalid amount")
                continue
            break
        except ValueError:
            print("invalid amount")
            continue

    while True:
        source_currency = input("Source currency (USD/EUR/CAD): ").upper()
        if source_currency not in ["USD", "EUR", "CAD"]:
            print("invalid currency")
            continue
        break

    while True:
        target_currency = input("Target currency (USD/EUR/CAD): ").upper()
        if target_currency not in ["USD", "EUR", "CAD"]:
            print("invalid currency")
            continue
        break

    if source_currency == "USD" and target_currency == "CAD":
        exchange_rate = 1.25
    elif source_currency == "USD" and target_currency == "EUR":
        exchange_rate = 0.88  
    elif source_currency == "EUR" and target_currency == "USD":
        exchange_rate = 1.13  
    elif source_currency == "EUR" and target_currency == "CAD":
        exchange_rate = 1.42  
    elif source_currency == "CAD" and target_currency == "USD":
        exchange_rate = 0.80  
    elif source_currency == "CAD" and target_currency == "EUR":
        exchange_rate = 0.70  
        
    if source_currency == target_currency:
        converted_amount = amount
    else:
        converted_amount = amount * exchange_rate
    print(f"{amount:.2f} {source_currency} is equal to {converted_amount:.2f}")

convert_currency()