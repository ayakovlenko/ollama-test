from ollama import chat  # type: ignore
from ollama import ChatResponse  # type: ignore


MODEL = "deepseek-r1:1.5b"


def main():
    content = "Hello, how are you?"

    response: ChatResponse = chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": content,
            },
        ],
    )

    print(response.message.content)


if __name__ == "__main__":
    main()
