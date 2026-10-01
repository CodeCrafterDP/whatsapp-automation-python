import os
from twilio.rest import Client
from dotenv import load_dotenv
from datetime import datetime, timedelta
import time


#twillio credencials
load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

#function to send sms
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',  # Twilio sandbox number
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"Message sent successfully! message SID{message.sid}")
    except Exception as e:
        print('an error occurred')


#user input
name = input ('Enter the recipient name =')       
recipient_number = input('Enter the recipient Whatsappp number with country code=')
message_body = input('Enter the message you want to send to {name}: ') 



#parse date/time and calculate delay
date_str =input ('enter the date to send the message (YYYY-MM-DD): ')
time_str = input('enter the time to send the message (HH:MM in 24-hour format): ')


#datetime
scheduled_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")

current_datetime = datetime.now()

time_difference = scheduled_datetime - current_datetime
delay_seconds = time_difference.total_seconds()


if delay_seconds <=0:
    print("The scheduled time is in the past. Please enter a future date and time:")
else:
    print(f"Message scheduled to be sent to {name} at {scheduled_datetime}.")


#wait untill the scheduled time
time.sleep(delay_seconds)


send_whatsapp_message(recipient_number, message_body)
