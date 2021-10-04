import speedtest
import time

test = speedtest.Speedtest()

print("Loading server list..")
time.sleep(1.5)
test.get_servers()
time.sleep(1.5)
print("Searching for best server.. \nThis could take a second or two...")
best = test.get_best_server()
print('\n ================================================================')
print(
    f"\n Found best server: {best['host']} \n Located in:{best['country']} \n Latency: {best['latency']} ")
print('\n ================================================================')
time.sleep(1.5)
print()

print ("Performing download test...")
download_result = test. download()
print ("Performing upload test. ..")
upload_result = test . upload()
ping_result = test . results. ping

print("\n")
print (f"Download speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print ("\n")
print (f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
print ("\n")
print (f"ping: {ping_result:.2f} ms")
