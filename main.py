from litellm import completion


def main():
    model = "ollama/deepseek-r1:1.5b"

    content = "Hello, how are you?"

    messages = [
        {
            "role": "user",
            "content": content,
        },
    ]

    response = completion(
        model=model,
        messages=messages,
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
