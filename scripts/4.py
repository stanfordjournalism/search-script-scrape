# The number of librarian-related job positions that the federal government is currently hiring for
import requests
# via http://www.opm.gov/policy-data-oversight/classification-qualifications/general-schedule-qualification-standards/#url=List-by-Occupational-Series
LIBSERIES = 1410
resp = requests.get("https://data.usajobs.gov/api/jobs", params = {'series': LIBSERIES})
print(resp.json()['TotalJobs'])
