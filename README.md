***

# **Password Auditor – IT610 Final Project**

* **Author:** Harsh Patel
* **Course:** IT 610:851 – NJIT
* **Project:** Multi‑Container Docker Password Auditor (Scanner + Viewer)

***

## **Overview**

This Final Project expands the midterm password auditing tool into a **multi‑container Docker Compose application**.  
The user enters a username and password **(which is hidden)**, and the tool:

1. Evaluates the password against strict complexity rules
2. Generates a full HTML report
3. Hosts the report in a live web viewer at: **`http://localhost:8080`**

***

## **Project Structure**

```
password-auditor-project-Final/
│
├── docker-compose.yml
│
├── scanner/
│   ├── Dockerfile
│   ├── password_auditor.py
│
├── output/
│   └── Password_Audit_Report.html   (generated automatically)
│
└── viewer/
│   ├── default.conf
│   ├── Dockerfile   (NGINX static hosting configuration)
│
```

**Important:❗**  
The `/output` directory is **outside** the `/scanner` folder NOT inside it like the Midterm Project.  
Both containers share this folder through Docker volumes.

***

## **HTML Report**

The report is generated automatically as: **`../output/Password_Audit_Report.html.`**


Each time the scanner container is run, a new entry is added to the HTML table containing:

* Username
* Hashed Password (Argon2)
* Weak Password? (YES/NO)
* Failed Requirements
* Timestamp

❗ The report updates dynamically and is hosted live through the viewer container at: **`http://localhost:8080`**

***
## **❗ Note:** 
Use the Getting Started Guide.md file to walkthrough the project. 

***

## **Author**

**Harsh Patel**  
IT 610:851 – NJIT

***
