import streamlit as st
import re

st.set_page_config(page_title="Nigslop Scanner", page_icon="🚨", layout="centered")
st.title("🚨 Nigslop Rug Scanner")
st.markdown("**Paste the full Soul Scanner result below**")

data = st.text_area("Scanner Output", height=500, placeholder="Paste everything here...")

if st.button("🚨 Generate Nigslop Report", type="primary", use_container_width=True):
    if not data.strip():
        st.error("Please paste the scanner data")
    else:
        # Improved Parsing
        ticker_match = re.search(r'• \$([A-Z0-9]+)', data)
        ca_match = re.search(r'([A-HJ-NP-Za-km-z1-9]{40,44}pump)', data)
        bundles_match = re.search(r'Bundles:?\s*(\d+)\s*•\s*(\d+)%\s*→\s*(\d+\.?\d*)%', data)
        dev_sold_match = re.search(r'Sold:\s*(\d+)%', data)
        holders_match = re.search(r'Hodls:?\s*(\d+)', data)
        age_match = re.search(r'Age:?\s*(\d+[mh])', data)

        ticker = ticker_match.group(1) if ticker_match else "UNKNOWN"
        ca = ca_match.group(1) if ca_match else "Unknown CA"
        bundles_early = bundles_match.group(2) if bundles_match else "??"
        bundles_now = bundles_match.group(3) if bundles_match else "??"
        dev_sold = dev_sold_match.group(1) if dev_sold_match else "??"
        holders = holders_match.group(1) if holders_match else "??"
        age = age_match.group(1) if age_match else "??"

        # Simple Risk Logic
        risk = "Medium"
        if int(bundles_now) <= 5:
            risk = "Low"
        elif int(bundles_now) > 25 or int(dev_sold) > 20:
            risk = "High"

        report = f"""**${ticker}** • `{ca}`

- **Rug Risk**: {risk}
- **Bundles**: {bundles_early}% early supply (now {bundles_now}%)
- **Dev Wallet**: Dev sold {dev_sold}%
- **Snipers / Other Flags**: {holders} holders, {age} old
- **Group Verdict**: Caution - Check remaining bundles and dev sell

**Nigslop Report 🚨**: quick check → {bundles_early}% bundled in ?? wallets (now {bundles_now}%). Dev sold {dev_sold}%. {risk} rug risk. Small size or wait. DYOR"""

        st.success("✅ Report Generated!")
        st.code(report, language="markdown")

        st.download_button("📥 Download Report", report, file_name=f"{ticker}_Nigslop_Report.txt", mime="text/plain")

st.caption("Nigslop Community • Improved Parser v2")
