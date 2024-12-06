# interview_sample_projects
#  Problem statement: Need to find average speed based on above data?
# ------------------------------------------------------------------

# Input Data:
# ------------------------------------------------------------------
Duration		Speed Km/h
------------------------------------
1 Minute - 4 Minute	2
4 Minute - 7 Minutes	4
7 Minute - 11 Minute	5
11 - 14 Minute		6
14 - 18 Minutes		5
18 - 20 Minutes		2


# Approach: 
# -------------
1. First get the distancetravelled based on speed and time 
2. Calculate Total Distance and Total Speed
3. Then calculate avg speed.

To find distance based on time and speed, you can use the formula:           
Distance = Time * Speed			

TotalTimeTaken = Subtract the lower range from upper range Duration and then sum it up

To find average speed based on duration, you can use the formula:           
AverageSpeed = TotalDistanceTraveled / TotalTimeTaken

	

Duration	Speed Km/h	distance	Total Distance	Total Time	Avg Speed
3		2		6		80		19		4.2105263157894735
3		4		12			
4		5		20			
3		6		18			
4		5		20			
2		2		4			

			
										
