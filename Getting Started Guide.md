
# **GETTING STARTED GUIDE – PASSWORD AUDITOR PROJECT**

**Author:** Harsh Patel  
**Course:** IT610:851 – NJIT  
**Project:** Docker-Based Password Auditor

---

## **Overview**
The Password Auditor evaluates password strength using complexity rules based on the NJ State SISM Policy.  
It generates an HTML report and runs entirely inside Docker — **no Python installation required**.

---

## **Requirements**
- Docker Desktop (Windows/macOS/Linux)  
- Terminal / PowerShell access  
- Permission to mount volumes  

---

## **Project Structure**
```
password-auditor-project/
│
└── scanner/
      ├── Dockerfile
      ├── password_auditor.py
      └── output/                            (generated automatically)
            └── Password_Audit_Report.html   (generated automatically)


```

The `output` directory and the HTML report are created automatically once the Docker image is built and run successfully inside the container.

---

## **Password Rules**
A password is **VALID** only if it meets *all* of the following:

- 8–14 characters  
- At least one uppercase  
- At least one lowercase  
- At least one digit  
- At least one special character  
- Does **not** contain the username  
- No 5+ consecutive letters  
- No 5+ consecutive digits  
- No character repeated 3+ times consecutively  

---

## **Build the Docker Image**
Navigate into the folder containing the Dockerfile (inside `/scanner`):

```
cd path/to/password-auditor-project/scanner
```

Build the image:

```
docker build -t password-auditor .
```

---

## **Run the Auditor *Inside* the Container**
Start a shell inside the container and mount the output directory:

```
docker run -it --entrypoint bash -v ${PWD}/output:/output password-auditor
```

Run the auditor manually:

```
python /scanner/password_auditor.py
```

Enter your username and password when prompted.  Don't worry about entering your password on the prompt, it is HIDDEN. 
The report will be saved to `/output`.

---

## **Exit the Container**
Inside the container:

```
exit
```

or press **Ctrl + D**.

---

## **View Your HTML Report**
Open:

```
output/Password_Audit_Report.html
```
A  `/output` directory will be created when the image is run and the report will be automatically generated. 

The report includes:

- Username  
- Argon2 hashed password  
- Weak/Strong status  
- Failed rules  
- Timestamp  

The report updates on each run. On the first run, a new report (HTML file) is created.

---

## **Troubleshooting Tips**

### **Report not generated**
Check the volume mount:

```
-v ${PWD}/output:/output
```

### **Build running too fast (cached layers)**
Force rebuild:

```
docker build --no-cache -t password-auditor .
```

### **Wrong working directory**
Make sure you run Docker commands from:

```
path/to/password-auditor-project/scanner
```

Make sure to run the commands from where the Dockerfile lives ( `/scanner` ).

---

## **Best Practices**
- Use during onboarding or periodic password audits  
- Store reports securely  
- Address weak passwords promptly  
- Archive reports regularly  
- Never share hashed passwords publicly  
