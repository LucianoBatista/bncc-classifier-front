import re
import streamlit as st
import streamlit.components.v1 as components
import requests
import json
import streamlit_modal as modal


st.write("# Classificador BNCC")

st.markdown(
    """
    --- 
    Este é um MVP (Minimum Viable Product) resultado do trabalho do **Grupo de Educação**: 
    - 👦 [Pedro](https://www.linkedin.com/in/pedromoreau/)
    - 👧 [Brisa](https://www.linkedin.com/in/brisarosatti/)
    - 👦 [Will](https://www.linkedin.com/in/wilson-font/)
    - 👦 [Luciano](https://www.linkedin.com/in/lucianobatistads/).
    ---
    Nosso classificador recebe uma *questão escrita* no campo abaixo e retorna a classificação da mesma dentro das seguintes categorias:
    
    ### Área do conhecimento

    - Matemática, Arte, Biologia, Ciências, Educação Física, Ensino Religioso, Física, Geografia, História, Inglês, Língua Portuguesa e Química

    ### Grau de escolaridade

    - Ensino Fundamental I, Ensino Fundamental II, Ensino Médio
    ---
    """
)

message_text = st.text_input("👇 Digite aqui a sua questão!")


def predict(text):
    headers = {
        "accept": "application/json",
    }

    params = {
        "item": text,
    }

    print("Preprocessing...")
    response = requests.get(
        "https://bncc-classifier.herokuapp.com/api/v1/model/classify/item",
        params=params,
        headers=headers,
    )

    return response


if message_text != "":

    counting_text_letters = len(message_text)

    if counting_text_letters > 10:

        prediction = st.button("Predict!")

        if prediction:
            response = predict(message_text)
            response_dict = json.loads(response.text)
            # st.write(json.loads(response.text))
            bncc_know_area = response_dict.get("bncc_know_area")
            grau_escolaridade = response_dict.get("school_phase")

            st.markdown(f"> **Área do Conhecimento**: {bncc_know_area[0]}")
            st.markdown(f"> **Grau de Escolaridade**: {grau_escolaridade[0]}")

    else:
        st.markdown(
            "**:warning:Desculpe, não possui caracteres suficientes para realizar a predição.**"
        )
