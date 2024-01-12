from fastapi import FastAPI


def main() -> FastAPI:
    app = FastAPI(
        title="Misc API",
        description="Miscellaneous api"
    )

    return app