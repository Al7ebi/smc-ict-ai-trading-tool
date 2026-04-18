import streamlit as st
import requests

# 1. إعدادات المظهر العام (تنسيق مريح للعين)
st.set_page_config(page_title="ICT Trading Hub", layout="wide", initial_sidebar_state="collapsed")

# تصميم الواجهة بـ CSS بسيط لجعلها تشبه منصات التداول الاحترافية
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    div[data-testid="stMetricValue"] { font-size: 1.8rem; }
    </style>
    """, unsafe_allow_html=True)

# 2. رابط المحرك (عدل الرابط هنا فقط)
RAILWAY_URL = "https://web-production-6c2d0.up.railway.app/webhook"

st.title("🏹 SMC/ICT Precision Terminal")
st.divider()

# 3. توزيع المربعات حسب استراتيجية ICT
col_settings, col_main, col_info = st.columns([1, 2, 1])

with col_settings:
    st.subheader("⚙️ الإعدادات")
    symbol = st.selectbox("الزوج", ["XAUUSD", "EURUSD", "GBPUSD", "BTCUSD"])
    side = st.radio("النوع", ["BUY", "SELL"], horizontal=True)
    lot = st.number_input("حجم اللوت", value=0.01, step=0.01, format="%.2f")
    
with col_main:
    st.subheader("🎯 تنفيذ الصفقة (PD Arrays)")
    entry = st.number_input("سعر الدخول (Entry)", format="%.5f")
    
    # صف للأهداف والوقف
    c1, c2 = st.columns(2)
    with c1:
        sl = st.number_input("وقف الخسارة (SL)", format="%.5f")
    with c2:
        tp = st.number_input("الهدف (TP)", format="%.5f")
    
    st.write("") # مسافة
    if st.button("🚀 إرسال الإشارة للمحرك"):
        payload = {
            "symbol": symbol, "side": side.lower(), 
            "quantity": lot, "price": entry, 
            "sl": sl, "tp": tp
        }
        try:
            r = requests.post(RAILWAY_URL, json=payload, timeout=5)
            if r.status_code == 200:
                st.success("✅ تم إرسال الأمر بنجاح إلى Railway!")
            else:
                st.error(f"❌ المحرك (Railway) أعطى خطأ: {r.status_code}")
        except:
            st.error("⚠️ فشل الاتصال! تأكد أن Railway في حالة Active وليس Crashed.")

with col_info:
    st.subheader("🕒 توقيت السيولة (Killzones)")
    st.info("🟢 **Asian:** 00:00 - 06:00")
    st.info("🔵 **London:** 08:00 - 12:00")
    st.info("🔴 **NY Open:** 13:00 - 17:00")
    
    st.divider()
    st.write("🔧 **حالة الربط:**")
    st.code("Railway: Connected" if ".up.railway.app" in RAILWAY_URL else "Railway: Missing Link")

st.divider()
st.caption("Mohammad's Private ICT Trading Terminal v1.0")
