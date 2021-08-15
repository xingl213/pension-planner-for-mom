def monthly_payment(x):
    """Return monthly payment depending on coefficient <x>.

    Precondition: 0.6 <= x <= 3
    """
    return 2400 * x


def monthly_return(x, n):
    """Return monthly (pension) return depending on coefficient <x>, and years
    of payment <n>.

    Precondition: 0.6 <= x <= 3 and 2 <= n <= 7
    """
    return 640 / 13 * n + 50 * (20 + n) * (1 + (52.8 + n * x) / (20 + n))


# Calculator
def cal(x, n):
    """Return relative information about pension given <x>, <n>."""
    print('profit_after_yrs    5yrs      10yrs      20yrs      30yrs      '
          '40yrs      50yrs')
    total_payment = monthly_payment(x) * n * 12
    return_per_yr = monthly_return(x, n) * 12
    profit_yr = round(total_payment / return_per_yr, 2)
    after5 = round(return_per_yr * 5 - total_payment, 2)
    after10 = round(return_per_yr * 10 - total_payment, 2)
    after20 = round(return_per_yr * 20 - total_payment, 2)
    after30 = round(return_per_yr * 30 - total_payment, 2)
    after40 = round(return_per_yr * 40 - total_payment, 2)
    after50 = round(return_per_yr * 50 - total_payment, 2)
    print(f'{profit_yr}               {after5}   {after10}   {after20}   '
          f'{after30}  {after40}  {after50}')


# Payment strategy 1
def most_profit(k):
    """A payment strategy to maximize profit after receiving pension for <k>
    years."""
    print('n    x   monthly_payment    monthly_return    total_profit')
    n = 2.0
    n_list = []
    x_list = []
    profit_list = []
    while n <= 7:
        n_list.append(n)
        x = 0.6
        local_x_list = []
        local_profit_list = []
        while x <= 3:
            local_x_list.append(x)
            total_profit = (monthly_return(x, n) * k * 12
                            - monthly_payment(x) * n * 12)
            local_profit_list.append(total_profit)
            x += 0.01
            assert len(local_x_list) == len(local_profit_list)
        i = local_profit_list.index(max(local_profit_list))
        x_list.append(local_x_list[i])
        profit_list.append(local_profit_list[i])
        n += 1 / 12
    assert len(n_list) == len(x_list) == len(profit_list)
    target_i = profit_list.index(max(profit_list))
    final_n = round(n_list[target_i], 2)
    final_x = round(x_list[target_i], 7)
    final_monthly_payment = round(monthly_payment(final_x), 2)
    final_monthly_return = round(monthly_return(final_x, final_n), 2)
    final_total_profit = round(monthly_return(final_x, final_n) * k * 12
                               - monthly_payment(final_x) * final_n * 12, 2)
    print(f'{final_n}  {final_x}    {final_monthly_payment}           '
          f'{final_monthly_return}            {final_total_profit}')


# Payment strategy 2
def least_yrs():
    """A payment strategy to minimize years to she has to wait to gain profit.
    Print a table."""
    print('n    x   monthly_payment    monthly_return    profit_after_yrs')
    n = 2.0
    while n <= 7:
        yrs = n * 12
        x_list = []
        yrs_list = []
        x = 0.6
        while x <= 3:
            x_list.append(x)
            monthly_pay = monthly_payment(x)
            total_pay = monthly_pay * yrs
            profit_yr = total_pay / monthly_return(x, n) / 12
            yrs_list.append(profit_yr)
            x += 0.1
        assert len(x_list) == len(yrs_list)
        target_i = yrs_list.index(min(yrs_list))
        best_x = x_list[target_i]
        print('{} {}   {}            {}             '
              '{}'.format(round(n, 2), best_x, monthly_payment(best_x),
                          round(monthly_return(best_x, n), 2),
                          round(min(yrs_list), 2)))
        n += 1 / 12


# Main program
def main():
    function = input('Do you want to use the calculator (enter 1)\nor the '
                     'planner (enter 2)? ')
    while function != '1' and function != '2':
        function = input('Please enter 1 or 2: ')
    if function == '1':
        x_input = input('Please enter x: ')
        try:
            float(x_input)
        except ValueError:
            x_input = input('Please enter a valid x: ')
        n_input = input('Please enter n: ')
        try:
            float(n_input)
        except ValueError:
            n_input = input('Please enter a valid n: ')
        print('Here is the calculation:')
        cal(float(x_input), float(n_input))
    else:
        prompt_question = 'Do you want to:\nmaximize profit ' \
                          '(enter 1), or\nstart to gain profit as soon as ' \
                          'possible (enter 2)? '
        strategy = input(prompt_question)
        while strategy != '1' and strategy != '2':
            strategy = input('Please enter 1 or 2: ')
        if strategy == '1':
            years = float(input('How many years do you expect to receive '
                                'pension? '
                                '(enter an integer or a float number): '))
            print('Here is your best strategy.')
            most_profit(years)
        else:
            print('Depending on the n you choose, here are your best '
                  'strategies.')
            least_yrs()
    again = input('Run the program again? (enter y for yes and n for no): ')
    while again != 'y' and again != 'n':
        again = input('Please enter y or n: ')
    if again == 'y':
        main()
    else:
        print('Have a nice day!')


if __name__ == '__main__':
    main()
