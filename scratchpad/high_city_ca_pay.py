# The top 100 California city employees by per-capita total wages
# across 2009 to 2013 (the most recent year as of publish date) salary data
# Modification to scripts/100.py
import csv
import requests
from io import BytesIO
from zipfile import ZipFile
YEARS = range(2009,2014)
def foosalary(row):
    return float(row['Total Wages']) / int(row['Entity Population'])
rows = []
for year in YEARS:
    url = 'http://publicpay.ca.gov/Reports/RawExport.aspx?file=%s_City.zip' % year
    print("Downloading:", url)
    resp = requests.get(url)
    with ZipFile(BytesIO(resp.content)) as zfile:
        fname = zfile.filelist[0].filename # 2012_City.csv
        print("\tUnzipping:", fname)
        # first 4 lines are Disclaimer lines
        # only print line[4] (i.e. the headers) if this is the first iteration
        xs = 4 if year == YEARS.start else 5
        rows.extend(zfile.read(fname).decode('latin-1').splitlines()[xs:])
# This massive array shouldn't cause your (modern) computer to crash...
print("Filtering %s rows..." % len(rows))
# remove rows without 'Total Wages'
employees = [r for r in csv.DictReader(rows) if r['Total Wages']]
templine = "{year}:\t{city}, {dept}; {position}:\t${money}"
for e in sorted(employees, key = foosalary, reverse = True)[0:100]: # show top 100
    line = templine.format(year = e['Year'], city = e['Entity Name'],
                    dept = e["Department / Subdivision"], position = e['Position'],
                    money = int(foosalary(e)))
    print(line)


