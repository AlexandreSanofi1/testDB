### Performance Check
*(10 million documents with 10 fields) -> Query time analysis*

#### Current Results:
- **10k Insertions:**
  - **MongoDB:** 17 seconds (in batches of 1000)
  - **DynamoDB:** 24 seconds (in batches of 25)
  - **DocumentDB:** Only accessible via an EC2 instance or VPC/subnets. To access from elsewhere, port forwarding from an EC2 instance is required.

#### DynamoDB, Removing Throttling:
To modify the throttling settings in DynamoDB:
1. Navigate to **DynamoDB** in the AWS Console.
2. Select **Tables** and choose the relevant **tableName**.
3. Go to **Additional Settings** > **Read/Write Capacity** > **Edit**.
4. Adjust the following:
   - Set to **On-Demand**.
   - Enable **Set Max Read Requests** and set the value to **40,000**.
   - Enable **Set Max Write Requests** and set the value to **40,000**.

#### MongoDB:
- Allows for batch insertions of up to 1000 lines without significant speed limitations.
- The number of insertions per batch seems to be limited only by the RAM memory allocated server-side.
- With this setup, the process went smoothly and quickly: 10k insertions in batches of 1000 took just **17 seconds**.

#### TO DO : DynamoDB Secondary Indexes Test:
- Testing performance for secondary indexes in DynamoDB.
- Investigating whether it's possible to exceed the limit of **20 Secondary Indexes** in DynamoDB.

#### TO DO : Testing DynamoDB vs. DocumentDB:
- Performance comparison focusing on secondary indexes and overall operation efficiency between DynamoDB and DocumentDB.
