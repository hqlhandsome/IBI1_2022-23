def can_buy_house(value, salary):
  # check if the value is no more than five times the salary
    if value <= 5 * salary:
    # return yes if the condition is met
        return "Yes"
    else:
    # return no otherwise
        return "No"
  # example values
value = 180000
salary = 35000

  # call the function and print the result
result = can_buy_house(value, salary)
print(result)

value = int(input('value='))
salary = int(input('salary='))
result =can_buy_house(value, salary)
print(result)
