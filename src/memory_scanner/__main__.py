"""Allow running as: python -m memory_scanner"""

from memory_scanner.server import mcp

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
