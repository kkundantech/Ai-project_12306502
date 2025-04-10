import streamlit as st
import google.generativeai as genai
from datetime import datetime
from PIL import Image
import io

# Configure Gemini API
API_KEY = "AIzaSyC_fKYzgmw9P4rbdR2LXwBD7M3CjHh4C68"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "gemini-1.5-pro-latest",
    safety_settings={
        "HARASSMENT": "BLOCK_LOW_AND_ABOVE",
        "HATE": "BLOCK_LOW_AND_ABOVE",
        "SEXUAL": "BLOCK_LOW_AND_ABOVE",
        "DANGEROUS": "BLOCK_LOW_AND_ABOVE"
    }
)

# Set Page Config
st.set_page_config(page_title="AI Ethical Fashion Assistant", layout="wide", initial_sidebar_state="expanded")

# Custom CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
            color: #333;
        }

        .main-container {
            background-color: rgba(255, 255, 255, 0.88);
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            backdrop-filter: blur(6px);
            animation: fadeIn 1s ease-in;
        }

        .answer-box {
            background-color: #eafaf1;
            border-left: 5px solid #00b894;
            padding: 1rem;
            border-radius: 10px;
            font-size: 1.1rem;
            margin-top: 1rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            animation: slideIn 0.8s ease-in;
        }

        div.stButton > button {
            background: linear-gradient(to right, #00b894, #55efc4);
            color: white;
            border: none;
            padding: 0.6rem 1.5rem;
            font-size: 1rem;
            border-radius: 10px;
            transition: 0.3s ease;
        }

        div.stButton > button:hover {
            background: linear-gradient(to right, #00cec9, #81ecec);
            transform: scale(1.04);
        }

        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }

        @keyframes slideIn {
            from {transform: translateY(30px); opacity: 0;}
            to {transform: translateY(0); opacity: 1;}
        }
    </style>
""", unsafe_allow_html=True)

# Theme Toggle
mode = st.sidebar.selectbox("Choose Theme", ["Light Mode", "Dark Mode"])
if mode == "Dark Mode":
    st.markdown("""
        <style>
            .main-container {
                background-color: #1e1e1e;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)

# Sidebar Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar.expander("📜 Chat History", expanded=True):
    if st.session_state.chat_history:
        for i, item in enumerate(reversed(st.session_state.chat_history), 1):
            st.markdown(f"**{i}. Q:** {item['question']}")
            st.markdown(f"**A:** {item['answer']}")
            st.markdown("---")
    else:
        st.write("No history yet.")

# Header
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
st.image("https://images.fastfashionnews.co.uk/wp-content/uploads/2021/02/Sustainable-fashion-brands-1024x1024.jpeg", width=100)
st.markdown("<h1>AI Ethical Fashion Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p>Shop smart, shop sustainably 🌿</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.subheader("💬 Ask Your Ethical Fashion Question")
user_input = st.text_area("Type your question here:", key="user_text")

uploaded_file = st.file_uploader("📷 Upload a fashion image (optional):", type=["jpg", "jpeg", "png"])

if st.button("✨ Get Insight"):
    if user_input.strip():
        blocked_keywords = ["kill", "hate", "suicide", "violence"]
        if any(word in user_input.lower() for word in blocked_keywords):
            st.error("Your question may contain unsafe content. Please rephrase.")
        else:
            with st.spinner("Generating sustainable insight..."):
                try:
                    prompt = (
                        "You're an ethical fashion expert with a friendly, positive vibe, like a helpful stylist. "
                        "Respond in a conversational tone with clear, easy-to-understand tips. "
                        f"Here's the user question: {user_input}"
                    )
                    if uploaded_file:
                        image_bytes = uploaded_file.read()
                        image = Image.open(io.BytesIO(image_bytes))
                        prompt += "\n\nAlso, analyze the uploaded fashion image."
                        response = model.generate_content([prompt, image])
                    else:
                        response = model.generate_content(prompt)

                    answer = response.text.strip()
                    answer = answer.replace("Tip", "✨ Tip")

                    st.session_state.chat_history.append({"question": user_input, "answer": answer})

                    st.markdown('<div class="answer-box">', unsafe_allow_html=True)
                    st.markdown(f"**You asked:** {user_input}")
                    st.markdown(f"**Bot says:** {answer}")
                    st.markdown('</div>', unsafe_allow_html=True)

                    st.markdown("#### 📊 Rate this answer:")
                    feedback = st.radio("Was this helpful?", ["👍 Yes", "👎 No"], key=f"feedback_{len(st.session_state.chat_history)}")
                    st.write("Thank you for your feedback!" if feedback else "")

                except Exception as e:
                    st.error(f"⚠️ API Error: {e}")
    else:
        st.warning("Please enter a valid question.")

with st.expander("📌 Ethical Fashion FAQs & Tips", expanded=False):
    st.markdown("""
        **🌿 What is Ethical Fashion?**  
        Ethical fashion focuses on creating clothes that are good for people, animals, and the planet.

        **👕 ✨ Tip 1: Choose Quality over Quantity**
        **♻️ ✨ Tip 2: Reuse & Recycle**
        **🧵 ✨ Tip 3: Support Local & Fair Trade Brands**
        **👖 ✨ Tip 4: Know Your Fabrics**
        **🛙️ ✨ Tip 5: Rent, Swap, or Thrift**
        **🧺 ✨ Tip 6: Wash Clothes Responsibly**
        **🧷 ✨ Tip 7: Mend, Don’t End**
        **🌍 ✨ Tip 8: Avoid Plastic Fibers**
        **📦 ✨ Tip 9: Choose Eco-Friendly Packaging**
        **🔄 ✨ Tip 10: Embrace Minimalism**
        **🧵 ✨ Tip 11: DIY Clothing Projects**
        **💚 ✨ Tip 12: Support Second-Hand Shops**
        **📱 ✨ Tip 13: Use Apps for Ethical Ratings**
        **🚫 ✨ Tip 14: Say No to Greenwashing**
        **🧶 ✨ Tip 15: Prefer Natural Dyes**
        **💼 ✨ Tip 16: Support Ethical Workplace Practices**
        **👟 ✨ Tip 17: Look for Vegan Footwear**
        **🌾 ✨ Tip 18: Buy Less, Wear More**
        **🛠️ ✨ Tip 19: Repurpose Old Clothes Creatively**
        **📚 ✨ Tip 20: Educate Yourself on Fashion Ethics**
    """)

# Download Chat
if st.session_state.chat_history:
    if st.button("📁 Download Chat"):
        chat_lines = [f"Q: {item['question']}\nA: {item['answer']}" for item in st.session_state.chat_history]
        full_chat = "\n\n".join(chat_lines)
        now = datetime.now().strftime("%Y-%m-%d_%H-%M")
        st.download_button(
            label="Download Chat as .txt",
            data=full_chat,
            file_name=f"ethical_fashion_chat_{now}.txt",
            mime="text/plain"
        )

# Footer
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align:center; font-size: 0.9rem; color: #aaa;">Made with ❤️ by Kundan | Powered by Streamlit & Gemini AI</div>', unsafe_allow_html=True)
