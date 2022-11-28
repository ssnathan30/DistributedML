import tensorflow as tf
import json
import os

working_dir = "/tmp/my_working_dir"
log_dir = os.path.join(working_dir, "log")
ckpt_filepath = os.path.join(working_dir, "ckpt")
backup_dir = os.path.join(working_dir, "backup")

cluster_dict = json.loads(os.environ['CLUSTER_CONFIG'])
cluster_spec = tf.train.ClusterSpec(cluster_dict)
cluster_resolver = tf.distribute.cluster_resolver.SimpleClusterResolver(
    cluster_spec, rpc_layer="grpc")

variable_partitioner = (
    tf.distribute.experimental.partitioners.MinSizePartitioner(
        min_shard_bytes=(256 << 10),
        max_shards=int(os.environ.get("NUM_PS"))))

strategy = tf.distribute.ParameterServerStrategy(
    cluster_resolver,
    variable_partitioner=variable_partitioner)


with strategy.scope():
    global_batch_size = 64
    x = tf.random.uniform((10, 10))
    y = tf.random.uniform((10,))

    dataset = tf.data.Dataset.from_tensor_slices((x, y)).shuffle(10).repeat()
    dataset = dataset.batch(global_batch_size)
    dataset = dataset.prefetch(2)

    model = tf.keras.models.Sequential([tf.keras.layers.Dense(10)])
    model.compile(tf.keras.optimizers.legacy.SGD(), loss="mse", steps_per_execution=10)

model.fit(dataset, epochs=5, steps_per_epoch=20)
