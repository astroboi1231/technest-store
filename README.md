# TechNest — Python Online Store Demo

A polished, dark-themed online store prototype built with **Python + Streamlit**.

## Features
- Responsive product catalog
- Product search and category filter
- Add-to-cart controls and cart count
- Cart total and item removal
- Demo checkout form with required-field validation
- Bangladesh taka (৳) price formatting
- No separate HTML/CSS files required (the app uses a small embedded CSS theme)

## Run on Windows

1. Install Python 3.11 or newer from https://www.python.org/downloads/
   - During installation, tick **Add Python to PATH**.
2. Extract this folder.
3. Open Command Prompt inside the project folder.
4. Run:

```bash
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
streamlit run app.py
```

Your browser should open the local app. If not, open the Local URL shown in the terminal, usually `http://localhost:8501`.

## Publish it online for free

1. Create a GitHub account at https://github.com/
2. Create a new repository and upload `app.py` and `requirements.txt`.
3. Open https://share.streamlit.io/
4. Sign in with GitHub and choose **Create app**.
5. Select the repository, branch, and `app.py`, then deploy.
6. Streamlit Community Cloud will provide a public URL.

## Important before a real commercial launch

This is a **working prototype**, not a production-ready payment system. The sample checkout does not charge customers, save orders, or send them to a seller. Before accepting real orders, add:
- A database and persistent inventory/order management
- A trusted payment gateway suitable for Bangladesh
- Server-side validation and secure handling of customer data
- Shipping, returns, warranty, privacy and terms pages
- Real product photos, verified prices, stock status and business contact details
- Secrets/environment variables for credentials; never commit secrets to GitHub

The sample product names and prices are placeholders for demonstration and must be verified/replaced before publishing as a real shop.
