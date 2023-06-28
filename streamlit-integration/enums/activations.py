from typing import Callable

import tensorflow as tf

activations: dict[str, Callable[..., tf.Tensor]] = {
    "Linear": tf.keras.activations.linear,
    "Tanh": tf.keras.activations.tanh,
    "ReLU": tf.keras.activations.relu,
}
