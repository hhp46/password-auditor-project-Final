# -*- coding: utf-8 -*-

import os
import re
from argon2 import PasswordHasher
from getpass import getpass
from datetime import datetime
from zoneinfo import ZoneInfo

REPORT_PATH = "/output/Password_Audit_Report.html"
ph = PasswordHasher()

# -----------------------------
#  Password Evaluation RULES
# -----------------------------

def evaluate_password(username, passwd):
    requirement = []
    passwd_lower = passwd.lower()
    user_lower = username.lower()

    if len(passwd) < 8 or len(passwd) > 14:
        requirement.append("Password must be between 8 and 14 characters long")

    if not any(c.isupper() for c in passwd):
        requirement.append("Password must contain at least 1 uppercase letter")

    if not any(c.islower() for c in passwd):
        requirement.append("Password must contain at least 1 lowercase letter")

    if not any(c.isdigit() for c in passwd):
        requirement.append("Password must contain at least 1 numeric digit")

    if not re.search(r"[^A-Za-z0-9]", passwd):
        requirement.append("Password must contain at least 1 special character")

    if user_lower in passwd_lower:
        requirement.append("Password cannot contain the username")

    if re.search(r"(.)\1\1", passwd):
        requirement.append("Password cannot contain a character repeated more than twice in a row")

    strong = len(requirement) == 0
    return strong, requirement


# -----------------------------
#  Build first row for the table
# -----------------------------

def create_table(username, hashed_password, requirement):
    if requirement:
        w_text = "YES"
        w_color = "background-color:#ff4d4d;"   # red
    else:
        w_text = "NO"
        w_color = "background-color:#4CAF50;"   # green

    requirement_text = "<br>".join(requirement) if requirement else "None"

    return (
        f"<tr>"
        f"<td style='text-align:center;'>{username}</td>"
        f"<td style='text-align:center;'>{hashed_password}</td>"
        f"<td style='text-align:center; {w_color}'>{w_text}</td>"
        f"<td style='text-align:center;'>{requirement_text}</td>"
        f"</tr>\n"
    )


# -----------------------------
#  Generate a HTML Report
# -----------------------------

def HTML_REPORT(username, hashed_password, requirement):
    timestamp = datetime.now(ZoneInfo("America/New_York")).strftime("%m-%d-%Y %H:%M")
    row_html = create_table(username, hashed_password, requirement)


    # -----------------------------
    # If a HTML report does NOT exist create new HTML file
    # -----------------------------
    
    if not os.path.exists(REPORT_PATH):
        with open(REPORT_PATH, "w") as f:
            f.write("<html><head><title>Password Audit Report</title></head><body>\n")
            f.write("<div style='text-align:center;'>\n")
            f.write("<h1>Password Audit Report</h1>\n")
            f.write(f"<p>Generated: {timestamp} (EST)</p>\n")
            f.write("</div>\n")
            f.write("<table border='1' cellpadding='8'>\n")
            f.write("<tr>"
                    "<th style='text-align:center;'>Username</th>"
                    "<th style='text-align:center;'>Hashed Password</th>"
                    "<th style='text-align:center;'>Weak Password?</th>"
                    "<th style='text-align:center;'>Requirement Failing</th>"
                    "</tr>\n")
            f.write(row_html)
            f.write("</table></body></html>\n")
        print(f"\nNew report created: {REPORT_PATH}")
        return


# -----------------------------
#  Update time on every run
# -----------------------------

    with open(REPORT_PATH, "r") as f:
        content = f.read()

    new_timestamp_line = f"<p>Report Updated: {timestamp} (EST)</p>"
    content = re.sub(r"<p>Generated:.*?</p>", new_timestamp_line, content)


# -----------------------------
# Append new row before </table>
# -----------------------------

    content = content.replace("</table>", row_html + "</table>")

    with open(REPORT_PATH, "w") as f:
        f.write(content)

    print(f"\nReport updated at: {REPORT_PATH}")


# -----------------------------------------
#  Main Program - Inteactive via cmdline
# -----------------------------------------

def main():
    print("Auditing for a Secure Password")

    username = input("Enter your username: ").strip()
    password = getpass("Enter your password (HIDDEN): ").strip()

    strong, requirement = evaluate_password(username, password)
    hashed = ph.hash(password)

    HTML_REPORT(username, hashed, requirement)

    if not strong:
        print("\nPassword is WEAK and must meet the complexity requirement. It is logged in the report.")
    else:
        print("\nPassword meets the complexity requirement. It is logged in the report.")


if __name__ == "__main__":
    main()
