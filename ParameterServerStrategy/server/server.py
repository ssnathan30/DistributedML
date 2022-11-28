import tensorflow as tf
import os
import json

cluster_dict = json.loads(os.environ['CLUSTER_CONFIG'])
cluster_spec = tf.train.ClusterSpec(cluster_dict)
worker_config = tf.compat.v1.ConfigProto()

server = tf.distribute.Server(
        cluster_spec,
        job_name=os.environ.get("job_type"),
        task_index=int(os.environ.get("task_index")),
        config=worker_config,
        protocol="grpc")

server.join()