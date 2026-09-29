# Password Auditor – IT610 Midterm Project  

This is a password auditing tool using Docker that evaluates a end users account password strength, and generates an HTML report (based on the audit) for the end user to review.

---

# Overview

This project provides a command‑line password auditing utility designed for specifically system administrators and end users. 
The user enter a username and password (which is hidden), and the tool:

- Evaluates the password against strict complexity rules
- Generates a HTML report to review the audit
  
The entire application runs inside a **Docker container**, ensuring consistent behavior across environments.

---

# Project Structure

<img width="308" height="158" alt="image" src="https://github.com/user-attachments/assets/90cdf58d-fa70-4ab5-9fd8-a8b3536d96bd" />

---

## HTML Report

The report is generated at: /output/Password_Audit_Report.html


Every time the docker is ran the results are added to the HTML report as a table containing:

- Username
- Hashed Password
- Weak Password? (YES/NO)
- Failed Requirements

  
The HTML report is automatically generated after the docker image is built and ran.

---


# Author  
**Harsh Patel**  
IT610:851 – NJIT Course

---
