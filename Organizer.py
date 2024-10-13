arr = {'a':{}, 'p':{}}
note = {'a':{}, 'p':{}}
arrAM = 0
arrPM = 0
location = []
import math
#z is an unused variable
#only for exception errors
def arr_print():
    global arr
    global note
    global arrAM
    global arrPM
    arrAM = sorted(arr['a'].items(), key = lambda x:int(x[0]))
    counter = 0
    #12 clock AM excpetion --> move to front
    for t in range(len(arrAM)):
        check = list(arrAM[t][0])
        if check.count(' ') == 0 and arrAM[t][0][:2] == '12':
            arrAM.insert(counter, arrAM[t])
            arrAM.pop(t+1)
            counter += 1
   
    arrPM = sorted(arr['p'].items(), key = lambda x:int(x[0]))
    counter = 0
    #12 clock PM excpetion --> move to front
    for t in range(len(arrPM)):
        check = list(arrPM[t][0])
        if check.count(' ') == 0 and arrPM[t][0][:2] == '12':
            arrPM.insert(counter, arrPM[t])
            arrPM.pop(t+1)
            counter += 1
   
    #Printing
    for r in arrAM:
        #Reg
        t=list(r[0])
        noteTime = ''.join(t)
        t.insert(len(t)-2, ':')
        t=''.join(t)
        print(t, 'AM ', '|', r[1])
        #Note
        #10 spaces, |, 2 spaces + '-'
        if noteExist('a', noteTime):
            for subS in note['a'][noteTime]:
                print('          | ', '-', subS)
                
    #tZone Separator            
    print('----------|')

    for r in arrPM:
        #Reg
        t=list(r[0])
        noteTime = ''.join(t)
        t.insert(len(t)-2, ':')
        t=''.join(t)
        print(t, 'PM ', '|', r[1])
        #Note
        #10 spaces, |, 2 spaces + '-'
        if noteExist('p', noteTime):
            for subS in note['p'][noteTime]:
                print('          | ', '-', subS)

def input_test(x):
    #Warning input_test only checks for time and tzone, not including the note feature
    #That is checked in the Argument evaluator
   
    #Space Test
    x = x.split()

    if len(x) >= 1:
        #Case of just time, no what
        if len(x) == 1:
            if len(x[0]) == 5 or len(x[0]) == 4:
                time = timeConversion(x[0])
                tZone = time[0]
                time = time [1]
                if len(time) == 3:
                    time = ' ' + time
                if tZone == 'p' or tZone == 'a':
                    if time.isdigit():
                        return True
            
            #Case of Operation
            char = x[0]
            if char == 'c' or char == 's' or char == 'r' or char == 'clear':
                return True
       
        #addDelEdit
        #Variable Split Test
        if x[0][0] == 'p' or x[0][0] == 'a':
            #Size Test
            if len(x[0]) == 5 or len(x[0]) == 4:
                x=x[0][1:]
                x=''.join(x)
                #Int test
                if x.isdigit():
                    return True
   
       
        if len(x) == 2:
            #Note Test
            #Variable Split Test
            if x[0] == 'n':
                if x[1][0] == 'p' or x[1][0] == 'a':
                    #Size Test
                    if len(x[1]) == 5 or len(x[1]) == 4:
                        z = ''.join(x[1][1:])
                        time = timeConversion(x[1])
                        tZone = time[0]
                        time = time [1]
                        #Int test
                        if z.isdigit():
                            if arrExist(tZone, time):
                                return True
                       
            #Del Test
            #Variable Split Test
            if x[0] == 'd':
                if x[1][0] == 'p' or x[1][0] == 'a':
                    #Size Test
                    if len(x[1]) == 5 or len(x[1]) == 4:
                        z = ''.join(x[1][1:])
                        #Int test
                        if z.isdigit():
                            time = timeConversion(x[1])
                            tZone = time[0]
                            time = time [1]
                            if arrExist(tZone, time):
                                return True
        
        if len(x) >= 3:
            #First time module
            if x[1][0] == 'p' or x[1][0] == 'a':
                #Size Test
                if len(x[1]) == 5 or len(x[1]) == 4:
                    z = ''.join(x[1][1:])
                    #Int test
                    if z.isdigit():
                        time = timeConversion(x[1])
                        tZone = time[0]
                        time = time [1]
                        tZone1 = tZone
                        if arrExist(tZone, time):
                            #Second time module
                            if x[2][0] == 'p' or x[2][0] == 'a':
                                #Size Test
                                if len(x[2]) == 5 or len(x[2]) == 4:
                                    z = ''.join(x[2][1:])
                                    #Int test
                                    if z.isdigit() and x[0] == 'e' and len(x) == 3:
                                        #If no time shift --> Time Edit
                                        #Don't need to check if time2 exists
                                        return True
                                    
                                    elif z.isdigit() and x[0] == 'e':
                                        #If time Shift instead
                                        #Repeat time2 existence process; time format is checked
                                        if len(x) == 4:
                                            time = timeConversion(x[2])
                                            tZone = time[0]
                                            time = time [1]
                                            tZone2 = tZone
                                            if arrExist(tZone, time):
                                                #If the shift number is an integer
                                                try:
                                                    possibleDigit = x[3]
                                                    possibleDigit = int(possibleDigit)
                                                    return True
                                                except:
                                                    return False
                                    
                                    elif z.isdigit() and x[0] == 'd':
                                        #If multiDel instead
                                        #Repeat time2 existence process; time format is checked
                                        time = timeConversion(x[2])
                                        tZone = time[0]
                                        time = time [1]
                                        tZone2 = tZone
                                        if arrExist(tZone, time):
                                            return True

    return False



