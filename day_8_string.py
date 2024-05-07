msg = "Hi, all"

# Case methods
print(msg.upper())
print(msg.lower())
print(msg.title())
print(msg.capitalize())


quote = "      Dream is not something that you see in sleep, Dream is something that does not let you sleep"

print(quote)
print(quote.strip())


quote1 = "----Dream is not something-that you see in sleep, Dream is something that does not let you sleep----"

print(quote1.strip("-"))
print(quote1.lstrip("-"))
# print(quote1.rstrip("-"))

quote = "Dream is not something that you see in sleep, Dream is something that does not let you sleep"

print(quote[0])
# print(quote[0])='Y' error:immutable
# quote = 'cool'

print(quote.find("**"))

print(quote.replace("Dream", "is"))

print(quote.replace("Dream", "is"))
print(quote)


message = "    🚨🔍📱🔑secret_code✌️"
code = "SECRET_CODE✌️"

key_index = message.find("🔑")

output = message[key_index + 1 :].upper().strip("*").upper()

if output == code:
    print("you are an hacker")
else:
    print("Try again")

# to remove junk
message1 = "    🚨🔍📱🔑****secret_code✌️((("
print(message1.strip("  🚨🔍📱🔑*(✌️"))
