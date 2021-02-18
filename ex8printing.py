formatter = "{} {} {} {}"

print(formatter.format(1,3,4,6))
print(formatter.format("one", "two", "five", "nine"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
  "Try your\n",
  "Own text there",
  "May be a poem",
  "Or a song about fear"
))

# debug with just running a print on the entries
print("xxxx printing just the strings, no formatting: ")
print("Try your"
"Own text there",
"May be a poem",
"Or a song about fear")
#missing comma after the first string
lines = (
  "Try your"
  "Own text there",
  "May be a poem",
  "Or a song about fear"
)
print(">>>>> lines", lines)
print("xxxx reper lines next xxxx")
print(">>>>> lines", repr(lines))
print(formatter.format(*lines))