def arr_save():
    global arr
    global note
    arrAM = arr['a']
    arrPM = arr['p']
   
    for r in arrAM:
        noteTime = r
        a = list(r)
        if a.count(' ') == 1:
            a.remove(' ')
        a=''.join(a)
       
        file.write( 'a' + a + ' '+ arrAM[r] + '\n' )
        if noteExist('a', noteTime):
            for subS in note['a'][noteTime]:
                file.write('-' + ' ' + subS + '\n')
       
    for r in arrPM:
        noteTime = r
        a = list(r)
        if a.count(' ') == 1:
            a.remove(' ')
        a=''.join(a)
       
        file.write( 'p' + a + ' ' + arrPM[r] + '\n')
        if noteExist('p', noteTime):
            for subS in note['p'][noteTime]:
                file.write('-' + ' ' + subS + '\n')
    print('Saved')



def arr_display():
    global arr
    global note
    arrAM = sorted(arr['a'].items(), key = lambda x:int(x[0]))
    counter = 0
    for t in range(len(arrAM)):
        check = list(arrAM[t][0])
        if check.count(' ') == 0 and arrAM[t][0][:2] == '12':
            arrAM.insert(counter, arrAM[t])
            arrAM.pop(t+1)
            counter += 1
   
    arrPM = sorted(arr['p'].items(), key = lambda x:int(x[0]))
    counter = 0
    for t in range(len(arrPM)):
        check = list(arrPM[t][0])
        if check.count(' ') == 0 and arrPM[t][0][:2] == '12':
            arrPM.insert(counter, arrPM[t])
            arrPM.pop(t+1)
            counter += 1
   
    for r in arrAM:    
        t=list(r[0])
        t.insert(len(t)-2, ':')
        t=''.join(t)
        file.write(t + ' AM ' + ' | ' + r[1] + '\n')
        #For notes
        #10 spaces, |, 2 spaces + '-'
        try:
            noteArr = note['a'][r[0]]
            for n in noteArr:
                file.write('          |  ' + '- ' + n + '\n')
        except:
            z=0
                 
    file.write('----------|' + '\n')
   
    for r in arrPM:
        t=list(r[0])
        t.insert(len(t)-2, ':')
        t=''.join(t)
        file.write(t + ' PM ' + ' | ' + r[1] + '\n')
       
        #For notes
        #10 spaces, |, 2 spaces + '-'
        try:
            noteArr = note['p'][r[0]]
            for n in noteArr:
                file.write('          |  ' + '- ' + n + '\n')
        except:
            z=0



