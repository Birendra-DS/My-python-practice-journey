"""In this question, you have to write a Python program to print 
the names of the players and the team of each player of all those
players whose jersey number is a prime number. The list should be
ordered in reverse alphabetical order of player names. If two or 
more players have the same name, then further sorting should be 
done on the team name, again in reverse alphabetical order. The 
format of output is as given below: Name of the player, followed 
by a comma (,), then a space and then the team name. For example,
if Arjun has jersey number 5 and is playing for All Stars and 
Pranav, with jersey number 7, is playing for team Amigos, then 
the output will be: Pranav, Amigos Arjun, All Stars
"""
# what I need to do:
"""
1) print the names of the players and the team of each player of 
all those players whose jersey number is a prime number
2) The list should be ordered in reverse alphabetical order of 
player names
3) If two or more players have the same name, then further sorting
should be done on the team name, again in reverse alphabetical order
4) O/p format: Name of the player, followed 
by a comma (,), then a space and then the team name.
"""
# write a function to check prime number
def check_prime(n):
    if n < 2:
        return False
    
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
            
    return True


players = [("Ajay", 2, "Assam_war"),
           ("Manas", 18, "Bengal_tiger"),
           ("Bir", 7, "Bihar_wala"),
           ("San", 12, "Gujarat_titan"),
           ("Bir",11, "Manipur_Miya")]

result =[]
for name,jer_num,team in players:
    # if prime then append in result
    if check_prime(jer_num):
        print(name,team)
        result.append((name,team))
        #result.extend([(name, team)])  # both give the same output
        
    
result.sort(reverse=True)       # reverse the name

for name, team in result:
    print(f"{name}, {team}")








