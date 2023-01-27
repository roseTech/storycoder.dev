""" Documentation:
At Empire State Building:

Contract One of Scratch Rapper:
- Up until today: Rapper Raw Scratch sells tapes for $5, 
- 10% of that goes to manager Mikey 
- Raw Sratch raps during Prime Time: 2pm to 6 pm: 12 sales tapes / hours (50% more sales than off prime hours) 
- Raw Scratch Raps during Off Prime hours: 10 am to 2 pm. And 6pm to 8pm: 8 sales tapes / hour
- Additionally: 3 sales tapes / hour on pedestrians, Raw Scratch keeps all profits from those 

- New competitor: Rapper Temple Thug sells tapes for $5, offers Mikey flat rate of $30
- Raps during Prime Time: 2pm to 6 pm:


New offer from manager Slug with new location Central Park:
- Rapper Raw Scratch: 20% of profit goes to manager 

- Scratch Raps during Prime Time: 2pm to 6 pm: 1.5x sales tapes / hours (50 % more sales than off prime hours) 
Raps during Off Prime hours: 10 am to 2 pm. And 6pm to 8pm: x sales tapes / hour 
- Additionally: 3 sales tapes / hour on pedestrians, Raw Scratch keeps all profits from those

Questions:

    1) How many tapes per hour during Prime Time and Off Time should Raw Scratch sell to make this the better proposition 
    compared to Raw Scratches old offer and Rapper Temple Thugs offer (assuming the same amount of non-tour affiliated sales 
    and the same ratio of prime time and off time sales)?

    2) How many tapes per hour during 4 hours of Prime Time should Raw Scratch sell in order to make 2x his own original deal? """

#
# Rapper Raw Scratch Contract 1

costRaw = 5 

# Prime Time: 4 hours, 12 (= a + a/2) tapes per hour 

costRawPrimeTime =  costRaw * 12 * 4 

# Off Time: 4 hours plus 2 hours, 8 (=a) tapes / hour

costRawOffTime= (costRaw) * (4+2) * 8

totalProfitScratchOne = (costRawPrimeTime + costRawOffTime) * 0.9 + (3* costRaw * 10) 


# Competitor Rapper Temple: Prime Time: 4 hours 


# Rapper Raw Scratch Contract 2

costRaw = 5 

# Prime Time: 4 hours, 12 tapes per hour 
tapesPerHourPrimeTime = 12
costRawPrimeTime =  tapesPerHourPrimeTime * 4 

tapesPerHourOffTime = 8


targetProfit = 0
while targetProfit < totalProfitScratchOne:
    tapesPerHourOffTime +=2

    tapesPerHourPrimeTime = tapesPerHourOffTime * 1.5
   

    # Off Time: 4 hours plus 2 hours, 8 tapes / hour

    costRawOffTime= (costRaw) * (4+2) * tapesPerHourOffTime

    targetProfit = (costRawPrimeTime + costRawOffTime) * 0.8 + (3* costRaw * 10) 

print(targetProfit)
print(tapesPerHourOffTime)
print(tapesPerHourPrimeTime)

    # Competitor Rapper Temple: Prime Time: 4 hours 
