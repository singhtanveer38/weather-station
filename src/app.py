import snowflake.connector
import credentials
from datetime import datetime
import fetch
import time

conn = snowflake.connector.connect(user=credentials.user, password=credentials.password, account=credentials.account)
curr = conn.cursor()

try:
	curr.execute("use role sysadmin")
	print("Using role sysadmin")
	
	curr.execute(f"use database {credentials.db}")
	print(f"Using database {credentials.db}")

	curr.execute(f"use warehouse {credentials.wh}")
	print(f"Using {credentials.wh} warehouse")

	while True:
		weather = fetch.fetch()

		dt = datetime.fromtimestamp(weather["dt"]).strftime("%Y-%m-%d %H:%M:%S")
		temp = weather["main"]["temp"]
		sunrise = datetime.fromtimestamp(weather["sys"]["sunrise"]).strftime("%Y-%m-%d %H:%M:%S")
		sunset = datetime.fromtimestamp(weather["sys"]["sunset"]).strftime("%Y-%m-%d %H:%M:%S")
		description = weather["weather"][0]["description"]

		curr.execute(f"insert into {credentials.table} values ('{dt}', {temp}, '{sunrise}', '{sunset}', '{description}')")

		print(f'{dt}, {temp}, {sunrise}, {sunset}, {description}')

		time.sleep(600)

	conn.close()

except Exception as e:
	print(e)
