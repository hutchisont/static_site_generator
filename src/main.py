import shutil


def main():
    _static_to_public()


def _static_to_public():
    shutil.rmtree("public")
    shutil.copytree("static", "public")


if __name__ == "__main__":
    main()
