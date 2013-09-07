import csv
from collections import defaultdict
from itertools import count

def export_data(data, fname):
    lines= []
    curr2id= defaultdict(count().next)
    for curr, curr_data in data.iteritems():
        for date, val in sorted(curr_data.iteritems(),key=lambda x:x[0]):
            date= date.strftime('%Y-%m-%d')
            lines.append({'id':curr2id[curr], 'curr':curr, 'date':date, 'val':val})
    
    with open(fname,'w') as f:
        writer= csv.DictWriter(f, 'id curr date val'.split())
        writer.writeheader()
        writer.writerows(lines)


