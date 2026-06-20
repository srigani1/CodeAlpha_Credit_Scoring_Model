import streamlit as st
import pickle
from io import BytesIO
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Credit Risk Predictor",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# THEME SWITCHER
# =====================================================

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

theme = st.sidebar.selectbox(
    "🎨 Select Theme",
    ["Light", "Dark"]
)

# =====================================================
# PROFESSIONAL CSS
# =====================================================

if theme == "Dark":

    st.markdown("""
    <style>

    .stApp{
        background:#0f172a;
    }

    h1,h2,h3,h4,h5,h6,p,label,span{
        color:white !important;
    }

    .main-card{
        background:#1e293b;
        padding:25px;
        border-radius:20px;
        border:1px solid #334155;
    }

    .metric-card{
        background:#1e293b;
        padding:20px;
        border-radius:15px;
        border-left:5px solid #3b82f6;
    }

    .stButton>button{
        background:#3b82f6;
        color:white;
        border:none;
        border-radius:10px;
        font-weight:bold;
        transition:0.3s;
    }

    .stButton>button:hover{
        background:#2563eb;
        transform:scale(1.02);
    }

    </style>
    """,
    unsafe_allow_html=True)

else:

    st.markdown("""
    <style>

    .stApp{
        background:#f4f8ff;
        color:#111827;
    }

    section.main > div{
        background:#f4f8ff;
    }

    h1,h2,h3,h4,h5,h6{
        color:#0f172a !important;
    }

    p, label, .stMarkdown, .stText, [data-testid="stMarkdownContainer"]{
        color:#1f2937 !important;
        font-weight:500;
    }

    .main-card{
        background:#ffffff !important;
        color:#111827 !important;
        padding:25px;
        border-radius:20px;
        border:1px solid #c7d9ff;
        box-shadow:0 12px 30px rgba(37,99,235,0.12);
        margin-bottom:18px;
    }

    .main-card *{
        color:#111827 !important;
        opacity:1 !important;
    }

    .hero-card h1,
    .hero-card p{
        color:#ffffff !important;
        opacity:1 !important;
    }

    .metric-card{
        background:#ffffff !important;
        color:#111827 !important;
        padding:20px;
        border-radius:15px;
        border-left:5px solid #2563eb;
        box-shadow:0 8px 22px rgba(37,99,235,0.10);
    }

    [data-testid="stSidebar"]{
        background:#ffffff !important;
        border-right:1px solid #d6e4ff;
    }

    [data-testid="stSidebar"] *{
        color:#111827 !important;
    }

    [data-testid="stWidgetLabel"] p,
    [data-testid="stWidgetLabel"] label,
    [data-testid="stWidgetLabel"] span{
        color:#111827 !important;
        font-weight:700 !important;
    }

    [data-testid="stNumberInput"] input,
    [data-testid="stTextInput"] input,
    textarea{
        background:#ffffff !important;
        color:#111827 !important;
        -webkit-text-fill-color:#111827 !important;
        border:1px solid #8aa4c8 !important;
        border-radius:10px !important;
        box-shadow:none !important;
        caret-color:#2563eb !important;
    }

    [data-testid="stNumberInput"] input:focus,
    [data-testid="stTextInput"] input:focus,
    textarea:focus{
        border:2px solid #2563eb !important;
        box-shadow:0 0 0 3px rgba(37,99,235,0.16) !important;
    }

    [data-baseweb="select"] > div{
        background:#ffffff !important;
        color:#111827 !important;
        border:1px solid #8aa4c8 !important;
        border-radius:10px !important;
    }

    [data-baseweb="select"] span,
    [data-baseweb="select"] svg,
    [data-baseweb="popover"] *{
        color:#111827 !important;
        fill:#111827 !important;
    }

    [data-baseweb="popover"] ul,
    [data-baseweb="menu"]{
        background:#ffffff !important;
        border:1px solid #d6e4ff !important;
    }

    [data-baseweb="menu"] li:hover{
        background:#e8f1ff !important;
    }

    [data-testid="stNumberInput"] button,
    [data-testid="stNumberInput"] button[kind="secondary"]{
        background:#eaf2ff !important;
        color:#1d4ed8 !important;
        border:1px solid #8fb8ff !important;
    }

    [data-testid="stNumberInput"] button:hover,
    [data-testid="stNumberInput"] button[kind="secondary"]:hover{
        background:#2563eb !important;
        color:#ffffff !important;
        border-color:#2563eb !important;
    }

    [data-testid="stNumberInput"] button svg{
        color:inherit !important;
        fill:currentColor !important;
    }

    [data-testid="stMetric"]{
        background:#ffffff;
        border:1px solid #d6e4ff;
        border-radius:16px;
        padding:16px 18px;
        box-shadow:0 8px 22px rgba(37,99,235,0.10);
    }

    [data-testid="stMetric"] label,
    [data-testid="stMetric"] div{
        color:#111827 !important;
    }

    [data-testid="stAlert"]{
        color:#111827 !important;
        border-radius:14px;
    }

    [data-testid="stAlert"] *{
        color:#111827 !important;
        font-weight:600;
    }

    [data-testid="stDataFrame"]{
        border:1px solid #d6e4ff;
        border-radius:14px;
        overflow:hidden;
    }

    .stButton>button{
        background:#2563eb;
        color:#ffffff !important;
        border:1px solid #2563eb;
        border-radius:12px;
        font-weight:bold;
        transition:0.3s;
        box-shadow:0 8px 18px rgba(37,99,235,0.22);
    }

    .stButton>button:hover{
        background:#1d4ed8;
        color:#ffffff !important;
        transform:scale(1.03);
        border-color:#1d4ed8;
    }

    .stDownloadButton>button{
        background:#16a34a !important;
        color:#ffffff !important;
        border:1px solid #16a34a !important;
        border-radius:12px;
        font-weight:bold;
        box-shadow:0 8px 18px rgba(22,163,74,0.22);
    }

    .stDownloadButton>button:hover{
        background:#15803d !important;
        border-color:#15803d !important;
        color:#ffffff !important;
    }

    input, textarea{
        color:#0f172a !important;
        background:#ffffff !important;
        -webkit-text-fill-color:#0f172a !important;
    }

    </style>
    """,
    unsafe_allow_html=True)

