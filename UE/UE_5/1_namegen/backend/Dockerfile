FROM mcr.microsoft.com/dotnet/core/sdk:3.0

#EXPOSE 8080

WORKDIR /app

COPY namegen .

# Set the gradlew script as executable
#RUN chmod +x gradlew

RUN dotnet build

CMD dotnet run --urls "http://0.0.0.0:5000" 

# run with 'docker run -p 8080:8080 exercise1:latest'