import os
import sys
import json
from json.decoder import JSONDecodeError


if __name__ == '__main__':
    path = sys.argv[-1]
    if not os.path.exists(path):
        exit(0)
    with open(path) as in_file:
        try:
            data = json.load(in_file)
        except JSONDecodeError:
            data = []
        formatted_data = json.dumps(data, sort_keys=False, indent=2)
    with open(path, 'w') as out_file:
        out_file.write(formatted_data)
    sys.stdout.write('"%s" beautified\n' % path)


# end of file
