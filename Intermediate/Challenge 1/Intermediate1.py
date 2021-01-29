# Create a menu driven program
# Using the menu drive program allow a user to add/delete items
# The menu should be based on an events calender where users enter the events by hour
# No events should be hard-coded.

import calendar
import datetime
import sys
import os
import CalendarEventClasses as events

#
# Global Vars
#
commandDict = {
	"ADD"     : (("ADD","ENTER","NEW","A","N"),"Add an event to the calendar.\n   Args: Year-Month-Day, Time"),
	"DELETE"  : (("DELETE","REMOVE","D"),"Remove an event from the calendar.\n   Args: EventName"),
	"LIST"    : (("LIST","L"),"List events for a specified month.\n Args: Month, Year"),
	"LOAD"    : (("LOAD","OPEN","O"),"Load a saved calendar.\n   Args: FileName"),
	"SAVE"    : (("SAVE","S"),"Save the current events to a calendar. Overwrites any existing events.\n   Args: FileName"),
	"SETDATE" : (("SET","SETDATE","SD"),"Set the month to display.\n   Args:Year(int), Month(int)"),
	"VIEW"    : (("VIEW","CALENDAR","V"),"View upcoming events.\n   Args: Year(int), Month(int)"),
	"HELP"    : (("HELP","H"),"Displays the help info."),
	"QUIT"    : (("QUIT","ESC","Q","X"),"Exits the program.")
}

eventList = {}

#
# Functions
#

# Clears the console screen
def clearScreen():
	os.system('cls')
	print()

# Prints a calendar for a specified month
def printCalendar(*args):
	now = datetime.datetime.now()
	try:
		now = datetime.datetime(int(args[1]),int(args[2]),1)
	except:
		if len(args) > 1:
			print("Invalid arguments. Displaying the current month.")
	nowYear = int(now.strftime("%Y"))
	nowMonth = int(now.strftime("%m"))
	monthDay = calendar.monthrange(nowYear,nowMonth)[0]
	monthLength = calendar.monthrange(nowYear,nowMonth)[1]
	calStrs = [["","","","","","",""],
	           ["","","","","","",""],
			   ["","","","","","",""],
			   ["","","","","","",""],
			   ["","","","","","",""],
			   ["","","","","","",""]]
	for i in range(1,monthLength+1):
		monthDay += 1
		calStrs[int(monthDay/7)][monthDay%7] = str(i)
	print("____________________________________")
	print("|  <<         {0} {1}         >>  |".format(now.strftime("%b"),now.strftime("%Y")))
	print("| Su | M  | Tu | W  | Th | F  | Sa |")
	for week in calStrs:
		print("| {0:>2} | {1:>2} | {2:>2} | {3:>2} | {4:>2} | {5:>2} | {6:>2} |".format(week[0],week[1],week[2],week[3],week[4],week[5],week[6]))
	print()

# Add an event to the event list
def addEvent(*args):
	try:
		eventDate = args[1]
		print("Event Date (YYYY-M-D): {}".format(args[1]))
	except:
		eventDate = input("Event Date (YYYY-MM-DD): ")
	try:
		eventTime = args[2]
		print("Start Time (tttt): {}".format(args[2]))
	except:
		eventTime = input("Start Time (tttt): ")
	eventName = input("Event Name: ")
	eventDesc = input("Event Description: ")
	try:
		eventDateTimeStr = "{} {}".format(eventDate,eventTime)
		eventDateTime = datetime.datetime.strptime(eventDateTimeStr,"%Y-%m-%d %H%M")
		newEvent = events.CalendarEvent(eventDateTime, eventName, eventDesc)
		eventList.update({newEvent.id : newEvent})
		print("Event added!")
	except:
		print("Invalid arguments.")
		#print("Unexpected error:", sys.exc_info()[0])
	
# Delete an event from the event list by event title
def deleteEvent(*args):
	try:
		eventFound = False
		for event in list(eventList.keys()):
			if args[1] in eventList[event].toString():
				eventList.pop(event)
				eventFound = True
				print("Event deleted.")
		if not(eventFound):
			print("No event \"{}\" found.".format(args[1]))
	except:
		print("Invalid arguments.")

# Print all events
def listEvents(*args):
	for event in eventList.keys():
		print(eventList[event].toString())
		
# Load an event list from a specified file
def loadEvents(*args):
	try:
		fileName = args[1]
	except:
		fileName = input("Enter file name: ")
	loadFile = open(fileName)
	eventList.clear()
	for event in loadFile:
		newEvent = events.CalendarEvent(datetime.datetime.now(),"","")
		newEvent.loadFromJsonStr(event)
		print(newEvent.toString())
		eventList.update({newEvent.id : newEvent})
	loadFile.close()
	print("Events loaded!")

# Save the event  list to a specified file
def saveEvents(*args):
	try:
		fileName = args[1]
	except:
		fileName = input("Enter file name: ")
	saveFile = open(fileName, "w")
	for event in list(eventList.keys()):
		saveFile.write(eventList[event].toJson() + "\n")
	print("Event(s) saved!")
	
# Set the month to be displayed in the calendar
def setDate(*args):
	print("Feature not yet added.")
	
# View events for a specified date
def viewEvents(*args):
	print("Feature not yet added.")
	

clearScreen()
printCalendar()
print("Welcome to Menu Calendar!")
print("This is a menu-based program. Enter \"help\" for more information.")
control = input("\nPlease enter a command: ").split()
command = control[0].upper()
while command not in commandDict["QUIT"][0]:
	clearScreen()
	if command not in (commandDict["HELP"][0] + commandDict["QUIT"][0]):
		printCalendar()
	if command in commandDict["HELP"][0]:
		print("Commands:")
		for command in commandDict:
			print(" {0}".format(command))
			print("   {0}".format(commandDict[command][1]))
			print("   Alternates: {0}".format(commandDict[command][0]))
	elif command in commandDict["ADD"][0]:
		addEvent(*control)
	elif command in commandDict["DELETE"][0]:
		deleteEvent(*control)
	elif command in commandDict["LIST"][0]:
		listEvents(*control)
	elif command in commandDict["LOAD"][0]:
		loadEvents(*control)
	elif command in commandDict["SAVE"][0]:
		saveEvents(*control)
	elif command in commandDict["SETDATE"][0]:
		setDate()
	elif command in commandDict["VIEW"][0]:
		listEvents(*control)
	elif command in commandDict["QUIT"][0]:
		break
	else:
		print("Invalid command. Enter \"help\" for more information.")
	control = input("\nPlease enter a command: ").split()
	command = control[0].upper()
	
clearScreen()