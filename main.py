"""
    it's a game
"""

cultures = ['chinese', 'egyptian', 'test']
personalitymad = ['pretty pleas type a choice', 'type one or il stop the program', 'now I realy will', 'error', '[computer fizzles]', 'I exploded'
]
claims = None
mad = 0
win = False
init = True
turn = 0
prv = [  'velia','terepto','hicroyo','hamming','lester','lancaster','worchester', 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,23, 24, 25, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 50, 40, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 63
]
prvind = {
    prv[0]: 10,
    prv[1]: 11,
    prv[2]: 15,
    prv[3]: 12,
    prv[4]: 11,
    prv[5]: 15,
    prv[6]: 134,
    prv[7]: 124,
    prv[8]: 129,
    prv[9]: 14,
    prv[10]: 27,
    prv[11]: 56,
    prv[12]: 97,
    prv[13]: 123,
    prv[14]: 1298,
    prv[15]: 15,
    prv[16]: 16,
    prv[17]: 17,
    prv[18]: 18,
    prv[19]: 19
}


#print money
def printcurr():
    print('you have ' + currstr + ' ' + curr + 's')
#chose culture
#please chose a culture
def choosecul():
    global mad
    print('please type one: chinese, egyptian')
    global culture
    culture = input('aps-inp-cul:/ ')
    if culture not in cultures:
        print(personalitymad[mad])
        mad = mad + 1
        if mad > 5:
            quit()
        choosecul()
    mad = 0
    return mad
#choose economy
def econ():
    global econ
    global curr
    econ = input('aps-inp-econ:/ ')
    curr = input('aps-inp-curr:/ ')
#manage exploration claims
def EXclaimmanager():
    global claims
    if init:
        if culture in cultures[0]:
            claims = ['india', 'peru']
        if culture in cultures[1]:
            claims = ['ethiopia', 'sicly']
        if culture in cultures[2]:
            claims = 'all'
def start():
    global mad
    inp = input('ajk:/ ')
    print(' ')
    if inp == 'LIST':
        print('''cultures = ['chinese', 'egyptian']
personalitymad = ['pretty pleas type a choice', 'type one or il stop the program', 'now I realy will', 'error', '[computer fizzles]', 'I exploded']
actoins = ['settle','explore']
claims = None
mad = 0
win = False
init = True

#say stuff
def printprompt(promt):
	print('say: ' + promt)
def printcurr():
	printprompt('you have ' + currstr + ' ' + curr + 's')

	
#chose culture
def choosecul():
	global mad
	print('please type one: chinese, egyptian')
	global culture
	culture = input('aps-inp-cul:/ ')
	if culture not in cultures:
		print(personalitymad[mad])
		mad = mad + 1
		if mad > 5:
			quit()
		choosecul()
	mad = 0
	return mad
#choose economy
def econ():
	global econ
	global curr
	econ = input('aps-inp-econ:/ ')
	curr = input('aps-inp-curr:/ ')
#manage exploration claims
def EXclaimmanager():
	global claims
	if init:
		if culture in cultures[0]:
			claims = ['iran','peru']
		if culture in cultures[1]:
			claims = ['ethiopia','mexico']

def start():
	global mad
	enter = input('ajk:/ ')
	print(' ')
	if enter == 'LIST' :
		print('''
              ''')
	if enter != 'RUN' :
		print(personalitymad[mad])
		mad = mad + 1
		if mad > 5:
			quit()
		start()
		mad = 0
		return mad
#main code
start()
choosecul()
econ()
currs = 10000
currstr = str(currs)
EXclaimmanager()
init = False
printprompt('your culture is: ' + culture + ' and you have 10000 ' + curr + 's')
while not win:
	inp = input('aps:/ ')
	currstr = str(currs)''')
        start()
    if inp != 'RUN':
        print(personalitymad[mad])
        mad = mad + 1
        if mad > 5:
            quit()
        start()
        mad = 0
        return mad
#main code

start()
choosecul()
econ()
currs = 10000
currstr = str(currs)
EXclaimmanager()
init = False
print('your culture is: ' + culture + ' and you have 10000 ' + curr + 's')
while not win:
    def spend(cash):
        global currs
        currs = currs - cash
        if currs >= 0:
            return currs
        else:
            print('not enuf muny')
            currs = currs + cash
    def income(cash):
        global currs
        currs = currs + cash
        return currs
    inp = input('aps:/ ')
    tk = inp.split()
    currstr = str(currs)
    if tk[0] == 'end':
        quit()
    if tk[0] == 'save':
        print('initializatoin data save protocal')
        save = curr + econ + culture
        print(save)
    if tk[0] == 'endturn':
        turn = turn + 1
        turnstr = str(turn)
        print('turn: ' + turnstr + ' you have ' + curr + 's ' + currstr)
    if tk[0] == 'invest' and tk[2] == 'in':
        spend(int(tk[1]))
        provice = tk[3]
    else:
        print('ERROR: invalid syntax')