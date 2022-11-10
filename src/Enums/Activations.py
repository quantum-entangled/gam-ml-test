from typing import Any

import tensorflow as tf

activations: dict[Any, Any] = {
    "Linear": tf.keras.activations.linear,
    "Hyperbolic Tangent": tf.keras.activations.tanh,
    "ReLU": tf.keras.activations.relu,
}
