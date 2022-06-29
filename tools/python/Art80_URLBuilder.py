# Hi.  THis program looks through a summary of the BPDA's Article 80 project review log.
# It tries to figure out the URL for a project based on its name.  It applies some RegX
# magic to form the string, and then it checks the return status of the URL.  
# A copy of the table is made with new values in for the corrected name string and for the 
# return status and the full URL.  
# 
# By just replacing spaces with strings It works for about 745 of the 2165 records. 
# Subsequently, if you change the RegX logic it will test any URL for records whose 
# corrected name has changed.
#
# 

import csv, requests, re

# This wouild be a summary of the Salesforce dump produced by the ArcGIS model, Initialize Art80 Log 
salesforce_csvfile = r'F:\current_work\projects\Boston\Bos3d\Bos3dDevpbc\Workflows\ModelMgt_20201214\Sources\art80_SalesForce\A80_log_20210121_c.csv'

output_csvfile = r'F:\current_work\projects\Boston\Bos3d\Bos3dDevpbc\Workflows\ModelMgt_20201214\Sources\art80_SalesForce\tmp_A80_log_urls20210121.csv'

urlbase = 'http://www.bostonplans.org/projects/development-projects/'


# Test the requests module. This module probably needs to be installed in your Python environment. 
# myUrl = 'https://api.github.com/events'
# r = requests.get(myUrl)
# print("URL: " + myUrl + " Status: " + str(r.status_code))


with open(salesforce_csvfile, mode='r', encoding='utf-8-sig') as incsv,  \
     open(output_csvfile, 'w', newline='') as outcsv:
#with open(salesforce_csvfile, mode='r') as csvfile:
    print('Opening input CSV')
    spamreader = csv.DictReader(incsv, delimiter=',')
    colnames = spamreader.fieldnames
    print('Opening Output CSF ') 
    spamwriter = csv.DictWriter(outcsv, fieldnames=colnames)
    spamwriter.writeheader()
    count = 0
    for row in spamreader:
        count +=1
        #print("Hello")
        #print (row.keys())
        urltarget = row['Name']
        urltarget = re.sub(r" - ", "-", urltarget)
        urltarget = re.sub(r"\s+", "-", urltarget)
        urltarget = urltarget.replace("'","-")
        full_url = urlbase + urltarget
        newrow = row 

        r = requests.get(full_url)
        stat = r.status_code
        newrow['URL_Stat'] = stat
        newrow['A80_URL'] = full_url
        newrow['URL_Base'] = urltarget

        spamwriter.writerow(newrow)

        print(str(count) + ' Status: ' + str(stat) + ' Project ID is:' + str(int(float((newrow ['A80_Proj_ID'])))) + ' Name is  ' + newrow['Name'] + ' URL Target: ' + newrow['URL_Base']) 

        #print(str(count) + ' Status: ' + str(r.status_code) + ' Project ID is:' + str(int(float((row ['A80_Proj_ID'])))) + ' Name is  ' + row['LAST_Name'] + ' URL Target: ' + urltarget) 



