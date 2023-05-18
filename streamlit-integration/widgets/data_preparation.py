import data_classes.data as data_cls
import streamlit as st

import managers.data_manager as dm


def show_dataframe_ui(data: data_cls.Data) -> None:
    """Generate UI for displaying a dataframe.

    Parameters
    ----------
    data : data_cls.Data
        Data container object.
    """
    st.header("Dataframe")
    data.file = st.experimental_data_editor(data.file, use_container_width=True)


def show_data_stats_ui(data: data_cls.Data) -> None:
    """Generate UI for displaying data statistics.

    Parameters
    ----------
    data : data_cls.Data
        Data container object.
    """
    df = dm.show_data_stats(data)
    st.header("Data Statistics")
    st.dataframe(df, use_container_width=True)


def show_data_plot_ui(data: data_cls.Data) -> None:
    """Generate UI for plotting data columns.

    Parameters
    ----------
    data : data_cls.Data
        Data container object.
    """
    st.header("Data Plot")
    col_1, col_2 = st.columns(2)

    with col_1:
        x = st.selectbox("Select X-axis:", data.columns)

    with col_2:
        y = st.selectbox("Select Y-axis:", data.columns)

    if x and y:
        fig = dm.show_data_plot(x, y, data)
        st.plotly_chart(fig, use_container_width=True)
