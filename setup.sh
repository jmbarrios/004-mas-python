#!/bin/bash
apt install python-numpy
pip3 install pytest git+https://github.com/jmbarrios/hw-conversion.git

# Convert homework to script
hwconvert
