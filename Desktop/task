Decision point 1 : Establishing correct transit-time between O-D pairs
	
	step 1:
		Get the data from data-warehouse using async call (cron job) or (tasks) basis date range (example 2nd sep - 10 sep)
		and create the entry in our table.
		route_schedule_uuid can be considered as primary key for our implementation
	step 2:
		Calculating in transit or past travel time for ORIGIN - DESTINATION pair	
	step 3:
		Define certain guide line (Matrix) basis vehicle data which we will be getting from FMS(fleet management system) and 			geographycal region (let say A,B,C,D) and vehicle average speed can be considered as 50km/hr for (midmile) line haul movement.
	  
	step 4:
		Writing Util functions for getting expected output (In transit time/ distance of path or route) considering OD pair as input 
	step 5:
		
		Exposing RESTFUL API


Route:
 A > B > C > D
 here (A-D) will be OD pair

		
	
Tech stack
	python-2.7 
	django-(1.11.15)
	postgres - 9.5.14
 	 
