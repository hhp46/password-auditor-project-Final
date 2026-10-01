***

# **GETTING STARTED GUIDE – PASSWORD AUDITOR FINAL PROJECT**

* **Author:** Harsh Patel
* **Course:** IT610:851 – NJIT
* **Project:** Multi‑Container Docker Password Auditor (Scanner + Viewer)

***

## **Overview**

The Final Project is expanded from the original Password Auditor into a **multi‑container Docker Compose application** consisting of:

* **password\_scanner** – Python‑based password auditing engine
* **password\_viewer** – NGINX web server that displays the generated audit report

The auditor evaluates passwords using NJ State SISM Policy complexity rules and writes results to a shared `output/` directory.  
We are also able to view the HTML report at:

```
http://localhost:8080
```

***

## **Requirements**

* Docker Desktop installed and running
* Windows PowerShell
* Docker Compose
* Correct working directory

***

## **Project Structure**

```
password-auditor-project-FINAL/
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
    └── Dockerfile   (NGINX config + static hosting)
```

**Important:❗**  
The `output/` directory is **outside** the `scanner/` folder NOT inside it like the Midterm Project.  
Both containers share this folder through Docker volumes.

***

## **Before You Begin ❗**

* Make sure **Docker Desktop is running**
* Run all commands from inside the project folder:
  ```
  C:\Users\<USERNAME>\Desktop\password-auditor-project-FINAL
  ```

***

## **Password Rules**

A password is considered **valid** only if it meets *all* of the following:

* 8–14 characters
* At least one uppercase
* At least one lowercase
* At least one digit
* At least one special character
* Does **not** contain the username
* No character repeated 3+ times consecutively

***

# **1. Navigate to the Project Directory**

Open PowerShell:

```
cd C:\Users\<USERNAME>\Desktop\password-auditor-project-FINAL
```

Replace `<USERNAME>` with your Windows username if your using PowerShell.

***

# **2. Build All Containers**

```
docker-compose build
```

This builds:

* `password_scanner` (Python)
* `password_viewer` (NGINX)

***

# **3. Start the Viewer (NGINX)**

**Run this in its own PowerShell window.**

```
docker-compose up password_viewer
```

This hosts the report at:

```
http://localhost:8080
```

**Leave this window running.**

***

# **4. Open a NEW PowerShell Window**

Navigate again:

```
cd C:\Users\<USERNAME>\Desktop\password-auditor-project-FINAL
```

***

# **5. Run the Scanner Container**

```
docker-compose run --rm password_scanner
```

This launches the Python auditor and prompts you for:

**Username**
AND 
**Password (hidden)**


The scanner will generate the HTML report to:

```
output/Password_Audit_Report.html
```

***

# **6. View the Report on a browser**

Open your browser and go to:

```
http://localhost:8080
```

You will see a full HTML password audit report in a table that consists of:

* Username
* Argon2 hashed password
* Weak/Strong status
* Failed requirements
* Timestamp

***

# **7. Shut Down All Containers**

In the viewer window, stop NGINX:

```
CTRL + C
```

Then remove all containers and networks:

```
docker-compose down
```

***

# **Troubleshooting**

### Viewer shows blank page

Make sure the viewer is running:
```
docker-compose up password_viewer
```

### Report not generating

Run the scanner again:
```
docker-compose run --rm password_scanner
```

### No report appearing in browser

Ensure the shared folder exists inside the project folder:
```
output/
```

### Build issues or cached layers

Force rebuild:
```
docker-compose build --no-cache
```

### Wrong directory

All commands must be executed from root of the project folder:
```
C:\Users\<USERNAME>\Desktop\password-auditor-project-FINAL
```

***

## **Best Practices**

* Use for periodic password audits or employee onboarding
* Store reports securely
* Address weak passwords quickly
* Archive HTML reports regularly
* Never expose Argon2 password hashes publicly

***
