import json
import sys
from parse import parse_video

def test_command_line():
    if len(sys.argv) != 5 or sys.argv[1] != "--input" or sys.argv[3] != "--output" or sys.argv[2].split(".")[-1] != "json" or sys.argv[4].split(".")[-1] != "json":
        print("Wrong command line. Try : python3 scrapper.py --input <input_json_file> --output <output_json_file>")
        sys.exit(1)
    else:
        input_file = sys.argv[2]
        output_file = sys.argv[4]
    try:
        with open(input_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)


def main():
    output = {}
    test_command_line()
    input_file = sys.argv[2]
    output_file = sys.argv[4]

    with open(input_file, "r") as f:
        data = json.load(f)
        print(data['videos_id'])
        videos_ids = data['videos_id']
    
    for id in videos_ids:
        html = parse_video(id)
        output[id] = html

    with open(output_file, "w", encoding="utf8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)

main()
