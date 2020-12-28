#!C:\Python27\pythonw.exe
# Arves100's Utility Library (v.1.2 ~ Revolution)

## Changelog
	### 1.0
		#### Initial Build
	### 1.1
		#### Added URLLib and Mega function
	### 1.2
		#### Restylized Module
		#### Added RunFile
		#### Added more Module Info
		#### Fixed Wait-Time

## Examples:
	### Check if you are using Windows:
		#### Utility.OsUtil().IsWin32()
		##### return True when you are using Windows
		##### return False when you are not using Windows

class OsUtil():
	def IsWin32(self):
		import sys
		if sys.platform == "win32":
			return True
		else:
			return False

class PythonUtil():
	def Version(self,major,minor,micro):
		import sys
		mjver = 0
		mnver = 0
		mcver = 0
		try:
			mjver = int(major)
		except:
			raise ValueError
		if not minor == False:
			try:
				mnver = int(minor)
			except:
				raise ValueError
			if not micro == False:
				try:
					mcver = int(micro)
				except:
					raise ValueError
				if sys.version_info[:3] == (mjver,mnver,mcver):
					return True
				else:
					return False
			if sys.version_info[:2] == (mjver,mnver):
				return True
			else:
				return False
		if sys.version_info[0] == (mjver):
			return True
		else:
			return False

class ConsoleUtil():
	def ClearConsole(self):
		import os
		if OsUtil().IsWin32():
			os.system("cls")
		else:
			os.system("clear")

	def Quit(self,status):
		import sys
		print "Premi INVIO per uscire..."
		try:
			raw_input()
		except EOFError:
			pass
		sys.exit(status)

	def SetTitle(self,title):
		if OsUtil().IsWin32():
			import os
			os.system("title " + title)
		else:
			import sys
			sys.stdout.write("\x1b]2;" + title + "\x07")

class FileUtil:
	def ReadLineByURL(self,url):
		import urllib2
		data = urllib2.urlopen(url)
		return data
		
	def ReadLineByFile(self,filename,num):
		rtn1 = ""
		var1 = 1
		tmp1 = open(filename,"r")
		for line in tmp1:
			if var1 == num:
				rtn1 = line
				break
			var1 = var1 + 1
		tmp1.close()
		return rtn1

	def WriteFile(self,filename,text):
		f = open(filename,"w")
		f.write(str(text))
		f.close()

	def AppendFile(self,filename,text):
		f = open(filename,"a")
		f.write(str(text) + "\n")
		f.close()

	def RemoveFile(self,filename):
		import os
		if OsUtil().IsWin32():
			os.system("del " + filename + ">nul 2>&1")
		else:
			os.system("rm -rf " + filename)

	def CheckFile(self,filename):
		import os
		if os.path.isfile(filename):
			return True
		else:
			return False

	def CheckDirectory(self,dirname):
		import os
		if os.path.isdir(dirname):
			return True
		else:
			return False

	def DownloadFileFromMega(self,url):
		from mega import Mega
		m = Mega.from_ephemeral()
		try:
			m.download_from_url(url)
		except:
			return False
		return True

	def DownloadFile(self,url,savefile):
		import urllib
		urllib.urlretrieve(url,savefile)

## TODO
'''def RunAppWithExitcode(app,elevate):
	if os.system(app) == 0:
		return True
	else:
		return False

def RunAppWithArgs(app,arg,elevate):
	if elevate == True:
		if not os.system("Powershell") == 0:
			print("Powershell e\' richiesto per l'avvio di app come administratore!\nDisabilita l'UAC o installa Powershell\nWindows XP:https://www.microsoft.com/it-it/download/details.aspx?id=9591\nWindows Vista:https://www.microsoft.com/it-it/download/details.aspx?id=9864")
			Quit(1)
		subprocess.call("powershell Start-Process \"" + app + )
		subprocess.call([app,arg1])

def RunAppWithNoArgs(app):
	subprocess.call([app,""])'''

class INIUtil():
		def ReadStringByIni(self,section,value,ini):
			import ConfigParser
			config = ConfigParser.RawConfigParser()
			try:
				config.read(ini)
			except:
				print("Impossibile leggere l'INI " + ini)
				ConsoleUtil().Quit(1)
			return config.get(section,value)

		def ReadBooleanByIni(self,section,value,ini):
			import ConfigParser
			config = ConfigParser.RawConfigParser()
			try:
				config.read(ini)
			except:
				print("Impossibile leggere l'INI " + ini)
				ConsoleUtil().Quit(1)
			return config.getboolean(section,value)

		def ReadIntByIni(self,section,value,ini):
			import ConfigParser
			config = ConfigParser.RawConfigParser()
			try:
				config.read(ini)
			except:
				print("Impossibile leggere l'INI " + ini)
				ConsoleUtil().Quit(1)
			return config.getint(section,value)

		def ReadFloatByIni(self,section,value,ini):
			config = ConfigParser.RawConfigParser()
			try:
				config.read(ini)
			except:
				print("Impossibile leggere l'INI " + ini)
				ConsoleUtil().Quit(1)
			return config.getfloat(section,value)

def Version():
	return 1.2

def NameVersion():
	return "Revolution"

def Author():
	return "Arves100"
