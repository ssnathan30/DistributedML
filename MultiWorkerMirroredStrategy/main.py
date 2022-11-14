import json
import os
from time import sleep

import tensorflow as tf
import mnist_setup

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
per_worker_batch_size = 64
model_path = '/tmp/keras-model'

tf_config = json.loads(os.environ['TF_CONFIG'])
num_workers = len(tf_config['cluster']['worker'])
strategy = tf.distribute.MultiWorkerMirroredStrategy()

global_batch_size = per_worker_batch_size * num_workers
multi_worker_dataset = mnist_setup.mnist_dataset(global_batch_size)


def _is_chief(cluster_resolver):
    task_type = cluster_resolver.task_type
    return task_type is None or task_type == 'chief'


def _get_temp_dir(model_path, cluster_resolver):
    worker_temp = f'worker{cluster_resolver.task_id}_temp'
    return os.path.join(model_path, worker_temp)


def save_model(_model_path, model):
    cluster_resolver = tf.distribute.cluster_resolver.TFConfigClusterResolver()
    is_chief = _is_chief(cluster_resolver)

    if not is_chief:
        _model_path = _get_temp_dir(_model_path, cluster_resolver)

    model.save(_model_path)

    if is_chief:
        # wait for workers to delete; check every 100ms
        # if chief is finished, the training is done
        while tf.io.gfile.glob(os.path.join(model_path, "worker*")):
            sleep(0.1)

    if not is_chief:
        tf.io.gfile.rmtree(model_path)


with strategy.scope():
    # Model building/compiling need to be within `strategy.scope()`.
    multi_worker_model = mnist_setup.build_and_compile_cnn_model()

multi_worker_model.fit(multi_worker_dataset, epochs=3, steps_per_epoch=70)
save_model(model_path,multi_worker_model)
