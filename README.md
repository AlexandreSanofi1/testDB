### Performance Check
*(10 million documents with 20+ fields) -> Query time analysis*

#### Current Results:
  

  - **DynamoDB:** 
                  10k insertions : 24 seconds (in batches of 25)
                  100k insertions : Total time taken to insert 10,000 items: 263.86 seconds ?

                
  - **Multiple Indexes** 
  Queries with multiple indexes requires a primary key index to be use filters.
  Scanner is similar to "select * where x,y,z" and has quick results.
  scanning for data is pretty quick, example :

  Scanning with filters...
  Total items found: 11290
  Total time taken for scan: 2.02 seconds
  

  - **with 20 indexes** : 10,000 items inserted in 80.90 seconds.
 
  IMPOSSIBLE to bypass the 20 secondary indexes limit by either AWS console or terminal.




#### MongoDB: 
- **MongoDB:** 17 seconds (in batches of 1000)
- Allows for batch insertions of up to 1000 lines without significant speed limitations.
- The number of insertions per batch seems to be limited only by the RAM memory allocated server-side.
- With this setup, the process went smoothly and quickly: 10k insertions in batches of 1000 took just **17 seconds**.

-- **READ from MULTIPLE INDEXES** --
possible and very fast. with the "find" method.
Total documents found: 129
Start time: 2024-09-18 20:22:53
End time: 2024-09-18 20:22:54
Total time taken for the query: 0.72 seconds

- **DocumentDB:** Only accessible via an EC2 instance or VPC/subnets. To access from elsewhere, port forwarding from an EC2 instance is required.


#### TO DO : DynamoDB Secondary Indexes Test : DONE
- Testing performance for secondary indexes in DynamoDB upload 10k lines with 20 indexes.

- Investigating whether it's possible to exceed the limit of **20 Secondary Indexes** in DynamoDB.

#### TO DO :  Test Atlas Hosted on AWS :
- testing performance for 100k to 10m insertions.
- testing with 30 and more indexes. if possible 100 indexes.


#### DynamoDB, Removing Throttling:
To modify the throttling settings in DynamoDB:
1. Navigate to **DynamoDB** in the AWS Console.
2. Select **Tables** and choose the relevant **tableName**.
3. Go to **Additional Settings** > **Read/Write Capacity** > **Edit**.
4. Adjust the following:
   - Set to **On-Demand**.
   - Enable **Set Max Read Requests** and set the value to **40,000**.
   - Enable **Set Max Write Requests** and set the value to **40,000**.