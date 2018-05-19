#!/usr/bin/env python

import sys

#Datacenter: <dc>
#===...
#<irrelevant>
#<irrelevant>
#-- \t Address \t Load \t Tokens \t Owns (effective) \t Host ID \t Rack
#for every node
#  <state> \t <address> \t <load> \t <irrelevant> \t <irrelevant> \t <hostId> \t <rack>


lines = sys.stdin.read().splitlines()

#the first thing we care about is the datacenter we're in
datacenter = [el for el in lines if el.startswith("Datacenter:")][0]
print datacenter

#now we need to find the header line. Every line below that is a node
header = None
for line in lines:
	if not header is None:
		node = line.split("  ")
		node = filter(None, node)
		node = [el.strip() for el in node]
		for item in node:
			print "!" + item + "!"
	if line.startswith("--"):
		header = line.split("  ")
		header = filter(None, header)
		header = [el.strip() for el in header]
