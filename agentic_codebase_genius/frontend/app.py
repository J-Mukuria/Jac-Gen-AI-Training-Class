import streamlit as st
import requests
import os

BACKEND_URL = "http://localhost:8000/walker/generate_docs/run"

st.set_page_config(page_title="🤖 Codebase Genius", layout="centered")
st.title("🤖 Agentic Codebase Genius")
st.caption("An AI-powered code documentation generator built with Jac and Streamlit.")

st.divider()
repo_url = st.text_input("Enter a GitHub Repository URL:", placeholder="https://github.com/jaseci-labs/jaseci")

if st.button("Generate Documentation 🚀"):
    if not repo_url.strip():
        st.warning("Please enter a valid GitHub repository URL.")
    else:
        with st.spinner("Processing repository..."):
            try:
                response = requests.post(BACKEND_URL, json={"repo_url": repo_url}, timeout=600)
                if response.status_code == 200:
                    st.success("✅ Documentation successfully generated!")
                    repo_name = repo_url.split('/')[-1].replace('.git','')
                    doc_path = f"../backend/outputs/{repo_name}/docs.md"

                    if os.path.exists(doc_path):
                        st.subheader("📄 Generated Documentation Preview:")
                        with open(doc_path, "r", encoding="utf-8") as f:
                            st.markdown(f.read())
                        diagram_path = f"../backend/outputs/{repo_name}/diagram.png"
                        if os.path.exists(diagram_path):
                            st.image(diagram_path, caption="Generated Code Context Graph")
                    else:
                        st.info("Documentation file not found yet. Check backend output folder.")
                else:
                    st.error(f"Backend error: {response.status_code}")
            except Exception as e:
                st.error(f"⚠️ Error connecting to backend: {e}")

st.divider()
st.markdown("**Tip:** Make sure your Jac backend is running before clicking the button.")
