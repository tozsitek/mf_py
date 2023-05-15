import statistics
import sys

print(statistics.mean([100,90]))


# command line arguments
# library of "sys"
#try:
 #   print("hello, my name is", sys.argv[1])
#except IndexError:
 #   print("Too few arguments")

#  one variety
#if len(sys.argv) < 2:
 #   print("Too few arguments")
#elif len(sys.argv) > 2:
#    print("Too many arguments")
#else:
#    print("hello, my name is", sys.argv[1])

# another variety
""" if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1]) """


for arg in sys.argv[1:]:
    print("hello, my name is: ", arg)


