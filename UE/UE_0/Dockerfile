# FROM load the specified image from docker hub
FROM ubuntu:20.04

# RUN executes the following linux command
# update package list
RUN apt-get update 
# download compiler, -y auto accepts the installation
RUN apt-get install -y g++

#or RUN apt-get update && apt-get install -y g++

# set the working directory
WORKDIR /root

# copy the file into the docker container
COPY main.cpp .

# compile the executable
RUN g++ main.cpp -o namegen

# execute the compiled program
CMD ./namegen