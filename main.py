from datetime import datetime, timezone


def main():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    line = f"Uruchomienie: {now} UTC\n"
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()