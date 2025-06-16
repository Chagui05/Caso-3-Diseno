import boto3

def sendMail(name, kek):

    try:
        ses = boto3.client('ses', region_name='us-east-2')

        # Estos valores son quemados para efectos del ejemplo
        source_email = "sagoch777@gmail.com"
        destination_email = "santichavesg@gmail.com"

        response = ses.send_email(
            Source=source_email,
            Destination={
                "ToAddresses": [destination_email],
            },
            Message={
                "Subject": {"Data": "Correo de prueba con SES"},
                "Body": {
                    "Text": {"Data": f"Hola {name},su administrador ha generado su kek:\n {kek}."}
                }
            }
        )

        print("Correo enviado. Message ID:", response["MessageId"])
    except Exception as e:
            print("Error enviando correo:", e)
