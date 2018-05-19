# Overview

Collection of simple Python scripts for parsing common nodetool commands. Mainly aimed to turn the output into something standard to use in automated monitoring, alarm systems, etc.

## Prerequisites

Requires Python. Only tested on v2.x currently.

## Usage

### parseNodetoolStatus.py

Used to parse output from `nodetool status` commands into JSON. Does not bother with the majority of the items in the command, but can be customised by editing the script and changing `importantHeaders`.

Usage: `nodetool status | python parseNodetoolStatus.py`

Will output JSON formatted data to stdout.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
