from app import PersonnelPay

# doc string (info about ParsonnelPay class)
print(PersonnelPay.__doc__)

personnel = "personnel.txt"
payroll = "payroll.txt"

obj1 = PersonnelPay(personnel, payroll)

obj1.read_files_into_dict()

# safe dictionary if needed 
my_dict = obj1.read_files_into_dict()

# calculate pay
obj1.calculate_pay()

# store names and total pay into file
obj1.pay_list_file()

# print data into terminal
obj1.print_data()
