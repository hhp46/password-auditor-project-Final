# -*- coding: utf-8 -*-

import os
import re
from argon2 import PasswordHasher
from getpass import getpass
from datetime import datetime
from zoneinfo import ZoneInfo

REPORT_PATH = "/output/password_report.html"
VERSION_FILE = "/output/version.txt"


ph = PasswordHasher()

# -----------------------------
# Password Strength Evaluation
# -----------------------------
def evaluate_password_strength(username, pwd):
    requirements = []
    pwd_lower = pwd.lower()
    user_lower = username.lower()

    if len(pwd) < 8 or len(pwd) > 14:
        requirements.append("Password must be between 8 and 14 characters long")

    if not any(c.isupper() for c in pwd):
        requirements.append("Password must contain at least 1 uppercase letter")

    if not any(c.islower() for c in pwd):
        requirements.append("Password must contain at least 1 lowercase letter")

    if not any(c.isdigit() for c in pwd):
        requirements.append("Password must contain at least 1 numeric digit")

    if not re.search(r"[^A-Za-z0-9]", pwd):
        requirements.append("Password must contain at least 1 special character")

    if user_lower in pwd_lower:
        requirements.append("Password cannot contain the username")

    if re.search(r"[A-Za-z]{5,}", pwd):
        requirements.append("Password cannot contain more than 4 consecutive letters")

    if re.search(r"\d{5,}", pwd):
        requirements.append("Password cannot contain more than 4 consecutive digits")

    if re.search(r"(.)\1\1", pwd):
        requirements.append("Password cannot contain a character repeated more than twice in a row")

    is_strong = len(requirements) == 0
    return is_strong, requirements


# -----------------------------
# Build one table row
# -----------------------------
def build_row(username, hashed_password, requirements):
    if requirements:
        weak_text = "YES"
        weak_color = "background-color:#ff4d4d;"   # red
    else:
        weak_text = "NO"
        weak_color = "background-color:#4CAF50;"   # green

    requirements_text = "<br>".join(requirements) if requirements else "None"

    return (
        f"<tr>"
        f"<td style='text-align:center;'>{username}</td>"
        f"<td style='text-align:center;'>{hashed_password}</td>"
        f"<td style='text-align:center; {weak_color}'>{weak_text}</td>"
        f"<td style='text-align:center;'>{requirements_text}</td>"
        f"</tr>\n"
    )


# -----------------------------
# HTML Report Generator
# -----------------------------
def generate_html_report(username, hashed_password, requirements):
    timestamp = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M:%S")
    row_html = build_row(username, hashed_password, requirements)

    # -----------------------------
    # If report does NOT exist ? create new file
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
                    "<th style='text-align:center;'>Requirements Failing</th>"
                    "</tr>\n")
            f.write(row_html)
            f.write("</table></body></html>\n")
        print(f"\nNew report created: {REPORT_PATH}")
        return

    # -----------------------------
    # Update timestamp every run
    # -----------------------------
    with open(REPORT_PATH, "r") as f:
        content = f.read()

    new_timestamp_line = f"<p>Generated: {timestamp} (EST)</p>"
    content = re.sub(r"<p>Generated:.*?</p>", new_timestamp_line, content)

    # -----------------------------
    # Append new row before </table>
    # -----------------------------
    content = content.replace("</table>", row_html + "</table>")

    with open(REPORT_PATH, "w") as f:
        f.write(content)

    print(f"\nReport updated: {REPORT_PATH}")


# -----------------------------
# Main Program
# -----------------------------
def main():
    print("Auditing for a Secure Password")

    username = input("Enter your username: ").strip()
    password = getpass("Enter your password (hidden): ").strip()

    is_strong, requirements = evaluate_password_strength(username, password)
    hashed = ph.hash(password)

    generate_html_report(username, hashed, requirements)

    if not is_strong:
        print("\nPassword is WEAK and logged.")
    else:
        print("\nPassword is STRONG and logged.")


if __name__ == "__main__":
    main()
