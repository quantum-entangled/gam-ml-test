import data_classes.data as data_cls
import data_classes.model as model_cls
import streamlit as st

import managers.data_manager as dm
import managers.errors as err
import managers.model_manager as mm


def upload_file_ui(data: data_cls.Data, model: model_cls.Model) -> None:
    """Generate UI for uploading a file.

    Parameters
    ----------
    data : Data
        Data container object.
    model : Model
        Model container object.
    """
    st.header("Upload File")
    st.markdown("Upload a file from your system by clicking the `Browse files` button.")

    uploaded_file = st.file_uploader("Choose a data file:", "csv", key="file_uploader")

    if uploaded_file:
        try:
            dm.upload_file(uploaded_file, data, model)
            st.success("File is uploaded and ready to be processed!", icon="✅")
        except err.UploadError as error:
            st.error(error, icon="❌")


def upload_model_ui(model: model_cls.Model) -> None:
    """Generate UI for uploading a model.

    Parameters
    ----------
    model : Model
        Model container object.
    """
    st.header("Upload Model")
    st.markdown(
        "Upload a model from your system by clicking the `Browse files` button."
    )

    uploaded_model = st.file_uploader(
        "Choose a model file:", "h5", key="model_uploader"
    )

    if uploaded_model:
        try:
            mm.upload_model(uploaded_model, model)
            st.success("Model is uploaded and ready to be processed!", icon="✅")
        except err.UploadError as error:
            st.error(error, icon="❌")
