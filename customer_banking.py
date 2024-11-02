# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input('What is your savings account balance? '))
    savings_interest = float(input('What is your APR interest rate? '))
    savings_months = int(input('What is your loan maturity rate in months? '))

    # Call the create_savings_account function and pass the variables from the user
    """Source Code: Tutor Assistance from Luna on 11/2 for adding both values returned"""
    updated_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('Here are the details of the Savings account balance for the loan maturity.')
    print("The updated balance is: $", format(updated_balance, ',.2f'))
    print("The interest earned is:", format(interest_earned, ',.2f'),'%')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input('What is your initial CD account balance? '))
    cd_interest = float(input('What is the APR for the CD account? '))
    cd_maturity = int(input('What is the length of months for your CD? '))

    # Call the create_cd_account function and pass the variables from the user.
    """Source Code: Tutor Assistance from Luna on 11/2 for adding both values returned"""
    updated_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('Here are the details of the CD account balance for the loan maturity.')
    print("The updated balance is: $", format(updated_balance, ',.2f'))
    print("The interest earned is:", format(interest_earned, ',.2f'),'%')


if __name__ == "__main__":
    # Call the main function.
    main()