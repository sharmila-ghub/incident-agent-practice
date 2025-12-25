import psutil

cpu = psutil.cpu_percent(interval=1)

if cpu > 80:
    print("⚠️ High CPU usage:", cpu)
else:
    print("✅ CPU OK:", cpu)
