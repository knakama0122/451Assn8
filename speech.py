import speech_recognition as sr
import distance
import os

class Speech:
	def __init__(self):
		self.original = []
		self.recognized = []
		self.similarity = []

	def read_original(self, inFile):
		f = open(inFile, "r")
		self.original = f.readlines()
			

	def conv_audio(self, inDir):
		self.recognized.clear()
		r = sr.Recognizer()

		for i in range(24):
			audio = sr.AudioFile(inDir + "-Sent" + str('{0:0>2d}'.format(i+1)) +".wav")
			with audio as source:
				audio = r.record(source)
			self.recognized.append(r.recognize_google(audio))
			print("sentence ", i , "read")
		
	def comp_string(self):
    	self.similarity.clear()
		for i in range(24):
			self.similarity.append(distance.levenshtein(self.original[i].split(), self.recognized[i].split()))
		

if __name__ == '__main__':
	speech = Speech()
	print("reading text")
	speech.read_original("How Speech Recognition Works.txt")
	print("reading and converting audio")
	speech.conv_audio(os.getcwd() + "/Audio/09-Spanish-male/09-Spanish-male")
	print("comparing text and audio")
	speech.comp_string()
	print(speech.similarity)
	speech.conv_audio(os.getcwd() + "/Audio/05-English-female/05-English-female")
	print("comparing text and audio")
	speech.comp_string()
	print(speech.similarity)
	speech.conv_audio(os.getcwd() + "/Audio/13-Bengali-male/13-Bengali-male")
	print("comparing text and audio")
	speech.comp_string()
	print(speech.similarity)
