from kavenegar import *

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('62572B316B5464595767584E7A30645156626D7538426B68515963346436777A43657875314133683178493D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'کد تایید شما برای ورود به *** {code}'
        }

        response = api.sms_send(params)
        print("Response:", response)
    except APIException as e:
        print(f"APIException: {e}")
    except HTTPException as e:
        print(f"HTTPException: {e}")

# نمونه استفاده
