import data_classes.data as data_cls
import data_classes.model as model_cls
import streamlit as st
import widgets.predictions as pr
import widgets.training as tr

import managers.data_manager as dm
import managers.model_manager as mm

st.set_page_config(page_title="Predictions", page_icon="🔮")

if "data" not in st.session_state or "model" not in st.session_state:
    st.session_state.data = data_cls.Data()
    st.session_state.model = model_cls.Model()

data = st.session_state.data
model = st.session_state.model

if not dm.file_exists(data) or not mm.model_exists(model):
    st.info(
        "You will be able to make predictions once you upload the data file, as well "
        "as create/upload and compile the model.",
        icon="💡",
    )
else:
    with st.container():
        tr.set_callbacks_ui(model)
        pr.make_predictions_ui(data, model)
