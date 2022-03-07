# Immfly Media Platform Project

## Installation

1. Copy docker.txt and paste it to the same path as docker.env (or just rename the file to docker.env)
2. You can change secret_key if you would like to.
3. Run command:

        docker-compose up -d --build

    You can tail the logs:

        docker-compose logs --follow app_immfly

4. Default superuser will be created by itself. You can login with the credentials based on parameters in docker.env:
   
       DJANGO_SUPERUSER_PASSWORD
       DJANGO_SUPER_USERNAME
       DJANGO_SUPER_USER_EMAIL

## About

- Non of services are using default ports to not have conflict if you have running another services on those ports.

   > Database (Postgres): 5438

   > Backend (Django): 8008

   So requests must be sent to: http://localhost:8008/

