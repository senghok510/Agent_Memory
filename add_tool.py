from langchain_core.tools import tool


@tool
def multiply(a: int, b: int) -> int:
    return a*b
