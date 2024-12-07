from obswebsocket import obsws, requests, events
import videoupload
import re

HOST = 'localhost'
PORT = 4444
PASSWORD = "does_not_matter"


def on_event(event):
    # Get the event data as String
    event_data = str(event)

    # Check if the event was a RecordingStopped one
    if event_data.startswith("<RecordingStopped"):
        print("Recording has stopped!")

        # Extract the file name from the event data
        match = re.search(r"'recordingFilename': '([^']*)'", event_data)
        file = match.group(1) if match else None

        # Upload to Vimeo, Generate a QR code and print on the label printer
        id = videoupload.generate_id()
        url = videoupload.uploadfile(file, id)
        png = videoupload.create_qr_code(id, url)
        videoupload.print_qr_code(png)

def main():
    # Connect to OBS WebSocket
    global ws
    ws = obsws(HOST, PORT, PASSWORD)

    try:
        ws.connect()
        print("Connected to OBS WebSocket!")

        # Register an event callback
        ws.register(on_event)

        # Keep the connection alive to listen for events
        print("Listening for events... Press Ctrl+C to stop.")
        while True:
            pass

    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        ws.disconnect()

if __name__ == "__main__":
    main()
