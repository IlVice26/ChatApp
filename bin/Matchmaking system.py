"""
Programma turnazioni squadre

@author Vicentini Elia, Olivieri Matteo, Gandini Simone
@version 1.1
"""
# Library
import random
from library import create
import os

# Global Variables
temp_var = 0
temp2 = 0

# Match Lists
match_list = []
teams_list = []
disciplines_list = []
var_list = []
riposa = []
teams1_list = []
another_list = []
riposa2 = []


def match(teams, temp_var, temp2, disciplines, another_list, riposa2):

    if teams % 2 == 0:
        team_p(teams, temp_var, temp2, disciplines, another_list, riposa2)
    else:
        team_d(teams, temp_var, temp2, disciplines, another_list, riposa2)


def team_p(teams, temp_var, temp2, disciplines, another_list, riposa2):
    
    if teams < ((disciplines * 2) + 1):
        while temp_var < teams - 1:

            var1 = tuple(teams_list)   # var 1 commutes the list in tuple
            var2 = list(var1)   # var 2 commutes var1 in list

            while var2 != []:
                num1 = random.randrange(1, teams + 1)
                while temp2 == 0:
                    for i in range(len(var2)):
                        if var2[i] == num1:  # temp2 control if num1 and num2 are in var2
                            temp2 += 1
                    if temp2 == 0:
                        num1 = random.randrange(1, teams + 1)
                var2.remove(num1)
                temp2 = 0
                num2 = random.randrange(1, teams + 1)
                while temp2 == 0:
                    for j in range(len(var2)):
                        if var2[j] == num2:
                            temp2 += 1
                    if temp2 == 0:
                        num2 = random.randrange(1, teams + 1)
                temp2 = 0
                var2.remove(num2)

                temp_list = [num1, num2]

                temp_list.sort()

                another_list.append(temp_list)
            r = 0

            if temp_var == 0:
                temp_var += 1
                match_list.append(another_list)

            for c in range(len(match_list)):
                for a in range(len(match_list[c])):
                    for b in range(len(another_list)):
                        if match_list[c][a] == another_list[b]:
                            r += 1
            
            if r == 0:
                match_list.append(another_list)
                temp_var += 1
            another_list = []

    else:
        while temp_var < teams:

            var1 = tuple(teams_list)   # var 1 commutes the list in tuple
            var2 = list(var1)   # var 2 commutes var1 in list
            riposa.append(var2[: teams - ((disciplines * 2) + 1)])
            del var2[0: teams - ((disciplines * 2))]

            while var2 != []:
                num1 = random.choice(var2)
                var2.remove(num1)
                num2 = random.choice(var2)
                var2.remove(num2)
                
                temp_list = [num1, num2]
                
                temp_list.sort()

                another_list.append(temp_list)
            r = 0

            for c in range(len(match_list)):
                for a in range(len(match_list[c])):
                    for b in range(len(another_list)):
                        if match_list[c][a] == another_list[b]:
                            r += 1
                
            if r == 0:
                match_list.append(another_list)
                temp_var += 1
                teams_list.append(teams_list[0])
                del teams_list[0]

            another_list = []


def team_d(teams, temp_var, temp2, disciplines, another_list, riposa2):

    if teams < ((disciplines * 2) + 1):

        while temp_var < teams:
            f = 0
            var1 = tuple(teams_list)
            var2 = list(var1)
            del(var2[temp_var])
            for t in range(len(riposa)):
                if riposa[t] == (temp_var + 1):
                    f += 1
            if f == 0:
                riposa.append(temp_var + 1)

            while var2 != []:
                num1 = random.randrange(1, teams + 1)
                while temp2 == 0:
                    for i in range(len(var2)):
                        if var2[i] == num1:  # temp2 control if num1 and num2 are in var2
                            temp2 += 1
                    if temp2 == 0:
                        num1 = random.randrange(1, teams + 1)
                var2.remove(num1)
                temp2 = 0
                num2 = random.randrange(1, teams + 1)
                while temp2 == 0:
                    for j in range(len(var2)):
                        if var2[j] == num2:
                            temp2 += 1
                    if temp2 == 0:
                        num2 = random.randrange(1, teams + 1)
                temp2 = 0
                var2.remove(num2)

                temp_list = [num1, num2]

                temp_list.sort()

                another_list.append(temp_list)
            r = 0

            if temp_var == 0:
                temp_var += 1
                match_list.append(another_list)
            for c in range(len(match_list)):
                for a in range(len(match_list[c])):
                    for b in range(len(another_list)):
                        if match_list[c][a] == another_list[b]:
                            r += 1
            
            if r == 0:
                match_list.append(another_list)
                temp_var += 1
            another_list = []

    else:
        while temp_var < teams:

            var1 = tuple(teams_list)  # var 1 commutes the list in tuple
            var2 = list(var1)  # var 2 commutes var1 in list
            riposa.append(var2[: teams - ((disciplines * 2) + 1)])
            del var2[0: teams - ((disciplines * 2))]

            while var2 != []:
                num1 = random.choice(var2)
                var2.remove(num1)
                num2 = random.choice(var2)
                var2.remove(num2)

                temp_list = [num1, num2]

                temp_list.sort()

                another_list.append(temp_list)
            r = 0

            for c in range(len(match_list)):
                for a in range(len(match_list[c])):
                    for b in range(len(another_list)):
                        if match_list[c][a] == another_list[b]:
                            r += 1

            if r == 0:
                match_list.append(another_list)
                temp_var += 1
                teams_list.append(teams_list[0])
                del teams_list[0]

            another_list = []


def file_tabel(match_list, disciplines_list, disciplines):

    create.css()
    create.html(match_list, disciplines_list, disciplines)

    return 0


if __name__ == '__main__':

    print('\nMatchmaking system for Fornace Studio by Gandini Simone, Vicentini Elia, Olivieri Matteo\n')

    temp1 = 0   # temp and temp1 control if the value in input is correct
    while temp1 == 0:
        try:
            disciplines = int(input("[+] Enter the number of disciplines present in the tournament: "))
            while disciplines < 5:
                print('\n[-] Enter a valid value! ')
                disciplines = int(input("[+] Enter the number of disciplines present in the tournament: "))
            temp1 += 1
        except ValueError:
            print('[-] Enter a valid value! ')

    temp = 0
    while temp == 0:
        try:
            teams1 = int(input("[+] Enter the number of teams participating in the tournament: "))
            while teams1 < disciplines + 1:
                print('[-] Enter a valid value! ')
                teams1 = int(input("[+] Enter the number of teams participating in the tournament: "))
            temp += 1
        except ValueError:
            print('[-] Enter a valid value! ')

    for i in range(1, teams1 + 1):
        teams_list.append(i)

    for j in range(1, disciplines + 1):
        disciplines_list.append("Discipline " + str(j))

    for k in range(1, teams1 + 1):
        teams1_list.append("Team " + str(k))

    print('\n[*] Matching the teams ...')
    match(teams1, temp_var, temp2, disciplines, another_list, riposa2)
    var1 = tuple(match_list)
    var2 = list(var1)
    e = 0
    for m in range(len(var2)):
        if m % 2 == 0:
            del match_list[e]
        else:
            e += 1
    '''for i in range(len(match_list)):
        print(match_list[i])'''


    file_tabel(match_list, disciplines_list, disciplines)

    print("\n[>] Html file is ready! Enjoy!")
    os.system("pause")

