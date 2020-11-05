import re
from urllib.request import urlopen
from collections import Counter

data = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
results = sorted(re.findall(r"<code>(.*?)</code>", data))
counter = Counter(results).most_common()

with open("result.txt", 'w') as res:
    for x in counter:
        res.write(x[0] + " ")