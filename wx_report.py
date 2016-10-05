from lxml import html

def frsn_wx():    
    #Loads 93704 weather forcast page
    page = requests.get('http://bit.ly/2dDCkAt')
    #Loads html xpage content
    tree = html.fromstring(page.content)
    #Takes text value from p class
    temp = tree.xpath('//p[@class="myforecast-current-lrg"]/text()')
    #Convers temp to a string and slices off garbage
    wex = str(temp)[3:5]
    #Converts wex to a integer just incase
    wx = int(wex)
    print ('It is currently {}F in Fresno, Ca'.format(wx))

frsn_wx()
