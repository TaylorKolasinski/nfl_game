import json

json_data = open('from_2000.json')
data = json.load(json_data)

first = []
second = []
third = []
fourth = []

firsts = []


# Sort data
for game in data:
	firsts.append(sorted(game['first_q']))


first_checked = []
first_totals = []
for game in firsts:
	if game in first_checked:
		for total in first_totals:
			if total['score'] == game:
				total['count'] += 1
	else:
		first_totals.append({'count': 1, 'score': game})
		first_checked.append(game)

# print first_totals

# Calculate totals
total_count = 0
for total in first_totals:
	total_count += total['count']

for count in first_totals:
	per = float(count['count'])/float(total_count)
	print count['score']
	print per * 100




# with open('total_stream_final.json', 'w') as outfile:
# 	json.dump(total_stream, outfile)