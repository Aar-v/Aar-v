import inputtime as it
import localtime as lt
import datetime
while True:
    print('''
Select the method for time conversion
MENU
--------------
1. Localtime Converter.
2. User Input Time-converter. 
3. Exit.''')
    try:
        ch = int(input("Enter a choice :"))
        if ch == 1:
            # local time received in
            time = datetime.datetime.now()
            time_received = str(time.strftime('%X'))
            lt.local_time_converter(time_received)
            input('PRESS ENTER')
            continue
        elif ch == 2:
            while True:
                try:
                    formt = int(input('''
1. 12 hr format to 24 hr format.
2. 24 hr format to 12 hr format.
3. Exit.

Select Format :'''))
                    if formt == 1:
                        input_time = input('Enter time { in HH:MM AM/PM format }:')
                        it.time_converter_12to24(input_time)
                        input('PRESS ENTER')
                    elif formt == 2:
                        input_time = input('Enter time {in HHMM format}:')
                        it.time_converter_24to12(input_time)
                        input('PRESS ENTER')
                    elif formt == 3:
                        break
                    else:
                        print('Sorry wrong entry')
                        continue
                except ValueError:
                    print("SORRY! wrong entry...")
                    input('Press any key to continue')
                except IndexError:
                    print('Sorry! wrong entry...')
                    print('Please Insert colon between hours and minutes and specify am/pm')
                    input('Press any key to continue')
        elif ch == 3:
            input('Press enter to exit')
            break
        else:
            print('Wrong entry!')
            input('Press any key to continue')
            continue
    except ValueError:
        print("SORRY! wrong entry... Please enter 1,2 or 3")
        input('Press any key to continue')
