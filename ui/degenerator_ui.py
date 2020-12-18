import os

import requests
import streamlit as st

MODEL_HOST = os.getenv("MODEL_HOST") or "localhost"


def get_text(host="localhost"):
    return requests.get(f"http://{host}:8000/text").json()["text"]


def get_pic(host="localhost"):
    return requests.get(f"http://{host}:8000/style_url").json()["output_url"]


def main():
    st.title("""deGenerator""")
    st.write("Power of AI to bring you brain damage")
    st.write("It's less than a generator.")
    if st.button("Random bullshit GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"):
        st.markdown("---")
        st.write(get_text(host=MODEL_HOST))
        st.image(get_pic(host=MODEL_HOST), use_column_width=True)
        st.markdown("---")


if __name__ == "__main__":
    main()
