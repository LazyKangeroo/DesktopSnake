## File is merely for my own debugging and error handling during production
## This mean the link between the files could be disconnected if so decided
## This isn't incurraged to disallow any accidental errors but feel free

class ErrMsg:
    def __init__(self) -> None:
        pass

    def dataErr(self, text, line):
        print(f"[!] Data error: {text}---\n > Line ({str(line)})")