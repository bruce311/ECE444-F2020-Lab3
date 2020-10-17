# ECE444-F2020-Lab4&5

this repo is a clone of
https://github.com/miguelgrinberg/flasky

### Activity 2

Navigate to the directory root folder to build the docker image with the command:

`docker build -t lab4:latest .`

Then run a docker container based on this image, set the local host port to 5000:

`docker run -p 5000:5000 lab4`

Here is the terminal screenshot
![docker command](https://github.com/bruce311/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/screenshots/docker%20commands.png)

Go to http://0.0.0.0:5000 to check out the deployed app with docker container
![deployed page](https://github.com/bruce311/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/screenshots/deployed%20page.png)

Docker desktop app:
![docker app](https://github.com/bruce311/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/screenshots/docker%20app.png)

Docker image:
![docker image](https://github.com/bruce311/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/screenshots/docker%20image.png)


### Activity 3
A virtual machine is like a separate computer running on the host computer. It occupies part of the operation system and hardware resources with the host computer for each of its running application. It's good for running applications that require lots of OS resources

A docker container virtualizes the operating system and it sits on top of a physical server and its host OS. Essentially it shares the same OS among different applications, making it lightweight and easily scalable.