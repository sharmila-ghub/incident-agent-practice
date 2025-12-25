def classify_incident(text):
    if "down" in text.lower():
        return "P1 - Critical"
    elif "slow" in text.lower():
        return "P2 - High"
    else:
        return "P3 - Normal"

incident = "Application is down for all users"
print(classify_incident(incident))
