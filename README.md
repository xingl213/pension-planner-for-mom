# Pension planner for mom

This is a direct translation of `user_manual.txt` which was originally written in Chinese.

# General
Run `mom_pension_planning.py` and input your answer according to the prompt

# Calculator
After you tell the program the key parameters **x** and **n**, it will present a table listing these information:
- Number of years of pension you need to receive to cover the cost
- Net profit of after receiving pension for 5, 10, 20, 30, 40, and 50 years

# Planner
Depending on your financial plans, this program will tell you the best payment strategy.

If you want to maximize profit after **k** years, the program will present a table listing these information:
- Optimized parameter **n**
- Optimized parameter **x**
- Monthly payment amount
- Monthly receiving amount
- Net profit after **k** years

If you want to cover the cost as soon as possbily, the program will present a table listing these information:
- Parameter **x** that corresponds to each parameter **n**
- Monthly payment amount
- Monthly receiving amount
- Number of years you need to receive pension to cover the cost
