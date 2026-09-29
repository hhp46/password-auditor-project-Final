
# **GETTING STARTED GUIDE – PASSWORD AUDIT**  


**Author:** Harsh Patel  
**Course:** IT610 – NJIT  
**Project:** Password Auditor (Docker-Based)

---

## **1. Introduction**

The Password Auditor is a lightweight security assessment tool designed for system administrators, IT auditors, and security teams. It evaluates password strength using a defined set of complexity rules and generates an HTML report containing audit results. The tool runs entirely inside a Docker container, ensuring consistent behavior across different environments.

This guide provides step‑by‑step instructions for installing, running, and using the Password Auditor.

---

## **2. System Requirements**

To use the Password Auditor, ensure the following prerequisites are met:

- **Docker Desktop** installed (Windows, macOS, or Linux)
- Ability to run terminal or PowerShell commands
- Permission to mount local directories
- Access to the project folder containing:
  - `scanner/password_auditor.py`
  - `scanner/Dockerfile`
  - `output/` directory

No Python installation is required on the host system.

---

## **3. Project Directory Structure**

Your project folder should contain the following structure:

```
password-auditor-project/
│
├── output/
│     Password_Audit_Report.html        (generated automatically)
│
└── scanner/
      Dockerfile
      password_auditor.py
```

The `output/` directory is used to store the generated HTML report.

---

## **4. Password Complexity Requirements**

The Password Auditor evaluates passwords using the following rules:

1. Length must be **8–14 characters**
2. Must contain **at least one uppercase** letter
3. Must contain **at least one lowercase** letter
4. Must contain **at least one digit**
5. Must contain **at least one special character**
6. Password **cannot contain the username**
7. No **5 or more consecutive letters**
8. No **5 or more consecutive digits**
9. No character repeated **three or more times** consecutively

Passwords failing any rule are marked **WEAK** and logged accordingly.

---

## **5. Building the Docker Image**

1. Open a terminal or PowerShell window.
2. Navigate to the project root directory:

   ```bash
   cd path/to/password-auditor-project
   ```

3. Build the Docker image using the Dockerfile inside the `scanner` directory:

   ```bash
   docker build -t password-auditor ./scanner
   ```

This command creates a Docker image named **password-auditor**.

---

## **6. Running the Password Auditor**

Run the following command:

```bash
docker run --rm -v ${PWD}/output:/output password-auditor
```

Explanation:

- `--rm` removes the container after execution  
- `-v ${PWD}/output:/output` mounts your local `output/` folder into the container  
- `password-auditor` is the image built in the previous step  

You will be prompted:

```
Auditing for a Secure Password
Enter your username:
Enter your password (HIDDEN):
```

The password input is hidden for security.

---

## **7. Viewing the Audit Report**

After running the tool, open:

```
output/Password_Audit_Report.html
```

Each audit entry includes:

- Username  
- Argon2 hashed password  
- Weak/Strong indicator  
- List of failed requirements  
- Timestamp of creation or update  

The report automatically grows with each run.

---

## **8. Troubleshooting**

### **Report Not Generated**
Ensure the volume mount is correct:

```bash
-v ${PWD}/output:/output
```

### **Permission Denied**
Run your terminal as Administrator or ensure write access to the `output/` directory.

### **Docker Build Completes Too Quickly**
Docker may be using cached layers.  
Force rebuild using:

```bash
docker build --no-cache -t password-auditor ./scanner
```

### **Git Push Rejected**
Pull remote changes first:

```bash
git pull origin main --allow-unrelated-histories
```

---

## **9. Best Practices for Administrators**

- Use this tool during onboarding or password audits  
- Store the HTML report securely  
- Review weak passwords and enforce remediation  
- Archive reports periodically  
- Do not share hashed passwords publicly  

---