def readReplace():
    global arr
    global note
    file = open('Organizer_save.py', 'r')
    lines = file.read().splitlines()   
    file.close()

    arr = {'a':{}, 'p':{}}
    note = {'a':{}, 'p':{}}
    for i in range(len(lines)):
        item = lines[i]
        item = item.split()
        #Either note or regular
        #try for if is not note
        if item[0] == '-':
            noteAddDelEdit(n=item, time = index, r = True)
        else:
            #Index tracks the note's previous time
            index = lines[i].split()
            index = index[0]
            addDelEdit(x=item, delete = False, r = True)
    print('Reformatted')



def arrExist(tZone, time):
    global arr
    #If the time exists in the arr before adding note
    #Otherwise it is an invalid time because it doesn't exist
    try:
        ArrDoesExist = arr[tZone][time]
        return True
    except:
        return False

def addDelEdit(x, delete, r):
    global arr
    global note
    #Input style: dp1200 what   or   p1200 what   or   dp1200 3-
    #delete is when regular is deleted
    #R for replace
    if delete == True:
        time = x[1]
        tZone = time[0]
        time = time[1:]
        if len(time) == 3:
            time = ' ' + time
        #Deleting. If there is note, delete it too
        del arr[tZone][time]
        if noteExist(tZone, time):
            del note[tZone][time]
       
    else:
        time = x[0]
        tZone = time[0]
        time = time[1:]
        what = ' '.join(x[1:])
        if len(time) == 3:
            time = ' ' + time
        #Edit (Include ask note delete)
        if arrExist(tZone, time) and r == False:
            if noteExist(tZone, time):
                #Note exist --> Ask for delete
                ask = input('Delete note? ')
                if ask == 'd':
                    #yes note delete + reg edit
                    del note[tZone][time]
                    arr[tZone].update({time: what})
               
                #No note delete + reg eidt
                else:
                    arr[tZone].update({time: what})
            else:
                #Note doesn't exist --> Auto reg edit
                arr[tZone].update({time: what})
       
        #Add
        else:
            #Reg edit
            arr[tZone].update({time: what})
       


def noteInputTest(x):
    #AddEdit
    if len(x) > 0:
        if x[0] == '-' or x[0].isdigit():
            if len(x) >= 1:
                return True
   
    #Del
    if len(x) == 2:
        if x[0] == 'd':
            if x[1].isdigit:
                return True
   
    if ''.join(x) == 'n':
        return True

    return False

def noteExist(tZone, time):
    #if the note at time exists or not --> Determine existence argument or first note added
    try:
        noteArrExists = note[tZone][time]
        return True
    except:
        return False

def noteAddDelEdit(n, time, r):
    global note
    #Input style: - what   or   3 what   or   d 3
    #Note style: 15 spaces, '-', what
    tZone = time[0]
    time = time[1:]
    if len(time) == 3:
        time = ' ' + time
    regTime=list(time)
    regTime.insert(len(regTime)-2, ':')
    regTime = ''.join(regTime)
    if tZone == 'a':
        regTZone = 'AM'
    else:
        regTZone = 'PM'
   
    #When replacing
    if r == True:
        what = ' '.join(n[1:])
        if noteExist(tZone, time):
            #Note exists --> adding note
            note[tZone][time].append(what)
        else:
            #Note does not exist --> creating note
            note[tZone].update({time:[]})
            note[tZone][time].append(what)
                       
    else:
        print('Note mode')
        noteLoop = 0
        while noteLoop == 0:
            print(regTime, regTZone, '|', arr[tZone][time])
            if noteExist(tZone, time):
                for r in range (len(note[tZone][time])):
                    print('            ', r+1, note[tZone][time][r])
           
            n = input().split()
            #Check input valid
            if noteInputTest(n) == True:
                #Create/add note
                if n[0] == '-':
                    what = ' '.join(n[1:])
                    if noteExist(tZone, time):
                        #Note exists --> adding note
                        note[tZone][time].append(what)
                    else:
                        #Note does not exist --> creating note
                        note[tZone].update({time:[]})
                        note[tZone][time].append(what)
                   
                #Edit note
                if n[0].isdigit():
                    num = int(n[0])
                    what = ' '.join(n[1:])
                    if num <= len(note[tZone][time]) and num > 0:
                        #Arr format
                        num = num - 1
                        what = ' '.join(n[1:])
                        note[tZone][time][num] = what
                    else:
                        print('Invalid input')
                   
                #Del note
                if n[0] == 'd':
                    num = int(n[1])
                    if num <= len(note[tZone][time]) and num > 0:
                        #Arr format
                        num = num - 1
                        note[tZone][time].pop(num)
                    else:
                        print('Invalid input')
               
                #Exit
                if n[0] == 'n':
                    noteLoop = 1

            else:
                print('Invalid input')
            print('')
            print('')
               
        print('Note done')



