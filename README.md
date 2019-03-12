# Vehicle Speed Data Collection and Visualisation

Overspeeding is one of the major causes of motor accidents. While educating drivers about the dangers of overspeeding can work, a more 
concrete method to prevent accidents is to upgrade stretches of roads where the average speed is higher based on accurate speed data.
This Vehicle Speed Data Collection and Visualisation system acurately and continuously monitors the location and speed of a vehicle and 
visualises the data. 

<b>Program Structure</b>

1. Find the location of the vehicle of interest once every 10 seconds, for 200 seconds using an IP address to location api.
2. Find the timestamp every time the location is calculated.
3. Use two subsequent location vectors and the time difference to calculate the speed.
4. Draw a simple graph between speed and time.
5. Store the list of speeds for several vehicles in a text file. 
6. Use the speed data from multiple vehicles to plot a graph showing the average speed in the stretch of road. 
