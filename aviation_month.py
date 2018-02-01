import urllib2
from lxml import etree
from xml.dom.minidom import parse
import xml.dom.minidom



url = "https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&startTime=2017-06-25T00:00:00Z&endTime=2017-06-25T22:30:00Z&stationString=SKRG"

s = urllib2.urlopen(url)
contents = s.read()
file = open("export.xml", 'w')
file.write(contents)
file.close()  
DOMTree = xml.dom.minidom.parse("export.xml")



data = DOMTree.documentElement
if data.hasAttribute("num_results"):
   print "Number of readings %s" % data.getAttribute("num_results")

# Get all the movies in the collection
metardata = data.getElementsByTagName("METAR")
  
# Print detail of each movie.
for METAR in metardata:
   print "RAW DATA"
   text = METAR.getElementsByTagName('raw_text')[0]
   print "Text: %s" % text.childNodes[0].data
   with open("today_medellin.txt", "a") as text_file:
       text_file.write(text.childNodes[0].data + "\n")
















 




      
 

	
