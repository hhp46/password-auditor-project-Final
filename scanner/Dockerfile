FROM python:3.11-slim

WORKDIR /scanner

COPY password_auditor.py /scanner/password_auditor.py
COPY accounts.txt /scanner/accounts.txt

RUN mkdir -p /output

ENTRYPOINT ["python", "/scanner/password_auditor.py"]
