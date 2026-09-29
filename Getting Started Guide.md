# GETTING STARTED GUIDE – PASSWORD AUDITING

**Author:** Harsh Patel  
**Course:** IT610:851 – NJIT  
**Project:** Docker-Based Password Auditor

## Overview

The Password Auditor checks password strength against several defined complexity rules based on NJ STATE SISM POLICY which I have used and then generates an HTML report. It runs fully in Docker. 
FYI... No additional Python installation is required.

## Requirements

* Docker Desktop (Windows/macOS/Linux)
* Terminal/Powershell access
* Permission to mount volumes
* Project structure:
  ```
  password-auditor-project/
  ├── output/
      ├── Password_Audit_Report.html   (Automatically Generated)
  └── scanner/
      ├── Dockerfile
      └── password_auditor.py
  ```
The output directory and the Password_Audit_Report.html file will be automatically generated once the Docker Image is built and ran successfully. 

## Password Rules

A password is **VALID** only if it meets ALL the requirements:

* 8–14 characters
* At least one uppercase
* At least one lowercase
* At least one digit
* At least one special character
* Does NOT contain username
* No 5+ consecutive letters
* No 5+ consecutive digits
* No character repeated 3+ times consecutively

## Build the Docker Image

```
cd path/to/password-auditor-project

run...
docker build -t password-auditor ./scanner
```

## Run the Auditor

```
docker run -it --rm -v ${PWD}/output:/output password-auditor
```

You will be prompted for username and a hidden password input.

## View Report

Open:

```
output/Password_Audit_Report.html
```

Report includes: username, Argon2 hash, weak/strong status, failed rules, timestamp for when the report was generated/updated.  
The file updates on each run. If its first time running the auditor, it will generate a new HTML file.

## Troubleshooting

* **No report generated:** Check volume mount
  ```
  -v ${PWD}/output:/output
  ```
* **Build too fast (cached):**
  ```
  run this...
  docker build --no-cache -t password-auditor ./scanner
  ```

## Best Practices to Keep

* Use for onboarding user accounts or periodic password audits
* Store reports securely
* Address weak passwords promptly
* Archive reports regularly
* Never share hashed passwords publicly
