import sys
from utils import source_to_target, generate_pages_recursive

def main(*args, **kwargs):
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]


    print(f"Base path: {basepath}")

    source_to_target("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

if __name__ == "__main__":
    main()