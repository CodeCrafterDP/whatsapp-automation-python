# WhatsApp Automation using Python & Twilio

A Python-based WhatsApp automation project that uses the Twilio WhatsApp API to send automated WhatsApp messages.

This project demonstrates how Python can communicate with WhatsApp through Twilio's WhatsApp API while keeping API credentials securely stored using environment variables.

---

## 📌 Project Overview

The purpose of this project is to build a simple and secure WhatsApp automation system using Python and Twilio.

The application:

1. Loads Twilio credentials securely from environment variables.
2. Connects to the Twilio API.
3. Creates a WhatsApp message.
4. Sends the message through the Twilio WhatsApp Sandbox.
5. Returns the message SID for verification.

### Basic Workflow

```text
Python Application
       │
       ▼
Environment Variables
(Twilio SID + Auth Token)
       │
       ▼
Twilio API
       │
       ▼
WhatsApp Sandbox
       │
       ▼
Recipient's WhatsApp


✨ Features
.Send WhatsApp messages using Python
.Twilio WhatsApp API integration
.Secure credential management
.Environment variable support
.Twilio WhatsApp Sandbox support
.Simple and easy-to-understand Python implementation


🛠️ Technologies Used
Python
Twilio
WhatsApp Business Platform
python-dotenv
Git & GitHub


📂 Project Structure

Whatsapp_automation/
│
├── main.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md



File Description
File	              Description
main.py	              Main Python application
.env	              Stores private Twilio credentials locally
.env.example	      Example environment variable configuration
.gitignore	          Prevents sensitive/unnecessary files     from being uploaded
requirements.txt	  Lists required Python packages
README.md	          Project documentation



🚀 Getting Started
1. Clone the Repository

Clone the repository using:
git clone YOUR_GITHUB_REPOSITORY_URL

Move into the project directory:
cd Whatsapp_automation


2. Install Python Dependencies

Install the required packages:
pip install -r requirements.txt
The main dependencies are:
twilio
python-dotenv


3. Configure Environment Variables

Create a file named:
.env

inside the project directory.

Add your Twilio credentials:

TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token


💻 Python Implementation

The application loads the Twilio credentials from environment variables.

Example:

import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

A WhatsApp message can then be sent using:

message = client.messages.create(
    from_="whatsapp:+14155238886",
    to="whatsapp:+91XXXXXXXXXX",
    body="Hello from my Python WhatsApp automation project!"
)

print("Message SID:", message.sid)

🧪 Testing

The project can be tested using the Twilio WhatsApp Sandbox.

Testing involves:

Joining the WhatsApp Sandbox.
Configuring the recipient number.
Starting the Python application.
Sending a test message.
Checking the WhatsApp recipient for the message.
Checking the Twilio Message SID for confirmation.


🔮 Future Improvements

This project can be expanded into a more advanced WhatsApp automation platform.

Possible improvements include:

Automated replies
WhatsApp chatbot
AI-powered responses
FAQ automation
Appointment booking
Database integration
Message scheduling
Webhook-based incoming messages
FastAPI backend
User conversation history
AI agent integration
Human-agent escalation
Logging and monitoring


📚 Learning Outcomes

Through this project, the following concepts are demonstrated:

Python API integration
REST API usage
Environment variables
Secure credential management
WhatsApp API integration
Twilio API
Git and GitHub
Project documentation
Basic automation development

⚠️ Important Notes

This project is intended for learning, development, and authorized WhatsApp automation.

When deploying a production WhatsApp application, follow the applicable Twilio and WhatsApp policies, including requirements related to user consent, messaging, templates, and responsible automation.




👨‍💻 Author

Debraj Podder

GitHub: CodeCrafterDP



⭐ Project Status

Status: 🚧 In Development

The current version focuses on sending WhatsApp messages through Python and Twilio. More automation features can be added in future versions.