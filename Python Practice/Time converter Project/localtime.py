# Takes local time from device and converts it.


def local_time_converter(time_received):
    condition = True
    while condition:
        y = (int(time_received[0])*1000)+(int(time_received[1])*100)+(int(time_received[3])*10)+(int(time_received[4]))
        if y >= 1200:
            ch = int(input('''
Enter choice
1. View time in 12 hour format.
2. View time in 24 hour format.
    
Enter choice:'''))
            try:
                if ch == 1:
                    changed_time = y-1200
                    if changed_time > 999:
                        display_time = str(changed_time)
                        print(f'{display_time[0]}{display_time[1]}:{display_time[2]}{display_time[3]} PM')
                        break
                    else:
                        display_time = str(changed_time)
                        print(f'0{display_time[0]}:{display_time[1]}{display_time[2]} PM')
                        break
                elif ch == 2:
                    print(y, end=' PM')
                    print()
                    break
                else:
                    print("wrong entry")
                    break
            except ValueError:
                print("Wrong entry... please enter 1 or 2")
                input('Press any key to continue')

        elif y < 1200:
            ch = int(input('''
Enter choice
1. View time in 12 hour format.
2. View time in 24 hour format.
    
Enter choice:'''))
            try:
                if ch == 1:
                    display_time = str(y)
                    print(f'{display_time[0]}{display_time[1]}:{display_time[2]}{display_time[3]} AM')
                    break
                else:
                    print(y, end=' AM')
                    print()
                    break
            except ValueError:
                print("Wrong Entry")

                break
