from twilio.rest import Client

TWILIO_SID = "twilio_sid"
TWILIO_AUTH_TOKEN = "auth_token"
TWILIO_VIRTUAL_NUMBER = "virtual_number"
TWILIO_VERIFIED_NUMBER = "verified_number"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
