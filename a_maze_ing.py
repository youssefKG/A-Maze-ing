from renderer.renderer import Renderer


class Amazeing:
    def __init__(self) -> None:
        self.renderer = Renderer()


def main():
    amazeing = Amazeing()
    amazeing.renderer.render()


if __name__ == "__main__":
    main()
