#!/usr/bin/python

import sys,requests,json

infocon_url = "https://www.dshield.org/api/infocon?json"

infocon = requests.get(infocon_url).json()

if infocon['status'] == "green":
        print "OK - Infocon is: %s." % infocon['status']
        sys.exit(0)
elif infocon['status'] == "orange":
        print "WARNING - Infocon is: %s." % infocon['status']
        sys.exit(1)
elif infocon['status'] == "yellow":
        print "WARNING - Infocon is: %s." % infocon['status']
        sys.exit(1)
elif infocon['status'] == "red":
        print "CRITICAL - Infocon is: %s." % infocon['status']
        sys.exit(2)
else:
        print "UKNOWN - Infocon is: %s." % infocon['status']
        sys.exit(3)

