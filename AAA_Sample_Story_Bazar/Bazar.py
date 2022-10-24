def main():
    elephant = 10
    sunflower = 10
    bicycle = 10
    initial_price = elephant + sunflower + bicycle

    elephant += 3
    sunflower -= 5
    bicycle = elephant + 2
    final_price = elephant + sunflower + bicycle

    gain_or_loss = final_price - initial_price
    
    if gain_or_loss > 0:
        result = "gained"
    else:
        result = "lost"
    
    print(f"In the end, the bazar seller has {result} ${gain_or_loss}.")

main()