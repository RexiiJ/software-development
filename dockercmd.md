Command to see hidden files
ls -lart  
# To build docker image
# Mkae sure you have created your docker file
# Mkae sure your docker dexktop is up and running
# Get the list of docker images locally
 $ docker images
 $ docker images -a
# Comand to build your image
 $ docker build -t feyiimage .

  docker rmi image seunimage
# ======================================================================================================
# Apply force to delete 1st, 2nd, 3rd, 4th
 $ docker images purge
 $ docker images prune
 # powerful ones
 $ docker image prune --all --force
 $ docker rmi -f $(docker images -aq)

# ============================================================================================================
# To build docker container image
 $ docker run --name feyi-container -dp 5004:5004 feyiimage
 $ bb0b75a1d3161ed96649fe7cf1b83b0a047def89b1c24892583913a46a2a34f6

# To check the list of containers
 $ docker ps
CONTAINER ID   IMAGE       COMMAND              CREATED          STATUS                             PORTS                    NAMES
bb0b75a1d316   feyiimage   "python ./main.py"   36 seconds ago   Up 35 seconds (health: starting)   0.0.0.0:5004->5004/tcp   exciting_poitras

# To remove unused images and containers
 $ docker system prune

# To remove containers
 $ docker rm -vf $(docker ps -a -q)

===== Creating and stopping docker container ================= 11/6/2024
# Command to check for running and unrunning containers
 $ docker ps
# command to check for unrunning container
 $ docker ps -a

# command to stop a running container
 $ docker stop feyi-container

======= Building docker images and pushing to docker hub============== 11/6/2024
# Always attach your docker hub username while building the images and always put a tag
 $ docker build -t feyidocker/rainbowimage:1.0 .
 $ docker login

# To create and  push an image to docker hub
 $ docker run --name rainbow-container -dp 5004:5004 feyidocker/rainbowimage:1.0
 $ docker push feyidocker/rainbowimage:1.0