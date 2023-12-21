import sys
import urllib.request as req
import urllib.parse as parse

if len(sys.argv) <= 1:
    print("")
    sys.exit()
    
regionNumber = sys.argv[1]
addr = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {'stnId' : regionNumber}
params = parse.urlencode(values)
url = addr + "?" + params

data = req.urlopen(url).read()
text = data.decode('utf-8')
print(text)