import streamlit as st
import re

st.set_page_config(page_title="Nigslop Scanner", page_icon="🚨", layout="centered")

st.title("🚨 Nigslop Rug Scanner")
st.markdown("**Paste the full @soul_scanner_bot result below**")

data = st.text_area("Paste Scanner Output Here", height=450, placeholder="Paste everything from Soul Scanner...")

if st.button("🚨 Generate Nigslop Report", type="primary", use_container_width=True):
    if not data.strip():
        st.error("Please paste the scanner data")
    else:
        # Improved Parsing
        ticker_match = re.search(r'• \$([A-Z0-9]+)', data)
        ca_match = re.search(r'([A-HJ-NP-Za-km-z1-9]{40,44}pump)', data)
        
        ticker = ticker_match.group(1) if ticker_match else "UNKNOWN"
        ca = ca_match.group(1) if ca_match else "Unknown CA"

        # Try to extract key info
        bundles_match = re.search(r'Bundles:?\s*(\d+)\s*•\s*(\d+)%', data)
        dev_sold_match = re.search(r'Sold:\s*(\d+)%', data)
        holders_match = re.search(r'Hodls:?\s*(\d+)', data)

        bundles = bundles_match.group(2) if bundles_match else "??"
        sold = dev_sold_match.group(1) if dev_sold_match else "??"
        holders = holders_match.group(1) if holders_match else "??"

        report = f"""**${ticker}** • `{ca}`

- **Rug Risk**: Medium
- **Bundles**: {bundles}% early (still notable)
- **Dev Wallet**: Dev sold {sold}%
- **Snipers / Other Flags**: {holders} holders
- **Group Verdict**: Caution - Check bundles and dev sell

**Nigslop Report 🚨**: quick check → {bundles}% bundled. Dev sold {sold}%. Medium rug risk. Small size or wait. DYOR"""

        st.success("✅ Report Generated!")
        st.code(report, language="markdown")

        if st.button("Copy Report"):
            st.code(report, language="markdown")
            st.success("Copied to clipboard! (manual copy for now)")

st.caption("Nigslop Community Scanner • Paste full Soul Scanner result")