# If you're a fan of True Detective Season 2, the output might ring a bell:
# http://www.latimes.com/local/california/la-me-vernon-true-detective-20150619-story.html
#
# 2010: Vernon, Finance; Finance Director:  $3572
# 2009: Vernon, Light & Power Administration; Director of Light & Power:  $3405
# 2012: Vernon, Fire; Fire Chief: $3312
# 2009: Vernon, City Attorney; City Attorney: $3115
# 2009: Vernon, Finance; Finance Director:  $3086
# 2009: Vernon, Office of Special Counsel; Special Counsel: $2912
# 2009: Vernon, City Attorney; Assistant City Attorney III: $2688
# 2010: Vernon, L&P Administration; Director of Light & Power Capital Projects: $2596
# 2010: Vernon, City Attorney; Assistant City Attorney III: $2455
# 2010: Vernon, Industrial Development; Assistant Director of Industrial Development: $2330
# 2011: Vernon, Finance; Finance Director:  $2321
# 2012: Vernon, Light And Power Administration; Director Of Light & Power:  $2318
# 2013: Vernon, City Administration; City Administrator:  $2224
# 2013: Vernon, Light And Power Administration; Director Of Light & Power:  $2218
# 2009: Vernon, Industrial Development; Assistant Director of Industrial Development: $2189
# 2009: Vernon, City Attorney; Chief Deputy City Attorney:  $2137
# 2013: Vernon, City Attorney; City Attorney: $2121
# 2009: Vernon, Administrative, Engineering & Planning; Director of Community Services: $2078
# 2013: Vernon, Fire; Fire Chief: $1982
# 2011: Vernon, City Attorney; Chief Deputy City Attorney:  $1979
# 2010: Vernon, City Attorney; Chief Deputy City Attorney:  $1969
# 2013: Vernon, Administrative, Engineering & Planning; Director Of Community Services: $1945
# 2010: Vernon, Administrative, Engineering & Planning; Director of Community Services: $1930
# 2009: Vernon, Fire; Fire Chief: $1928
# 2012: Vernon, City Attorney; Chief Deputy City Attorney:  $1905
# 2011: Vernon, Administrative, Engineering & Planning; Director Of Community Services & Water: $1903
# 2009: Vernon, Police; Chief:  $1875
# 2011: Vernon, Fire; Fire Chief: $1857
# 2013: Vernon, Light And Power Engineering; Engineering Manager: $1834
# 2012: Vernon, Light And Power Engineering; Engineering Manager: $1783
# 2009: Vernon, Health; Health Officer/Director Of Health & Environmental Control:  $1782
# 2013: Vernon, Fire; Battalion Chief:  $1769
# 2009: Vernon, Police; Sergeants:  $1758
# 2010: Vernon, Fire; Fire Chief: $1743
# 2012: Vernon, Finance; Finance Director:  $1737
# 2013: Vernon, Police; Police Chief: $1728
# 2011: Vernon, L&P Engineering; Engineering Manager: $1712
# 2012: Vernon, Police; Police Chief: $1693
# 2013: Vernon, Finance; Finance Director:  $1691
# 2009: Vernon, Fire; Assistant Fire Chief: $1687
# 2009: Vernon, Fire; Battalion Chief:  $1675
# 2010: Vernon, Police; Sergeants:  $1661
# 2012: Vernon, Fire; Captain:  $1648
# 2011: Vernon, Health; Director Health & Environmental Control:  $1646
# 2010: Vernon, Health; Director Health & Environmental Control:  $1642
# 2012: Vernon, Administrative, Engineering & Planning; Director Of Community Services: $1630
# 2013: Vernon, Health; Director Health & Environmental Control:  $1623
# 2011: Vernon, Fire; Assistant Fire Chief: $1623
# 2013: Vernon, Fire; Battalion Chief:  $1620
# 2011: Vernon, Fire; Battalion Chief:  $1619
# 2013: Vernon, Human Resources; Director Of Human Resources: $1605
# 2009: Vernon, Fire; Battalion Chief:  $1592
# 2011: Vernon, L&P Administration; Director Of Light & Power:  $1589
# 2012: Vernon, Fire; Battalion Chief:  $1589
# 2012: Vernon, Health; Director Health & Environmental Control:  $1583
# 2010: Vernon, Fire; Battalion Chief:  $1577
# 2013: Vernon, Fire; Battalion Chief:  $1576
# 2009: Vernon, Police; Captain:  $1576
# 2010: Vernon, Police; Police Chief: $1559
# 2012: Vernon, Fire; Battalion Chief:  $1556
# 2012: Vernon, Fire; Battalion Chief:  $1552
# 2009: Vernon, Police; Captain:  $1551
# 2009: Vernon, Resource Planning; Electric Resources Planning And Development Manager: $1548
# 2009: Vernon, System Dispatch; Transmission & Distribution Manager: $1547
# 2013: Vernon, Resources Planning; Electric Resource Planning & Development Manager: $1539
# 2009: Vernon, Fire; Captain:  $1529
# 2010: Vernon, Fire; Assistant Fire Chief: $1528
# 2012: Vernon, Fire; Battalion Chief:  $1527
# 2013: Vernon, City Attorney; Chief Deputy City Attorney:  $1520
# 2010: Vernon, Police; Interim Police Chief: $1516
# 2011: Vernon, Fire; Battalion Chief:  $1504
# 2009: Vernon, Fire; Fire Marshall:  $1499
# 2009: Vernon, Police; Police Officer: $1498
# 2009: Vernon, Fire; Battalion Chief:  $1497
# 2009: Vernon, Fire; Regional Training Captain:  $1494
# 2009: Vernon, Fire; Captain:  $1492
# 2009: Vernon, Police; Sergeants:  $1488
# 2009: Vernon, Light & Power Engineering; Engineering Manager: $1488
# 2009: Vernon, Fire; Captain:  $1484
# 2010: Vernon, Fire; Battalion Chief:  $1470
# 2009: Vernon, Police; Police Officer: $1457
# 2013: Vernon, Fire; Captain:  $1451
# 2013: Vernon, Resources Planning; Resource Scheduler: $1450
# 2012: Vernon, City Administration; Assistant To The City Administrator: $1450
# 2011: Vernon, Resources Planning; Electric Resources Planning And Development Manager:  $1449
# 2010: Vernon, System Dispatch; Transmission & Distribution Manager: $1448
# 2012: Vernon, Resources Planning; Electric Resource Planning & Development Manager: $1446
# 2012: Vernon, Fire; Fire Marshall:  $1445
# 2012: Vernon, Fire; Engineer: $1440
# 2010: Vernon, L&P Engineering; Engineering Manager: $1437
# 2009: Vernon, Police; Sergeants:  $1437
# 2013: Vernon, Fire; Captain:  $1435
# 2013: Vernon, Fire; Captain:  $1434
# 2010: Vernon, Fire; Battalion Chief:  $1433
# 2012: Vernon, Fire; Engineer: $1427
# 2009: Vernon, Fire; Captain:  $1423
# 2009: Vernon, Fire; Captain:  $1420
# 2009: Vernon, Fire; Captain:  $1415
# 2009: Vernon, Fire; Captain:  $1414
# 2013: Vernon, Fire; Captain:  $1413
