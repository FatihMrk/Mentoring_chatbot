import streamlit as st
import pandas as pd


st.title("Mentorluk Chatbotu 🤖")

@st.cache_data
def load_data():
    df = pd.read_excel("mentoring_soruEklenmis_dataset.xlsx")
    return df

df = load_data()

user_input = st.text_input("Sorunuzu yazın:")

if user_input:
    matching_row = df[df['Questions'].str.contains(user_input, case=False, na=False)]

    if not matching_row.empty:
        cevap = matching_row.iloc[0]['Answer']
        st.success(f"Cevap: {cevap}")
    else:
        # Burada tahmini yanıt üretiyoruz
        if "data science" in user_input.lower():
            st.info("Tahmini cevap: Data science, veriden anlam çıkarmak için istatistik, programlama ve iş bilgilerini birleştiren bir alandır.")
        elif "cv" in user_input.lower():
            st.info("Tahmini cevap: CV yazarken deneyimlerinizi, yetkinliklerinizi ve eğitiminizi kısa ve etkili bir şekilde sunmalısınız.")
        elif "mülakat" in user_input.lower():
            st.info("Tahmini cevap: Mülakatlara hazırlanırken sık sorulan soruları çalışmak ve şirketi araştırmak önemlidir.")
        else:
            st.warning("Üzgünüm, bu soruya uygun bir yanıt bulamadım.")
