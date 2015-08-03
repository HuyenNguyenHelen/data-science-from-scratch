import pandas as pd
from collections import Counter
from collections import defaultdict


#-----------------------
#finding key connectors

#create list of dictionaries where each dictionary is a user
users = [
	{"id": 0, "name": "Ashley"},
	{"id": 1, "name": "Ben"},
	{"id": 2, "name": "Conrad"},
	{"id": 3, "name": "Doug"},
	{"id": 4, "name": "Evin"},
	{"id": 5, "name": "Florian"},
	{"id": 6, "name": "Gerald"}
]

#apparently users is better. it's easier to sort, easier to search, and more compact.
users2 = {
	"id": [0, 1, 2, 3, 4, 5, 6],
	"name": ["Ashley", "Ben", "Conrad", "Doug","Evin", "Florian", "Gerald"]
	}

#when converted to pandas dataframes, both are identical 
pd_users = pd.DataFrame(users)
pd_users2 = pd.DataFrame(users2)


#create list of tuples where each tuple represents a friendships between ids
friendships = [(0,1), (0,2), (0,5), (1,2), (1,5), (2,3), (2,5), (3,4), (4,5), (4,6)]

#add friends key to each user 
for user in users:
	user["friends"] = []

#go through friendships and add each one to the friends key in users
for i, j in friendships:
	users[i]["friends"].append(j)
	users[j]["friends"].append(i)

#get number of connections
def number_of_friends(user):
	return len(user["friends"])

#total connections
total_connections = sum(number_of_friends(user) for user in users)

#average users
avg_connections =  total_connections / len(users)

#most connected users
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
num_friends_sorted = sorted(num_friends_by_id, key = lambda (user_id, num_friends) : num_friends, reverse = True)


#--------------------------------------
#data scientists you may know

def friends_of_friend_ids_bad(user): 
 	return [users[foaf]["id"]
    	for friend in user["friends"]
		for foaf in users[friend]["friends"]]

def friends_of_friends_ids_bad_2(user):
	foafs = []
	for friend in user["friends"]:
		for foaf in users[friend]["friends"]:
			foafs.append(foaf)
	return foafs

def not_the_same(user, other_user):
	return user["id"] != other_user["id"]

def not_friends(user, other_user):
    return all(not_the_same(users[friend], other_user) 
        for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(users[foaf]["id"]
        for friend in user["friends"]
        for foaf in users[friend]["friends"]
        if not_the_same(user, users[foaf]) and 
           not_friends(user, users[foaf]))

#interests
interests = [
	(0, "soccer"), (0, "tennis"), (1, "soccer"), (2, "tennis"), (3, "boxing"),
	(4, "soccer"), (5, "swimming"), (6, "swimming"), (6, "soccer"), (6, "tennis")]

def data_scientists_who_like(target_interest):
	scientists = []
	for i, j in interests:
		if j == target_interest:
			scientists.append(i)
	return scientists

def data_scientists_who_like_2(target_interest):
	return [user_id
		for user_id, user_interest in interests
		if user_interest == target_interest]

#build index from interests to users and from users to interests
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
	user_ids_by_interest[interest].append(user_id)

interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
	interests_by_user_id[user_id].append(interests)

#don't understand
def most_common_interests_with(user):
	return Counter(interested_user_id
		for interest in interests_by_user_id[user["id"]]
		for interested_user_id in user_ids_by_interest[interest]
		if interested_user_id != user["id"])

#------------------------------------
#salaries and experience

salaries_and_tenures = [(83000, 8.5), (88000, 8.1),
						(48000, 0.7), (76000, 6,),
						(69000, 6.5), (76000, 7.5)]

salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
	salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
	tenure: sum(salaries) / len(salaries)
	for tenure, salaries in salary_by_tenure.items()
}

#bucket the tenures since all different
def tenure_bucket(tenure):
	if tenure < 2:
		return "less than two"
	elif tenure < 5:
		return "between two and five"
	else:
		return "more than five"

salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
	bucket = tenure_bucket(tenure)
	salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {
	tenure_bucket: sum(salaries) / len(salaries)
	for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
}

#----------------------------------
#paid accounts

def predict_paid_or_unpaid(years_experience):
	if years_experience < 3.0:
		return "paid"
	elif years_experience < 8.5:
		return "unpaid"
	else:
		return "paid"


#------------------------------------
#topics of interest

interests = [
	(0, "Hadoop"), (0, "Big data"), (1, "Mathmeatics"),
	(2, "Hadoop"), (3, "Small Data"), (5, "Tennis")
]

words_and_counts = Counter(word
						   for user, interest in interests
						   for word in interest.lower().split())

for word, count in words_and_counts.most_common():
	if count > 1:
		print word, count





