## Search-Script-Scrape 

#### 101 webscraping and research tasks for the data journalist

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


__Note:__ The second column of this table refers to __line count__ of the script, __not__ the answer to the prompt.

## The tasks

The repo currently contains scripts for __91__ of __101__ tasks:

|                                                                                                                        Title                                                                                                                         | Line count |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| 1. <a id='task-1' href='scripts/1.py'>Number of datasets currently listed on data.gov</a>                                                                                                                                                            | 7 lines    |
| 2. <a id='task-2' href='scripts/2.py'>The name of the most recently added dataset on data.gov</a>                                                                                                                                                    | 7 lines    |
| 3. <a id='task-3' href='scripts/3.py'>The number of people who visited a U.S. government website using Internet Explorer 6.0 in the last 90 days</a>                                                                                                 | 4 lines    |
| 4. <a id='task-4' href='scripts/4.py'>The number of librarian-related job positions that the federal government is currently hiring for</a>                                                                                                          | 6 lines    |
| 5. <a id='task-5' href='scripts/5.py'>The name of the company cited in the most recent consumer complaint involving student loans</a>                                                                                                                | 27 lines   |
| 6. <a id='task-6' href='scripts/6.py'>From 2010 to 2013, the change in median cost of health, dental, and vision coverage for California city employees</a>                                                                                          | 38 lines   |
| 7. <a id='task-7' href='scripts/7.py'>The number of listed federal executive agency internet domains</a>                                                                                                                                             | 8 lines    |
| 8. <a id='task-8' href='scripts/8.py'>The number of times when a New York heart surgeon's rate of patient deaths for all cardiac surgical procedures was "significantly higher" than the statewide rate, according to New York state's analysis.</a> | 7 lines    |
| 9. <a id='task-9' href='scripts/9.py'>The number of roll call votes that were rejected by a margin of less than 5 votes, in the first session of the U.S. Senate in the 114th Congress</a>                                                           | 26 lines   |
| 10. <a id='task-10' href='scripts/10.py'>The title of the highest paid California city government position in 2010</a>                                                                                                                               | 35 lines   |
| 11. <a id='task-11'></a>How much did the state of California collect in property taxes, according to the U.S. Census 2013 Annual Survey of State Government Tax Collections?                                                                         |            |
| 12. <a id='task-12'></a>In 2010, the year-over-year change in enplanements at America's busiest airport                                                                                                                                              |            |
| 13. <a id='task-13' href='scripts/13.py'>The number of armored carrier bank robberies recorded by the FBI in 2014</a>                                                                                                                                | 15 lines   |
| 14. <a id='task-14' href='scripts/14.py'>The number of workplace fatalities at reported to the federal and state OSHA in the latest fiscal year</a>                                                                                                  | 14 lines   |
| 15. <a id='task-15' href='scripts/15.py'>Total number of wildlife strike incidents reported at San Francisco International Airport</a>                                                                                                               | 48 lines   |
| 16. <a id='task-16' href='scripts/16.py'>The non-profit organization with the highest total revenue, according to the latest listing in ProPublica's Nonprofit Explorer</a>                                                                          | 11 lines   |
| 17. <a id='task-17' href='scripts/17.py'>In the "Justice News" RSS feed maintained by the Justice Department, the number of items published on a Friday</a>                                                                                          | 11 lines   |
| 18. <a id='task-18' href='scripts/18.py'>The number of U.S. congressmembers who have Twitter accounts, according to Sunlight Foundation data</a>                                                                                                     | 9 lines    |
| 19. <a id='task-19' href='scripts/19.py'>The total number of preliminary reports on aircraft safety incidents/accidents in the last 10 business days</a>                                                                                             | 12 lines   |
| 20. <a id='task-20' href='scripts/20.py'>The number of OSHA enforcement inspections involving Wal-Mart in California since 2014</a>                                                                                                                  | 25 lines   |
| 21. <a id='task-21' href='scripts/21.py'>The current humidity level at Great Smoky Mountains National Park</a>                                                                                                                                       | 6 lines    |
| 22. <a id='task-22' href='scripts/22.py'>The names of the committees that Sen. Barbara Boxer currently serves on</a>                                                                                                                                 | 7 lines    |
| 23. <a id='task-23' href='scripts/23.py'>The name of the California school with the highest number of girls enrolled in kindergarten, according to the CA Dept. of Education's latest enrollment data file.</a>                                      | 21 lines   |
| 24. <a id='task-24' href='scripts/24.py'>Percentage of NYPD stop-and-frisk reports in which the suspect was white in 2014</a>                                                                                                                        | 24 lines   |
| 25. <a id='task-25' href='scripts/25.py'>Average frontal crash star rating for 2015 Honda Accords</a>                                                                                                                                                | 14 lines   |
| 26. <a id='task-26'></a>The dropout rate for all of Santa Clara County high schools, according to the latest cohort data in CALPADS                                                                                                                  |            |
| 27. <a id='task-27' href='scripts/27.py'>The number of Class I Drug Recalls issued by the U.S. Food and Drug Administration since 2012</a>                                                                                                           | 14 lines   |
| 28. <a id='task-28' href='scripts/28.py'>Total number of clinical trials as recorded by the National Institutes of Health</a>                                                                                                                        | 7 lines    |
| 29. <a id='task-29' href='scripts/29.py'>Number of days until Texas's next scheduled execution</a>                                                                                                                                                   | 17 lines   |
| 30. <a id='task-30' href='scripts/30.py'>The total number of inmates executed by Florida since 1976</a>                                                                                                                                              | 7 lines    |
| 31. <a id='task-31' href='scripts/31.py'>The number of proposed U.S. federal regulations in which comments are due within the next 3 days</a>                                                                                                        | 10 lines   |
| 32. <a id='task-32' href='scripts/32.py'>Number of Titles that have changed int he United States Code since its last release point</a>                                                                                                               | 6 lines    |
| 33. <a id='task-33' href='scripts/33.py'>The number of FDA-approved, but now discontinued drug products that contain Fentanyl as an active ingredient</a>                                                                                            | 14 lines   |
| 34. <a id='task-34' href='scripts/34.py'>In the latest FDA Weekly Enforcement Report, the number of Class I and Class II recalls involving food</a>                                                                                                  | 10 lines   |
| 35. <a id='task-35' href='scripts/35.py'>Most viewed data set on New York state's open data portal as of this month</a>                                                                                                                              | 9 lines    |
| 36. <a id='task-36' href='scripts/36.py'>Total number of visitors to the White House in 2012</a>                                                                                                                                                     | 27 lines   |
| 37. <a id='task-37' href='scripts/37.py'>The last time the CIA's Leadership page has been updated </a>                                                                                                                                               | 6 lines    |
| 38. <a id='task-38' href='scripts/38.py'>The domain of the most visited U.S. government website right now</a>                                                                                                                                        | 5 lines    |
| 39. <a id='task-39' href='scripts/39.py'>Number of medical device recalls issued by the U.S. Food and Drug Administration in 2013</a>                                                                                                                | 6 lines    |
| 40. <a id='task-40' href='scripts/40.py'>Number of FOIA requests made to the Chicago Public Library</a>                                                                                                                                              | 6 lines    |
| 41. <a id='task-41' href='scripts/41.py'>The number of currently open medical trials involving alcohol-related disorders</a>                                                                                                                         | 5 lines    |
| 42. <a id='task-42' href='scripts/42.py'>The name of the Supreme Court justice who delivered the opinion in the most recently announced decision</a>                                                                                                 | 31 lines   |
| 43. <a id='task-43' href='scripts/43.py'>The number of citations that resulted from FDA inspections in fiscal year 2012</a>                                                                                                                          | 10 lines   |
| 44. <a id='task-44' href='scripts/44.py'>Number of people visiting a U.S. government website right now</a>                                                                                                                                           | 6 lines    |
| 45. <a id='task-45' href='scripts/45.py'>The number of security alerts issued by US-CERT in the current year</a>                                                                                                                                     | 6 lines    |
| 46. <a id='task-46' href='scripts/46.py'>The number of Pinterest accounts maintained by U.S. State Department embassies and missions</a>                                                                                                             | 13 lines   |
| 47. <a id='task-47' href='scripts/47.py'>The number of international travel alerts from the U.S. State Department currently in effect</a>                                                                                                            | 7 lines    |
| 48. <a id='task-48' href='scripts/48.py'>The difference in total White House staffmember salaries in 2014 versus 2010</a>                                                                                                                            | 19 lines   |
| 49. <a id='task-49' href='scripts/49.py'>Number of sponsored bills by Rep. Nancy Pelosi that were vetoed by the President</a>                                                                                                                        | 11 lines   |
| 50. <a id='task-50' href='scripts/50.py'>In the most recently transcribed Supreme Court argument, the number of times laughter broke out</a>                                                                                                         | 22 lines   |
| 51. <a id='task-51' href='scripts/51.py'>The title of the most recent decision handed down by the U.S. Supreme Court</a>                                                                                                                             | 6 lines    |
| 52. <a id='task-52' href='scripts/52.py'>The average wage of optomertrists according to the BLS's most recent National Occupational Employment and Wage Estimates report</a>                                                                         | 8 lines    |
| 53. <a id='task-53' href='scripts/53.py'>The total number of on-campus hate crimes as reported to the U.S. Office of Postsecondary Education, in the most recent collection year</a>                                                                 | 45 lines   |
| 54. <a id='task-54' href='scripts/54.py'>The number of people on FBI's Most Wanted List for white collar crimes</a>                                                                                                                                  | 6 lines    |
| 55. <a id='task-55' href='scripts/55.py'>The number of Government Accountability Office reports and testimonies on the topic of veterans</a>                                                                                                         | 10 lines   |
| 56. <a id='task-56' href='scripts/56.py'>Number of times Rep. Darrell Issa's remarks have made it onto the Congressional Record</a>                                                                                                                  | 9 lines    |
| 57. <a id='task-57'></a>The number of comments posted to the regulation that is currently at the top of Regulations.gov's "What's Trending" list                                                                                                     |            |
| 58. <a id='task-58' href='scripts/58.py'>The number of published research papers from the NSA</a>                                                                                                                                                    | 6 lines    |
| 59. <a id='task-59' href='scripts/59.py'>The number of university-related datasets currently listed at data.gov</a>                                                                                                                                  | 7 lines    |
| 60. <a id='task-60' href='scripts/60.py'>Number of chapters in Title 20 (Education) of the United States Code</a>                                                                                                                                    | 15 lines   |
| 61. <a id='task-61' href='scripts/61.py'>The number of miles traveled by the current U.S. Secretary of State</a>                                                                                                                                     | 6 lines    |
| 62. <a id='task-62' href='scripts/62.py'>For all of 2013, the number of potential signals of serious risks or new safety information that resulted from the FDA's FAERS</a>                                                                          | 14 lines   |
| 63. <a id='task-63' href='scripts/63.py'>In the current dataset behind Medicare's Nusring Home Compare website, the total amount of fines received by penalized nursing homes</a>                                                                    | 35 lines   |
| 64. <a id='task-64' href='scripts/64.py'>from March 1 to 7, 2015, the number of times in which designated FDA policy makers met with persons outside the U.S. federal executive branch</a>                                                           | 5 lines    |
| 65. <a id='task-65' href='scripts/65.py'>The number of failed votes in the roll calls 1 through 99, in the U.S. House of the 114th Congress</a>                                                                                                      | 12 lines   |
| 66. <a id='task-66' href='scripts/66.py'>The highest minimum wage as mandated by state law.</a>                                                                                                                                                      | 28 lines   |
| 67. <a id='task-67'></a>According to the TSA.gov's customer satisfication survey, what is the number of customers in October 2014 who rated their overall experience with tsa.gov as "Excellent"?                                                    |            |
| 68. <a id='task-68' href='scripts/68.py'>Number of FDA-approved prescription drugs with GlaxoSmithKline as the applicant holder</a>                                                                                                                  | 11 lines   |
| 69. <a id='task-69' href='scripts/69.py'>The average number of comments on the last 50 posts on NASA's official Instagram account</a>                                                                                                                | 40 lines   |
| 70. <a id='task-70' href='scripts/70.py'>The highest salary possible for a White House staffmember in 2014</a>                                                                                                                                       | 10 lines   |
| 71. <a id='task-71' href='scripts/71.py'>The percent increase in number of babies named Archer nationwide in 2010 compared to 2000, according to the Social Security Administration</a>                                                              | 32 lines   |
| 72. <a id='task-72' href='scripts/72.py'>The number of magnitude 4.5+ earthquakes detected worldwide by the USGS</a>                                                                                                                                 | 8 lines    |
| 73. <a id='task-73' href='scripts/73.py'>The total amount of contributions made by lobbyists to Congress according to the latest downloadable quarterly report</a>                                                                                   | 34 lines   |
| 74. <a id='task-74' href='scripts/74.py'>The description of the bill most recently signed into law by the governor of Georgia</a>                                                                                                                    | 12 lines   |
| 75. <a id='task-75' href='scripts/75.py'>Total number of officer-involved shooting incidents listed by the Philadelphia Police Department </a>                                                                                                       | 9 lines    |
| 76. <a id='task-76' href='scripts/76.py'>The total number of publications produced by the U.S. Government Accountability Office</a>                                                                                                                  | 9 lines    |
| 77. <a id='task-77' href='scripts/77.py'>Number of Dallas officer-involved fatal shooting incidents in 2014</a>                                                                                                                                      | 7 lines    |
| 78. <a id='task-78' href='scripts/78.py'>Number of Cupertino, CA restaurants that have been shut down due to health violations in the last six months.</a>                                                                                           | 6 lines    |
| 79. <a id='task-79' href='scripts/79.py'>The change in total airline revenues from baggage fees, from 2013 to 2014</a>                                                                                                                               | 19 lines   |
| 80. <a id='task-80' href='scripts/80.py'>The total number of babies named Odin born in Colorado according to the Social Security Administration</a>                                                                                                  | 20 lines   |
| 81. <a id='task-81'></a>The latest release date for T-100 Domestic Market (U.S. Carriers) statistics report                                                                                                                                          |            |
| 82. <a id='task-82'></a>From 2010 to 2013, the total number of patient deaths listed in the FDA's Adverse Events Reporting System                                                                                                                    |            |
| 83. <a id='task-83' href='scripts/83.py'>The sum of White House staffermember salaries in 2014</a>                                                                                                                                                   | 12 lines   |
| 84. <a id='task-84' href='scripts/84.py'>The total number of notices published on the most recent date to the Federal Register</a>                                                                                                                   | 6 lines    |
| 85. <a id='task-85' href='scripts/85.py'>The number of iPhone units sold in the latest quarter, according to Apple Inc's most recent 10-Q report</a>                                                                                                 | 49 lines   |
| 86. <a id='task-86' href='scripts/86.py'>Number of computer vulnerabilities in which IBM was the vendor in the latest Cyber Security Bulletin </a>                                                                                                   | 10 lines   |
| 87. <a id='task-87'></a>Number of airports with existing construction related activity                                                                                                                                                               |            |
| 88. <a id='task-88' href='scripts/88.py'>The number of posts on TSA's Instagram account</a>                                                                                                                                                          | 24 lines   |
| 89. <a id='task-89'></a>In fiscal year 2013, the short description of the most frequently cited type of FDA's inspectional observations related to food products.                                                                                    |            |
| 90. <a id='task-90' href='scripts/90.py'>The currently serving U.S. congressmember with the most Twitter followers</a>                                                                                                                               | 76 lines   |
| 91. <a id='task-91' href='scripts/91.py'>Number of stop-and-frisk reports from the NYPD in 2014</a>                                                                                                                                                  | 22 lines   |
| 92. <a id='task-92' href='scripts/92.py'>In 2012-Q4, the total amount paid by Rep. Aaron Schock to Lobair LLC, according to Congressional spending records, as compiled by the Sunlight Foundation</a>                                               | 14 lines   |
| 93. <a id='task-93' href='scripts/93.py'>Number of Github repositories maintained by the GSA's 18F organization, as listed on Github.com</a>                                                                                                         | 5 lines    |
| 94. <a id='task-94'></a>The New York City high school with the highest average math score in the latest SAT results                                                                                                                                  |            |
| 95. <a id='task-95' href='scripts/95.py'>Since 2002, the most commonly occurring winning number in New York's Lottery Mega Millions</a>                                                                                                              | 9 lines    |
| 96. <a id='task-96' href='scripts/96.py'>The number of scheduled arguments according to the most recent U.S. Supreme Court argument calendar</a>                                                                                                     | 11 lines   |
| 97. <a id='task-97' href='scripts/97.py'>The New York school with the highest rate of religious exemptions to vaccinations</a>                                                                                                                       | 10 lines   |
| 98. <a id='task-98' href='scripts/98.py'>The latest estimated population percent change for Detroit, MI, according to the latest Census QuickFacts summary.</a>                                                                                      | 8 lines    |
| 99. <a id='task-99' href='scripts/99.py'>According to the Medill National Security Zone, the number of chambered guns confiscated at airports by the TSA</a>                                                                                         | 11 lines   |
| 100. <a id='task-100' href='scripts/100.py'>The California city whose city manager earns the most total wage per population of its city in 2012</a>                                                                                                  | 23 lines   |
| 101. <a id='task-101' href='scripts/101.py'>The number of women currently serving in the U.S. Congress, according to Sunlight Foundation data</a>                                                                                                    | 8 lines    |


-----

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
