arr = []
with open('nyc_weather.csv','r') as f:
    for line in f:
        tokens = line.split(',')
        try:
            temp = int(tokens[1])
            arr.append(temp)
        except:
            print("invalid temp")
#  What was the average temperature in first week of Jan
total = 0
for i in range(7):
    total = total + arr[i]
print(f"the average temperature in first week of Jan: {round(total/7,2)}")


# What was the maximum temperature in first 10 days of Jan
print(f"the maximum temperature in first 10 days of Jan: {max(arr[0:10])}")


weather_dict = {}

with open('nyc_weather.csv','r') as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temp = int(tokens[1])
            weather_dict[day] = temp
        except:
            print("invalid temp")
# What was the temperature on Jan 9?
print(f"the temperature on Jan 9: {weather_dict['Jan 9']}")

# What was the temperature on Jan 4?
print(f"the temperature on Jan 4: {weather_dict['Jan 4']}")