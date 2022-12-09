
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
| January 2012 Rows  |   |   |   |   |
| October 2012 Rows  |   |   |   |   |
| Month with Fewest  |   |   | Yes/No  | NA  |
| Num Rows in Month with Fewest  |   |   |   |   |
| Month with Most  |   |   | Yes/No  | NA  |
| Num Rows in Month with Most  |   |   |   |   |
| Null_TS  |   |   |   |   |
| Null_DT  |   |   |   |   |
| Null_Local  |   |   |   |   |
| Null_CN  |   |   |   |   |
| Num 5 on High Volume Cards  |   |   | Yes/No  | NA  |
|  Num Rows for Number 5 |   |   |   |   |
| Num Rows for 18736  |   |   |   |   |
| Product with Most Rows  |   |   | Yes/No  | NA  |
| Num Rows for that Product  |   |   |   |   |
| Product with Fourth-Most Rows  |   |   | Yes/No  | NA  |
| Num Rows for that Product  |   |   |   |   |
| Num Single Record Products  |   |   |   |   |
| Year with Highest Portion of Owner Rows  |   |   | Yes/No  | NA |
| Fraction of Rows from Owners in that Year  |   |   |   |   |
| Year with Lowest Portion of Owner Rows  |   |   | Yes/No  | NA |
| Fraction of Rows from Owners in that Year  |   |   |   |   |

## Reflections

<!-- I'd love to get 100-200 words on your experience doing the Wedge Project --> 
