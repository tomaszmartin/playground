import subprocess
import threading
import signal
import time
import sys


RELOAD = 3


def main(arg):
    # Just pretending to have something to do.
    # In werkzeug it handles incoming requests
    while True:
        time.sleep(1)
        print(f'Incoming request.')


def run_main(arg):
    # In werkzeug ReloaderLoop.restart_with_reloader
    while True:
        print(f'Spawning new process with reloader.')
        exit_code = subprocess.call(['python3', 'reloader.py', 'with-reloader'], close_fds=False)
        # If process returns exit RELOAD
        # Than spawn another subprocess
        # Else exit the app
        if exit_code != RELOAD:
            return exit_code


def run_reloader():
    # In werkzeug ReloaderLoop.run
    time.sleep(3)
    print('Found changes in file. Killing current subprocess.')
    sys.exit(RELOAD)


if __name__ == '__main__':
    arg = sys.argv[1:]
    # Run the main loop only from subprocesses
    # not from the main process.
    # Won't be run at first launch.
    if arg and arg[0] == 'with-reloader':
        t = threading.Thread(target=main, args=[arg])
        t.setDaemon(True)
        t.start()
        # Simulating waiting for changes in files
        run_reloader()
    # At first launch start the loop that spawns
    # subprocesses with current file.
    else:
        sys.exit(run_main(arg))