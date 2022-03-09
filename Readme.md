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

5. **Import Languages**

       docker-compose exec app_immfly python manage.py loaddata languages.json

6. **Create Dummy Data**

       docker-compose exec app_immfly python manage.py setup_test_data

## About

- Non of services are using default ports to not have conflict if you have running another services on those ports.

  > Database (Postgres): 5438

  > Backend (Django): 8008

  So requests must be sent to: http://localhost:8008/

- Contents have *get_age_rate* which presents the maximum appropriate age to reach the content based on genre.

- *get_rating* shows the average rating of contents of channels.

- If you send request with a channel id in *having_parent* parameter to *channels*, it checks the child of sent channel.

    - If any child is exists, channel list comes and **deepest_channel** field comes as False.

    - If there is no child, having_parent id comes as channel, *content_set* will be reachable and **deepest_channel**
      field comes as True.

- Contents can have many people as director, cast or author. Like *get_author_list* field, we can receive list of any
  type of people of content.

## API Documentation

Postman API documentation is created and can be accessible by visiting public urls.

- **Visit Online Documentation:** https://documenter.getpostman.com/view/11424728/UVsFxntV
- **Send Requests Online:** https://www.postman.com/berkaymizrak/workspace/immfly-media-platform-project

**Note:** Be sure you selected the environment *Immfly Environment*

## Exporting Channel Info

There are 2 types of files and 2 ways to export channel info. (Channel title and average rating) 

### 1. CSV

1. Using serializer action:

        http://localhost:8008/api/channels/export/?excel_type=csv

2. Using management command:

        docker-compose exec app_immfly python manage.py export_channels_csv

### 2. XLSX

1. Using serializer action:

        http://localhost:8008/api/channels/export/?excel_type=xlsx

2. Using management command:

        docker-compose exec app_immfly python manage.py export_channels_xlsx

## Continuous Development

docker-compose.yml file has the volume as:

        volumes:
              - static-data:/srv/public
        #      - socket-data:/srv/socket-data
              - .:/srv/app

We use current folder as working directory in container instead socket-data. This makes Django reloading function to be
run itself when we are developing.

On continuous development some commands:

        docker-compose exec app_immfly python manage.py makemigrations
        docker-compose exec app_immfly python manage.py migrate
        docker-compose exec app_immfly python manage.py createsuperuser

However, *entrypoint.sh* will make migrate and createsuperuser steps by itself so no need to run those.

