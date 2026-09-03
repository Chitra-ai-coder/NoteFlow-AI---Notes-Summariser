import uvicorn
import webbrowser
import threading
import time

def open_browser():
    # Wait 2 seconds to give the server time to boot up
    time.sleep(2)
    
    print("\n🌐 Opening your app in the browser...\n")
    # CHANGED: We now open the local web server URL instead of the file path!
    webbrowser.open("http://127.0.0.1:8000/")

if __name__ == "__main__":
    threading.Thread(target=open_browser, daemon=True).start()
    print("🚀 Starting the AI Backend Server...")
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)