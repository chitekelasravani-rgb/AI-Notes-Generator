import streamlit as st
from pypdf import PdfReader

st.set_page_config(
    page_title="AI Notes Generator",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Notes Generator")
st.write("Upload a PDF and generate simple notes from it.")

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("PDF uploaded successfully!")

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    st.subheader("📄 Extracted Text")

    if text.strip():
        st.text_area(
            "PDF Content",
            text,
            height=300
        )

        # Simple note generation
        words = text.split()

        if len(words) > 100:
            notes = " ".join(words[:100]) + "..."
        else:
            notes = text

        st.subheader("📝 Generated Notes")

        st.write(notes)

        st.download_button(
            label="⬇️ Download Notes",
            data=notes,
            file_name="generated_notes.txt",
            mime="text/plain"
        )


    else:
        st.error("Could not extract text from this PDF.")