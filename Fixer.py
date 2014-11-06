import os, re

def walk_hands(input_folder, output_folder, processed_folder):
    '''
    This method walks all the hands in the directory and converts them
    '''

    if not os.path.exists(processed_folder):
        os.makedirs(processed_folder)

    files = []
    for (dirpath, dirnames, filenames) in os.walk(input_folder):
        # TODO: wanna recursively get into directories?
        files.extend(filenames)
        break

    for filename in files:
        full_path = input_folder + "/" + filename
        f = open(full_path, "r")
        hands = []
        isHand = False
        hand_lines = []
        for line in map(lambda x: x.strip(), f.readlines()):
            if len(line) > 0:
                if not isHand:
                    isHand = True
                hand_lines.append(line)
            else:
                #is a separation of next hand
                if isHand:
                    isHand = False
                    hands.append(hand_lines[:])
                    hand_lines = []
        f.close()
        process_hands(hands, output_folder, filename)
        os.rename(full_path, processed_folder + "/" + filename)
        print len(hands)

def replace_mucked_to_folded(m):
    return "Seat %s: %s folded %s" % (m.group(1), m.group(2), m.group(4))

def process_hands(hands, output_folder, filename):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for i in xrange(len(hands)):
        for j in xrange(len(hands[i])):
            line = hands[i][j]
            hands[i][j] = line.replace("mucked", "folded")
    #output result to file
    full_path = output_folder + "/" + filename
    f = open(full_path, "w")
    f.write("\r\n\r\n\r\n".join(map(lambda hand: "\r\n".join(hand), hands)))
    f.close()


def main():
    input_folder = "C:/Users/Simon/Documents/BovadaHandHistory"
    output_folder = "C:/Users/Simon/Documents/BovadaHandHistoryFixed"
    processed_folder = "C:/Users/Simon/Documents/BovadaHandHistoryProcessed"
    walk_hands(input_folder, output_folder, processed_folder)

if __name__ == "__main__":
    main()