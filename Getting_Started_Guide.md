
# **GETTING STARTED GUIDE – PASSWORD AUDITING**  


**Author:** Harsh Patel  
**Course:** IT610 – NJIT  
**Project:** Docker-Based Password Auditor

---

## **Overview**

The Password Auditor checks password strength against defined complexity rules and generates an HTML report. It runs fully in Docker—no Python installation required.

---
## Requirements

Docker Desktop (Windows/macOS/Linux)
Terminal/Powershell access
Permission to mount volumes

---


## Project Structure

<img width="308" height="158" alt="image" src="https://github.com/user-attachments/assets/31c7cd5f-78a8-4830-977c-4b5e436c88b2" />

password-auditor-project/
├── output/
└── scanner/
    ├── Dockerfile
    └── password_auditor.py
    
```

The `output/` directory is used to store the generated HTML report.

---



Here’s a **short, Git‑friendly** version of your Getting Started Guide.  
Clean, compact, and ready to drop into a README.md in your repo.

***

# Password Auditor – Getting Started

**Author:** Harsh Patel  
**Course:** IT610 – NJIT  
**Project:** Docker-Based Password Auditor

## Overview

The Password Auditor checks password strength against defined complexity rules and generates an HTML report. It runs fully in Docker—no Python installation required.

## Requirements

* Docker Desktop (Windows/macOS/Linux)
* Terminal/Powershell access
* Permission to mount volumes
* Project structure:
  ```
  password-auditor-project/
  ├── output/
  └── scanner/
      ├── Dockerfile
      └── password_auditor.py
  ```

## Password Rules

A password is **strong** only if it meets ALL:

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
docker build -t password-auditor ./scanner
```

## Run the Auditor

```
docker run --rm -v ${PWD}/output:/output password-auditor
```

You will be prompted for username and a hidden password input.

## View Report

Open:

```
output/Password_Audit_Report.html
```

Report includes: username, Argon2 hash, weak/strong status, failed rules, timestamp.  
The file updates/grows on each run.

## Troubleshooting

* **No report generated:** Check volume mount
  ```
  -v ${PWD}/output:/output
  ```
* **Permission errors:** Run terminal as Admin or fix write permissions
* **Build too fast (cached):**
  ```
  docker build --no-cache -t password-auditor ./scanner
  ```

## Best Practices

* Use for onboarding or periodic audits
* Store reports securely
* Address weak passwords promptly
* Archive reports regularly
* Never share hashed passwords publicly

***

If you'd like, I can also **format this as a README.md file**, **generate a Markdown badge**, or **add usage examples** for your repo—just tell me!


