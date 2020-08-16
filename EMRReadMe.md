# spark v 2.4.4
-------------------------

amazon-kinesis-client-1.7.5.jar
Link: https://repo1.maven.org/maven2/com/amazonaws/amazon-kinesis-client/1.7.5/amazon-kinesis-client-1.7.5.jar

spark-streaming-kinesis-asl_2.12-2.4.4.jar
Link: https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kinesis-asl_2.12/2.4.4/spark-streaming-kinesis-asl_2.12-2.4.4.jar

# Run at EMR

spark-submit --jars spark-streaming-kinesis-asl_2.12-2.4.4.jar,amazon-kinesis-client-1.7.5.jar tweetEMR.py
