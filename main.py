'EOF'
#!/usr/bin/env python3

import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Barrier Gateway Started")
    logging.info("Waiting for VMS integration...")

    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()
EOF