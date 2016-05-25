#!/bin/bash
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file q3map2.py q3reduce.py -mapper q3map2.py -reducer q3reduce.py
