from pymavlink import mavutil

master = mavutil.mavlink_connection('/dev/ttyAMA0',baud=57600)

print("waiting for heartbeat...")

master.wait_heartbeat()
print(f"{master.target_system}")
