import sys
import subprocess
from twarc import Twarc

def main(in_path, out_path):
    """

    :param str in_path:
    :param str out_path:
    """

    t = Twarc("CONSUMER_KEY","CONSUMER_SECRET","ACCESS_TOKEN","ACCESS_TOKEN_SECRET")

    out = open(out_path,"w+")

    for line in open(in_path):
        print(line)
        for follower in t.follower_ids(line):
            out.write(follower+","+line)
            print(follower+","+line);

    out.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python all_followers.py <in_file> <out_file>]')
        sys.exit(0)
    main(sys.argv[1], sys.argv[2])
