
# Applied Data Analytics

## Wedge Project

This project felt cohesive and applicable to real world data problems.  It helped me form a better connection between my sql and python skills and helped build confidence in my skillset.

All code is contained in the "Wedge_Code.ipynb" file

### Task 1

I began by downloading and decompressing wedge_clean_files.zip

The 53 transaction files were stored in a single folder on my local machine. 

I then created a data bucket on Google Cloud Storage using the same account used for Google BigQuery
I uploaded the 53 transaction files to the data bucket and removed them from my local machine. 

In BigQuery, I created an empty dataset called msba_wedge.

Using the batch upload feature avaialable between BigQuery and Cloud Storage, I was able to batch upload all 53 transaction files into a single table, and validate a single table schema instead of 53 separate schemas. Batch loading to a single table also removed the need to combine the data programatically for Tasks 2 and 3. 


### Task 2

After creating my GBQ dataset, I used python to create a .txt file of all transaction data for a random sample of 500 users. 
The code for sampling is flexible and the number of users can be adjusted. The sample will contain different results each time the code is run. 


### Task 3

Using the GQB dataset, I created a SQLite databse with three summary tables. I used SQL to aggregate and summarize wedge sales information and stored the results in Pandas dataframes. The dataframes were used to populate the SQLite database. 


## Query Comparison Results

Fill in the following table with the results from the 
queries contained in `gbq_assessment_query.sql`. You only
need to fill in relative difference on the rows where it applies. 
When calculating relative difference, use the formula 
` (your_results - john_results)/john_results)`. 



|  Query  |  Your Results  |  John's Results | Difference | Rel. Diff | 
|---|---|---|---|---|
| Total Rows  |85760139|85760139|  0|   |
| January 2012 Rows  |1070907| 1070907| 0  |   |
| October 2012 Rows  |1042287|1042287| 0  |   |
| Month with Fewest  |2|2| Yes  | NA  |
| Num Rows in Month with Fewest  |6556770|6556770|0|   |
| Month with Most  |5|5|Yes| NA  |
| Num Rows in Month with Most  |7578372|7578372|0|   |
| Null_TS  |7123792|7123792|0|   |
| Null_DT  |0|0|0|   |
| Null_Local  |234843|234843|0|   |
| Null_CN  |0|0|0|   |
| Num 5 on High Volume Cards  |14987|14987.0| Yes| NA  |
|  Num Rows for Number 5 |460630|460630|0|   |
| Num Rows for 18736  |12153|12153|0|   |
| Product with Most Rows  |banana organic|banana organic| Yes| NA  |
| Num Rows for that Product  |908639|908639|0|   |
| Product with Fourth-Most Rows  |avocado hass organic|avocado hass organic| Yes| NA  |
| Num Rows for that Product  |456771|456771|0|   |
| Num Single Record Products  |2769|2769|0|   |
| Year with Highest Portion of Owner Rows  |2014|2014| Yes | NA |
| Fraction of Rows from Owners in that Year  |0.7591|0.7591|0|   |
| Year with Lowest Portion of Owner Rows  |2011|2011| Yes| NA |
| Fraction of Rows from Owners in that Year  |0.7372|0.7372|0|   |

## Reflections

I approached this project confident in my SQL and GBQ abilities but with almost no Python confidence. However, I suprised myself and very much enjoyed working through the python portions.  In my opinion, the structure of the project helped set us all up for success. We had exposure to the data early on, a solid SQL and Python foundation with numerous examples to fall back on, and the tasks set forth were logical in such a way that the solutions could be conceptualized without knowing the exact execution. The ability to mentally visualize the process and outcome helped me understand what to try, what to search, and what success looked like. Overall, I think this is a great project, and I am happy to have the completed work to reference. 

<!-- I'd love to get 100-200 words on your experience doing the Wedge Project --> 
