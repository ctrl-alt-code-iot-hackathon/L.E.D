import time
import requests
import json
import datetime
import math 
import re
from matplotlib import pyplot as plt
import numpy

def speed(lat1, long1, lat2, long2, hr1, min1, sec1, hr2,min2, sec2):
   
    la1 = (math.pi/180)*int(lat1)
    la2 = (math.pi/180)*int(lat2) 
    lo1 = (math.pi/180)*int(long1)
    lo2 = (math.pi/180)*int(long2) 
    r = 6378100 
    
    rho1 = r * math.cos(la1)
    z1 = r * math.sin(la1)
    x1 = rho1 * math.cos(lo1)
    y1 = rho1 * math.sin(lo1)

    rho2 = r * math.cos(la2)
    z2 = r * math.sin(la2)
    x2 = rho2 * math.cos(lo2)
    y2 = rho2 * math.sin(lo2)

    dot = (x1*x2)+(y1*y2)+(z1*z2)
    cos_theta = dot/(r*r)
    theta = math.acos(cos_theta)
    distance = r * theta

    tim1 = (hr1*3600)+(min1*60)+sec1
    tim2 = (hr2*3600)+(min2*60)+sec2
    del_t = tim2-tim1 
    speed_ms = distance/del_t
    speed_km = speed_ms*(18/5) 
    return speed_km




def location():
    send_url = "http://api.ipstack.com/check?access_key=d80038576f0bb466b424cd92872cfb9f"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    city = geo_json['city']
    current = datetime.datetime.now()
    hour = current.hour
    minu = current.minute
    seco = current.second
    loc = [latitude,longitude,hour,minu,seco]
    l = ""
    for i in range(len(loc)):
        l = l+str(loc[i])+' '
    print(l)
    fh = open('location.txt','a')
    fh.write(l)


reg_no = 'UP64K9696' #Vehicle Registration Number (varies from vehicle to vehicle)
#vehic_type = input('Enter type of Vehicle: "a" for vehicle with upto 7 passengers,"b" for more than 7 passengers,"c" for transport of goods","d" for motor vehicles')
#road = input('Enter the type of road: "1" for Highway, "2" for municipal road')


spd_list=[]
for i in range(10):
    for j in range(2):
        location()
        time.sleep(10)


    fh = open('location.txt')
    lin = fh.read()
    l = lin.split()
    #print(l)
    ls = []
    for i in range(len(l)):
        ls.append(float(l[i]))
    fh = open('location.txt','w')
    fh.write('')
       
    
    lat1 = ls[0]
    long1 = ls[1]
    hr1 = ls[2]
    min1 = ls[3]
    sec1 = ls[4]
    lat2 = ls[5]
    long2 = ls[6]
    hr2 = ls[7]
    min2 = ls[8]
    sec2 = ls[9]
    spd = speed(lat1,long1,lat2,long2,hr1,min1,sec1,hr2,min2,sec2)
    spd_list.append(spd)
tem = ""
for i in range(len(spd_list)):
    tem = tem+str(spd_list[i])+' '
#print(l)
fh = open('Speed_List.txt','a')
fh.write(tem)

print(spd_list)
y = numpy.array(spd_list)
x = numpy.array([20,40,60,80,100,120,140,160,180,200])
plt.plot(x,y)
plt.xlabel('Time')
plt.ylabel('Speed')
plt.title('Speed Variation')
plt.show()

    















