import rt
import sys
import getopt
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('rt-rest.ini')

url = parser.get('rt-rest', 'url')
username = parser.get('rt-rest', 'username')
password = parser.get('rt-rest', 'password')

try:
    opts, args = getopt.getopt(sys.argv[1:], "tra", ["ticket=", "reply=", "filename="])

except getopt.GetoptError:
    sys.exit(2)

reply = ""
filename = ""
ticket = ""

for opt, arg in opts:
    if opt in ("-t", "--ticket"):
        ticket = arg
    elif opt in ("-r", "--reply"):
        reply = arg
    elif opt in ("-a", "--filename"):
        filename = arg

if username and password:
    tracker = rt.Rt('https://consult.tacc.utexas.edu/REST/1.0/', username, password, basic_auth=(username, password))
    tracker.login()

    print tracker.get_ticket(ticket)

    attachment = open(filename, 'r')

    print tracker.reply(ticket, reply, '', '', ([filename,attachment],))

    attachment.close()
