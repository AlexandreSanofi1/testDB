Check performance 
(10 million de documents avec 10 fields) -> temps de requete 

results for now :

10k insertions :
mongoDB = 17 seconds. (consistently)
dynamoDB = 15 minutes. (consistently)


mongoDB : allow for batch insertions of up to 1000 lines without any speed limitations.
the numbers of insertions per batches appears to be only limited by ram memory allocated server side,
but for this im not sure.

that being said, everything went smoothly and fast. 10k insertions by batches of 1000 took 17 seconds.


dynamoDB : is already throttling request with 100 insertions let alone 1000 and 10k.
Tried to insert 500ms delay but it still throttle request rate.
at 10k insertions, this is 400 batches of 25 insertions, so that is a total delay of 200seconds,
and it does not includes throttling that appears anyway.

there is also limit of batch size of 25 insertions maximum per request.






what is a secondary index in dynamoDB?



Test secondary indexes et perf de DynamoDB vs DocumentDB 

Est-ce qu’on peut dépasser la limite de 20 Secondary Indexes  dans DynamoDB

 


