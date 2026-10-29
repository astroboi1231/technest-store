import streamlit as st
from collections import Counter

st.set_page_config(
    page_title="TechNest | Premium Tech Store",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Theme ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
:root { --bg:#070d16; --panel:#0d1724; --panel2:#101e2e; --line:#1b2b3d; --blue:#1688ff; --muted:#9fb0c4; }
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: radial-gradient(ellipse at 70% 0%, #0b2140 0%, var(--bg) 46%); color:#f4f7fb; }
.block-container { max-width: 1440px; padding-top: 1.25rem; padding-bottom: 2rem; }
section[data-testid="stSidebar"] { background:#0a1320; border-right:1px solid var(--line); }
div[data-testid="stVerticalBlockBorderWrapper"] { border-color:var(--line)!important; }
.hero { border:1px solid #18314b; border-radius:24px; padding:38px 42px; background:linear-gradient(110deg,rgba(12,29,49,.98),rgba(7,13,22,.88)), radial-gradient(circle at 80% 30%,#163e7a,#07101c); position:relative; overflow:hidden; }
.hero:after { content:""; position:absolute; width:330px;height:330px;right:5%;top:-120px;border-radius:50%;background:radial-gradient(circle,#0c7cff55,transparent 68%);pointer-events:none; }
.eyebrow { color:#65b4ff; letter-spacing:3px; font-size:.72rem; font-weight:800; text-transform:uppercase; }
.hero h1 { font-size:clamp(2.2rem,4vw,3.7rem); line-height:1.08; letter-spacing:-1.8px; margin:.65rem 0; color:#f7faff; font-weight:800; }
.hero h1 span { background:linear-gradient(90deg,#7b72ff,#24a5ff); -webkit-background-clip:text; color:transparent; }
.hero p { color:#b7c7d9; font-size:1rem; max-width:560px; line-height:1.7; }
.section-title { font-size:1.4rem; font-weight:800; margin:1.3rem 0 .3rem; }
.subtle { color:var(--muted); font-size:.9rem; }
.metric { background:linear-gradient(135deg,#0d1b2b,#0b1420); border:1px solid var(--line); border-radius:15px; padding:15px 17px; min-height:80px; }
.metric b { display:block; font-size:1rem; color:#f3f8ff; }
.metric small { color:#9fb0c4; }
.product-card { background:linear-gradient(180deg,#101c2b,#0b1420); border:1px solid #1b2b3d; border-radius:16px; padding:13px; height:100%; }
.product-emoji { background:radial-gradient(circle at 50% 40%,#203c60,#101a29 68%); border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:4.4rem; height:140px; margin-bottom:12px; }
.product-name { font-weight:750; color:#f4f7fb; min-height:2.5rem; }
.product-desc { color:#9fb0c4; font-size:.78rem; min-height:2rem; }
.price { font-size:1.1rem; font-weight:800; color:#fff; }
.old-price { color:#77889b; text-decoration:line-through; font-size:.8rem; margin-left:6px; }
.pill { color:#ff8797; background:#4a1625; padding:3px 7px; border-radius:20px; font-size:.7rem; font-weight:800; }
.trust { border-radius:14px; padding:17px; border:1px solid #1d3349; background:linear-gradient(110deg,#0d3158,#0c1c2c); }
.trust h4 { margin:0 0 5px; font-size:.95rem; }
.trust p { margin:0; color:#b2c5d8; font-size:.8rem; }
div.stButton > button { border-radius:10px; border:1px solid #1e8cff; background:linear-gradient(90deg,#0879f9,#169cff); color:white; font-weight:700; min-height:2.55rem; }
div.stButton > button:hover { border-color:#75bdff; color:white; filter:brightness(1.08); }
div[data-baseweb="input"] > div, div[data-baseweb="select"] > div { background:#0b1522; border-color:#24374b; border-radius:10px; }
.stTextInput label, .stSelectbox label, .stNumberInput label { color:#b6c5d7!important; }
hr { border-color:#1b2b3d; }
footer { visibility:hidden; }
@media (max-width: 700px) { .hero { padding:25px 22px; } .product-emoji {height:105px;font-size:3.3rem;} }
</style>
""", unsafe_allow_html=True)

PRODUCTS = [
    {"id":"laptop-rog","name":"ASUS ROG Strix G16","category":"PC & Laptops","desc":"i7 · RTX graphics · 16GB RAM · 1TB SSD","price":139999,"old":159999,"emoji":"💻","rating":"★★★★★","tag":"BESTSELLER"},
    {"id":"monitor-tuf","name":"ASUS TUF Gaming VG27AQ","category":"Monitors","desc":"27” · 1440p · 165Hz · IPS","price":32999,"old":38999,"emoji":"🖥️","rating":"★★★★★","tag":"POPULAR"},
    {"id":"gpu-4060","name":"MSI RTX 4060 Ventus 2X","category":"Components","desc":"8GB GDDR6 · Dual-fan GPU","price":49999,"old":57999,"emoji":"🎮","rating":"★★★★★","tag":"GAMING"},
    {"id":"cpu-5600","name":"AMD Ryzen 5 5600","category":"Components","desc":"6 cores · 12 threads · AM4","price":16499,"old":18999,"emoji":"🧠","rating":"★★★★★","tag":"VALUE PICK"},
    {"id":"keyboard-k617","name":"Redragon K617 Fizz","category":"Peripherals","desc":"60% layout · Red switches · RGB","price":5499,"old":7499,"emoji":"⌨️","rating":"★★★★☆","tag":"TRENDING"},
    {"id":"mouse-g502","name":"Logitech G502 X Plus","category":"Peripherals","desc":"Wireless · RGB · Precision gaming","price":14999,"old":18999,"emoji":"🖱️","rating":"★★★★★","tag":"TOP RATED"},
    {"id":"headset-cloud","name":"HyperX Cloud III","category":"Audio","desc":"Comfort fit · DTS spatial audio","price":10999,"old":12999,"emoji":"🎧","rating":"★★★★★","tag":"FAN FAVORITE"},
    {"id":"ssd-nvme","name":"1TB NVMe Gen4 SSD","category":"Components","desc":"Fast storage · Heatsink ready","price":8999,"old":10999,"emoji":"💾","rating":"★★★★☆","tag":"FAST"},
    {"id":"controller","name":"Wireless Gaming Controller","category":"Gaming Gear","desc":"Dual vibration · PC compatible","price":3999,"old":4999,"emoji":"🎮","rating":"★★★★☆","tag":"NEW"},
    {"id":"mic","name":"USB Streaming Microphone","category":"Audio","desc":"Cardioid pickup · Plug and play","price":6999,"old":8499,"emoji":"🎙️","rating":"★★★★☆","tag":"CREATOR"},
    {"id":"webcam","name":"Full HD Streaming Webcam","category":"Accessories","desc":"1080p · Auto light correction","price":4499,"old":5999,"emoji":"📷","rating":"★★★★☆","tag":"WORK & PLAY"},
    {"id":"deskmat","name":"Extended RGB Desk Mat","category":"Accessories","desc":"Large surface · Stitched edges","price":1999,"old":2699,"emoji":"🌈","rating":"★★★★☆","tag":"SETUP PICK"},
]
CATEGORIES = ["All Products"] + sorted({p["category"] for p in PRODUCTS})

if "cart" not in st.session_state:
    st.session_state.cart = {}
if "page" not in st.session_state:
    st.session_state.page = "Home"

def money(n):
    return "৳" + f"{n:,.0f}"

def add_to_cart(pid):
    st.session_state.cart[pid] = st.session_state.cart.get(pid, 0) + 1

def cart_count():
    return sum(st.session_state.cart.values())

def cart_total():
    return sum(next(p["price"] for p in PRODUCTS if p["id"] == pid) * qty for pid, qty in st.session_state.cart.items())

# Header
h1, h2, h3, h4 = st.columns([2.2, 3.5, 1.1, 1])
with h1:
    st.markdown("<div style='font-size:1.65rem;font-weight:850;letter-spacing:-.8px;padding-top:3px'>🔷 TechNest</div><div style='color:#8da3ba;font-size:.72rem;letter-spacing:1.5px'>PREMIUM TECH STORE</div>", unsafe_allow_html=True)
with h2:
    query = st.text_input("Search products", placeholder="Search laptops, components, accessories…", label_visibility="collapsed")
with h3:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"
with h4:
    if st.button(f"🛒 Cart ({cart_count()})", use_container_width=True):
        st.session_state.page = "Cart"
st.markdown("<hr>", unsafe_allow_html=True)

if st.session_state.page == "Cart":
    st.markdown("<div class='section-title'>Your shopping cart</div><div class='subtle'>Review your items before checkout.</div>", unsafe_allow_html=True)
    if not st.session_state.cart:
        st.info("Your cart is empty. Head back to the store to find something you love.")
        if st.button("← Continue shopping"):
            st.session_state.page = "Home"
            st.rerun()
    else:
        for pid, qty in list(st.session_state.cart.items()):
            p = next(p for p in PRODUCTS if p["id"] == pid)
            c1, c2, c3, c4 = st.columns([3, 1, 1, 1])
            c1.markdown(f"**{p['emoji']} {p['name']}**  \n<span class='subtle'>{p['category']}</span>", unsafe_allow_html=True)
            c2.write(f"Qty: {qty}")
            c3.write(money(p["price"] * qty))
            if c4.button("Remove", key=f"remove-{pid}"):
                del st.session_state.cart[pid]
                st.rerun()
            st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown(f"### Total: {money(cart_total())}")
        st.caption("Demo storefront: no real payment is collected and no order is sent.")
        with st.form("checkout_form"):
            st.subheader("Checkout details")
            name = st.text_input("Full name")
            email = st.text_input("Email address")
            phone = st.text_input("Phone number")
            address = st.text_area("Delivery address")
            submitted = st.form_submit_button("Place demo order", use_container_width=True)
            if submitted:
                if not all([name.strip(), email.strip(), phone.strip(), address.strip()]):
                    st.error("Please fill in all checkout fields.")
                else:
                    st.success(f"Demo order prepared for {name}. This sample does not save or send personal details.")
                    st.session_state.cart = {}
        if st.button("← Continue shopping"):
            st.session_state.page = "Home"
            st.rerun()
else:
    st.markdown("""
    <div class="hero">
      <div class="eyebrow">THE NEXT LEVEL STARTS HERE</div>
      <h1>Upgrade Your Setup.<br><span>Level Up Your Life.</span></h1>
      <p>Discover gaming gear, PC components and everyday tech essentials — carefully picked for your next great setup.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    m1, m2, m3, m4 = st.columns(4)
    for col, icon, title, sub in [
        (m1,"🚚","Fast delivery","Selected areas in Bangladesh"),
        (m2,"🔒","Secure checkout","Payment integration ready to add"),
        (m3,"🛡️","Warranty support","Clear product information"),
        (m4,"💬","Friendly support","Here when you need us"),
    ]:
        with col:
            st.markdown(f"<div class='metric'><b>{icon} &nbsp;{title}</b><small>{sub}</small></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Shop by category</div><div class='subtle'>Find the right gear for your setup.</div>", unsafe_allow_html=True)
    chosen_cat = st.selectbox("Choose a category", CATEGORIES, label_visibility="collapsed")

    st.markdown("<div class='section-title'>Featured products</div><div class='subtle'>Handpicked tech for work, play and everything in between.</div>", unsafe_allow_html=True)
    filtered = PRODUCTS
    if chosen_cat != "All Products":
        filtered = [p for p in filtered if p["category"] == chosen_cat]
    if query.strip():
        q = query.lower().strip()
        filtered = [p for p in filtered if q in p["name"].lower() or q in p["category"].lower() or q in p["desc"].lower()]
    if not filtered:
        st.warning("No products matched that search. Try a different term or category.")
    else:
        cols_per_row = 4
        for start in range(0, len(filtered), cols_per_row):
            cols = st.columns(cols_per_row, gap="medium")
            for col, p in zip(cols, filtered[start:start+cols_per_row]):
                with col:
                    st.markdown(
                        f"<div class='product-card'><div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:8px'><span style='font-size:.65rem;font-weight:800;color:#62b6ff;letter-spacing:.6px'>{p['tag']}</span><span style='font-size:.75rem;color:#ffc84b'>{p['rating']}</span></div><div class='product-emoji'>{p['emoji']}</div><div class='product-name'>{p['name']}</div><div class='product-desc'>{p['desc']}</div><div style='margin:10px 0 12px'><span class='price'>{money(p['price'])}</span><span class='old-price'>{money(p['old'])}</span></div></div>",
                        unsafe_allow_html=True,
                    )
                    if st.button("＋ Add to cart", key=f"add-{p['id']}", use_container_width=True):
                        add_to_cart(p["id"])
                        st.toast(f"{p['name']} added to cart")
                        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    t1, t2, t3 = st.columns(3)
    with t1:
        st.markdown("<div class='trust'><h4>🚚 Fast & reliable delivery</h4><p>Delivery options can be configured for your area.</p></div>", unsafe_allow_html=True)
    with t2:
        st.markdown("<div class='trust' style='background:linear-gradient(110deg,#06483f,#0c1c2c)'><h4>🔐 Checkout-ready design</h4><p>Connect a payment provider before accepting real orders.</p></div>", unsafe_allow_html=True)
    with t3:
        st.markdown("<div class='trust' style='background:linear-gradient(110deg,#39206a,#0c1c2c)'><h4>🎧 Support that helps</h4><p>Add your real support contact details before launch.</p></div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
f1, f2 = st.columns([3,2])
with f1:
    st.markdown("**🔷 TechNest**  \n<span class='subtle'>Your setup. Your style. Your next level.</span>", unsafe_allow_html=True)
with f2:
    st.markdown("<div style='text-align:right;color:#8fa3b8;font-size:.8rem;padding-top:8px'>Demo storefront · Built with Python + Streamlit</div>", unsafe_allow_html=True)
