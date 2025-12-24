# Incident Classification Agent
# This program classifies an ITSM incident based on keywords
# and suggests category, priority, and resolver group.

# Ask the user to describe the incident
incident = input("Describe the incident: ").strip().lower()

# Check if the user entered nothing
if incident == "":
    print("No incident description provided. Please rerun and enter details.")

else:
    # Decision logic starts here

    # Case 1: Infrastructure related issues
    if "server" in incident or "down" in incident:
        category = "Infrastructure"
        priority = "P1"
        resolver = "Infra Support Team"
        reason = "Critical system availability issue"

    # Case 2: Access / login issues
    elif "password" in incident or "login" in incident:
        category = "Access Management"
        priority = "P3"
        resolver = "Service Desk"
        reason = "User access related issue"

    # Case 3: Default case for application issues
    else:
        category = "Application"
        priority = "P2"
        resolver = "Application Support"
        reason = "Functional or performance issue in application"

    # Display the final classification
    print("\n--- Incident Classification ---")
    print("Category       :", category)
    print("Priority       :", priority)
    print("Resolver Group :", resolver)
    print("Reason         :", reason)