def timeEdit(x):
    #Input style = e p1200 p100
    # Or e p1200 p100 10
    #The second style is a shift from time1 to time2 by 10 minutes
    global arr
    global note
    time2 = timeConversion(x[2])
    tZone2 = time2[0]
    time2 = time2 [1]
    
    time = timeConversion(x[1])
    tZone = time[0]
    time = time [1]
    what = arr[tZone][time]
    
    if arrExist(tZone2, time2):
        x.remove('e')
        addDelEdit(x, delete = True, r = False)
        x.insert(0, 'e')
    #Time at new time exists --> Ask for deletion
    arr[tZone2].update({time2: what})
    #If the original time has note --> Also edit to new time
    if noteExist(tZone, time):
        if noteExist(tZone2, time2):
            del note[tZone2][time2]
        timeNote = tZone2 + time2
        for i in note[tZone][time]:
            #Formatting for note
            i=i.split()
            i.insert(0, '-')
            noteAddDelEdit(n=i, time = timeNote, r = True)
            
    #Formatting for Original delete
    addDelEdit(x, delete = True, r = False)



def timeDifferenceCalculate(minute, timeDifference):
    #Calculate any minute overlaps to convert into extra hours
    shift = minute + timeDifference
    if shift >= 60:
        hourDifference = int(shift/60)
        return hourDifference
    elif shift < 0:
        hourDifference = shift/60
        if hourDifference <= 0:
            #Because of the rounding formula for clocks, round DOWN to nearest integer
            hourDifference = math.floor(hourDifference)
        return hourDifference
    else:
        return 0
   
def newTimeCalculate(tType):
    #With timeDifferences calculated, generate a new time from calculated times
    global location
    global prevTime
    global timeDifference
    previousTime = spaceRemover(location[tType][r])
    prevTime = list(previousTime)
    if tType == 0:
        prevTime.insert(0, 'a')
    else:
        prevTime.insert(0, 'p')
    prevTime = ''.join(prevTime)
    
    #Calculate minute and hour
    #Hour is based on 0-11 scale 
    if len(previousTime) == 3:
        minute = int(previousTime[1:])
        prevHour = int(previousTime[0]) % 12
    else:
        minute = int(previousTime[2:])
        prevHour = int(previousTime[:2]) % 12
        
    #Calculate difference between hour changes
    #If difference (based on hour # scale) switch between TZones, calculate new tZone and time
    #Also reconvert prevHour to 12-11 scale
    netHour = (prevHour + timeDifferenceCalculate(minute, timeDifference)) % 24
    #Case of <12:00 to >=12:00
    if netHour >= 12 and prevHour < 12:
        #Calculate the hour Difference relative to the tZone
        newHour = netHour % 12
        #12:00 excpetion
        if newHour == 0:
            newHour = 12
        
        if tType == 0:
            tType = 1
        else:
            tType = 0
    #Case of >=12:00 to <12:00
    #Note that the hour Difference only applies to adding hours
    elif netHour < 0 and prevHour >= 0:
        newHour = netHour % 12
        if tType == 0:
            tType = 1
        else:
            tType = 0
    
    #No TZone/time change
    else:
        newHour = netHour % 12
        #if >12:00 and <1:00 (Between the 12 range but not cause tZone change)
        if newHour == 0:
            newHour = 12

    minute = (minute + timeDifference)%60
    minute = list(str(minute))
    if len(minute) == 1:
        minute.insert(0, '0')
    minute = ''.join(minute)

    newTime = list(str(newHour) + str(minute))
    if tType == 0:
        newTime.insert(0, 'a')
    else:
        newTime.insert(0, 'p')
    newTime = ''.join(newTime)
    return newTime

