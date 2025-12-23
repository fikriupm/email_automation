# Email Automation for Market Outreach

## Overview
This project is a Gmail-based email automation script developed to support
customer service and business marketing activities. It is used to automate
outreach emails to potential audit and accounting firms in Thailand (and other potential regions) in order to promote an AI-powered audit software solution.

The automation helps reduce manual work, improve email delivery reliability,
and support business expansion into a new market.

---

## Key Features
- Automated bulk email sending using Gmail SMTP
- HTML-formatted emails for professional presentation
- Personalized email content using recipient data
- Automatic retry for failed email deliveries
- Configurable delay between emails to reduce spam risk
- Email activity logging (success and failure)
- Supports Gmail, Outlook, and Yahoo recipients
- Contact management via Excel file

## Output
- Emails are sent automatically based on the Excel contact list
- All sending activities are logged in `email_log.txt`
- Failed emails are retried automatically based on configuration

---

## Requirements
- Python 3.10 or later
- Gmail account with App Password enabled
- Internet connection

---

## Important Notes
- Gmail App Password is required (regular Gmail password will not work)
- Gmail daily sending limits apply
- Email delays are implemented to improve deliverability
- This script is intended for legitimate business outreach only

---

## Future Improvements
- Email attachment support
- Resume sending for failed emails
- Campaign summary reporting
- Enhanced HTML templates

## Instructions

1. download python, add path to the env
verify installation using "python --version"

2. create folder for python app 
install pandas "pip install pandas openpyxl" / "python -m pip  install pandas openpyxl"

3. create gmail app password -> https://myaccount.google.com/security
find app password, then generate 16 char password

4. adjust all the requirement needed (email list, info)

5. python send_email.py




