from email import message
import sqlite3
import asyncio
from email.mime.text import MIMEText
from email.message import EmailMessage
from aiosmtplib import SMTP
from aiosmtplib import response
from aiosmtplib.response import SMTPResponse


def sql_request():
    conn = sqlite3.connect("contacts.db")
    #conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    sql = "SELECT contact_id, first_name, last_name, email FROM contacts"
    rows = cursor.execute(sql).fetchall()
    return rows





async def send_with_send_message(message):

    smtp_client = SMTP()

    await smtp_client.connect(hostname="smtp.gmail.com", port=587, start_tls=True,  username='test97wave@gmail.com', password='evaw79tset')
    response = await smtp_client.send_message(message)
    print(response)
    await smtp_client.quit()


def main():
    event_loop = asyncio.get_event_loop()
    for row in sql_request():
        message = EmailMessage()
        message["From"] = "test97wave@gmail.com"
        message["To"] = "e97.wav@gmail.com"
        message["Subject"] = "Async send!"
        message.set_content(f"Уважаемый {row[1]} {row[2]}! Cпасибо, что пользуетесь нашим сервисом объявлений.")

        event_loop.run_until_complete(send_with_send_message(message))
        message = 0
    
    

if __name__ == "__main__":
    main().run
