from datetime import datetime

def get_dates():
    from_date = input("Enter the 'from' date (mm/dd/yyyy): ")
    to_date = input("Enter the 'to' date (mm/dd/yyyy): ")
    return from_date, to_date
def calculate_income_tax(gross_pay, tax_rate):
    return gross_pay * tax_rate / 100
def display_totals(totals):
    print("\nTotal number of employees:", totals['total_employees'])
    print("Total hours worked:", totals['total_hours'])
    print("Total income tax:", totals['total_tax'])
    print("Total net pay:", totals['total_net_pay'])
def main():
    employees = [] 
    totals = {'total_employees': 0, 'total_hours':0,'total_tax': 0, 'total_net_pay': 0 }
   
    while True:
        from_date, to_date = get_dates()
        name= input("Enter employee name: ")
        hours_worked = float(input("enter total hours worked:"))
        hourly_rate = float(input("Enter hourly rate: " ))
        tax_rate = float(input("Enter income tax rate (in percentage): "))
        employees.append({
            'from_date' : from_date,
            'to_date': to_date,
            'name': name,
            'hours_worked': hours_worked,
            'hourly_rate': hourly_rate,
            'tax_rate': tax_rate
        })
        continue_input = input("Do you want to enter date for another employee?(yes/no):").strip().lower()
        if continue_input != 'yes':
            break
    for employee in employees:
        gross_pay = employee['hours_worked'] * employee['hourly_rate']
        income_tax = calculate_income_tax(gross_pay, employee['tax_rate'])
        net_pay = gross_pay - income_tax
        print("\nEmployee:", employee['name'])
        print(f"From Date: {employee['from_date']}, To date: {employee['to_date']}")
        print(f"Hours worked: {employee['hours_worked']},hourly Rate: {employee['hourly_rate']}")
        print(f"Gross Pay:{gross_pay}, Income Tax Rate: {employee['tax_rate']}")
        print(f"Income Tax: {income_tax}, Net Pay:{net_pay}")
        totals['total_employees'] += 1
        totals['total_hours'] += employee['hours_worked']
        totals['total_tax'] += income_tax
        totals['total_net_pay'] += net_pay
    display_totals(totals)
if __name__ =="__main__":   
    main()

    import re
def is_valid_date(date):
    return bool(re.match(r'^\d{2}/\d{2}/\d{4}$',date))
def write_employee_data(file_name,from_date, to_date,name,hours_worked,pay_rate,income_tax_rate):
     with open(file_name,'a') as file:
         file.write(f"{from_date}|{to_date}|{name}|{hours_worked}|{pay_rate}|{income_tax_rate}\n")
def process_employee_data(file_name,from_date_input):
    total_employee = 0
    total_hours = 0
    total_taxes = 0
    total_net_pay = 0
    report_data = []
    with open(file_name, 'r') as file:
         for line in file:
             from_date, to_date,name,hours_worked, pay_rate, income_tax_rate =  line.strip().split('l')
             if from_date_input == "All" or from_date_input == from_date:
                 hours_worked = float(hours_worked)
                 pay_rate = float(pay_rate)
                 income_tax_rate = float(income_tax_rate)
                 gross_pay = hours_worked * pay_rate
                 income_tax = gross_pay * (income_tax_rate / 100)
                 net_pay = gross_pay - income_tax
                 total_employees += 1
                 total_hours += hours_worked
                 total_tax += income_tax
                 total_net_pay += net_pay
                 report_data.append({
                     'from_date': from_date,
                     'to_date': to_date,
                     'name':name,
                     'hours_worked': hours_worked,
                     'pay_rate': pay_rate,
                     'gross_pay': gross_pay,
                     'income_tax_rate': income_tax_rate,
                     'income_tax': income_tax,
                     'net_pay': net_pay
                 })    
                 print(f"From Date: {from_date}, To Date:{to_date}, Employee:{name}, Hours Worked:{hours_worked},"
                       f"Hourly Rate: {pay_rate}, Gross Pay:{gross_pay}, Income Tax Rate: {income_tax_rate},"
                       f"Income Taxes: {income_tax}, Net Pay:{net_pay}")
                 print("\Totals:")
                 print(f"Total Employees:{total_employees}")
                 print(f"Total Hours:{total_hours}")
                 print(f"Total Tax : {total_tax}")
                 print(f"Total Net Pay: {total_net_pay}")
def main():
    file_name = "employee_data.txt"
    while True:
        print("\Enter Emploree Data(or type 'done' to finish):")
        from_date = input("From Date (mm/dd/yyyy):")
        if from_date.lower()=='done':
            break
        if not is_valid_date(from_date):
            print("Invalid date format. Please enter in mm/dd/yyyy format.")
            continue
        to_date = input("To Date (mm/dd/yyyy):")
        if not is_valid_date(to_date):
            print("Invalid date format. Please enter in mm/dd/yyyy format.")
            continue
        name = input("Employee Name:")
        hours_worked = input("Hours Worked:")
        try:
            hours_worked = float(hours_worked)
        except ValueError:
            print("Invalid input for hours worked.")
            continue
        pay_rate = input("Hourly Pay Rate:")
        try:
           pay_rate = float(pay_rate)
        except ValueError:
            print("Invalid input for pay rate.")
            continue
        income_tax_rate = input("Income Tax Rate(as a percentage):")
        try:
            income_tax_rate = float(income_tax_rate)
        except ValueError:
            print("Invalid input for tax rate.")
            continue
        write_employee_data(file_name,from_date, to_date, name, hours_worked, pay_rate, income_tax_rate)
    while True:
            from_date_input = input("\nEnter From Date for report (mm/dd/yyyy) or 'All' for records:")
            if from_date_input.lower() == "all" or is_valid_date(from_date_input):
                break
            else:
                print("Invalid date format. Please enter in mm/dd/yyyy format or 'All'.")
    process_employee_data(file_name, from_date_input)
    if __name__ == "__main__":
       main()
                        
    
                       
                       
                       
                       
                       
               
