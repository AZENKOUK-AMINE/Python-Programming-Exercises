

year = int(input('Enter a year :'))
month = input('Enter a month :').upper()


def leap_year(year):
    if year%4 == 0 and year %100!=0 or year %400==0:
        return True
    

def month_of_the_year(month , year):
    months_31=['JANUARY','MARCH','MAY','JULY','AUGUST','OCTOBER','DECEMBER']
    months_30=['APRIL','JUNE','SEPTEMBER','NOVEMBER']
    if month in months_30:
        print(f'{month} has 30 days')
    elif month in months_31:
        print(f'{month} has 31 days')
    elif month=='FEBRUARY':
        if leap_year(year):
            print(f'{month} has 29 days')
        else:
            print(f'{month} has 28 days')
        
        
month_of_the_year(month,year)