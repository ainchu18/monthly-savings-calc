import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('monthly_savings_calculator')

def get_monthly_salary_data():
    """
    Gets the monthly salary value of the user.
    """
    print("Please enter your salary this month.")
    print("This should be a whole number value with no decimal point")
    print("Example: 4000\n")

    monthly_salary = input("Enter your salary this month here:\n")
    
    salary_data = int(monthly_salary)


def get_monthly_expenses_data():
    """
    Gets the monthly salary value of the user.
    """
    print("Please enter your total expenses this month.")
    print("This should be a whole number value with no decimal point")
    print("Example: 900\n")

    monthly_expenses = input("Enter your total expenses this month here:\n")
    
    expenses_data = int(monthly_expenses)


get_monthly_salary_data()
get_monthly_expenses_data()