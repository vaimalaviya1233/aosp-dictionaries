#!/bin/python
import sys
import os
import time
import gzip
import langcodes
import pathlib
from wordlist_combined import DictionaryHeader, WordlistCombined

# this script generates source entries for the readme from .source files
# source file format:
#  license: <license (optional)>
#  language: <language in English (optional, e.g. for toki pona)>
#  source: <link / text>


def get_source_file_names(folder: str) -> list[str]:
    files = []
    folder = os.path.join(os.path.dirname(__file__), "..", folder)
    if not os.path.isdir(folder):
        sys.exit(f"{folder} is not a directory")
    for (dirpath, dirnames, filenames) in os.walk(folder):
        for name in filenames:
            name = os.path.join(folder, name)
            if not name.endswith(".combined.gz"):
                continue
            source_file = name.replace("combined.gz", "source")
            if not os.path.isfile(source_file):
                sys.exit(f"{source_file} not found")
            files.append(source_file)
    return files


def create_dict_if_not_exists(dict_path: str, word_list_path: str) -> None:
    if os.path.isfile(dict_path):
        return
    word_list = WordlistCombined.read_from_file(word_list_path)
    word_list.compile(dict_path)


def get_infos(folder: str) -> list[dict]:
    files = get_source_file_names(folder)
    infos = []
    for file in files:
        source_info = {}
        filepath = pathlib.Path(file)
        word_list_path = file.replace(".source", ".combined.gz")
        if not os.path.isfile(word_list_path):
            raise FileNotFoundError("word list does not exist: " + word_list_path)
        dict_path_relative = filepath.parent.name.replace("wordlists", "dictionaries") + "/" + filepath.stem.lower() + ".dict"
        create_dict_if_not_exists(filepath.parent.parent.name + "/" + dict_path_relative, word_list_path)
        source_info["dictfile"] = dict_path_relative
        with gzip.open(word_list_path, 'rt') as f:
            header = DictionaryHeader.parse(f.readline())
            if header is None:
                sys.exit(f"could not parse header for {file}")
            source_info["header"] = header
            wordcount = 0
            for line in f:
                if line.startswith(" word="):
                    wordcount += 1
            source_info["wordcount"] = wordcount
            for line in f:
                if line.trim().startswith("bigram="):
                    source_info["bigrams"] = True
                    break
        with open(file) as f:
            for line in f:
                if ":" not in line:
                    continue
                (name, value) = line.split(":", 1)
                value = value.strip()
                if len(value) == 0:
                    continue
                source_info[name] = value
            if "source" not in source_info:
                sys.exit(f"no source given in {file}")
        infos.append(source_info)
    return infos


def info_to_text(info: dict) -> str:
    header: DictionaryHeader = info["header"]
    language = info.get("language", None)
    if language is None:
        language = langcodes.Language.get(header.locale).display_name('en')
    dictfile = info["dictfile"]
    description = ""
    if len(header.description.strip()) > 0:
        description = f"{header.description}, "
    timestring = time.strftime('%Y-%m-%d', time.localtime(header.date))
    wordcount = info["wordcount"]
    bigrams = ""
    if info.get("bigrams", False):
        bigrams = "has next-word suggestions, "
    source = info["source"]
    dict_license = ""
    if "license" in info:
        dict_license = ", license: " + info["license"]
    return f"* [{language} {header.type}]({dictfile}): {description}v{header.version}, {timestring}, " \
        f"{wordcount} entries, {bigrams}source: {source}{dict_license}"


def main():
    readmefile = os.path.join(os.path.dirname(__file__), "..", "README.md")
    outlines = []
    with open(readmefile) as f:
        skiplists = False
        for line in f:
            if skiplists:
                if line.startswith("* "):
                    continue
                else:
                    skiplists = False
            if line == "# Dictionaries\n":
                outlines.append(line)
                skiplists = True
                infos = get_infos("wordlists")
                infolines = []
                for info in infos:
                    infolines.append(info_to_text(info) + "\n")
                infolines.sort()
                outlines += infolines
            elif line == "# Experimental dictionaries\n":
                outlines.append(line)
                skiplists = True
                infos = get_infos("wordlists_experimental")
                infolines = []
                for info in infos:
                    infolines.append(info_to_text(info) + "\n")
                infolines.sort()
                outlines += infolines
            else:
                outlines.append(line)
    return
    with open(readmefile, 'w') as f:
        f.writelines(outlines)


if __name__ == "__main__":
    main()
