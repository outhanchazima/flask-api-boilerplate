from flask_mail import Mail, Message
from celery import Celery
from app.src.config import Config
from app.src.utils import logging
from app import app


logger = logging.GetLogger(__name__)

mail = Mail(app)
appContext = app.app_context()

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL,
             backend=Config.CELERY_BROKER_URL)

@celery.task(bind=True)
def sendAsyncMail(self, emailData):
    """Send Email in the background"""
    try:
        appContext.push()
        msg = Message(emailData['subject'],
                sender=Config.MAIL_DEFAULT_SENDER,
                recipients=[emailData['to']])
        msg.body = emailData['body']
        logger.info("async background email sent")
        mail.send(msg)
        appContext.pop()

    except Exception as e:
        logger.exception("Error! Mail Sending Fail, {}".format(e))
        raise self.retry(exc=e, countdown=300, max_retries=3)
        
if __name__ == '__main__':
    celery.start()