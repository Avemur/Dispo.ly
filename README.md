# Dispo.ly
Submission to TreasureHacks 2.0.

## Inspiration 
Within many high schools, including our own have compost clubs which aim to lessen their schools carbon foot print through various means such as planting gardens, recycling programs, or itemized bins in the cafeteria for compostables, recyclables, or trash. To help make sure people put items in the right bins, there is a need for volunteers to stand by them and make sure people put everything in the correct places. We wish to eliminate and/or reduce the number of volunteers needed with a web app using machine learning.

## What it does
Dispo.ly, takes in a file input from a folder, and uses machine learning via tensor flow to analyze the photo and determine if its a compostable, recyclable, or trash, outputted on the web page.

## How we built it
We built, Dispo.ly, through using Flask, TensorFlow, BootStrap, CompostNet's dataset. The front end comprises of two web pages, one to run the ML, and another to display the results of the ML algorithm. 

## Challenges we ran into
During the process of making it, we ran into the major issue of direct file upload from the website not working due to an issue with php. A few other challenges that we had to effectively pass through the image into the ml algorithm, which gave some difficulties, but was nonetheless solved and how to effectively implement a database to store uploaded images, which we scrapped all together in favor of the faster(faster for the lunchroom use case) method of storing the image under a folder of our project file.

## Future plans
We plan on making the web app have a live camera feed, identifying the best waste management solution for a given item in real time, eliminating the need for any real user input apart from pointing the object at the camera. Additionally, a custom 3d printed enclosure for school tablets to be in to safely scan the objects would useful. 
