from mom_pension_planning import monthly_payment, monthly_return


file = open('data_small.csv', 'w')
file.write('n,x,monthly_payment,monthly_return,profit_after_yrs,5yrs,10yrs,'
           '20yrs,40yrs\n')
n = 2
while n <= 7.1:
    x = 0.6
    while x <= 3.05:
        mpay = monthly_payment(x)
        mreturn = round(monthly_return(x, n), 2)
        total_pay = mpay * n * 12
        yreturn = mreturn * 12
        pyrs = round(total_pay / yreturn, 2)
        p5 = round(5 * yreturn - total_pay, 2)
        p10 = round(10 * yreturn - total_pay, 2)
        p20 = round(20 * yreturn - total_pay, 2)
        p40 = round(40 * yreturn - total_pay, 2)
        file.write(f'{round(n,2)},{x},{mpay},{mreturn},{pyrs},{p5},{p10},{p20},'
                   f'{p40}\n')
        x += 0.1
    n += 1
