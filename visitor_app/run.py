from backend.app import create_app
from frontend.main import VisitorApp
import threading

def run_flask():
    app = create_app()
    app.run(use_reloader=False)

if __name__ == '__main__':
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Run the Kivy app
    VisitorApp().run()