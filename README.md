# bewise.ai_testw
## Junior Python Dev - Test Task for bewise.ai

**Project Description:** This project is a test task for the Junior Python Developer position at bewise.ai. The project consists of two tasks, each requiring the development of a web service using various technologies and tools.

## Installation:

1. Clone the repository:
```bash
git clone https://github.com/richardmaxwell2001/bewise.ai_testw.git
```
2. Navigate to the project directory:
```bash
cd bewise.ai_testw
``` 
3. Allow execution of the `Makefile`:
```bash
chmod +x Makefile
``` 
4. Build the project using the following command:
```bash
make build
```
5. Now you have two ways to run the application:

    + Standard mode: Run the application using the following command:
        ```bash
        make run
        ```
    + Test mode: Run the application and perform additional tests to verify its functionality. Use the following command:
        ```bash
        make run_test
        ```


## Usage
### Make
+ `check-docker`: Checks if Docker is installed.
+ `build`: Builds the project.
+ `run`: Runs the project.
+ `run_test`: Runs the project and tests.
+ `stop`: Stops the project.
+ `stop_clear_db`: Stops the project and clears the database. > :warning: **Attention:** Data Loss!
+ `clear_docker`: Clears Docker resources. > :warning: **Attention:** Data Loss!


#### Target Details
##### `check-docker`

This target checks if Docker is installed. If Docker is not installed, it displays an error message and exits.
##### `build`

This target builds the project using docker-compose.yml.
##### `run`

This target will start the database in normal mode.
##### `run_test`

This target will start the database in normal mode and run 2 tests: the first one inside the QA container and the second one using curl requests from the system.
##### `stop`

This target stops the running project using docker-compose.
##### `stop_clear_db` > :warning: **Attention:** Data Loss!

This target stops the project and prompts for confirmation to proceed with clearing the database. If confirmed, it clears the database by removing the docker_tut_db Docker volume.
##### `clear_docker` > :warning: **Attention:** Data Loss!

This target stops the project, clears the database, and removes any unused Docker resources using docker system prune -af.

Feel free to use these targets as per your requirements.



### Task 1

To populate the database with a specified number of random questions using the `https://jservice.io/api/random` API, execute the following command:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"questions_num": <desired_questions_num>}' http://localhost/task_1
```

The server will respond with the latest question stored in the database:

```json
{
  "answer_text": "mango tango",
  "creation_date": "Fri, 30 Dec 2022 19:20:03 GMT",
  "question_id": 92784,
  "question_text": "Exotic dance for the exotic fruit seen here"
}
```

<br>

### Task 2

#### User Registration

To register a new user with a desired username, execute the following command:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "<desired_username>"}' http://localhost/task_2/new_user
```

The server will respond with an access token and the user ID:

```json
{
  "access_token": "<access_token>",
  "user_id": <user_id>
}
```

#### Audio File Upload

To upload a WAV file to the server using the registration data, execute the following command:

```bash
curl -F 'Access_token=<access_token>' -F 'User_id=<user_id>' -F "audio=@<wav_file_path>" http://localhost/task_2/upload_audio
```

The server will respond with a URL from which you can download the MP3 version of the file:

```json
{
  "URL": "<download_url>"
}
```

#### Downloading MP3 File

You can download the file by either opening the provided URL in a browser or using the following curl command:

```bash
curl -o <desired_mp3_file> "<download_url>"
```

