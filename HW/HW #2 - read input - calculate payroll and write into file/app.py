import datetime as dt
import pprint 
pp = pprint.PrettyPrinter(indent=4)


class PersonnelPay:
    ''' 
        Class used to calculate total pay for each babysitter
        Attributes:
        -----------
        personnel_file: str
            text file that stores personnel info
        payroll_file: str
            text file that stores payroll for each person
        data: dict
            storage for file data (dictionary)
        
        Methods:
        --------
        read_files_into_dict:
            reads personnel_file and payroll_file and stores info into data
            returns dictionary with personnel data
        calculate_pay:
            calculates working hours of personnel for each rate
            stores calculated pay into data
        get_sorted_names:
            helper method
            takes personnel names and sorts in alphabetical order
            returns list (array) of names in alphabetical order
        pay_list_file:
            writes personnel name and total pay into file
        print_data:
            prints all personnel info into terminal
        '''
    def __init__(self, personel_file, payroll_file):
        self.personnel_file = personel_file
        self.payroll_file = payroll_file
        self.data = {}


    def read_files_into_dict(self):
        '''method reads passed files to the object,
           reads data into dictionary
           returns dictionary
        '''
        personnel_info = []
        payroll_info = []

        with open(f'{self.personnel_file}','r') as personnel, open(f'{self.payroll_file}','r') as payroll:

            # retrieve personnel info into list first
            # skip first two lines (file name, and empty string)
            next(personnel)
            next(personnel)

            counter = 0
            address_str = ''
            for empl in personnel:
                empl = empl.rstrip()
                if len(empl) == 0:
                    counter = 0
                    address_str = ''
                else:
                    counter = counter+1
                    if counter == 1:
                        person_id = empl
                    elif counter == 2:
                        person_name = empl
                    elif counter == 3 or counter == 4:
                        address_str = address_str + empl
                    else:
                        h = empl.split(' ')
                        hours = h
                        personnel_info.append([person_id, person_name, address_str, hours])

            # retrieve payroll info into list first
            # skip first two lines (file name, and empty string)
            next(payroll)
            next(payroll)

            counter = 0
            times = []
            for empl in payroll:

                empl = empl.rstrip()
                if len(empl) == 0:     
                    payroll_info.append(times)
                    counter = 0  
                    times =[] 
                else:
                    counter = counter+1
                    times.append(empl)
            payroll_info.append(times)  

        # organize personnel data into dictionary (hashmap)
        for p in personnel_info:
            if p[0] in self.data:
                    continue
            else:
                self.data[p[0]] = {"Name": p[1], "Address": p[2], "Rate": {"before 9pm": p[3][0], "9pm - midnight": p[3][1], "past midnight": p[3][2]}}
        
        # organize payroll data into dictionary (hashmap)
        for r in payroll_info:
            hours = {}
            for t in range(len(r[2:])):
                hours.update({t+1 : r[2:][t]})
            self.data[r[0]].update({ "Days" : hours})
        
        return self.data


    def calculate_pay(self):
        ''' method calculates hours according hour rate for each person
            stores data into object's data
            returns None
        '''
        for p in self.data.keys():
            total_pay = 0
            # go through dictionary and calculate pay
            print(self.data[p]["Name"])
            for d in self.data[p]['Days'].values():
                tt = d.split(" ")
                start_dt = dt.datetime.strptime(tt[0], '%H:%M')
                end_dt = dt.datetime.strptime(tt[1], '%H:%M')

                # if start time > end time, then end_time past midnight
                if start_dt > end_dt:
                    # check if start date before 9pm
                    if start_dt.hour < 9:
                        # count hours before 9
                        end = dt.datetime.strptime("9:00", '%H:%M')
                        hr1 = end - start_dt
                        # count hours between 9 and midnight
                        midnight = dt.datetime.strptime("12:00", '%H:%M')
                        hr2 = midnight - end
                        # add to total pay 
                        total_pay = total_pay + (hr1.seconds/3600)*float(self.data[p]['Rate']['before 9pm']) + (hr2.seconds/3600)*float(self.data[p]['Rate']['9pm - midnight'])
                    
                    # check if start time between 9 and midnight only    
                    if start_dt.hour >= 9 and start_dt.hour < 12:
                        # count hours
                        end = dt.datetime.strptime("12:00", '%H:%M')
                        hr3 = end - start_dt

                        # add calculated 9-12 hours pay to total 
                        total_pay = total_pay + (hr3.seconds/3600)*float(self.data[p]['Rate']['9pm - midnight'])

                    # calculate hours past midnight
                    end = dt.datetime.strptime("0:00", '%H:%M')
                    hr4 = end_dt - end

                    # add past midnight hours pay to total
                    total_pay = total_pay + (hr4.seconds/3600)*float(self.data[p]['Rate']['past midnight'])

                # start_time less than end_time
                else:
                    # check if morning hours
                    if start_dt.hour < 6:
                        # calculate hours
                        hr9 = end_dt - start_dt
                        # add to total
                        total_pay = total_pay + (hr9.seconds/3600)*float(self.data[p]['Rate']['past midnight'])
                    # check if start hours less than 9pm and more than 6 (avoid morning hours)
                    if start_dt.hour >= 6 and start_dt.hour < 9:
                        # in case if end_time before 9pm
                        if end_dt.hour < 9:
                            # calculate pay
                            hr5 = end_dt - start_dt
                            # add to total pay
                            total_pay = total_pay + (hr5.seconds/3600)*float(self.data[p]['Rate']['before 9pm'])
                        # in case if end_time between 9 and midnigt
                        elif end_dt.hour >= 9 and end_dt.hour <= 12:
                            # calculate hours from start_time to 9 and from 9 to end_time
                            end = dt.datetime.strptime("9:00", '%H:%M')
                            hr6 = end - start_dt
                            hr7 = end_dt - end
                            # add calculated pay to total
                            total_pay = total_pay + (hr6.seconds/3600)*float(self.data[p]['Rate']['before 9pm'])
                            total_pay = total_pay + (hr7.seconds/3600)*float(self.data[p]['Rate']['9pm - midnight'])

                    # check if start time between 9 and midnight
                    elif start_dt.hour >= 9 and start_dt.hour <= 12:
                        # in case if end time between 9 and 12 as well, then
                        if end_dt.hour >= 9 and end_dt.hour <= 12:
                            # calculate pay
                            hr8 = end_dt - start_dt
                            # add to total
                            total_pay = total_pay + (hr8.seconds/3600)*float(self.data[p]['Rate']['9pm - midnight'])
                # add pay total to dictionary
                self.data[p].update({"TotalPay": total_pay})
                

    def print_data(self):
        '''method prints data dictionary
           to terminal
        '''
        pp.pprint(self.data)


    def get_sorted_names(self):
        ''' helper method sorts personnel names 
            into separate list in alphabetical order
            returns list of names 
        '''
        names =[]
        for value in self.data.values():
            names.append(value["Name"])
    
        sorted_names = sorted(names)
        return sorted_names
    

    def pay_list_file(self):
        ''' method retrieves infor from object's data
            and writes it into file
        '''
        sorted_names = self.get_sorted_names()
        for n in sorted_names:
            with open('list.txt', 'a') as personnel_list:
                for v in self.data.values():
                    if n in v["Name"]:
                        personnel_list.write(f'{v["Name"]}, Total Pay: ${v["TotalPay"]:.2f}\n\n')

                