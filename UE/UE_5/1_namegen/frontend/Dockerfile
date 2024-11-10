FROM node:lts

#EXPOSE 8080

WORKDIR /app

COPY web .

# Set the gradlew script as executable
#RUN chmod +x gradlew

RUN npm install

CMD node app.js