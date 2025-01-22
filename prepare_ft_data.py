import pandas as pd

def main():

	raw_df = pd.read_csv('about_supermart.csv')

	print(raw_df.info())
	print(raw_df.shape)

	f = open("ft_messages.jsonl","w")

	messages = {}
	role = ''

	for ind, row in raw_df.iterrows():

		ft_message = '{"messages": [{"role":"system","content" : "You are assistant with knowledge of online retailer SuperMart"},'
#	#	print(ft_message)

		ft_message += '{"user":"' + str(row['user_content']) + '"},'
		ft_message += '{"assistant":"' + str(row['assistant_content']) + '"}]}'
		f.write(ft_message)
		print(ft_message)
		ft_message = ''

	f.close()

if __name__== "__main__":
   main()

