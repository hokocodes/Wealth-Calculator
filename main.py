div = 0.01 #dividend interest rate
c = int(input('Enter in your monthly contribution: ')) #monthly contribution
i = int(input('Enter in your starting investments balance: ')) #starting balance
interest = 0 #starting interest gained balance
months = input('Enter in how many months you want to calculate for: ')
count = 1
while count <= int(months):
  print("month " + str(count))
  print("invested " + str(i) )
  print("interest in total gained " + str(interest))
  print("interest gained this month " + str(i * div))
  print(" ")
  i = i + c + (i * div)
  interest = interest + (i * div)
  count += 1
  c += 200
