INSTRUCTIONS:-

1. Unzip the file provided and run it on visual studio code
2. Make sure you are in the correct root directory i.e medicine
3. Set up a python virtual environment and run the following command

"pip install -r requirements.txt"

4. after all the requirements are installed
run
"python manage.py runserver"
5. Press ctrl + click on local host server to launch the application

NOTE:-
if you face any error during running server. make sure to recheck your current directory
you can run the following commands to ensure clear migrations

"python manage.py makemigrations"
"python manage.py migrate"



SIDE INFORMATION TO HELP YOU ACCESS YOUR FILES
The whole project is divided into two main apps
1. Medicine
2. Recommendation

The reason for two different apps is because this is the standard procedure of django to divide your project into multiple apps to keep all the related modules confined and perform low cohesion and high coupling. 

If you want to access your:
1. Driver code (replicated by your main.py in flask) -> recommendation/views.py
2. HTML files -> recommendation/templates/recommendation
3. The svc.pkl -> models/
4. Medicine Recommendation System.ipynb-> ip/
5. Datasets -> datasets/

Make sure to understand Django procedures and how the static and installed apps are defined in settings.py before moving forward.
Let me know if you face any issues
ENJOY!

