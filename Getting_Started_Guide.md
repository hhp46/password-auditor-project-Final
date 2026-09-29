**Getting Started Guide – Password Auditor**





\# \*\*Getting Started Guide – Password Auditor\*\*



\## \*\*1. Introduction\*\*



The Password Auditor is a lightweight security tool designed to help system administrators and users evaluate password strength and enforce organizational complexity requirements. The tool runs inside a Docker container and generates an HTML report that logs each password audit, including failed requirements and secure Argon2 password hashes.



This guide explains how to install, run, and use the Password Auditor.



\---



\## \*\*2. System Requirements\*\*



To use the Password Auditor, you need:



\- \*\*Docker\*\* installed on your system  

\- Ability to run terminal commands  

\- Permission to mount local directories  

\- Access to the project folder containing:

&#x20; - `scanner/password\_auditor.py`

&#x20; - `scanner/Dockerfile`

&#x20; - `output/` directory (for the HTML report)



No Python installation is required — all dependencies run inside the container.



\---



\## \*\*3. Project Directory Structure\*\*



Your project should look like this:



```

password-auditor-project/

│

├── output/

│     Password\_Audit\_Report.html     (generated automatically)

│

└── scanner/

&#x20;     Dockerfile

&#x20;     password\_auditor.py

```



The `output/` folder will store the generated HTML report.



\---



\## \*\*4. Building the Docker Image\*\*



Open a terminal and navigate to the project root directory.



Run the following command to build the Docker image:



```bash

docker build -t password-auditor ./scanner

```



This command:



\- Uses the Dockerfile inside `/scanner`

\- Installs Python 3.11 and Argon2 hashing library

\- Packages the password auditor script into a runnable container



\---



\## \*\*5. Running the Password Auditor\*\*



Use the following command to run the tool:



```bash

docker run --rm -v ${PWD}/output:/output password-auditor

```



Explanation:



\- `--rm` removes the container after it finishes running  

\- `-v ${PWD}/output:/output` mounts your local `output/` directory into the container  

\- `password-auditor` is the image you built  



When the container starts, you will see:



```

Auditing for a Secure Password

Enter your username:

Enter your password (HIDDEN):

```



The password input is hidden for security.



\---



\## \*\*6. Understanding the Password Rules\*\*



The auditor checks the password against the following requirements:



\- Length between \*\*8 and 14 characters\*\*

\- Contains \*\*at least one uppercase\*\* letter

\- Contains \*\*at least one lowercase\*\* letter

\- Contains \*\*at least one digit\*\*

\- Contains \*\*at least one special character\*\*

\- Does \*\*not\*\* contain the username

\- Does \*\*not\*\* contain \*\*5 or more consecutive letters\*\*

\- Does \*\*not\*\* contain \*\*5 or more consecutive digits\*\*

\- Does \*\*not\*\* repeat any character \*\*three or more times\*\* in a row



If any rule fails, the password is marked \*\*WEAK\*\*.



\---



\## \*\*7. Viewing the HTML Report\*\*



After running the tool, open:



```

output/password\_report.html

```



Each entry in the report includes:



\- Username  

\- Argon2 hashed password  

\- Weak/Strong indicator  

\- List of failed requirements  

\- Timestamp of creation or update  



The report grows automatically with each audit.



\---



\## \*\*8. Troubleshooting\*\*



\### \*\*Report not generated\*\*

Ensure the volume mount is correct:



```bash

\-v ${PWD}/output:/output

```



\### \*\*Permission denied\*\*

Run your terminal as Administrator or ensure write access to the `output/` folder.



\### \*\*Docker build fails\*\*

Verify that the Dockerfile is located inside the `/scanner` directory.



\---



\## \*\*9. Best Practices for Administrators\*\*



\- Use this tool during onboarding or password audits  

\- Store the HTML report in a secure location  

\- Review weak passwords and enforce remediation  

\- Rotate or archive reports periodically  

\- Do not share hashed passwords publicly  



\---



\## \*\*10. Support\*\*



For academic or project‑related questions, refer to your IT610 course instructor.  

For Docker‑related issues, consult Docker’s official documentation.



\---

