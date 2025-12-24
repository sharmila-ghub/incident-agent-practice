incident = input("Describe the incident: ").lower()

if "server" in incident or "down" in incident:
    category = "Infrastructure"
    priority = "P1"
    resolver = "Infra Support Team"

elif "password" in incident or "login" in incident:
    category = "Access Management"
    priority = "P3"
    resolver = "Service Desk"

else:
    category = "Application"
    priority = "P2"
    resolver = "Application Support"

print("\n--- Incident Classification ---")
print("Category:", category)
print("Priority:", priority)
print("Resolver Group:", resolver)
