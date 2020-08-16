from __future__ import print_function

import sys
import json

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kinesis import KinesisUtils, InitialPositionInStream

if __name__ == "__main__":
    applicationName = "PythonStreamingKinesisWordCountAsl"
    streamName = "KinesisDemo"
    endpointUrl = "https://kinesis.us-east-1.amazonaws.com"
    regionName = "us-east-1"
    sc = SparkContext(appName=applicationName)
    ssc = StreamingContext(sc, 5)

    print("appname is" + applicationName +
          streamName + endpointUrl + regionName)
    lines = KinesisUtils.createStream(
        ssc, applicationName, streamName, endpointUrl, regionName, InitialPositionInStream.LATEST, 2)

    # lines.pprint()

    def filter_tweets(x):
        json_tweet = json.loads(x)
	if json_tweet.has_key('lang'):  # When the lang key was not present it caused issues
       	if json_tweet['lang'] == 'ar':
		return True  # filter() requires a Boolean value
    	return False

    lines.foreachRDD(lambda rdd: rdd.filter(filter_tweets).coalesce(
        1).saveAsTextFile("./tweets/%f" % time.time()))

    ssc.start()
    ssc.awaitTermination()
