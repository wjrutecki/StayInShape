# CalendarEventClasses
# Classes for Challenge 2

import datetime
import calendar
import uuid
import json

class CalendarEvent:
	def __init__(self,dateTime,name,description):
		self.id = uuid.uuid4().hex
		self.dateTime = dateTime
		self.name = name
		self.description = description
		
	def setDateTime(self, dateTime):
		self.dateTime = dateTime
		
	def setName(self, name):
		self.name = name
		
	def setDesc(self, description):
		self.description = description
		
	def toString(self):
		return "{} - {}: {}".format(self.dateTime.strftime("%Y-%m-%d at %H:%M"), self.name, self.description)
		
	def toJson(self):
		return json.dumps(self.__dict__, default=str)
	
	def loadFromJsonStr(self, jsonStr):
		newValues = json.loads(jsonStr)
		self.id = newValues["id"]
		try:
			self.dateTime = datetime.datetime.strptime(newValues["dateTime"],"%Y-%m-%d %H:%M:%S.%f")
		except ValueError:
			self.dateTime = datetime.datetime.strptime(newValues["dateTime"],"%Y-%m-%d %H:%M:%S")
		self.name = newValues["name"]
		self.description = newValues["description"]
		

# cDate = datetime.datetime.now()
# test = CalendarEvent(cDate,"Test","Test event.")
# print(test.toJson())

# test.loadFromJsonStr("{\"id\": \"39a2e8c0cd944f6b9826e25b50ed4094\", \"dateTime\": \"2020-02-24 12:0:00.000000\", \"name\": \"Test\", \"description\": \"Test event.\"}")
# print(test.toString())