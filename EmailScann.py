import smtplib
import re

"""Функция для отправки ответного сообщения"""
def send_email(receiver_email, subject, body):
    """Настройки SMTP сервера"""
    smtp_server = 'smtp.gmail..com'
    smtp_port = 587
    sender_email = 'Ваша почта@gmail.com'
    password = 'Пароль от почты'

    """Установка соединения с SMTP сервером"""
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)

    """Отправка сообщения"""
    message = f'From: {sender_email}\nTo: {receiver_email}\nSubject: {subject}\n\n{body}'
    server.sendmail(sender_email, receiver_email, message)

    """Закрытие соединения с SMTP сервером"""
    server.quit()


"""Функция для проверки ключевых слов в сообщении и отправки ответа"""
def check_keywords_in_email(receiver_email, email_subject, email_body):
    """Здесь можно указать ключевые слова"""
    keywords = ['', '', '']

    for keyword in keywords:
        if re.search(keyword, email_body, re.IGNORECASE):
            response_subject = 'Re: ' + email_subject
            """Здесь прописывается сообщение  ответа"""
            response_body = ''
            send_email(receiver_email, response_subject, response_body)
            break
