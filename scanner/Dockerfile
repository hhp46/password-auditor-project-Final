FROM python:3.11-slim

WORKDIR /scanner

# Copy files from the doccker folder (build context)
COPY password_auditor.py /scanner/password_auditor.py


RUN pip install argon2-cffi


ENTRYPOINT ["python", "/scanner/password_auditor.py"]
CMD ["bash"]
