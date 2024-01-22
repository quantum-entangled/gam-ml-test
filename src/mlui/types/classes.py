import typing

import altair as alt
import numpy as np
import numpy.typing as npt
import pandas as pd
import tensorflow as tf

# Session
FuncType: typing.TypeAlias = typing.Callable[..., None]
DecorType: typing.TypeAlias = typing.Callable[[FuncType], FuncType]
PageTasks: typing.TypeAlias = list[str]

# Data & Model
Columns: typing.TypeAlias = list[str]
Features: typing.TypeAlias = list[str]
DataFrame: typing.TypeAlias = pd.DataFrame

Object: typing.TypeAlias = tf.keras.Model
Side: typing.TypeAlias = typing.Literal["input", "output"]
Shape: typing.TypeAlias = tuple[None, int]
Shapes: typing.TypeAlias = dict[str, Shape] | list[Shape] | Shape
NDArray: typing.TypeAlias = npt.NDArray[np.float64]
EvaluationResults: typing.TypeAlias = DataFrame
Predictions: typing.TypeAlias = list[DataFrame]

# Charts
LogsNames: typing.TypeAlias = list[str]
Chart: typing.TypeAlias = alt.Chart

# Activations
Tensor: typing.TypeAlias = tf.Tensor
ActivationType: typing.TypeAlias = typing.Type[typing.Callable[..., tf.Tensor]]
ActivationTypes: typing.TypeAlias = dict[str, ActivationType]

# Layers
Layer: typing.TypeAlias = tf.keras.layers.Layer
LayerType: typing.TypeAlias = typing.Type[Layer]
LayerTypes: typing.TypeAlias = dict[str, LayerType]
Layers: typing.TypeAlias = list[str]
LayerShape: typing.TypeAlias = dict[str, int]
LayerFeatures: typing.TypeAlias = dict[str, Features]
LayerConfigured: typing.TypeAlias = dict[str, bool]
LayerObject: typing.TypeAlias = dict[str, Layer]
LayerData: typing.TypeAlias = dict[str, NDArray]
LayerConnection: typing.TypeAlias = Layer | list[Layer] | None


class LayerParams(typing.TypedDict):
    """Base type annotation class for the parameters of the layer."""


class InputParams(LayerParams):
    """Type annotation class for the Input layer."""

    shape: tuple[int]


class DenseParams(LayerParams):
    """Type annotation class for the Dense layer."""

    units: int
    activation: typing.Callable[..., Tensor]


class BatchNormalizationParams(LayerParams):
    """Type annotation class for the BatchNormalization layer."""

    momentum: float
    epsilon: float


class DropoutParams(LayerParams):
    """Type annotation class for the Dropout layer."""

    rate: float


# Optimizers
Optimizer: typing.TypeAlias = tf.keras.optimizers.Optimizer | None
OptimizerType: typing.TypeAlias = tf.keras.optimizers.Optimizer
OptimizerTypes: typing.TypeAlias = dict[str, OptimizerType]


class OptimizerParams(typing.TypedDict):
    """Base type annotation class for the parameters of the optimizer."""


class AdamParams(OptimizerParams):
    """Type annotation class for the Adam optimizer."""

    learning_rate: float
    beta_1: float
    beta_2: float


class RMSpropParams(OptimizerParams):
    """Type annotation class for the RMSprop optimizer."""

    learning_rate: float
    rho: float
    momentum: float


class SGDParams(OptimizerParams):
    """Type annotation class for the SGD optimizer."""

    learning_rate: float
    momentum: float


# Losses
Loss: typing.TypeAlias = str | None
LossType: typing.TypeAlias = str
LossTypes: typing.TypeAlias = list[LossType]
LayerLosses: typing.TypeAlias = dict[str, Loss]


# Metrics
Metric: typing.TypeAlias = str
MetricType: typing.TypeAlias = str
MetricTypes: typing.TypeAlias = list[MetricType]
Metrics: typing.TypeAlias = list[Metric]
LayerMetrics: typing.TypeAlias = dict[str, Metrics]

# Callbacks
Callback: typing.TypeAlias = tf.keras.callbacks.Callback | None
CallbackType: typing.TypeAlias = typing.Type[tf.keras.callbacks.Callback]
CallbackTypes: typing.TypeAlias = dict[str, CallbackType]
Callbacks: typing.TypeAlias = dict[str, Callback]


class CallbackParams(typing.TypedDict):
    """Base type annotation class for the parameters of the callback."""


class EarlyStoppingParams(CallbackParams):
    """Type annotation class for the EarlyStopping callback."""

    min_delta: float
    patience: int
