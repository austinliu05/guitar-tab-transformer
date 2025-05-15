import guitarpro as gp
import os

data_folder = "/home/claudehu/Desktop/data/music/gps/rdcf"

def string_tuning_combinations(data_folder):
    gps_files = os.listdir(data_folder)

    val_tune_dict = {}

    string_tunings = []
    string_values = []
    for i in range(6):
        string_tunings.append([])
        string_values.append([])

    for gp_file in gps_files:
        song = gp.parse(os.path.join(data_folder, gp_file))
        for track in song.tracks:
            strings = track.strings
            for i in range(6):
                string_tunings[i].append(str(strings[i]))
                string_values[i].append(strings[i].value)
                val_tune_dict[strings[i].value] = str(strings[i])

    unique_tunings = [set(string) for string in string_tunings]
    uniqe_values = [set(string) for string in string_values]

    return {
        "tunings": unique_tunings,
        "values": uniqe_values,
        "map": val_tune_dict
    }

tuning_combos = string_tuning_combinations(data_folder)

note_vocabs = []

for i, string in enumerate(tuning_combos["tunings"]):
    string_idx = i + 1
    sprefix = f"note:s{str(string_idx)}"

    for fret in range(0, 25):
        sfprefix = f"{sprefix}:f{str(fret)}"
        for tune in string:
            note = f"{sfprefix}:{tune}"
            note_vocabs.append(note)

with open(os.path.join(data_folder, "note_vocab.txt"), "w") as f:
    for note in note_vocabs:
        f.write(note + "\n")


