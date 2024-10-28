FROM eclipse-temurin:17

EXPOSE 8080

WORKDIR /app

COPY Exercise1 .

# Set the gradlew script as executable
RUN chmod +x gradlew

RUN ./gradlew clean build

CMD java -jar build/libs/NotesService-0.1.0.jar

# run with 'docker run -p 8080:8080 exercise1:latest'