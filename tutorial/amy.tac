from twisted.application import service, internet
from twisted.internet import protocol
from twisted.mail import smtp

application = service.Application('SMTP Client Tutorial')
smtpClientFactory = protocol.ClientFactory()
smtpClientService = internet.TCPClient('local', 8025, smtpClientFactory)
smtpClientFactory.protocol = protocol.Protocol

class SMTPClientFactory(protocol.ClientFactory):
      protocol = smtp.ESMTPClient
      
      def buildProtocol(self, addr):
          return self.protocol(secret = None, identity='example.com')

class SMTPTutorialClient(smtp.ESMTPClient):
      mailFrom = 'tutorial_sender@example.cim'
      mailTo = 'tutorial_recipient@localhost'
      mailData = '''\
      a sample email with stuff in it
      '''

      def getMailFrom(self):
          result =selg.mailFrom
          self.mailFrom = None
          return result 

      def getMailTo(self):
          return [self.mailTo]

      def getMailData(self):
          return StringIO.StringIO(self.mailData)

      def sentMail(self, code, resp, numOK, addressess, log):
          print 'Sent', numOk, 'messages'
    
    
smtpClientFactory = SMTPClientFactory()

