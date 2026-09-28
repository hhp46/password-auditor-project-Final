import os
import time
import re

ACCOUNTS_FILE = "/scanner/accounts.txt"
REPORT_PATH = "/output/password_report.html"

def evaluate_password_strength(username, pwd):
    reasons = []
    pwd_lower = pwd.lower()
    user_lower = username.lower()

    # Rule 1: Minimum length
    if len(pwd) < 8 or len(pwd) > 14:
        reasons.append("Password must be between 8 and 14 characters long")

    # Rule 2: Minimum 1 uppercase
    if not any(c.isupper() for c in pwd):
        reasons.append("Password must contain at least 1 uppercase letter")

    # Rule 3: Minimum 1 lowercase
    if not any(c.islower() for c in pwd):
        reasons.append("Password must contain at least 1 lowercase letter")

    # Rule 4: Minimum 1 digit
    if not any(c.isdigit() for c in pwd):
        reasons.append("Password must contain at least 1 numeric digit")

    # Rule 5: Minimum 1 special character
    if not re.search(r"[^A-Za-z0-9]", pwd):
        reasons.append("Password must contain at least 1 special character")

    # Rule 6: Cannot contain username
    if user_lower in pwd_lower:
        reasons.append("Password cannot contain the username")

    # Rule 7: Cannot contain more than 4 consecutive letters
    if re.search(r"[A-Za-z]{5,}", pwd):
        reasons.append("Password cannot contain more than 4 consecutive letters")

    # Rule 8: Cannot contain more than 4 consecutive digits (updated rule)
    if re.search(r"\d{5,}", pwd):
        reasons.append("Password cannot contain more than 4 consecutive digits")

    # Rule 9: Cannot repeat any character more than twice
    if re.search(r"(.)\1\1", pwd):
        reasons.append("Password cannot contain a character repeated more than twice in a row")

    is_strong = len(reasons) == 0
    return is_strong, reasons


def load_accounts():
    accounts = {}
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip().replace("\r", "").replace("\n", "")
                if ":" in line:
                    user, pwd = line.split(":", 1)
                    accounts[user.strip()] = pwd.strip()
    return accounts


def audit_passwords(accounts):
    results = []
    for user, pwd in accounts.items():
        pwd_clean = pwd.strip().replace("\r", "").replace("\n", "")
        is_strong, reasons = evaluate_password_strength(user, pwd_clean)
        results.append((user, pwd_clean, is_strong, reasons))
    return results


def generate_report(results):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    html = []
    html.append("<html><head><title>Password Audit Report</title></head><body>")
    html.append(f"<h1>Password Audit Report</h1>")
    html.append(f"<p>Generated: {timestamp}</p>")
    html.append("<table border='1'><tr><th>User</th><th>Password</th><th>Weak</th><th>Reasons</th></tr>")

    for user, pwd, is_strong, reasons in results:
        weak = not is_strong
        reason_text = "<br>".join(reasons) if reasons else "None"
        html.append(f"<tr><td>{user}</td><td>{pwd}</td><td>{weak}</td><td>{reason_text}</td></tr>")

    html.append("</table></body></html>")

    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(html))


def main():
    print("Running password audit...")
    accounts = load_accounts()
    results = audit_passwords(accounts)
    generate_report(results)
    print(f"Audit complete. Report written to {REPORT_PATH}")


if __name__ == "__main__":
    main()
