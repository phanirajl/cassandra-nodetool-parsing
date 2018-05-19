#!/usr/bin/env python

import sys, json

#Datacenter: <dc>
#===...
#<irrelevant>
#<irrelevant>
#-- \t Address \t Load \t Tokens \t Owns (effective) \t Host ID \t Rack
#for every node
#  <state> \t <address> \t <load> \t <irrelevant> \t <irrelevant> \t <hostId> \t <rack>
#repeat for every datacenter from start

if sys.stdin.isatty():
	print "You must pipe the output of `nodetool status` into this script."
	print "Example: nodetool status | python script.py"
	sys.exit(1)

stdin = sys.stdin.read()
lines = stdin.splitlines()

#now we need to find the header line. Every line below that is a node
header = None
datacenter = None
keyHeader = "Host ID"
importantHeaders = ["--", "Address", "Load", "Rack"]
response = {}
for line in lines:
	#datacenter line signals a new datacenter starts from here
	if line.startswith("Datacenter:"):
		datacenter = line.split(" ")[1].strip()
	#check if we've already read a header. if so, likely a node so parse it
	if not header is None and not line.startswith("--"):
		node = line.split("  ")
		node = filter(None, node)
		node = [el.strip() for el in node]

		key = None
		value = {}
		for i in range(len(node)):
			if header[i] == keyHeader:
				key = node[i]
			if header[i] in importantHeaders:
				headerKey = header[i]
				if header[i] == "--":
					headerKey = "State"
				value[headerKey] = node[i]
		if not key is None:
			value["Datacenter"] = datacenter
			response[key] = value
	#check if it's a header. if so, parse it
	if line.startswith("--"):
		header = line.split("  ")
		header = filter(None, header)
		header = [el.strip() for el in header]
print json.dumps(response)
