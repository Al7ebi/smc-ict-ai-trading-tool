import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. إعدادات الصفحة (شاشة كاملة)
st.set_page_config(page_title="MARKET PULSE // GRID", layout="wide", initial_sidebar_state="collapsed")

# 2. حقن كود CSS عنيف لمحاكاة التصميم المظلم والنيون
st.markdown("""
    <style>
    /* لون الخلفية الأسود المائل للرمادي */
    .stApp { background-color: #0b0e14; color: #8b9bb4; font-family: 'Courier New', Courier, monospace; }
    
    /* إخفاء الهوامش العلوية */
    .block-container { padding-top: 1rem; padding-bottom: 0rem; }
    
    /* تنسيق النصوص والعناوين */
    h1, h2, h3 { color: #ffffff; font-weight: bold; font-family: 'Arial', sans-serif; }
    
    /* الصناديق (Cards) */
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] {
        background-color: #151a22;
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #1f2937;
    }
    
    /* الألوان المخصصة (الأصفر الفسفوري والأخضر) */
    .neon-yellow { color: #f5d300; font-weight: bold; }
    .neon-green { color: #00ffaa; font-weight: bold; }
    .neon-red { color: #ff3366; font-weight: bold; }
    
    /* خطوط الأرقام الكبيرة */
    .big-pnl { font-size: 3rem; color: #f5d300; font-weight: bold; margin: 0; line-height: 1.2; }
    </style>
""", unsafe_allow_html=True)

# --- الهيدر العلوي ---
header_col1, header_col2, header_col3 = st.columns([2, 4, 2])
with header_col1:
    st.markdown("### MARKET PULSE\n<span class='neon-yellow'>// G R I D</span>", unsafe_allow_html=True)
with header_col2:
    st.markdown("<div style='text-align: center; margin-top: 10px;'><span class='neon-green'>PNL: +$12,184</span> | 80% WIN RATE | VOL: 5H | SCAN: 680/HR</div>", unsafe_allow_html=True)
with header_col3:
    st.markdown("<h3 style='text-align: right;'>7:45:46 PM <span class='neon-yellow'>LIVE</span></h3>", unsafe_allow_html=True)

st.markdown("<hr style='border-color: #1f2937; margin-top: 0;'>", unsafe_allow_html=True)

# --- التقسيمة الرئيسية (3 أعمدة مثل الصورة) ---
col_left, col_center, col_right = st.columns([1, 2, 1])

# --- العمود الأيسر (الرادار والأخبار) ---
with col_left:
    st.markdown("##### SIGNAL RADAR <span style='float:right; color:#f5d300;'>LIVE</span>", unsafe_allow_html=True)
    st.markdown("🟡 **ENTER Gold @ 2350**")
    st.markdown("🟢 **ENTER EU @ 1.0850**")
    st.markdown("🟡 Scanned 395 markets. 20 hits.")
    
    st.markdown("<br>##### MARKET TAPE", unsafe_allow_html=True)
    st.markdown("Debt ceiling <span style='float:right;' class='neon-green'>+551</span>", unsafe_allow_html=True)
    st.markdown("Waymo public <span style='float:right;' class='neon-red'>-2</span>", unsafe_allow_html=True)
    st.markdown("Uranium $80 <span style='float:right;' class='neon-green'>+58</span>", unsafe_allow_html=True)
    
    st.markdown("<br>##### DESK METRICS", unsafe_allow_html=True)
    st.markdown("<h2 class='neon-yellow'>00:01:17</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c1.markdown("CAPITAL DEPLOYED<br>**$765**", unsafe_allow_html=True)
    c2.markdown("CAPITAL VELOCITY<br><span class='neon-green'>51x</span>", unsafe_allow_html=True)

# --- العمود الأوسط (الشارت والـ PNL) ---
with col_center:
    st.markdown("##### FUTURES PULSE / DESK SESSION 302")
    st.markdown("<p class='big-pnl'>+$12,184</p>", unsafe_allow_html=True)
    
    # صنع شارت وهمي يحاكي الشارت الأصفر اللي بالصورة
    np.random.seed(42)
    prices = np.cumsum(np.random.randn(100) * 10 + 5) + 1000
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=prices, mode='lines', line=dict(color='#f5d300', width=2), fill='tozeroy', fillcolor='rgba(245, 211, 0, 0.1)'))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=10, b=0),
        xaxis=dict(showgrid=False, visible=False),
        yaxis=dict(showgrid=True, gridcolor='#1f2937', side='right', tickfont=dict(color='#8b9bb4')),
        height=350
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("##### <span class='neon-green'>73%</span> AGGRESSIVE BID FLOW", unsafe_allow_html=True)
    st.progress(0.73)

# --- العمود الأيمن (الحيتان والسيولة) ---
with col_right:
    st.markdown("##### FLOW BIAS")
    c1, c2 = st.columns(2)
    c1.markdown("<h2 class='neon-green'>75%</h2>", unsafe_allow_html=True)
    c2.markdown("<h2 class='neon-yellow' style='text-align:right;'>25%</h2>", unsafe_allow_html=True)
    st.progress(0.75)
    
    st.markdown("<br>##### WHALE WATCH <span style='float:right; color:#f5d300;'>5 WALLETS</span>", unsafe_allow_html=True)
    st.markdown("0xe41f... <span style='float:right;' class='neon-green'>$40.3K</span>", unsafe_allow_html=True)
    st.markdown("0xa226... <span style='float:right;' class='neon-green'>$41.2K</span>", unsafe_allow_html=True)
    st.markdown("0xf882... <span style='float:right;' class='neon-green'>$9.7K</span>", unsafe_allow_html=True)
    
    st.markdown("<br>##### SECTOR YIELD")
    st.markdown("CRYPTO <span style='float:right;' class='neon-green'>+$1181</span>", unsafe_allow_html=True)
    st.markdown("WEATHER <span style='float:right;' class='neon-green'>+$759</span>", unsafe_allow_html=True)
