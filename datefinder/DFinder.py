import re

monthvalues = {	1:['Jan.','Jan','January','1','01'],
				2:['Feb.','Feb','February','2','02'],
				3:['Mar.','Mar','March','3','03'],
				4:['Apr.','Apr','April','4','04'],
				5:['May','5','05'],
				6:['June','6','06'],
				7:['July','7','07'],
				8:['Aug.','Aug','8','08'],
				9:['Sept.','Sept','9','09'],
				10:['Oct.','Oct','10'],
				11:['Nov.','Nov','11'],
				12:['Dec.','Dec','12']
				}
#monthstring contains the 'Jan.','Jan',etc.
monthstring=[]
def makemonthstring():
	for x in monthvalues.keys():
		for y in x:
			monthstring.append(y)


#date for __/__/____
regex1='(\d{1,2}\/\d{1,2}\/\d{4})'
#date for __/__/__
regex2='(\d{1,2}\/\d{1,2}\/\d{2}'
#date for __-__-____
regex3='(\d{1,2}-\d{1,2}-\d{4}'
#date for __-__-__
regex4='(\d{1,2}-\d{1,2}-\d{2}'
#date for January __,____
regex5=''
#Not really sure how to do this one


dates = []
#this will read all the regex's into outside list
#data is the string of data gotten from the google search
def analyzedata(data):
	#run through all the regex's
	a = re.findall(regex1,data,flags = 0)
	b = re.findall(regex2,data,flags = 0)
	c = re.findall(regex3,data,flags = 0)
	d = re.findall(regex4,data,flags = 0)
	#e = re.findall(regex5,data,flags = 0)
	dates = a+b+c+d

translateddates = []
#uses the monthvalues to convert all the data into one format
#not sure how to complete this function
def translatedata():
	for x in dates:
		for y in range(12):
			#convert using the monthvalues to one format that's going to be read by readdata()	

finaldata={}
def readdata():
	for x in translateddates:
		if x in finaldata.keys():
			finaldata[x]=finaldata[x]+1
		else:
			finaldata[x]=1

def giveanswer():
	max = 0
	answer = ""
	for x in finaldata.keys():
		if finaldata[x]>max:
			answer = x
			max = finaldata[x]
	return answer

if __name__=="__main__":
	makemonthstring()
	analyzedata("data from the google change this later")
	translatedata()
	readdata()
	giveanswer()