# =====================================================
# LOAD SAVED MODEL
# =====================================================

APP_DIR = Path(__file__).resolve().parent
MODEL_PATH = APP_DIR / "credit_risk_model.pkl"


@st.cache_resource(show_spinner=False)
def load_saved_model():

    if not MODEL_PATH.exists():
        return None

    with MODEL_PATH.open("rb") as file:
        return pickle.load(file)


bundle = load_saved_model()

if bundle is None:

    st.error(
        "Model file not found. Run train_credit_risk_model.py once, then start this app again."
    )

    st.stop()

model = bundle["model"]
le_home = bundle["encoders"]["home"]
le_intent = bundle["encoders"]["intent"]
le_grade = bundle["encoders"]["grade"]
le_default = bundle["encoders"]["default"]
accuracy = bundle["accuracy"]
feature_columns = bundle["feature_columns"]
record_count = bundle["record_count"]


# =====================================================
# PDF REPORT
# =====================================================

def create_pdf_report(report_text):
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

    buffer = BytesIO()

    pdf = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()
    content = [
        Paragraph("AI Credit Risk Report", styles["Title"]),
        Spacer(1, 16)
    ]

    for line in report_text.splitlines():

        clean_line = line.strip()

        if clean_line:
            content.append(
                Paragraph(clean_line, styles["Normal"])
            )
        else:
            content.append(
                Spacer(1, 8)
            )

    pdf.build(content)
    buffer.seek(0)

    return buffer.getvalue()


# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="hero-card" style="
background:linear-gradient(
90deg,
#2563eb,
#3b82f6,
#7c3aed
);
padding:30px;
border-radius:25px;
text-align:center;
margin-bottom:25px;
color:white;
box-shadow:0px 10px 30px rgba(0,0,0,0.15);
">

<h1>💳 AI Credit Risk Predictor</h1>

<p style="font-size:18px;">
Advanced Machine Learning Credit Risk Assessment Platform
</p>

</div>
""",
unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("📊 Analytics Dashboard")

    st.success(
        f"🎯 Model Accuracy: {accuracy:.2f}%"
    )

    st.info("""
