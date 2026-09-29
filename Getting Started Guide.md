***

# GETTING STARTED GUIDE – PASSWORD AUDITOR PROJECT

**Author:** Harsh Patel  
**Course:** IT610:851 – NJIT  
**Project:** Docker-Based Password Auditor

***

## Overview

The Password Auditor checks password strength against several defined complexity rules based on **NJ State SISM Policy** which I have used for the project, then generates an HTML report.  
It runs fully in Docker — *no Python installation required.*

***

## Requirements

* Docker Desktop (Windows/macOS/Linux)
* Terminal/Powershell access
* Permission to mount volumes
* Project structure:

```


```

The `output` directory and the `Password_Audit_Report.html` file will be automatically generated once the Docker image is built and ran successfully.

***

## Password Rules

A password is **VALID** only if it meets **ALL** the requirements below:

* 8–14 characters
* At least one uppercase
* At least one lowercase
* At least one digit
* At least one special character
* Does **NOT** contain username
* No 5+ consecutive letters
* No 5+ consecutive digits
* No character repeated 3+ times consecutively

***

## Build the Docker Image

```
cd path/to/password-auditor-project/scanner    (CHANGE YOUR PATH ACCORDINGLY)

docker build -t password-auditor .
```

**This command creates a Docker image for the project.**


***

## Run the Auditor

```
docker run -it --entrypoint bash -v ${PWD}/output:/output password-auditor

```

*This command runs a container from the image built above.*

When inside the container run the script manually
python /scanner/password_auditor.py

Enter username/password when prompted

Report will save to /output (mounted to your Windows folder)



  This allows the report file generated inside the container to appear on your PC.



You will be prompted to enter a username and a password which will be hidden on the screen.


Exit the container
When you're done, exit the shell to stop the container.

Inside the container:

Type exit or press Ctrl+D


***

## View Your HTML Report

Open:

```
output/Password_Audit_Report.html
```

The report will include the following:

* Username
* Argon2 hashed password
* Weak/Strong status
* Failed rules
* Timestamp

The file updates on each run. On the first run, a new HTML file is generated.

***

## Troubleshooting Tips


* **No report generated:** Check volume mount
  ```
  -v ${PWD}/output:/output
  ```

* **Build too fast (cached)??:**
  ```
  docker build --no-cache -t password-auditor ./scanner
  ```
* **Things to remember:**
  ```
  Make sure your inside the correct working directory when running the Docker commands.

  path/to/password-auditor-project

  Do NOT run the commands from inside the scanner or output directory. It will NOT work. 

  ```
***

## Best Practices

* Use for onboarding user accounts and/or for periodic password audits
* Store reports securely
* Address weak passwords promptly
* Archive reports regularly
* Never share hashed passwords publicly

***
