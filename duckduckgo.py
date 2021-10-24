# import requests
# import pytest
import pytest
import requests

ddg_url = "https://duckduckgo.com/?q=presidents+of+the+united+states&format=json"

# Last names of presidents with no duplicates. For example: Bush is only there once.
list_of_presidents = ['Adams', 'Arthur', 'Biden', 'Buchanan', 'Bush', 'Carter', 'Cleveland', 'Clinton', 'Coolidge',
                      'Eisenhower', 'Fillmore', 'Ford', 'Garfield', 'Grant', 'Harding', 'Harrison', 'Hayes', 'Hoover',
                      'Taft', 'Jackson', 'Jefferson', 'Johnson', 'Kennedy', 'Lincoln', 'Madison', 'McKinley', 'Monroe',
                      'Nixon', 'Obama', 'Pierce', 'Polk', 'Reagan', 'Roosevelt', 'Taylor', 'Truman', 'Trump', 'Tyler',
                      'Van Buren', 'Washington', 'Wilson']

resp = requests.get(ddg_url)
resp_data = resp.json()
wiki_data = resp_data['RelatedTopics']
all_presidents = []

for line in wiki_data:
 all_presidents.append(line['Text'])

all_presidents_combined = ' '.join(all_presidents)


@pytest.mark.parametrize("president", list_of_presidents)
def test_ddg(president):
 assert president in all_presidents_combined
