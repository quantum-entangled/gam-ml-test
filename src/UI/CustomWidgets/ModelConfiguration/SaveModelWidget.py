from typing import Any, Protocol

import ipywidgets as iw


class ModelManager(Protocol):
    """Protocol for model managers."""

    def save_model(self, output_handler: Any) -> None:
        ...


class SaveModelWidget(iw.VBox):
    """Widget to save a model."""

    name = "Save Model"

    def __init__(self, model_manager: ModelManager, **kwargs) -> None:
        """Initialize the save model widget window."""
        self.model_manager = model_manager

        self.save_model_button = iw.Button(description="Save Model")
        self.save_model_button.on_click(self._on_save_model_button_clicked)
        self.save_model_output = iw.Output()

        super().__init__(
            children=[self.save_model_button, self.save_model_output], **kwargs
        )

    def _on_save_model_button_clicked(self, _) -> None:
        """Callback for save model button."""
        self.model_manager.save_model(output_handler=self.save_model_output)
