
import re

str = "Please contact info@sololearn.com for assistance"
padrao = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

match = re.search(padrao, str)
if match:
	print(match.group())