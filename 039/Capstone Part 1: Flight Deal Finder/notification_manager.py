from twilio.rest import Client

TWILIO_SID = "ACc5a7f305d6ce7b8d2fa66b590828ba73"
TWILIO_AUTH_TOKEN = "65de56ad4bb17121bd19d38a04e19b2b"
TWILIO_VIRTUAL_NUMBER = "+12028580362"
TWILIO_VERIFIED_NUMBER = "+919669915010"


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
