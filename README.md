# Endocode Academy learning project
 Learning project with following requirements.
1. Create an application to find the results from wikipedia (title, image(s),
description) for any search queries. Store all the information in google
cloud (using appropriate storage option(s)). Future queries should return
the data from storage instead of searching wikipedia again.
2. Deploy the application in google cloud, using the execution environment
of your choice. (Tip: create a functional web interface to interact with
your application - aesthetics doesn’t matter).

## Pre requisites

The project currently assumes that infrastructure is set up separately. A GCP project with a vm instance( that runs the application),
a cloud sql database instance with postgresql and users set up. A cloud storage bucket to store the images. APIs enabled and networking set up.

## Running the app


## TBD

Automate creation of infrastructure.

Find better ways to handle authorization and passwords other than environment variables.

Create a table with foreign key relationship to main table to store image links than selecting one image now.