This application predicts
loan repayment risk using
Random Forest Machine Learning.
""")

    st.markdown("---")

    st.subheader("📌 Dataset Info")

    st.metric(
        "Records",
        f"{record_count:,}"
    )

    st.metric(
        "Features",
        f"{len(feature_columns)}"
    )

    st.markdown("---")

    st.subheader("📝 Risk Levels")

    st.success("Low Risk : 0 - 30%")

    st.warning("Medium Risk : 30 - 70%")

    st.error("High Risk : 70 - 100%")

# =====================================================
# QUICK ACTIONS
# =====================================================

st.subheader("⚡ Quick Actions")

sample_data = st.button(
    "📋 Load Sample Applicant"
)

# =====================================================
# DEFAULT VALUES
# =====================================================

if sample_data:

    age_default = 28
    income_default = 600000
    emp_length_default = 6
    loan_amount_default = 150000
    interest_rate_default = 11.5
    percent_income_default = 20
    credit_history_default = 7

else:

    age_default = 25
    income_default = 500000
    emp_length_default = 5
    loan_amount_default = 100000
    interest_rate_default = 12.0
    percent_income_default = 20
    credit_history_default = 6

# =====================================================
# SECTION TITLE
# =====================================================

st.markdown("""
<div class="main-card">

<h2>
📝 Applicant Information
</h2>

<p>
Fill all fields accurately for
better credit risk prediction.
</p>

