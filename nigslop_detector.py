import streamlit as st
import re

st.set_page_config(page_title="Nigslop Scanner", page_icon="🚨", layout="centered")

st.title("🚨 Nigslop Rug Scanner")
st.markdown("**Paste the full @soul_scanner_bot result below**")

data = st.text_area("Scanner Data", height=500, placeholder="Paste everything from Soul Scanner here...")

if st.button("Generate Nigslop Report 🚨", type="primary", use_container_width=True):
    if not data.strip():
        st.error("Please paste the scanner data")
    else:
        # Basic auto-detection
        ticker_match = re.search(r'\$([A-Z0-9]+)', data)
        ca_match = re.search(r'([A-Za-z0-9]{40,44})', data)
        
        ticker = ticker_match.group(1) if ticker_match else "UNKNOWN"
        ca = ca_match.group(1) if ca_match else "Unknown CA"

        report = f"""**${ticker}** • `{ca}`

- **Rug Risk**: [Analyze manually or add AI logic]
- **Bundles**: [XX% bundled...]
- **Dev Wallet**: [XX SOL...]
- **Snipers / Other Flags**: ...
- **Group Verdict**: ...

**Nigslop Report 🚨**: quick check → ... DYOR"""

        st.success("✅ Report Generated!")
        st.code(report, language="markdown")
        
        st.download_button("Download Report", report, file_name=f"{ticker}_Nigslop_Report.txt")

st.caption("Public Nigslop Scanner • Powered by Grok + Community")
