from speedtest import Speedtest #import speedtest module

st = Speedtest()
download = st.download()
upload = st.upload()
download_speed = round(download / (10**6), 2)
upload_speed = round(upload / (10**6), 2)
print("Download Speed:" + str(download_speed) + "Mbps")
print("Upload Speed:" + str(upload_speed) + "Mbps")
