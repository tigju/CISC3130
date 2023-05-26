from linked_list import *

input_data = 'data input.txt'

# create 2 linked lists for each type of wood
oak = FIFO()
cherry = FIFO()

# read file 
with open(input_data,'r') as data:
    # skip the column names 
    next(data)
    # keep track of discount card 
    next_cust_disc = 0
    # loop through file line by line
    for line in data:
        line = line.rstrip()
        line = line.split(',') 


        # if receipt from manufacturer add wood to linked list
        if line[0] == "R":
            # if oak wood, add to oak linked list
            if line[1] == "O":
                oak.add_to_rear(line[2:])
                print("Receipt from Manufacturer:\n--------------------------")
                print(f'Received Oak, quantity: {line[-2]}, price: {line[-1]}')
                print("======================================================\n")
            # if cherry wood add to cherry linked list
            if line[1] == "C":
                cherry.add_to_rear(line[2:])
                print("Receipt from Manufacturer:\n--------------------------")
                print(f'Received Cherry, quantity: {line[-2]}, price: {line[-1]}')
                print("======================================================\n")
        # if promo card, print promo for next customer
        if line[0] == "P":
            print(f"PROMO: Next customer gets {line[-1]} discount")
            print("========================")
            next_cust_disc = int(line[-1].rstrip("%"))
        
        # if order from customer 
        if line[0] == "S":
            # if it's oak assign first oak node pointer to current
            if line[1] == 'O':
                current = oak.head
                wood_name = "Oak"
            # if it's cherry assign first cherry node pointer to current
            elif line[1] == 'C':
                current = cherry.head
                wood_name = "Cherry"

            # keep track of quantity, message and total 
            quant = int(line[-1])
            message = ''
            total = 0

            # go over linked list (either oak list or cherry list)
            while current != None:
                # check order quantity for zero, if it is, end the loop
                if quant == 0:
                    break
                
                # get inventory and price from the oldest node (which is assigned to current)
                inv = int(current.info[0])
                price = float(current.info[1].lstrip("$"))

                # if order quantity less then inventory
                if quant < inv:
                    # update message and total 
                    message = message + f'{quant} at ${price} each    Sales: ${quant*price}\n'
                    total = total + quant*price

                    # update node's inventory after the order qty
                    quant = inv - quant
                    current.info[0] = quant

                    # reset quantity
                    quant = 0
                # if order quantity greater or equal to inventory
                else:
                    # update message and total 
                    message = message + f'{inv} at ${price} each    Sales: ${inv*price}\n'
                    total = total + inv*price

                    # update quantity
                    quant = quant - inv
                    
                    # remove node since it's inventory exhausted 
                    # either from oak linked list 
                    if line[1] == 'O':
                        oak.remove_from_head()
                    # or from cherry linked list
                    elif line[1] == 'C':
                        cherry.remove_from_head()
                # set current to next node in the linked list
                current = current.next_node

            # prepare message to print:
            # get widgets sold
            widgets_sold = int(line[-1]) - quant
            # add to message
            message = f'{widgets_sold} Widgets of {wood_name} wood Sold\n' + message
            
            # if there was a discount 
            if next_cust_disc > 0:
                # update total
                total_disc = total - total * next_cust_disc/100
                # update message
                message = message + f'Discount: -{next_cust_disc}% Total: ${total_disc}\n'
                # reset discount
                next_cust_disc = 0
            # otherwise 
            else:
                # update message with original total (no discount)
                message = message + f'Total: ${total}\n'

            # update message if some of the wood was not available 
            if quant > 0 :
                message = message + f'Remainder of {quant} pieces of {wood_name} wood not available\n'

            # add dividers to the order to look clear when printed
            message =  "Order from customer:\n--------------------\n" + message + "======================================================\n"
            print(message)

# Remaining inventory
print("Remaining inventory:\n--------------------\n")
print("Inventory of Oak wood:")
current = oak.head
while current:
    print("Quantity: ", current.info[0], "Price: ", current.info[1])
    current = current.next_node
print("\nInventory of Cherry wood:")
current = cherry.head
while current:
    print("Quantity: ", current.info[0], "Price: ", current.info[1])
    current = current.next_node

