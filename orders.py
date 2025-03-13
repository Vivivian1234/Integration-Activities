import payments  #Import the payments module

def place_order():
    order_id = 101
    amount = 50.00
    confirmation = payments.process_payment(order_id, amount)  #Integration happens here
    print(confirmation)

place_order() #Run the function to simulate order placement
