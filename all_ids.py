import sys
import json

def main(in_path, user_path, out_path):
    """

    :param str in_path:
    :param str out_path:
    """

    out = open(out_path,"w+")

    users = {}
    for line in open(user_path):
        userdata = json.loads(line)
        # if (hasattr(userdata,"id_str")):
        users[userdata["screen_name"]] = userdata["id_str"]
        # else:
        #     print(userdata)
    # print(users)


    for line in open(in_path):
        linedata  = line.split(",")
        # print(linedata)
        linedata[1] = users[linedata[1].strip()]
        outline = linedata[0]+","+linedata[1]+"\n"
        out.write(outline)
        # print(outline);

    out.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python all_followers.py <in_file> <out_file>]')
        sys.exit(0)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
