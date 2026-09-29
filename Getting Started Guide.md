***

# GETTING STARTED GUIDE – PASSWORD AUDITING

**Author:** Harsh Patel  
**Course:** IT610:851 – NJIT  
**Project:** Docker-Based Password Auditor

***

## Overview

The Password Auditor checks password strength against several defined complexity rules based on **NJ State SISM Policy** which i have used for the project, then generates an HTML report.  
It runs fully in Docker — *no Python installation required.*

***

## Requirements

* Docker Desktop (Windows/macOS/Linux)
* Terminal/Powershell access
* Permission to mount volumes
* Project structure:

```
password-auditor-project/
├── output/
│   ├── Password_Audit_Report.html   (Automatically Generated)
└── scanner/
    ├── Dockerfile
    └── password_auditor.py
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
cd path/to/password-auditor-project

docker build -t password-auditor ./scanner
```

**This command creates a Docker image for the project.**

**Breakdown:**

* **docker build**  
  Tells Docker to create (build) an image.

* **-t password-auditor**  
  Tags the image with the name `password-auditor`.

* **./scanner**  
  Directory containing the Dockerfile and Python script.

Docker looks inside this folder for:

* **Dockerfile**
* **password\_auditor.py** (copied into the image)

***

## Run the Auditor

```
docker run -it --rm -v ${PWD}/output:/output password-auditor
```

*This command runs a container from the image built above.*

**Breakdown:**

* **docker run**  
  Starts a new container instance.

* **-it**
  * `-i` = interactive mode
  * `-t` = terminal mode  
    Allows the script to prompt for username/password.

* **--rm**  
  Deletes the container automatically after completion.

* **-v ${PWD}/output:/output**  
  Volume mount linking your local `output` folder to the container’s `/output` directory.

  This allows the report file generated inside the container to appear on your PC.

* **password-auditor**  
  The name of the image created previously.

You will be prompted for username and a hidden password input.

***

## View Report

Open:

```
output/Password_Audit_Report.html
```

The report includes:

* Username
* Argon2 hashed password
* Weak/Strong status
* Failed rules
* Timestamp

The file updates on each run. On the first run, a new HTML file is generated.

***

## Troubleshooting


* **No report generated:** Check volume mount
  ```
  -v ${PWD}/output:/output
  ```

* **Build too fast (cached):**
  ```
  docker build --no-cache -t password-auditor ./scanner
  ```
* **Things to remember:**
  ```
  Make sure your inside the correct working directory when running the Docker commands.

  path/to/password-auditor-project

   Do NOT be inside the scanner or output directory.

  ```
***

## Best Practices

* Use for onboarding user accounts or periodic password audits
* Store reports securely
* Address weak passwords promptly
* Archive reports regularly
* Never share hashed passwords publicly

***
