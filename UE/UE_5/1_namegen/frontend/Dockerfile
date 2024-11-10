FROM node:lts

#EXPOSE 8080

WORKDIR /app

COPY web .

# Set the gradlew script as executable
#RUN chmod +x gradlew

RUN npm install

CMD node app.js

# run with 'docker run -p 8080:8080 exercise1:latest'