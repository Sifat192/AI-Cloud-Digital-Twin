# ws integrted in the lst prt of the ppliction 
import streamlit as st 
st.subheader("Optimization Recommendations")

recommendations = []

if cpu > 85:
    recommendations.append(
        "Scale CPU Resources"
    )

if mem > 85:
    recommendations.append(
        "Increase Memory Allocation"
    )

if x.iloc[-1]["Disk_IO"] > 80:
    recommendations.append(
        "Increase Disk Throughput"
    )

if x.iloc[-1]["Network_IO"] > 80:
    recommendations.append(
        "Increase Network Capacity"
    )

if anomaly == 1:
    recommendations.append(
        "Investigate Abnormal System Behaviour"
    )

if cpu_pred > 90:
    recommendations.append(
        "Proactively Scale CPU Resources"
    )

if memory_pred > 90:
    recommendations.append(
        "Proactively Increase Memory Resources"
    )

if len(recommendations) == 0:
    st.success(
        "No optimization required."
    )

for r in recommendations:
    st.write("•", r)
