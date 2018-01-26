import logging
import subprocess
import smtplib

import email.mime.text

import omsaalert.config.email
import omsaalert.utility

_LOGGER = logging.getLogger(__name__)


class Notify(object):
    def send_emails(self, emails, problems):
        print("Notifying: {}".format(emails))

        content = omsaalert.utility.get_pretty_json(problems)

        m = email.mime.text.MIMEText(content)

        m['Subject'] = omsaalert.config.email.DEFAULT_SUBJECT
        m['From'] = omsaalert.config.email.FROM_EMAIL_ADDRESS
        m['To'] = ', '.join(emails)

        s = smtplib.SMTP(omsaalert.config.email.SMTP_HOSTNAME)
        s.sendmail(
            omsaalert.config.email.FROM_EMAIL_ADDRESS,
            emails,
            m.as_string())

        s.quit()

    def invoke_command(self, command, problems, stdin=False):
        print("Command: {}".format(command))
        print('')

        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

        if stdin is True:
            content = omsaalert.utility.get_pretty_json(problems)
            content = content.encode('utf8')
        else:
            content = None

        stdout, _ = p.communicate(input=content)
        stdout = stdout.decode('utf8')

        print(stdout)
        print('')