</div>
""",
unsafe_allow_html=True)

st.write("")

# =====================================================
# FORM LAYOUT
# =====================================================

col1, col2 = st.columns(2)

# =====================================================
# PERSONAL DETAILS
# =====================================================

with col1:

    st.markdown("""
    <div class="main-card">

    <h3>
    👤 Personal Information
    </h3>

    </div>
    """,
    unsafe_allow_html=True)

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=age_default,
        help="Applicant age (18 - 100)"
    )

    income = st.number_input(
        "Annual Income (₹)",
        value=income_default,
        help="Example: 500000"
    )

    emp_length = st.number_input(
        "Employment Length (Years)",
        value=emp_length_default,
        help="Total years employed"
    )

    home = st.selectbox(
        "Home Ownership",
        le_home.classes_,
        help="Current housing status"
    )

    default = st.selectbox(
        "Previous Default",
        le_default.classes_,
        help="Any previous loan default?"
    )

    credit_history = st.number_input(
        "Credit History Length",
        value=credit_history_default,
        help="Years of credit history"
    )

# =====================================================
# LOAN DETAILS
# =====================================================

with col2:

    st.markdown("""
    <div class="main-card">

    <h3>
    💰 Loan Information
    </h3>

    </div>
    """,
    unsafe_allow_html=True)

    loan_amount = st.number_input(
        "Loan Amount (₹)",
        value=loan_amount_default,
        help="Requested loan amount"
    )

    interest_rate = st.number_input(
        "Interest Rate (%)",
        value=interest_rate_default,
        help="Example: 12.5"
    )

    intent = st.selectbox(
        "Loan Purpose",
        le_intent.classes_
    )

    grade = st.selectbox(
        "Loan Grade",
        le_grade.classes_
    )

    percent_income = st.number_input(
        "Loan % of Income",
        value=percent_income_default,
        help="Example: 20 means 20% of income"
    )

# =====================================================
# PREDICT BUTTON
# =====================================================

st.write("")

predict_btn = st.button(
    "🚀 Predict Credit Risk",
    use_container_width=True
)
# =====================================================
# PREDICTION ENGINE
# =====================================================

if predict_btn:

    input_data = [[
        age,
        income,
        le_home.transform([home])[0],
        emp_length,
        le_intent.transform([intent])[0],
        le_grade.transform([grade])[0],
        loan_amount,
        interest_rate,
        percent_income,
        le_default.transform([default])[0],
        credit_history
    ]]

    probability = model.predict_proba(input_data)[0]

    risk_score = probability[1] * 100

    confidence = max(probability) * 100

    st.markdown("---")

    st.markdown("""
    <div class="main-card">

    <h2>
    📊 Credit Risk Analytics Dashboard
    </h2>

    </div>
    """,
    unsafe_allow_html=True)

    # =====================================================
    # KPI CARDS
    # =====================================================

    k1, k2, k3 = st.columns(3)

    with k1:

        st.metric(
            "Risk Score",
            f"{risk_score:.2f}%"
        )

    with k2:

        st.metric(
            "Prediction Confidence",
            f"{confidence:.2f}%"
        )

    with k3:

        st.metric(
            "Model Accuracy",
            f"{accuracy:.2f}%"
        )

    # =====================================================
    # RISK METER
    # =====================================================

    st.subheader("📈 Risk Meter")

    st.progress(
        risk_score / 100
    )

    # =====================================================
    # RESULT CARD
    # =====================================================

    st.write("")

    if risk_score < 30:

        risk_level = "LOW RISK"

        st.success(
            f"""
            🟢 LOW CREDIT RISK

            Risk Score : {risk_score:.2f}%

            Recommendation:
            Loan Approval Recommended
            """
        )

    elif risk_score < 70:

        risk_level = "MEDIUM RISK"

        st.warning(
            f"""
            🟠 MEDIUM CREDIT RISK

            Risk Score : {risk_score:.2f}%

            Recommendation:
            Manual Review Required
            """
        )

    else:

        risk_level = "HIGH RISK"

        st.error(
            f"""
            🔴 HIGH CREDIT RISK

            Risk Score : {risk_score:.2f}%

            Recommendation:
            Loan Approval Not Recommended
            """
        )

    # =====================================================
    # RISK BREAKDOWN
    # =====================================================

    st.markdown("---")

    st.subheader("📋 Applicant Summary")

    summary_col1, summary_col2 = st.columns(2)

    with summary_col1:

        st.info(f"""
        👤 Age : {age}

        💰 Income : ₹{income:,.0f}

        🏠 Home Ownership : {home}

        📚 Credit History : {credit_history} Years
        """)

    with summary_col2:

        st.info(f"""
        💳 Loan Amount : ₹{loan_amount:,.0f}

        📈 Interest Rate : {interest_rate}%

        🎯 Loan Intent : {intent}

        ⭐ Loan Grade : {grade}
        """)

    # =====================================================
    # FEATURE IMPORTANCE
    # =====================================================

    st.markdown("---")

    st.subheader("⭐ Feature Importance")

    import pandas as pd

    feature_df = pd.DataFrame({

        "Feature": feature_columns,

        "Importance":
        model.feature_importances_

    })

    feature_df = feature_df.sort_values(
        by="Importance",
        ascending=False
    )

    st.bar_chart(
        feature_df.set_index(
            "Feature"
        )
    )

    # =====================================================
    # TOP IMPORTANT FEATURES
    # =====================================================

    st.subheader("🏆 Top Influencing Factors")

    top_features = feature_df.head(5)

    st.dataframe(
        top_features,
        use_container_width=True
    )

    # =====================================================
    # DOWNLOAD REPORT
    # =====================================================

    report_text = f"""
AI CREDIT RISK REPORT

=================================

Applicant Information

Age : {age}

Annual Income : {income}

Employment Length : {emp_length}

Home Ownership : {home}

Previous Default : {default}

Credit History Length : {credit_history}

=================================

Loan Information

Loan Amount : {loan_amount}

Interest Rate : {interest_rate}

Loan Intent : {intent}

Loan Grade : {grade}

Loan Percent Income : {percent_income}

=================================

Prediction Result

Risk Score : {risk_score:.2f}%

Confidence : {confidence:.2f}%

Risk Category : {risk_level}

Model Accuracy : {accuracy:.2f}%

=================================
"""

    st.download_button(

        label="📄 Download Credit Report",

        data=report_text,

        file_name="Credit_Risk_Report.txt",

        mime="text/plain"

    )

    pdf_report = create_pdf_report(report_text)

    st.download_button(
        label="Export Report as PDF",
        data=pdf_report,
        file_name="Credit_Risk_Report.pdf",
        mime="application/pdf",
        use_container_width=True
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown("""
<div style="
text-align:center;
padding:20px;
">

<h4>
💳 AI Credit Risk Predictor
</h4>

<p>
Developed by
<strong>Bandi Siva Naga Ganesh</strong>
</p>

<p>
Machine Learning Internship Project
</p>

</div>
""",
unsafe_allow_html=True)
