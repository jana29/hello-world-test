def main():
    with open("data/message.txt", "r") as f:
        text = f.read().strip()

    print(text)


if __name__ == "__main__":
    main()
