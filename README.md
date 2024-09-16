Check performance 
(10 million de documents avec 10 fields) -> temps de requete 

results for now :

10k insertions :
mongoDB = 17 seconds. (blocks of 1000)
dynamoDB = 24 seconds. (bloks of 25)
DocumentDB = only accessible via EC2 instance or VPC/subnets
to be accessible from, anywhere else will require port forwarding from an EC2 instance.






notes about removing DynamoDB throttling :

in amazon console :
dynamoDB, tables, tableName, additional settings, read/write capacity, edit 

- on demand
- set max read reqests ticked, value 40 000
- set max write requests ticked, value 40 000

mongoDB : allow for batch insertions of up to 1000 lines without any speed limitations.
the numbers of insertions per batches appears to be only limited by ram memory allocated server side,
but for this im not sure.

that being said, everything went smoothly and fast. 10k insertions by batches of 1000 took 17 seconds.






test for secondary indexes in dynamoDB?



Test secondary indexes et perf de DynamoDB vs DocumentDB 

Est-ce qu’on peut dépasser la limite de 20 Secondary Indexes  dans DynamoDB

 


