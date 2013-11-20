import StringIO

from twisted.application import service

application = service.Application("SMTP Client Tutorial")

from twisted.application import internet
from twisted.internet import protocol
from twisted.mail import smtp
from twisted.internet import reactor


class SMTPTutorialClient(smtp.ESMTPClient):
    mailFrom = "tutorial_sender@example.com"
    mailTo = "tutorial_recipient@localhost"
    mailData = '''\
Date: Fri, 6 Feb 2004 10:14:39 -0800
From: Tutorial Guy <tutorial_sender@example.com>
To: Tutorial Gal <tutorial_recipient@localhost>
Subject: Tutorate!

Hello, how are you, goodbye.
'''

    def getMailFrom(self):
        result = self.mailFrom
        self.mailFrom = None
        return result

    def getMailTo(self):
        return [self.mailTo]

    def getMailData(self):
        return StringIO.StringIO(self.mailData)

    def sentMail(self, code, resp, numOk, addresses, log):
        print 'Sent', numOk, 'messages'

class SMTPClientFactory(protocol.ClientFactory):
    protocol = SMTPTutorialClient

    def buildProtocol(self, addr):
        return self.protocol(secret=None, identity='example.com')

smtpClientFactory = SMTPClientFactory()

smtpClientService = internet.TCPClient('localhost', 8025, smtpClientFactory)
smtpClientService.setServiceParent(application)
reactor.stop()