url = input("URL: ").strip()
print(url)

#username = url.replace("https://twitter.com/", "")
#username = url.removeprefix("https://twitter.com/")

#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE)
if matches:
    print(f"Username: ", matches.group(1))

#print(f"Username: {username}")
