import re

mystr = '''Tata Motors Logo.svg
Formerly	Tata Engineering and Locomotive Company Ltd. (TELCO)
Type	Public
Traded as	
BSE: 500570
NSE: TATAMOTORS
NYSE: TTM
NSE NIFTY 50 Constituent
ISIN	IN9155A01020
Industry	Automotive
Founded	1945; 77 years ago
Founder	Jehangir Ratanji Dadabhoy Tata
Headquarters	Mumbai, Maharashtra, India[1]
Area served	Worldwide
Key people	
Natarajan Chandrasekaran (Chairman)

Martin Uhlarik (CDO)
Products	
Automobiles
Luxury vehicles
Commercial vehicles
Automotive parts
Pickup trucks
SUVs
Production output	Increase 1.1 Million (approx) (2021)
Services	
Automotive finance
Vehicle leasing
Vehicle service
Revenue	Increase ₹281,507 crore (US$35 billion) (2022)[2]
Operating income	Increase ₹−7,003 crore (US$−880 million) (2022)[2]
Parent	Tata Group
Divisions	Tata Motors Cars
Subsidiaries	
Tata Daewoo
Jaguar Land Rover
Tata Technologies
Tata Hispano
Tata Hitachi Construction Machinery
Tata Passenger Electric Mobility
Website	www.tatamotors.com'''

# findall,search,split,sub,finditer

# patt = re.compile(r'Public')
# patt = re.compile(r'.ct')
# patt = re.compile(r'^T')
# patt = re.compile(r'm$')
patt = re.compile(r'ai*')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
