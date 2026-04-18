import streamlit as st
import requests

# إعدادات الصفحة
st.set_page_config(page_title="ICT Trading Hub", layout="wide")

st.title("📊 ICT Smart Money Dashboard")

# استبدل هذا الرابط برابط Railway الخاص بك (تأكد من وجود https:// و /webhook)
RAILWAY_URL = "https://web-production-6c2d0.up.railway.app/webhook"

# --- توزيع الشاشة (المربعات المرتبة) ---
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.subheader("🛠 Settings")
    symbol = st.selectbox("Market", ["EURUSD", "GBPUSD", "XAUUSD", "BTCUSD"])
    side = st.radio("Order Type", ["BUY", "SELL"])
    size = st.number_input("Lot Size", value=0.1, step=0.01)

with col2:
    st.subheader("🎯 PD Arrays Entry")
    entry = st.number_input("Entry Price", format="%.5f")
    # ترتيب الخانات بالعرض
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        sl = st.number_input("Stop Loss", format="%.5f")
    with sub_col2:
        tp = st.number_input("Target (TP)", format="%.5f")
    
    if st.button("🚀 EXECUTE SIGNAL", use_container_width=True):
        data = {
            "symbol": symbol,
            "side": side.lower(),
            "quantity": size,
            "price": entry,
            "sl": sl,
            "tp": tp
        }
        try:
            resp = requests.post(RAILWAY_URL, json=data, timeout=10)
            if resp.status_code == 200:
                st.success("✅ Signal Sent Successfully!")
            else:
                st.error(f"❌ Error: Railway is not responding (Code {resp.status_code})")
        except Exception as e:
            st.error(f"⚠️ Connection Failed: Make sure Railway is Active")

with col3:
    st.subheader("🕒 Market Sessions")
    st.info("**Asian Killzone**: 00:00 - 06:00")
    st.info("**London Open**: 08:00 - 12:00")
    st.info("**NY Open**: 13:00 - 17:00")

st.divider()
st.caption("Connected to Railway Engine: " + RAILWAY_URL)
