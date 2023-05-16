# packages: https://pypi.org/

#cowsay : pypi.org/projects/cowsay
# pip: package manager to install packages
# pip install cowsay
import cowsay
import sys

if len(sys.argv) == 2:
    #cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])

