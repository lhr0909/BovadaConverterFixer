import os, time, re
from difflib import Differ

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
        os.rename(full_path, processed_folder + "/" + filename)
        print len(hands)

def process_hands(hands, output_folder, filename):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

def main():
    input_folder = "C:/Users/Simon/Documents/BovadaHandHistory"
    output_folder = "C:/Users/Simon/Documents/BovadaHandHistoryFixed"
    processed_folder = "C:/Users/Simon/Documents/BovadaHandHistoryProcessed"
    walk_hands(input_folder, output_folder, processed_folder)

if __name__ == "__main__":
    main()