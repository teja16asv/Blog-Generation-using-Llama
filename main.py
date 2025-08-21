import streamlit as st
import ollama

# Page setup
st.set_page_config(page_title="📝 Blog Generator", page_icon="🖋️", layout="centered")

#CSS Styling
st.markdown("""
    <style>
        body {
            background-color: #0f172a;
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            background-color: #1e293b;
            padding: 2rem;
            border-radius: 16px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.4);
            max-width: 700px;
            margin: auto;
        }
        h1 {
            color: #38bdf8;
            text-align: center;
            margin-bottom: 1rem;
        }
        input, select {
            border-radius: 8px;
            padding: 10px;
            border: none;
            width: 100%;
            font-size: 1rem;
            margin-top: 0.5rem;
        }
        .stButton > button {
            background: linear-gradient(90deg, #6366f1, #3b82f6);
            color: white;
            padding: 12px 28px;
            border-radius: 12px;
            font-weight: bold;
            font-size: 1rem;
            border: none;
            margin-top: 20px;
            width: 100%;
        }
        .stButton > button:hover {
            background: linear-gradient(90deg, #3b82f6, #1d4ed8);
            cursor: pointer;
        }
        .result-box {
            background-color: #334155;
            padding: 1.2rem;
            border-radius: 12px;
            margin-top: 1.5rem;
            font-size: 1.05rem;
            line-height: 1.6;
            color: #f1f5f9;
        }
    </style>
""", unsafe_allow_html=True)

# Main app
with st.container():
    st.markdown("<div class='main'>", unsafe_allow_html=True)

    st.markdown("<h1>📝 Blog Generator with Ollama</h1>", unsafe_allow_html=True)
    st.write("Generate professional blogs using **LLaMA 2 via Ollama** with customizable tone and length.")

    # Inputs
    topic = st.text_input("🔹 Enter Blog Topic")
    col1, col2 = st.columns(2)
    with col1:
        no_words = st.text_input("🔹 Number of Words", placeholder="e.g. 150")
    with col2:
        blog_style = st.selectbox("✍️ Writing Style", ["Researchers", "Data Scientist", "Common People"])

    if st.button("🚀 Generate Blog"):
        if topic and no_words:
            with st.spinner("Generating blog... ⏳"):
                prompt = f"Write a blog for {blog_style} on the topic '{topic}' within {no_words} words."

                # Call Ollama api
                response = ollama.chat(
                    model="llama2:7b",
                    messages=[{"role": "user", "content": prompt}]
                )

                blog = response["message"]["content"]
                st.markdown(f"<div class='result-box'>{blog}</div>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter both topic and number of words.")

    st.markdown("</div>", unsafe_allow_html=True)