def timeShift(x):
    global location
    global time
    global tZone
    global r
    global timeDifference
    #Initialization
    location = [[], []]
    time2 = timeConversion(x[2])
    tZone2 = time2[0]
    time2 = time2 [1]
    
    time = timeConversion(x[1])
    tZone = time[0]
    time = time [1]
    
    for r in arrAM:
        location[0].append(r[0])
    for r in arrPM:
        location[1].append(r[0])
   
    timeDifference = int(x[3])
    maxA = len(location[0])
    maxP = len(location[1])
    #Calculate edits with 4 different arrangements of A and P,
    #with order determined through adding or subtracting time
    
    #Two for loops are used when times are between tZones
    #+1 and -1 for loop requirements
    try:
        #time Shift
        #Subtract time
        if timeDifference < 0:
            if tZone == 'p':
                if tZone2 == 'p':
                    #P, P
                    PPoint1 = location[1].index(time)
                    PPoint2 = location[1].index(time2) + 1
                    for r in range(PPoint1, PPoint2):
                        newTime = newTimeCalculate(1)
                        x = ['e', prevTime, newTime]
                        timeEdit(x)
                else:
                    #P, A
                    PPoint = location[1].index(time)
                    APoint = location[0].index(time2)+1
                    for r in range (PPoint, maxP):
                        newTime = newTimeCalculate(1)
                        x = ['e', prevTime, newTime]
                        timeEdit(x)
                    for r in range (0, APoint):
                        newTime = newTimeCalculate(0)
                        x = ['e', prevTime, newTime]
                        timeEdit(x)
            else:
                if tZone2 == 'a':
                    #A, A
                    APoint1 = location[0].index(time)
                    APoint2 = location[0].index(time2) + 1
                    for r in range (APoint1, APoint2):
                        newTime = newTimeCalculate(0)
                        x = ['e', prevTime, newTime]
                        timeEdit(x)
                else:
                    #A, P
                    APoint = location[0].index(time)
                    PPoint = location[1].index(time2)+1
                    for r in range (APoint, maxA):
                        newTime = newTimeCalculate(0)
                        x = ['e', prevTime, newTime]
                        timeEdit(x)
                    for r in range(0, PPoint):
                        newTime = newTimeCalculate(1)
                        x = ['e', prevTime, newTime]
                        timeEdit(x)
                        
                       
                       
        #Add time
        else:
            #Adjust for For Loop requirements
            #All loops reversed for easy edit
            maxA = maxA-1
            maxP = maxA-1
            if tZone == 'p':
                if tZone2 == 'p':
                    #P, P
                    PPoint1 = location[1].index(time)-1
                    PPoint2 = location[1].index(time2)
                    for r in range(PPoint2, PPoint1, -1):
                        newTime = newTimeCalculate(1)
                        x = ['e', prevTime, newTime]
                        timeEdit(x)
                else:
                    #P, A
                    PPoint = location[1].index(time) - 1
                    APoint = location[0].index(time2)
                    for r in range (APoint, -1, -1):
                        newTime = newTimeCalculate(0)
                        x = ['e', prevTime, newTime]
                        timeEdit(x)
                    for r in range(maxP, PPoint, -1):
                        newTime = newTimeCalculate(1)
                        x = ['e', prevTime, newTime]
                        timeEdit(x)
                       
                   
           
            else:
                if tZone2 == 'a':
                    #A, A
                    APoint1 = location[0].index(time)-1
                    APoint2 = location[0].index(time2)
                    for r in range (APoint2, APoint1, -1):
                        newTime = newTimeCalculate(0)
                        x = ['e', prevTime, newTime]
                        timeEdit(x)
                else:
                    #A, P
                    APoint = location[0].index(time)-1
                    PPoint = location[1].index(time2)
                    for r in range (PPoint, -1, -1):
                        newTime = newTimeCalculate(1)
                        x = ['e', prevTime, newTime]
                        timeEdit(x)
                    for r in range (maxA, APoint, -1):
                        newTime = newTimeCalculate(0)
                        x = ['e', prevTime, newTime]
                        timeEdit(x)
   
    except:
        print('Invalid input')


