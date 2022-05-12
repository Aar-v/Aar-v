# Takes input from user in 12 hour format and converts it to 24 hour format
def time_converter_12to24(time_input):
    while True:
        new_time = (int(time_input[0])*1000)+(int(time_input[1])*100)+(int(time_input[3])*10)+(int(time_input[4]))
        check = time_input.upper()
        if 'AM' in check:
            print('0', end='')
            print(new_time, end=' AM')
            print()
            break
        elif 'PM' in check:
            print(new_time+1200, end=' PM')
            print()
            break
# Takes time from user in 24 hour format and converts it to 12 hour format.


def time_converter_24to12(time_input):
    while True:
        new_time = int(time_input)
        if new_time in range(1201, 2401):
            new_time -= 1200
            if new_time > 999:
                print_time = str(new_time)
                print(f'{print_time[0]}{print_time[1]}:{print_time[2]}{print_time[3]} PM')
                print()
                break
            elif new_time > 99:
                print_time = str(new_time)
                print(f'0{print_time[0]}:{print_time[1]}{print_time[2]} PM')
                print()
                break
            elif new_time > 9:
                print_time = str(new_time)
                print(f'00:{print_time[0]}{print_time[1]} PM')
                print()
                break
            else:
                print_time = str(new_time)
                print(f'00:0{print_time[0]} PM')
                print()
                break
        elif new_time in range(0, 1201):
            new_time = str(time_input)
            print(f'{new_time[0]}{new_time[1]}:{new_time[2]}{new_time[3]} AM')
            print()
            break
        elif new_time > 2400:
            print('Wrong entry')
            break
