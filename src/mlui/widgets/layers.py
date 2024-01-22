import abc

import streamlit as st

import mlui.classes.errors as errors
import mlui.enums as enums
import mlui.types.classes as t


class LayerWidget(abc.ABC):
    """Base class for a widget of the layer."""

    def __init__(self, layers: t.LayerObject) -> None:
        """
        Initialize the widgets of parameters.

        Parameters
        ----------
        layers : dict of Layer
            Layers of the model.
        """
        self._layers = layers

    @abc.abstractmethod
    def get_connection(self) -> t.LayerConnection:
        """Get the connection of the layer.

        Returns
        -------
        Layer or list of Layer
            Connection layer(s).

        Raises
        ------
        LayerError
            If no layer is selected to connect. If fewer than 2 layers are selected
            for concatenation.
        """

    @property
    @abc.abstractmethod
    def params(self) -> t.LayerParams:
        """Adjustable parameters of the layer."""


class Input(LayerWidget):
    """Widget class for the Input layer."""

    def __init__(self, layers: t.LayerObject) -> None:
        super().__init__(layers)

        self._input_shape = st.number_input(
            "Number of input columns:", value=1, min_value=1, max_value=10_000
        )

    def get_connection(self) -> None:
        return

    @property
    def params(self) -> t.InputParams:
        return {"shape": (int(self._input_shape),)}


class Dense(LayerWidget):
    """Widget class for the Dense layer."""

    def __init__(self, layers: t.LayerObject) -> None:
        super().__init__(layers)

        activations = enums.activations.classes
        self._units_num = st.number_input(
            "Number of units:", value=1, min_value=1, max_value=10_000
        )
        self._activation = st.selectbox("Activation function:", activations)
        self._connect_to = st.selectbox("Connect layer to:", self._layers)

    def get_connection(self) -> t.Layer:
        if not self._connect_to:
            raise errors.LayerError("Please, select the connection!")

        return self._layers[self._connect_to]

    @property
    def params(self) -> t.DenseParams:
        return {
            "units": int(self._units_num),
            "activation": enums.activations.classes[self._activation]
            if self._activation
            else enums.activations.classes["Linear"],
        }


class Concatenate(LayerWidget):
    """Widget class for the Concatenate layer."""

    def __init__(self, layers: t.LayerObject) -> None:
        super().__init__(layers)

        self._concatenate = st.multiselect("Select layers (at least 2):", self._layers)

    def get_connection(self) -> list[t.Layer]:
        if len(self._concatenate) < 2:
            raise errors.LayerError("Please, select the layers to concatenate!")

        return [self._layers[name] for name in self._concatenate]

    @property
    def params(self) -> t.LayerParams:
        return {}


class BatchNormalization(LayerWidget):
    """Widget class for the BatchNormalization layer."""

    def __init__(self, layers: t.LayerObject) -> None:
        super().__init__(layers)

        self._momentum = st.number_input(
            "Momentum:", value=0.99, min_value=1e-2, max_value=1.0, step=1e-2
        )
        self._epsilon = st.number_input(
            "Epsilon",
            value=1e-3,
            min_value=1e-4,
            max_value=1e-2,
            step=1e-4,
            format="%e",
        )
        self._connect_to = st.selectbox("Connect layer to:", self._layers)

    def get_connection(self) -> t.Layer:
        if not self._connect_to:
            raise errors.LayerError("Please, select the connection!")

        return self._layers[self._connect_to]

    @property
    def params(self) -> t.BatchNormalizationParams:
        return {"momentum": float(self._momentum), "epsilon": float(self._epsilon)}


class Dropout(LayerWidget):
    """Widget class for the Dropout layer."""

    def __init__(self, layers: t.LayerObject) -> None:
        super().__init__(layers)

        self._rate = st.number_input(
            "Rate:", value=0.2, min_value=1e-2, max_value=0.99, step=1e-2
        )
        self._connect_to = st.selectbox("Connect layer to:", self._layers)

    def get_connection(self) -> t.Layer:
        if not self._connect_to:
            raise errors.LayerError("Please, select the connection!")

        return self._layers[self._connect_to]

    @property
    def params(self) -> t.DropoutParams:
        return {"rate": float(self._rate)}
