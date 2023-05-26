import pprint
pp = pprint.PrettyPrinter(indent=4)

from invoice_methods import CustomerInvoice

# initiate an object passing master file and transactions file
obj = CustomerInvoice('customers.txt', 'transactions.txt')

# read files
obj.open_and_read()

# print invoices into specified folder
obj.get_invoices('invoices')
# obj.get_invoices('INV')

# update master file with new balances
obj.update_master_file()

# print balances to terminal
# obj.print_balances()

