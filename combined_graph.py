from matplotlib import pyplot as plt
import numpy

fh = open('Speed_List.txt','r')
st = fh.read()
st= st.split()
temp = [] 
for i in range(len(st)):
    temp.append(float(st[i]))

y = numpy.array(temp)

temp2 = []
for i in range(len(temp)):
    temp2.append(i)

x = numpy.array(temp2)

plt.plot(x,y,linestyle='--', marker='o', color='b')
plt.xlabel('time')
plt.ylabel('Speed')
plt.title('Speed Variation')
plt.show()





