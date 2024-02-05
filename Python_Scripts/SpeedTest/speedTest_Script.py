import speedtest

def main():
    speed_test = speedtest.Speedtest()
    
    download_speed = speed_test.download()
    upload_speed = speed_test.upload()
    
    print(f"Download Speed: {download_speed / 1024 / 1024:.2f} Mbps")
    print(f"Upload Speed: {upload_speed / 1024 / 1024:.2f} Mbps")

if __name__ == "__main__":
    main()
