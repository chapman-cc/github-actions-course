import os
import time
import requests


def ping_url(url: str, delay: float, max_trials: int):
    trials: int = 0
    while trials < max_trials:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"URL {url} is reachable.")  
                return True
        except requests.exceptions.ConnectionError:
            print(f"URL {url} is unreachable. Retrying in {delay} seconds...")
            time.sleep(delay)
            trials += 1
        except requests.exceptions.MissingSchema:
            print(f"URL {url} is malformed. Please check the URL format.")
            return False
    return False


def run():
    url = os.getenv("INPUT_URL")
    max_trials = int(os.getenv("INPUT_MAX_TRIALS"))
    delay = int(os.getenv("INPUT_DELAY"))
    
    website_reachable = ping_url(url=url, delay=delay, max_trials=max_trials)

    if not website_reachable:
        raise Exception(f"URL {url} is unreachable after {max_trials} trials.")
    
    print(f"Successfully reached URL {url}.")


if __name__ == "__main__":
    run()
