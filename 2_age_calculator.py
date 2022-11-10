# this is my second project
# making an age calculator, ended up only being able to make it accurate to the year

# functions
def getBirth():
    date = input("What is the start date? (MM/DD/YY)\n")
    try:
        month = int(date[:2])
        day = int(date[3:5])
        year = int(date[6:])
        return month, day, year
    except:
        print("Please enter the date in the correct format.")
        getBirth()

def getCurrent():
    date = input("What is the end date? (MM/DD/YY)\n")
    try:
        month = int(date[:2])
        day = int(date[3:5])
        year = int(date[6:])
        return month, day, year
    except:
        print("Please enter the date in the correct format.")
        getCurrent()

def calcAge(bMonth, bDay, bYear, cMonth, cDay, cYear):
    years = cYear - bYear - 1 if (cMonth - bMonth < 0) or (cMonth - bMonth == 0 and cDay - bDay < 0) else cYear - bYear
    return f"Age is {years} years."

# main code
bMonth, bDay, bYear = getBirth()
cMonth, cDay, cYear = getCurrent()
print(calcAge(bMonth, bDay, bYear, cMonth,  cDay, cYear))