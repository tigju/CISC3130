import os
import pprint 
pp = pprint.PrettyPrinter(indent=4)


class CustomerInvoice:
  def __init__(self, master_file, trans_file):
    self.master_file = master_file
    self.trans_file = trans_file
    self.data = {}

  def open_and_read(self):
    with open(f'{os.getcwd()}/{self.master_file}','r') as customers, open(f'{os.getcwd()}/{self.trans_file}','r') as transactions:
      next(transactions)
      next(customers)

      # Read files into dictionary for convenience

      # read master file
      for customer in customers:
          customer = customer.rstrip()
          customer = customer.split(',') 
          if customer[0] in self.data:
              continue
          else:
              self.data[customer[0]] = {"Name": customer[1], "CurrBal": customer[-1]}  

      # read transactions
      for trans in transactions:
          trans = trans.rstrip()
          trans = trans.split(',')
          if trans[0] in self.data:
              if trans[2] in self.data[trans[0]]:
                  self.data[trans[0]][trans[2]].append(trans[1:])
              else:
                  self.data[trans[0]].update({trans[2]: [trans[1:]]})
          else:
            # if customer doesn't exist in master file, don't throw an error, 
            # print to terminal and still make a record for unknown customer to see what orders/payments associated 
            print(f"customer {trans[0]} doesn't exist" )
            self.data[trans[0]] = {"Name": "Unknown Customer    ", "CurrBal": 0}
            self.data[trans[0]].update({trans[2]: [trans[1:]]})
            
      
      # calculate balance
      for k in self.data.keys():
        # get the current balance
        total = float(self.data[k]['CurrBal'])
        # check if orders exist for current customer
        if 'O' in self.data[k].keys():
          # loop through Orders
          for i in self.data[k]['O']:
            # orders with no discount
            if len(i) <= 5:
              # add to total
              total = total + float(i[-1]) * int(i[-2])
            else:
              # add to total with discount
              cost_discounted = float(i[-2]) - (float(i[-2]) * float(i[-1])/100)
              total = total + cost_discounted * int(i[3])
        # check if payments exist for current customer
        if 'P' in self.data[k].keys():
          # loop though payments
          for j in self.data[k]['P']:
            # payments with no early pmt discount
            if len(j) <= 3:
              total = total - float(j[-1])
            # payments with early pmt discount
            else:
              # calculate discount amount out of discounted balance
              credit = float(j[-2]) * float(j[-1])/100
              # add to total
              total = total - float(j[-2]) - credit
              
        # update dictionary
        self.data[k].update({'NewBal': str(total)})     
      # return in case of re-using data 
      return self.data

  def get_invoices(self, location_folder):
    # create a folder in current location if doesn't exist
    if not os.path.exists(location_folder):
      os.makedirs(location_folder)

    # loop through customers
    for k in self.data.keys():

      # create a new file for each invoice
      with open(f'{location_folder}/{k}.txt', 'w') as invoice:
        # write first 2 lines in invoice (name and previous balance)
        invoice.write(f'{self.data[k]["Name"]}{k}\n\n\t\tPrevious Balance{" "*14}${self.data[k]["CurrBal"]}\n\n')
        # check if orders exist for current customer
        if 'O' in self.data[k].keys():
          # loop through Orders
          for i in self.data[k]['O']:
            # orders with no discount
            if len(i) <= 5:    
              # create formatted string
              string = f'{i[0]}\t\t{i[2]}(qty {int(i[-2])})\t\t  ${float(i[-1])*int(i[-2])}\n'
            # orders with discount
            else:
              # add to total with discount
              cost_discounted = float(i[-2]) - (float(i[-2]) * float(i[-1])/100)
              # create formatted string 
              string = f'{i[0]}\t\t{i[2]}(qty {i[3]}) -{i[-1]}%\t  ${cost_discounted*int(i[3])}\n'
            # write order string to invoice file
            invoice.write(string)
          # check if payments exists for current customer
        if 'P' in self.data[k].keys():
          # loop though payments
          for j in self.data[k]['P']:
            # payments with no early pmt discount
            if len(j) <= 3:
              string = f'{j[0]}\t\tpayment{" "*19}${j[-1]}\n'
            # payments with early pmt discount
            else:
              # calculate discount amount out of discounted balance
              credit = float(j[-2]) * float(j[-1])/100
              # create formatted string 
              string = f'{j[0]}\t\tpayment  +{j[-1]}% (${credit})\t  ${j[-2]}\n'
            # write payment string to invoice file
            invoice.write(string)
        # write the last string to invoice file with total balance
        invoice.write(f'\n\t\tBalance Due{" "*19}${self.data[k]["NewBal"]}')
    
  # update balances in master file
  def update_master_file(self):
    with open(f'{os.getcwd()}/{self.master_file}', 'r') as master:
      first_line = next(master)
      records = master.readlines()

    for i in range(len(records)):
      records[i] = records[i].rstrip()
      records[i] = records[i].split(',')
      if records[i][0] in self.data.keys():
        records[i][-1] = f"{self.data[records[i][0]]['NewBal']}\n"
      records[i] = ", ".join(records[i])

    with open(f'{os.getcwd()}/{self.master_file}', 'w') as master:
      master.write(first_line)
      master.writelines(records)


  # print all balances in terminal
  def print_balances(self):

    for k in self.data.keys():
      # print Customer name and balance to terminal
      pp.pprint(self.data[k]['Name'])
      pp.pprint(f"Total: {self.data[k]['NewBal']}")
      pp.pprint('---------------')

    