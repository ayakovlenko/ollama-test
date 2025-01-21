import aisuite as ai  # type: ignore


def main():
    client = ai.Client()

    model = "ollama:deepseek-r1:1.5b"

    content = "Hello, how are you?"

    messages = [
        {
            "role": "user",
            "content": content,
        },
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
