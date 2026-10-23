import streamlit as st

st.set_page_config(
    page_title="Vietcombank KYC Demo",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        :root {
            --bg-dark: #071b2d;
            --bg-mid: #0d233d;
            --panel: #122d49;
            --panel-soft: rgba(18, 45, 73, 0.78);
            --accent: #2f7df6;
            --accent-soft: #6bb5ff;
            --text: #edf6ff;
            --text-soft: #a9bdd4;
            --border: rgba(255,255,255,0.08);
            --shadow: rgba(0,0,0,0.22);
        }

        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(180deg, var(--bg-dark) 0%, var(--bg-mid) 100%);
            color: var(--text);
        }

        .stApp {
            background: linear-gradient(180deg, var(--bg-dark) 0%, var(--bg-mid) 100%);
        }

        section[data-testid="stSidebar"] {
            background: var(--bg-mid);
            border-right: 1px solid var(--border);
        }

        .block-container {
            padding-top: 0.5rem;
            padding-bottom: 2rem;
        }

        .topbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            padding: 10px 18px;
            margin: 0 0 1rem 0;
            background: rgba(255,255,255,0.03);
            border: 1px solid var(--border);
            border-radius: 14px;
            box-shadow: 0 8px 20px var(--shadow);
        }

        .brand-wrap {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            min-width: 180px;
        }

        .brand-mark {
            width: 12px;
            height: 12px;
            background: linear-gradient(180deg, var(--accent-soft) 0%, var(--accent) 100%);
            border-radius: 50%;
            box-shadow: 0 0 12px rgba(47,125,246,0.8);
        }

        .brand-name {
            font-size: 1.2rem;
            font-weight: 700;
            letter-spacing: 0.02em;
            color: var(--text);
        }

        .nav-menu {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            gap: 0.8rem;
            flex: 1;
        }

        .nav-item {
            color: var(--text-soft);
            font-size: 0.9rem;
            font-weight: 600;
            padding: 0.45rem 0.8rem;
            border-radius: 10px;
            transition: all 0.2s ease;
        }

        .nav-item:hover {
            background: rgba(255,255,255,0.04);
            color: var(--text);
        }

        .nav-item.active {
            background: rgba(47,125,246,0.12);
            color: var(--text);
            border: 1px solid rgba(47,125,246,0.25);
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .mini-pill {
            color: var(--text-soft);
            border: 1px solid var(--border);
            background: rgba(255,255,255,0.02);
            border-radius: 999px;
            padding: 0.45rem 0.8rem;
            font-size: 0.8rem;
        }

        .primary-btn {
            background: linear-gradient(180deg, var(--accent) 0%, #1d63d6 100%);
            color: white !important;
            font-weight: 600;
            border: none;
            border-radius: 12px;
            padding: 0.6rem 1.1rem;
            box-shadow: 0 8px 18px rgba(47,125,246,0.25);
        }

        .primary-btn:hover {
            background: linear-gradient(180deg, var(--accent-soft) 0%, var(--accent) 100%);
        }

        .stTabs [data-baseweb="tab-list"] {
            background: rgba(255,255,255,0.02);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 4px;
            gap: 6px;
        }

        .stTabs [data-baseweb="tab"] {
            background: transparent;
            color: var(--text-soft);
            border-radius: 10px;
            padding: 8px 12px;
            font-weight: 600;
            font-size: 13px;
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(180deg, var(--accent) 0%, #1f67d9 100%);
            color: white;
            box-shadow: 0 8px 18px rgba(47,125,246,0.35);
        }

        div.stButton > button {
            background: linear-gradient(180deg, var(--accent) 0%, #1d63d6 100%);
            border: none;
            color: white;
            border-radius: 12px;
            font-weight: 600;
            padding: 0.45rem 1.1rem;
            box-shadow: 0 8px 18px rgba(47,125,246,0.25);
        }

        div.stButton > button:hover {
            background: linear-gradient(180deg, var(--accent-soft) 0%, var(--accent) 100%);
        }

        .card {
            background: var(--panel-soft);
            border: 1px solid var(--border);
            border-radius: 18px;
            box-shadow: 0 8px 22px var(--shadow);
            padding: 1rem;
        }

        h1, h2, h3, h4, h5, h6, p, span, div {
            color: var(--text);
        }

        div[data-testid="stSidebarNavLink"] {
            border-radius: 10px;
            color: var(--text-soft);
        }

        div[data-testid="stSidebarNavLink"]:hover {
            background: rgba(255,255,255,0.04);
            color: var(--text);
        }

        div[data-testid="stSidebarNavLink"][aria-current="page"] {
            background: rgba(47,125,246,0.12);
            color: var(--text);
            border: 1px solid rgba(47,125,246,0.25);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="topbar">
        <div class="brand-wrap">
            <div class="brand-mark"></div>
            <div class="brand-name">Vietcombank</div>
        </div>

        <div class="nav-menu">
            <div class="nav-item active">Trang chủ</div>
            <div class="nav-item">Sản phẩm</div>
            <div class="nav-item">Dịch vụ</div>
            <div class="nav-item">Giải pháp</div>
            <div class="nav-item">Tin tức</div>
            <div class="nav-item">Liên hệ</div>
        </div>

        <div class="header-actions">
            <div class="mini-pill">1900 54 54 13</div>
            <button class="primary-btn">Đăng nhập</button>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.tabs(["Tổng quan", "KYC", "Xác minh", "Báo cáo"])

with st.container():
    col1, col2 = st.columns([1.4, 1])

    with col1:
        st.markdown(
            """
            <div class="card">
                <h2 style="margin-bottom: 0.4rem;">Chào mừng bạn trở lại</h2>
                <p style="color: var(--text-soft); margin-top: 0;">Hệ thống KYC thông minh dành cho doanh nghiệp và khách hàng.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <h3 style="margin-bottom: 0.5rem;">Trạng thái hệ thống</h3>
                <p style="color: var(--text-soft); margin: 0;">Hoạt động bình thường · 99.98% uptime</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")

metrics = st.columns(4)
for i, label in enumerate(["Khách hàng", "Đơn xác minh", "Tỉ lệ thành công", "Tổng doanh thu"]):
    with metrics[i]:
        st.metric(label=label, value="--", delta="--")

st.write("")

left, right = st.columns([1.3, 1])

with left:
    st.markdown(
        """
        <div class="card">
            <h3>Tiến độ xử lý</h3>
            <p style="color: var(--text-soft);">Theo dõi tiến độ xác minh và xử lý hồ sơ hiện tại.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        """
        <div class="card">
            <h3>Thông báo</h3>
            <p style="color: var(--text-soft);">Không có cảnh báo mới trong 24 giờ qua.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.sidebar.title("Menu")
st.sidebar.page_link("app.py", label="Trang chủ", icon="🏠")
st.sidebar.page_link("app.py", label="KYC", icon="🧾")
st.sidebar.page_link("app.py", label="Tài liệu", icon="📚")
st.sidebar.page_link("app.py", label="Cài đặt", icon="⚙️")
