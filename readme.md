<!-- create 3 apps -->
# Driver
# Car
# Race
# add apps to project settings

<!-- create superuser -->

<!-- create Driver DB -->
# Name
# Country
# Car (FK - Car)
# Score
# Standing


<!-- create Car DB -->
# Name
# Drivers 
# Score
# Standing 


<!-- create Race DB -->
# race_name
# standing
# fastest_driver (FK - Driver)
# race_type
# race_date

<!-- create Standing_in_race DB (in Race app) -->
# driver (FK - Driver)
# race (FK - Race)
# standing

<!-- create static folder  -->
# add what necessary in setting.py
# add what necessary in urls.py

<!-- create views for Driver -->
# create list of all drivers and all_drivers path in urls (via drivers.html)
# create single driver template and <pk> path in urls (via single_driver.html)
# create edit and delete for each driver and <pk> edit/delete path in urls (via edit_driver.html)
# create driver standing by score and driver_standing path in urls (via standing.html)

<!-- create views for Car -->
# create points calculation by car (take it from drivers score) 
# create car standing by score and car_standing path in urls

<!-- create views for Race -->
# create list of standing in each race and all_races path in urls (via races.html)
# create update_fast_driver_score function to add 1 point for the fastest driver
# create add race, add race action and urls for both (use Form with add_rave.html)
# create add standing, add standing action and urls for both (use Form with addstanding.html)
# create update_driver_score function to calculate points for each driver and update driver.score in DB