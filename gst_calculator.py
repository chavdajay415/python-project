def calculate_gst(amount, gst_rate):
    """
    Calculate GST amount and total price including GST.
    
    :param amount: The original amount before GST
    :param gst_rate: GST rate as a percentage (e.g., 18 for 18%)
    :return: Tuple containing GST amount and total price including GST
    """
    gst_amount = (amount * gst_rate) / 100
    total_price = amount + gst_amount
    return gst_amount, total_price

def main():
    print("GST Calculator")
    
    # Input original amount and GST rate
    try:
        amount = float(input("Enter the original amount: ₹"))
        gst_rate = float(input("Enter the GST rate (as a percentage): "))
        
        if amount < 0 or gst_rate < 0:
            print("Amount and GST rate should be non-negative values.")
            return
        
        gst_amount, total_price = calculate_gst(amount, gst_rate)
        
        # Display results
        print(f"Original Amount: ₹{amount:.2f}")
        print(f"GST Amount: ₹{gst_amount:.2f}")
        print(f"Total Price (including GST): ₹{total_price:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
