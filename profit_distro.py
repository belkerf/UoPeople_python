#defining the function and its arguments
def profit_distro(profit,percent):
    if percent >=0 and percent <= 100:
        return profit * (percent / 100)
    else:
        return "your percentage is not correct, please try again!"

#calling the function to check if there is any errors
print(profit_distro(1000,10))
print(profit_distro(400,50))
print(profit_distro(9000,300))
