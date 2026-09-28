
# 📘 Password Auditor — IT610 Midterm Project  
A Python‑based password auditing tool that evaluates user passwords against a strict enterprise‑grade policy.  
This project was developed as part of the **IT610 – Security Administration** course at **NJIT**.

---

## 🔍 Overview  
The Password Auditor scans a list of username/password pairs and evaluates each password against a defined set of security rules.  
It generates a detailed **HTML report** showing which passwords are weak and why.

This project demonstrates secure coding practices, password policy enforcement, file parsing, reporting, and containerization using Docker.

---

## 🛡️ Password Policy Rules  
Each password is evaluated against the following rules:

### **Length Requirements**
- Minimum **8** characters  
- Maximum **14** characters  

### **Character Requirements**
- At least **1 uppercase** letter  
- At least **1 lowercase** letter  
- At least **1 digit**  
- At least **1 special character** (non‑alphanumeric)

### **Restrictions**
- Cannot contain the **username**  
- Cannot contain **more than 4 consecutive letters**  
- Cannot contain **more than 4 consecutive digits**  
- Cannot repeat **any character more than twice** in a row  

---

## 📁 Project Structure

```
password-auditor-project_harshpatel_IT610/
│
├── scanner/
│   └── password_auditor.py        # Main audit script
│
├── output/
│   └── password_report.html       # Generated audit report
│
├── accounts.txt                   # Username/password input file
├── Dockerfile                     # Containerized execution
├── README.md                      # Project documentation
└── MIDTERM_DOC.md                 # Midterm write-up
```

---

## ▶️ How to Run (Local)

### **1. Ensure Python 3 is installed**

Check version:

```bash
python --version
```

### **2. Run the auditor**

From the project root:

```bash
python scanner/password_auditor.py
```

### **3. View the report**

Open:

```
output/password_report.html
```

---

## 🐳 Running with Docker

### **1. Build the image**

```bash
docker build -t password-auditor .
```

### **2. Run the container**

```bash
docker run --rm -v ${PWD}/output:/output password-auditor
```

The report will appear in your local `output/` folder.

---

## 📄 Input Format (accounts.txt)

Each line must follow:

```
username:password
```

Example:

```
harsh:Adm12121!
john:Welcome123!
```

---

## 📊 Output Report

The generated HTML report includes:

- Username  
- Password  
- Weak/Strong indicator  
- Detailed reasons for failure  

This makes it easy to identify which passwords violate policy and why.

---

## 🧑‍💻 Technologies Used

- **Python 3**
- **Regex (re module)**
- **HTML reporting**
- **Docker**
- **Git/GitHub**

---

## 🎓 Author  
**Harsh Patel**  
IT610 – Security Administration  
New Jersey Institute of Technology (NJIT)

---