def multiDel(x):
    global arr
    global tZone
    location = [[], []]
    for r in arrAM:
        z = list(r[0])
        if z[0] == ' ':
            z.pop(0)
        z.insert(0, 'a')
        z = ''.join(z)
        location[0].append(z)
        
    for r in arrPM:
        z = list(r[0])
        if z[0] == ' ':
            z.pop(0)
        z.insert(0, 'p')
        z = ''.join(z)
        location[1].append(z)
    
    tZone_time2 = x[2]
    time2 = timeConversion(x[2])
    tZone2 = time2[0]
    time2 = time2 [1]
    
    tZone_time = x[1]
    time = timeConversion(x[1])
    tZone = time[0]
    time = time [1]
    
    maxA = len(location[0])
    maxP = len(location[1])
    try:
        if tZone == 'p':
            if tZone2 == 'p':
                #P, P
                PPoint1 = location[1].index(tZone_time)
                PPoint2 = location[1].index(tZone_time2) + 1
                for r in range(PPoint1, PPoint2):
                    xDel = 'd ' + location[1][r]
                    xDel = xDel.split()
                    addDelEdit(xDel, delete = True, r = False)
            else:
                #P, A
                PPoint = location[1].index(tZone_time)
                APoint = location[0].index(tZone_time2)+1
                for r in range (PPoint, maxP):
                    xDel = 'd' + location[1][r]
                    xDel = xDel.split()
                    addDelEdit(xDel, delete = True, r = False)
                for r in range (0, APoint):
                    xDel = 'd ' + location[0][r]
                    xDel = xDel.split()
                    addDelEdit(xDel, delete = True, r = False)
        else:
            if tZone2 == 'a':
                #A, A
                APoint1 = location[0].index(tZone_time)
                APoint2 = location[0].index(tZone_time2) + 1
                for r in range (APoint1, APoint2):
                    xDel = 'd ' + location[0][r]
                    xDel = xDel.split()
                    addDelEdit(xDel, delete = True, r = False)
            else:
                #A, P
                APoint = location[0].index(tZone_time)
                PPoint = location[1].index(tZone_time2)+1
                for r in range (APoint, maxA):
                    xDel = 'd ' + location[0][r]
                    xDel = xDel.split()
                    addDelEdit(xDel, delete = True, r = False)
                for r in range(0, PPoint):
                    xDel = 'd ' + location[1][r]
                    xDel = xDel.split()
                    addDelEdit(xDel, delete = True, r = False)
    except:
        print("Invalid Input")
    
    
    
def timeConversion(x):
    global tZone
    global time
    tZone = x[0]
    time = x[1:]
    if len(time) == 3:
        time = ' ' + time
    return [tZone, time]
def spaceRemover(x):
    x=list(x)
    try:
        x.remove(' ')
        x = ''.join(x)
        return x
    except:
        x=''.join(x)
        return x
        z = 0

loop = 0
readReplace()
while loop == 0:
    inputValid = True
    arr_print()
    x = input()
    if input_test(x) == False:
        print("Invalid input")
        inputValid = False
       
    if inputValid == True:
        x = x.split()
     
       #Create --> Save, Display, and Quit
        if x[0] == 's':
            #Save
            open('Organizer_save.py', 'w').close()
            file = open('Organizer_save.py', 'w')
            arr_save()
            file.close()
            #Display
            open('Organizer_display.py', 'w').close()
            file = open('Organizer_display.py', 'w')
            arr_display()
            file.close()
            #Quit
            loop = 1
            break
       
       #read and replace
        elif x[0] == 'r':
            readReplace()
       
        #Note addDelEdit
        elif x[0] == 'n':
            noteAddDelEdit(x, x[1], r=False)
       
       #Time/note Delete
        elif x[0] == 'd':
            if len(x) == 3:
                multiDel(x)
            else:
                addDelEdit(x, delete = True, r = False)
        
        #TimeEdit
        elif x[0] == 'e':
            if len(x) == 4:
                timeShift(x)
            else:
                timeEdit(x)

        
        #When you want to CLEAR THE SCHEDULE ENTIRELY; too dangerous to use until necessary
        #elif x[0] == 'clear':
            #arr = {'a':{}, 'p':{}}
            #note = {'a':{}, 'p':{}}
            #arrAM = 0
            #arrPM = 0
            #location = []
        
        #Regular
        else:
            addDelEdit(x, delete = False, r = False)
   
    print('')
    print('')
