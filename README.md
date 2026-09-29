# Password Auditor – IT610 Midterm Project  

Password auditing tool using Docker that evaluates password strength, enforces complexity rules, and generates an HTML report for security review.
This project was developed for the **IT610 – Security Administration** course.
---

# Overview

This project provides a command‑line password auditing utility designed for system administrators. 
Users enter a username and password (which is hidden), and the tool:

- Evaluates the password against strict complexity rules  
- Hashes the password using **Argon2** (industry‑standard secure hashing)  
- Logs the results into a growing **HTML report**  
- Marks weak passwords and lists failed requirements  
- Updates timestamps automatically on each run  

The entire application runs inside a **Docker container**, ensuring consistent behavior across environments.

---


# Project Structure
<img width="511" height="237" alt="image" src="https://github.com/user-attachments/assets/35a1760a-7b01-4e67-ac30-59afcdc446a0" />




---

## Password Complexity Requirements

The password auditing tool checks for the following:

1. Length between **8–14 characters**  
2. At least **1 uppercase** letter  
3. At least **1 lowercase** letter  
4. At least **1 digit**  
5. At least **1 special character**  
6. Password cannot contain the username  
7. No **5+ consecutive letters**  
8. No **5+ consecutive digits**  
9. No character repeated **3+ times** in a row  

If any requirement is NOT met, the password is marked **WEAK** and the failing requirements are logged in a HTML report.

---

## HTML Report

The report is generated at: /output/Password_Audit_Report.html


Every time the docker is ran the results are added to the HTML report as a table containing:

- Username
- Hashed Password
- Weak Password? (YES/NO)
- Failed Requirements

  
The report is automatically created if missing and updated on subsequent runs.

---


# Author  
**Harsh Patel**  
IT610 – Security Administration  
New Jersey Institute of Technology (NJIT)

---
