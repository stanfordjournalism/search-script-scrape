## Search-Script-Scrape: 101 webscraping and research tasks for the data journalist

__Note:__ This exercise set is part of the [Stanford Computational Journalism Lab](http://cjlab.stanford.edu). I've also written [a blog post that gives a little more elaboration about the libraries used and a few of the exercises](http://blog.danwin.com/examples-of-web-scraping-in-python-3-x-for-data-journalists/).

-------------

This repository contains [101 Web data-collection tasks](#the-tasks) in Python 3 that I assigned to my [Computational Journalism class in Spring 2015](http://www.compjour.org) to give them regular exercise in programming and conducting research, and to expose them to the variety of data published online.

The hard part of many of these tasks is researching and finding the actual data source. The scripts need only concern itself with fetching the data and printing the answer in the least painful way possible. Since the [Computational Journalism class](http://www.compjour.org) wasn't intended to be an actual programming class, adherence to idioms and best codes practices was not emphasized...(especially since I'm new to Python myself!)

Some examples of the tasks:

- [The California city whose city manager has the highest total wage per capita in 2012](https://github.com/compjour/search-script-scrape/blob/master/scripts/100.py) ([expanded version](scratchpad/high_city_ca_pay.py))
- [In the most recently transcribed Supreme Court argument, the number of times laughter broke out](https://github.com/compjour/search-script-scrape/blob/master/scripts/50.py) ([expanded version](scratchpad/more_scotus_laughs.py))
- [Number of days until Texas's next scheduled execution](scripts/29.py)
- [The U.S. congressmember with the most Twitter followers](https://github.com/compjour/search-script-scrape/blob/master/scripts/90.py)
- [The number of people who visited a U.S. government website using Internet Explorer 6.0 in the last 90 days](https://github.com/compjour/search-script-scrape/blob/master/scripts/3.py)

## Repo status


The table below links to the available scripts. If there's not a link, it means I haven't committed the code. Some of them I had to rethink a less verbose solution (or the target changed, as the Internet sometimes does), and now this repo has taken a backseat to many other data projects on my list. `¯\_(ツ)_/¯` 

Note: A lot of the code is not best practice. The tasks are a little repetitive so I got bored and [ignored PEP8](https://www.python.org/dev/peps/pep-0008/) and/or tried new libraries/conventions for fun.


__Note:__ The "__related URL__" links to either the official source of the data, or at least a page with some background information. The second column of this table refers to __line count__ of the script, __not__ the answer to the prompt.

## The tasks

<!--begintasks-->
The repo currently contains scripts for __100__ of __101__ tasks:

|          Title          |  Line count |
|-------------------------|-------------|
| 1. <i id='task-1'></i>Number of datasets currently listed on data.gov <br> <a href='http://catalog.data.gov/dataset'>[related URL]</a>&nbsp;<a href='scripts/1.py'>[script]</a> |  7 lines |
| 2. <i id='task-2'></i>The name of the most recently added dataset on data.gov <br> <a href='http://catalog.data.gov/dataset?q=&sort=metadata_created+desc'>[related URL]</a>&nbsp;<a href='scripts/2.py'>[script]</a> |  7 lines |
| 3. <i id='task-3'></i>The number of people who visited a U.S. government website using Internet Explorer 6.0 in the last 90 days <br> <a href='https://analytics.usa.gov/data/live/ie.json'>[related URL]</a>&nbsp;<a href='scripts/3.py'>[script]</a> |  4 lines |
| 4. <i id='task-4'></i>The number of librarian-related job positions that the federal government is currently hiring for <br> <a href='https://data.usajobs.gov/api/jobs?series=1410'>[related URL]</a>&nbsp;<a href='scripts/4.py'>[script]</a> |  6 lines |
| 5. <i id='task-5'></i>The name of the company cited in the most recent consumer complaint involving student loans <br> <a href='https://data.consumerfinance.gov/dataset/Student-loan-complaints/c8k9-ryca'>[related URL]</a>&nbsp;<a href='scripts/5.py'>[script]</a> |  27 lines |
| 6. <i id='task-6'></i>From 2010 to 2013, the change in median cost of health, dental, and vision coverage for California city employees <br> <a href='http://publicpay.ca.gov/Reports/RawExport.aspx'>[related URL]</a>&nbsp;<a href='scripts/6.py'>[script]</a> |  38 lines |
| 7. <i id='task-7'></i>The number of listed federal executive agency internet domains <br> <a href='https://inventory.data.gov/dataset/federal-executive-agency-internet-domains-as-of-06172014/resource/b626ef1f-9019-41c4-91aa-5ae3f7457328'>[related URL]</a>&nbsp;<a href='scripts/7.py'>[script]</a> |  8 lines |
| 8. <i id='task-8'></i>The number of times when a New York heart surgeon's rate of patient deaths for all cardiac surgical procedures was "significantly higher" than the statewide rate, according to New York state's analysis. <br> <a href='https://health.data.ny.gov/Health/Cardiac-Surgery-by-Surgeon-Beginning-2008/dk4z-k3xb'>[related URL]</a>&nbsp;<a href='scripts/8.py'>[script]</a> |  7 lines |
| 9. <i id='task-9'></i>The number of roll call votes that were rejected by a margin of less than 5 votes, in the first session of the U.S. Senate in the 114th Congress <br> <a href='http://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_114_1.htm'>[related URL]</a>&nbsp;<a href='scripts/9.py'>[script]</a> |  26 lines |
| 10. <i id='task-10'></i>The title of the highest paid California city government position in 2010 <br> <a href='http://publicpay.ca.gov/Reports/RawExport.aspx'>[related URL]</a>&nbsp;<a href='scripts/10.py'>[script]</a> |  35 lines |
| 11. <i id='task-11'></i>How much did the state of California collect in property taxes, according to the U.S. Census 2013 Annual Survey of State Government Tax Collections? <br> <a href='http://www.census.gov/govs/statetax/historical_data.html'>[related URL]</a>&nbsp;<a href='scripts/11.py'>[script]</a> |  23 lines |
| 12. <i id='task-12'></i>In 2010, the year-over-year change in enplanements at America's busiest airport <br> <a href='http://www.faa.gov/airports/planning_capacity/passenger_allcargo_stats/passenger/?year=2010'>[related URL]</a>&nbsp;<a href='scripts/12.py'>[script]</a> |  51 lines |
| 13. <i id='task-13'></i>The number of armored carrier bank robberies recorded by the FBI in 2014 <br> <a href='http://www.fbi.gov/stats-services/publications/bank-crime-statistics-2014/bank-crime-statistics-2014'>[related URL]</a>&nbsp;<a href='scripts/13.py'>[script]</a> |  15 lines |
| 14. <i id='task-14'></i>The number of workplace fatalities at reported to the federal and state OSHA in the latest fiscal year <br> <a href='https://www.osha.gov/dep/fatcat/dep_fatcat.html'>[related URL]</a>&nbsp;<a href='scripts/14.py'>[script]</a> |  14 lines |
| 15. <i id='task-15'></i>Total number of wildlife strike incidents reported at San Francisco International Airport <br> <a href='http://wildlife.faa.gov/database.aspx'>[related URL]</a>&nbsp;<a href='scripts/15.py'>[script]</a> |  48 lines |
| 16. <i id='task-16'></i>The non-profit organization with the highest total revenue, according to the latest listing in ProPublica's Nonprofit Explorer <br> <a href='https://projects.propublica.org/nonprofits/'>[related URL]</a>&nbsp;<a href='scripts/16.py'>[script]</a> |  11 lines |
| 17. <i id='task-17'></i>In the "Justice News" RSS feed maintained by the Justice Department, the number of items published on a Friday <br> <a href='http://www.justice.gov/doj/news-feeds'>[related URL]</a>&nbsp;<a href='scripts/17.py'>[script]</a> |  11 lines |
| 18. <i id='task-18'></i>The number of U.S. congressmembers who have Twitter accounts, according to Sunlight Foundation data <br> <a href='https://sunlightlabs.github.io/congress/#legislator-spreadsheet'>[related URL]</a>&nbsp;<a href='scripts/18.py'>[script]</a> |  9 lines |
| 19. <i id='task-19'></i>The total number of preliminary reports on aircraft safety incidents/accidents in the last 10 business days <br> <a href='http://www.asias.faa.gov/pls/apex/f?p=100:93:0::NO:::'>[related URL]</a>&nbsp;<a href='scripts/19.py'>[script]</a> |  12 lines |
| 20. <i id='task-20'></i>The number of OSHA enforcement inspections involving Wal-Mart in California since 2014 <br> <a href='https://www.osha.gov/pls/imis/establishment.html'>[related URL]</a>&nbsp;<a href='scripts/20.py'>[script]</a> |  25 lines |
| 21. <i id='task-21'></i>The current humidity level at Great Smoky Mountains National Park <br> <a href='http://www.nature.nps.gov/air/WebCams/parks/grsmcam/grsmcam.cfm'>[related URL]</a>&nbsp;<a href='scripts/21.py'>[script]</a> |  6 lines |
| 22. <i id='task-22'></i>The names of the committees that Sen. Barbara Boxer currently serves on <br> <a href='http://www.senate.gov/general/committee_assignments/assignments.htm'>[related URL]</a>&nbsp;<a href='scripts/22.py'>[script]</a> |  7 lines |
| 23. <i id='task-23'></i>The name of the California school with the highest number of girls enrolled in kindergarten, according to the CA Dept. of Education's latest enrollment data file. <br> <a href='http://www.cde.ca.gov/ds/sd/sd/filesenr.asp'>[related URL]</a>&nbsp;<a href='scripts/23.py'>[script]</a> |  21 lines |
| 24. <i id='task-24'></i>Percentage of NYPD stop-and-frisk reports in which the suspect was white in 2014 <br> <a href='http://www.nyc.gov/html/nypd/html/analysis_and_planning/stop_question_and_frisk_report.shtml'>[related URL]</a>&nbsp;<a href='scripts/24.py'>[script]</a> |  24 lines |
| 25. <i id='task-25'></i>Average frontal crash star rating for 2015 Honda Accords <br> <a href='http://www.safercar.gov/Vehicle+Shoppers/5-Star+Safety+Ratings/2011-Newer+Vehicles/Search-Results?searchtype=model&make=HONDA&model=ACCORD&year='>[related URL]</a>&nbsp;<a href='scripts/25.py'>[script]</a> |  14 lines |
| 26. <i id='task-26'></i>The dropout rate for all of Santa Clara County high schools, according to the latest cohort data in CALPADS <br> <a href='http://www.cde.ca.gov/ds/sd/sd/filescohort.asp'>[related URL]</a>&nbsp;<a href='scripts/26.py'>[script]</a> |  48 lines |
| 27. <i id='task-27'></i>The number of Class I Drug Recalls issued by the U.S. Food and Drug Administration since 2012 <br> <a href='http://www.fda.gov/Drugs/DrugSafety/DrugRecalls/default.htm'>[related URL]</a>&nbsp;<a href='scripts/27.py'>[script]</a> |  14 lines |
| 28. <i id='task-28'></i>Total number of clinical trials as recorded by the National Institutes of Health <br> <a href='https://clinicaltrials.gov/'>[related URL]</a>&nbsp;<a href='scripts/28.py'>[script]</a> |  7 lines |
| 29. <i id='task-29'></i>Number of days until Texas's next scheduled execution <br> <a href='https://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html'>[related URL]</a>&nbsp;<a href='scripts/29.py'>[script]</a> |  24 lines |
| 30. <i id='task-30'></i>The total number of inmates executed by Florida since 1976 <br> <a href='http://www.dc.state.fl.us/oth/deathrow/execlist.html'>[related URL]</a>&nbsp;<a href='scripts/30.py'>[script]</a> |  10 lines |
| 31. <i id='task-31'></i>The number of proposed U.S. federal regulations in which comments are due within the next 3 days <br> <a href='http://regulationsgov.github.io/developers/console/'>[related URL]</a>&nbsp;<a href='scripts/31.py'>[script]</a> |  29 lines |
| 32. <i id='task-32'></i>Number of Titles that have changed in the United States Code since its last release point <br> <a href='http://uscode.house.gov/download/download.shtml'>[related URL]</a>&nbsp;<a href='scripts/32.py'>[script]</a> |  6 lines |
| 33. <i id='task-33'></i>The number of FDA-approved, but now discontinued drug products that contain Fentanyl as an active ingredient <br> <a href='http://www.accessdata.fda.gov/scripts/cder/ob/docs/tempai.cfm'>[related URL]</a>&nbsp;<a href='scripts/33.py'>[script]</a> |  14 lines |
| 34. <i id='task-34'></i>In the latest FDA Weekly Enforcement Report, the number of Class I and Class II recalls involving food <br> <a href='http://www.fda.gov/Safety/Recalls/EnforcementReports/default.htm'>[related URL]</a>&nbsp;<a href='scripts/34.py'>[script]</a> |  10 lines |
| 35. <i id='task-35'></i>Most viewed data set on New York state's open data portal as of this month <br> <a href='https://data.ny.gov/browse?sortBy=most_accessed&sortPeriod=month&utf8=%E2%9C%93'>[related URL]</a>&nbsp;<a href='scripts/35.py'>[script]</a> |  9 lines |
| 36. <i id='task-36'></i>Total number of visitors to the White House in 2012 <br> <a href='https://www.whitehouse.gov/briefing-room/disclosures/visitor-records'>[related URL]</a>&nbsp;<a href='scripts/36.py'>[script]</a> |  27 lines |
| 37. <i id='task-37'></i>The last time the CIA's Leadership page has been updated  <br> <a href='https://www.cia.gov/about-cia/leadership'>[related URL]</a>&nbsp;<a href='scripts/37.py'>[script]</a> |  6 lines |
| 38. <i id='task-38'></i>The domain of the most visited U.S. government website right now <br> <a href='https://analytics.usa.gov/data/live/top-pages-realtime.json'>[related URL]</a>&nbsp;<a href='scripts/38.py'>[script]</a> |  5 lines |
| 39. <i id='task-39'></i>Number of medical device recalls issued by the U.S. Food and Drug Administration in 2013 <br> <a href='http://www.fda.gov/MedicalDevices/Safety/ListofRecalls/ucm384618.htm'>[related URL]</a>&nbsp;<a href='scripts/39.py'>[script]</a> |  6 lines |
| 40. <i id='task-40'></i>Number of FOIA requests made to the Chicago Public Library <br> <a href='http://www.cityofchicago.org/city/en/depts/cpl/dataset/foialog.html'>[related URL]</a>&nbsp;<a href='scripts/40.py'>[script]</a> |  6 lines |
| 41. <i id='task-41'></i>The number of currently open medical trials involving alcohol-related disorders <br> <a href='https://clinicaltrials.gov/ct2/results?recr=Open&cond=%22Alcohol-Related+Disorders%22'>[related URL]</a>&nbsp;<a href='scripts/41.py'>[script]</a> |  5 lines |
| 42. <i id='task-42'></i>The name of the Supreme Court justice who delivered the opinion in the most recently announced decision <br> <a href='http://www.supremecourt.gov/'>[related URL]</a>&nbsp;<a href='scripts/42.py'>[script]</a> |  31 lines |
| 43. <i id='task-43'></i>The number of citations that resulted from FDA inspections in fiscal year 2012 <br> <a href='http://www.fda.gov/ICECI/Inspections/ucm346077.htm'>[related URL]</a>&nbsp;<a href='scripts/43.py'>[script]</a> |  10 lines |
| 44. <i id='task-44'></i>Number of people visiting a U.S. government website right now <br> <a href='https://analytics.usa.gov/data/live/realtime.json'>[related URL]</a>&nbsp;<a href='scripts/44.py'>[script]</a> |  6 lines |
| 45. <i id='task-45'></i>The number of security alerts issued by US-CERT in the current year <br> <a href='https://www.us-cert.gov/ncas/alerts'>[related URL]</a>&nbsp;<a href='scripts/45.py'>[script]</a> |  6 lines |
| 46. <i id='task-46'></i>The number of Pinterest accounts maintained by U.S. State Department embassies and missions <br> <a href='http://www.state.gov/r/pa/ode/socialmedia/'>[related URL]</a>&nbsp;<a href='scripts/46.py'>[script]</a> |  13 lines |
| 47. <i id='task-47'></i>The number of international travel alerts from the U.S. State Department currently in effect <br> <a href='http://travel.state.gov/content/passports/english/alertswarnings.html'>[related URL]</a>&nbsp;<a href='scripts/47.py'>[script]</a> |  7 lines |
| 48. <i id='task-48'></i>The difference in total White House staffmember salaries in 2014 versus 2010 <br> <a href='https://open.whitehouse.gov/Government/2010-Report-to-Congress-on-White-House-Staff/rcp4-3y7g'>[related URL]</a>&nbsp;<a href='scripts/48.py'>[script]</a> |  19 lines |
| 49. <i id='task-49'></i>Number of sponsored bills by Rep. Nancy Pelosi that were vetoed by the President <br> <a href='https://www.congress.gov/member/nancy-pelosi/P000197?q=%7B%22sponsorship%22%3A%22sponsored%22%7D'>[related URL]</a>&nbsp;<a href='scripts/49.py'>[script]</a> |  11 lines |
| 50. <i id='task-50'></i>In the most recently transcribed Supreme Court argument, the number of times laughter broke out <br> <a href='http://www.supremecourt.gov/oral_arguments/argument_transcript.aspx'>[related URL]</a>&nbsp;<a href='scripts/50.py'>[script]</a> |  22 lines |
| 51. <i id='task-51'></i>The title of the most recent decision handed down by the U.S. Supreme Court <br> <a href='http://www.supremecourt.gov/opinions/slipopinions.aspx'>[related URL]</a>&nbsp;<a href='scripts/51.py'>[script]</a> |  6 lines |
| 52. <i id='task-52'></i>The average wage of optomertrists according to the BLS's most recent National Occupational Employment and Wage Estimates report <br> <a href='http://www.bls.gov/oes/current/oes_nat.htm'>[related URL]</a>&nbsp;<a href='scripts/52.py'>[script]</a> |  8 lines |
| 53. <i id='task-53'></i>The total number of on-campus hate crimes as reported to the U.S. Office of Postsecondary Education, in the most recent collection year <br> <a href='http://ope.ed.gov/security/GetDownloadFile.aspx'>[related URL]</a>&nbsp;<a href='scripts/53.py'>[script]</a> |  45 lines |
| 54. <i id='task-54'></i>The number of people on FBI's Most Wanted List for white collar crimes <br> <a href='http://www.fbi.gov/wanted/wcc/@@wanted-group-listing'>[related URL]</a>&nbsp;<a href='scripts/54.py'>[script]</a> |  6 lines |
| 55. <i id='task-55'></i>The number of Government Accountability Office reports and testimonies on the topic of veterans <br> <a href='http://www.gao.gov/browse/topic/Veterans'>[related URL]</a>&nbsp;<a href='scripts/55.py'>[script]</a> |  10 lines |
| 56. <i id='task-56'></i>Number of times Rep. Darrell Issa's remarks have made it onto the Congressional Record <br> <a href='https://www.congress.gov/search?q=%7B%22source%22%3A%22congrecord%22%2C%22crHouseMemberRemarks%22%3A%22Issa%2C+Darrell+E.+%5BR-CA%5D%22%7D'>[related URL]</a>&nbsp;<a href='scripts/56.py'>[script]</a> |  9 lines |
| 57. <i id='task-57'></i>The top 3 auto manufacturers, ranked by total number of recalls via NHTSA safety-related defect and compliance campaigns since 1967. <br> <a href='http://www-odi.nhtsa.dot.gov/downloads/'>[related URL]</a>&nbsp;<a href='scripts/57.py'>[script]</a> |  24 lines |
| 58. <i id='task-58'></i>The number of published research papers from the NSA <br> <a href='https://www.nsa.gov/research/publications/index.shtml'>[related URL]</a>&nbsp;<a href='scripts/58.py'>[script]</a> |  6 lines |
| 59. <i id='task-59'></i>The number of university-related datasets currently listed at data.gov <br> <a href='http://catalog.data.gov/dataset?organization_type=University&sort=metadata_created+desc&q='>[related URL]</a>&nbsp;<a href='scripts/59.py'>[script]</a> |  7 lines |
| 60. <i id='task-60'></i>Number of chapters in Title 20 (Education) of the United States Code <br> <a href='http://uscode.house.gov/browse/prelim@title20/chapter9&edition=prelim'>[related URL]</a>&nbsp;<a href='scripts/60.py'>[script]</a> |  15 lines |
| 61. <i id='task-61'></i>The number of miles traveled by the current U.S. Secretary of State <br> <a href='http://www.state.gov/secretary/travel/index.htm'>[related URL]</a>&nbsp;<a href='scripts/61.py'>[script]</a> |  6 lines |
| 62. <i id='task-62'></i>For all of 2013, the number of potential signals of serious risks or new safety information that resulted from the FDA's FAERS <br> <a href='http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082196.htm'>[related URL]</a>&nbsp;<a href='scripts/62.py'>[script]</a> |  14 lines |
| 63. <i id='task-63'></i>In the current dataset behind Medicare's Nusring Home Compare website, the total amount of fines received by penalized nursing homes <br> <a href='https://data.medicare.gov/data/nursing-home-compare'>[related URL]</a>&nbsp;<a href='scripts/63.py'>[script]</a> |  35 lines |
| 64. <i id='task-64'></i>from March 1 to 7, 2015, the number of times in which designated FDA policy makers met with persons outside the U.S. federal executive branch <br> <a href='http://www.fda.gov/NewsEvents/MeetingsConferencesWorkshops/PastMeetingsWithFDAOfficials/ucm439318.htm'>[related URL]</a>&nbsp;<a href='scripts/64.py'>[script]</a> |  5 lines |
| 65. <i id='task-65'></i>The number of failed votes in the roll calls 1 through 99, in the U.S. House of the 114th Congress <br> <a href='http://clerk.house.gov/evs/2015/ROLL_000.asp'>[related URL]</a>&nbsp;<a href='scripts/65.py'>[script]</a> |  12 lines |
| 66. <i id='task-66'></i>The highest minimum wage as mandated by state law. <br> <a href='http://www.dol.gov/whd/minwage/america.htm'>[related URL]</a>&nbsp;<a href='scripts/66.py'>[script]</a> |  28 lines |
| 67. <i id='task-67'></i>For the most recently posted TSA.gov customer satisfication survey, post the percentage of respondents who rated their "overall experience today" as "Excellent" <br> <a href='http://www.tsa.gov/web-metrics'>[related URL]</a> |   |
| 68. <i id='task-68'></i>Number of FDA-approved prescription drugs with GlaxoSmithKline as the applicant holder <br> <a href='http://www.accessdata.fda.gov/scripts/cder/ob/docs/queryah.cfm'>[related URL]</a>&nbsp;<a href='scripts/68.py'>[script]</a> |  11 lines |
| 69. <i id='task-69'></i>The average number of comments on the last 50 posts on NASA's official Instagram account <br> <a href='https://instagram.com/nasa'>[related URL]</a>&nbsp;<a href='scripts/69.py'>[script]</a> |  40 lines |
| 70. <i id='task-70'></i>The highest salary possible for a White House staffmember in 2014 <br> <a href='https://open.whitehouse.gov/Government/2014-Report-to-Congress-on-White-House-Staff/i9g8-9web'>[related URL]</a>&nbsp;<a href='scripts/70.py'>[script]</a> |  10 lines |
| 71. <i id='task-71'></i>The percent increase in number of babies named Archer nationwide in 2010 compared to 2000, according to the Social Security Administration <br> <a href='http://www.ssa.gov/oact/babynames/limits.html'>[related URL]</a>&nbsp;<a href='scripts/71.py'>[script]</a> |  32 lines |
| 72. <i id='task-72'></i>The number of magnitude 4.5+ earthquakes detected worldwide by the USGS <br> <a href='http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php'>[related URL]</a>&nbsp;<a href='scripts/72.py'>[script]</a> |  8 lines |
| 73. <i id='task-73'></i>The total amount of contributions made by lobbyists to Congress according to the latest downloadable quarterly report <br> <a href='https://www.senate.gov/legislative/Public_Disclosure/contributions_download.htm'>[related URL]</a>&nbsp;<a href='scripts/73.py'>[script]</a> |  34 lines |
| 74. <i id='task-74'></i>The description of the bill most recently signed into law by the governor of Georgia <br> <a href='https://gov.georgia.gov/bills-signed'>[related URL]</a>&nbsp;<a href='scripts/74.py'>[script]</a> |  12 lines |
| 75. <i id='task-75'></i>Total number of officer-involved shooting incidents listed by the Philadelphia Police Department  <br> <a href='https://www.phillypolice.com/ois/'>[related URL]</a>&nbsp;<a href='scripts/75.py'>[script]</a> |  9 lines |
| 76. <i id='task-76'></i>The total number of publications produced by the U.S. Government Accountability Office <br> <a href='http://www.gao.gov/browse/date/custom'>[related URL]</a>&nbsp;<a href='scripts/76.py'>[script]</a> |  9 lines |
| 77. <i id='task-77'></i>Number of Dallas officer-involved fatal shooting incidents in 2014 <br> <a href='https://www.dallasopendata.com/resource/4gmt-jyx2.json'>[related URL]</a>&nbsp;<a href='scripts/77.py'>[script]</a> |  7 lines |
| 78. <i id='task-78'></i>Number of Cupertino, CA restaurants that have been shut down due to health violations in the last six months. <br> <a href='https://services.sccgov.org/facilityinspection/Closure/Index?sortField=sortbyEDate'>[related URL]</a>&nbsp;<a href='scripts/78.py'>[script]</a> |  6 lines |
| 79. <i id='task-79'></i>The change in total airline revenues from baggage fees, from 2013 to 2014 <br> <a href='http://www.rita.dot.gov/bts/sites/rita.dot.gov.bts/files/subject_areas/airline_information/baggage_fees/index.html'>[related URL]</a>&nbsp;<a href='scripts/79.py'>[script]</a> |  19 lines |
| 80. <i id='task-80'></i>The total number of babies named Odin born in Colorado according to the Social Security Administration <br> <a href='http://www.ssa.gov/oact/babynames/limits.html'>[related URL]</a>&nbsp;<a href='scripts/80.py'>[script]</a> |  20 lines |
| 81. <i id='task-81'></i>The latest release date for T-100 Domestic Market (U.S. Carriers) statistics report <br> <a href='http://www.transtats.bts.gov/releaseinfo.asp'>[related URL]</a>&nbsp;<a href='scripts/81.py'>[script]</a> |  13 lines |
| 82. <i id='task-82'></i>In the most recent FDA Adverse Events Reports quarterly extract, the number of patient reactions mentioning "Death" <br> <a href='http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm'>[related URL]</a>&nbsp;<a href='scripts/82.py'>[script]</a> |  47 lines |
| 83. <i id='task-83'></i>The sum of White House staffermember salaries in 2014 <br> <a href='https://open.whitehouse.gov/Government/2014-Report-to-Congress-on-White-House-Staff/i9g8-9web'>[related URL]</a>&nbsp;<a href='scripts/83.py'>[script]</a> |  12 lines |
| 84. <i id='task-84'></i>The total number of notices published on the most recent date to the Federal Register <br> <a href='https://www.federalregister.gov/articles/current'>[related URL]</a>&nbsp;<a href='scripts/84.py'>[script]</a> |  6 lines |
| 85. <i id='task-85'></i>The number of iPhone units sold in the latest quarter, according to Apple Inc's most recent 10-Q report <br> <a href='http://www.sec.gov/Archives/edgar/data/320193/000119312515023697/0001193125-15-023697-index.htm'>[related URL]</a>&nbsp;<a href='scripts/85.py'>[script]</a> |  49 lines |
| 86. <i id='task-86'></i>Number of computer vulnerabilities in which IBM was the vendor in the latest Cyber Security Bulletin  <br> <a href='https://www.us-cert.gov/ncas/bulletins'>[related URL]</a>&nbsp;<a href='scripts/86.py'>[script]</a> |  10 lines |
| 87. <i id='task-87'></i>Number of airports with existing construction related activity <br> <a href='https://nfdc.faa.gov/xwiki/bin/view/NFDC/Construction+Notices'>[related URL]</a>&nbsp;<a href='scripts/87.py'>[script]</a> |  6 lines |
| 88. <i id='task-88'></i>The number of posts on TSA's Instagram account <br> <a href='https://instagram.com/tsa/'>[related URL]</a>&nbsp;<a href='scripts/88.py'>[script]</a> |  24 lines |
| 89. <i id='task-89'></i>In fiscal year 2013, the short description of the most frequently cited type of FDA's inspectional observations related to food products. <br> <a href='http://www.fda.gov/ICECI/Inspections/ucm250720.htm'>[related URL]</a>&nbsp;<a href='scripts/89.py'>[script]</a> |  32 lines |
| 90. <i id='task-90'></i>The currently serving U.S. congressmember with the most Twitter followers <br> <a href=''>[related URL]</a>&nbsp;<a href='scripts/90.py'>[script]</a> |  76 lines |
| 91. <i id='task-91'></i>Number of stop-and-frisk reports from the NYPD in 2014 <br> <a href='http://www.nyc.gov/html/nypd/html/analysis_and_planning/stop_question_and_frisk_report.shtml'>[related URL]</a>&nbsp;<a href='scripts/91.py'>[script]</a> |  22 lines |
| 92. <i id='task-92'></i>In 2012-Q4, the total amount paid by Rep. Aaron Schock to Lobair LLC, according to Congressional spending records, as compiled by the Sunlight Foundation <br> <a href='https://sunlightfoundation.com/tools/expenditures/'>[related URL]</a>&nbsp;<a href='scripts/92.py'>[script]</a> |  14 lines |
| 93. <i id='task-93'></i>Number of Github repositories maintained by the GSA's 18F organization, as listed on Github.com <br> <a href='https://api.github.com/orgs/18F'>[related URL]</a>&nbsp;<a href='scripts/93.py'>[script]</a> |  5 lines |
| 94. <i id='task-94'></i>The New York City high school with the highest average math score in the latest SAT results <br> <a href='http://schools.nyc.gov/Accountability/data/TestResults/default.htm'>[related URL]</a>&nbsp;<a href='scripts/94.py'>[script]</a> |  96 lines |
| 95. <i id='task-95'></i>Since 2002, the most commonly occurring winning number in New York's Lottery Mega Millions <br> <a href='https://data.ny.gov/Government-Finance/Lottery-Mega-Millions-Winning-Numbers-Beginning-20/5xaw-6ayf'>[related URL]</a>&nbsp;<a href='scripts/95.py'>[script]</a> |  9 lines |
| 96. <i id='task-96'></i>The number of scheduled arguments according to the most recent U.S. Supreme Court argument calendar <br> <a href='http://www.supremecourt.gov/oral_arguments/argument_calendars.aspx'>[related URL]</a>&nbsp;<a href='scripts/96.py'>[script]</a> |  11 lines |
| 97. <i id='task-97'></i>The New York school with the highest rate of religious exemptions to vaccinations <br> <a href='https://health.data.ny.gov/Health/School-Immunization-Survey-Beginning-2012-13-Schoo/5pme-xbs5'>[related URL]</a>&nbsp;<a href='scripts/97.py'>[script]</a> |  10 lines |
| 98. <i id='task-98'></i>The latest estimated population percent change for Detroit, MI, according to the latest Census QuickFacts summary. <br> <a href='http://quickfacts.census.gov/qfd/states/26/2622000.html'>[related URL]</a>&nbsp;<a href='scripts/98.py'>[script]</a> |  8 lines |
| 99. <i id='task-99'></i>According to the Medill National Security Zone, the number of chambered guns confiscated at airports by the TSA <br> <a href='https://docs.google.com/spreadsheet/ccc?key=0AhAxyUlnJGbpdGhPSGhwWUp0QkowdEhXRXFKZE5Fb0E&usp=sharing'>[related URL]</a>&nbsp;<a href='scripts/99.py'>[script]</a> |  11 lines |
| 100. <i id='task-100'></i>The California city whose city manager earns the most total wage per population of its city in 2012 <br> <a href='http://publicpay.ca.gov/Reports/RawExport.aspx'>[related URL]</a>&nbsp;<a href='scripts/100.py'>[script]</a> |  23 lines |
| 101. <i id='task-101'></i>The number of women currently serving in the U.S. Congress, according to Sunlight Foundation data <br> <a href='https://sunlightlabs.github.io/congress/#legislator-spreadsheet'>[related URL]</a>&nbsp;<a href='scripts/101.py'>[script]</a> |  8 lines |
<!--endtasks-->


----

## How to run this stuff

Each task is meant to be a self-contained script: you run it, and it prints the answer I'm looking for. The [scripts](/scripts) in this repo should "just work"...if you have all the dependencies installed that I had while writing them, and the web URLs they target haven't changed...so, basically, these may not work at all.

To copy the scripts quickly via the command-line; by default, a ./search-script-scrape directory will be created:

    $ git clone https://github.com/compjour/search-script-scrape.git

To run a script:

    $ cd search-script-scrape
    $ python3 scripts/1.py

I leave it to you and Google to figure out how to run Python 3 on your own system. FWIW, I was using the [Python 3.4.3 provided by the Anaconda 2.2.0 installer for OS X](http://continuum.io/downloads#py34). The most common third-party libraries used are [Requests](http://www.python-requests.org/en/latest/) for downloading the files and [lxml for HTML parsing](http://lxml.de/).

## Expanding on these scripts

To reiterate: each of these scripts are meant to print out single answers, and so they don't actually show the full potential of how programming can automate data collection. As you get better at programming and recognizing its patterns, you'll find out how easy it is to abstract what seemed like a narrow task into something much bigger.

For example, [Script #50](scripts/50.py) prints out the number of times laughter broke out in the _most recently_ transcribed Supreme Court argument. Change two lines and that script will print out the laugh count in _every_ transcribed Supreme Court argument: ([demo here](scratchpad/more_scotus_laughs.py))

The same kind of small code restructuring can be done to many of the tasks here. And you can also modify the _parameters_; why limit yourself to finding the [highest paid "City Manager" in California](https://github.com/compjour/search-script-scrape/blob/master/scripts/100.py) when you can extend the search to every kind of California employee, across every year of salary data? ([demo here](scratchpad/high_city_ca_pay.py))

And of course, in real-world data projects, you aren't typically interested in just printing the answer to your Terminal. You generally want to send them to a spreadsheet or spreadsheet and eventually to a web application (or other kind of publication). That's just a few more lines of programming, too...So while this repo contains a bunch of toy scripts, see if you can think of ways to turn them into bigger data explorations.


## Post-mortem

The original requirement was that students finish all 100 scripts by the end of the quarter. That didn't quite work out so I reduced the requirement to 50. It was a bad idea to make this a "oh, just turn it in at the end of the year", as most people have the tendency to wait for finals week to do such work.

Most of the tasks are pretty straightforward, in terms of the Python programming. The majority of the time is figuring out exactly what the hell I'm referring to, so next time I do this, I'll probably provide the URL of the target page rather than having people attempt to divine the Google Path I used to get to the data.

- Class instructions for [Computational Journalism: Search-Script-Scrape](http://www.compjour.org/search-script-scrape)
- [List of tasks as a Google Doc](https://docs.google.com/spreadsheets/d/1JbY_-g9MkGH78Rta0PnE6D8rG8T-wdKGsMa3kAC3bDs/edit?usp=sharing)
