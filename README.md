This repository contains dictionaries for AOSP keyboard and compatible apps, as well as word lists used to create the dictionaries.
Use [`dicttool_aosp.jar`](https://github.com/remi0s/aosp-dictionary-tools) and run `java -jar dicttool_aosp.jar makedict -s <language>_wordlist.combined -d main_<language>.dict`

Source of the word lists:
* `wordlists/ar_wordlist.combined`: https://github.com/remi0s/aosp-dictionary-tools/blob/master/dictsCreated/WikiAndOpenSubtitles/ar_wordlist.combined
* `wordlists/he_wordlist.combined`: https://github.com/Hananel-Hazan/aosp-dictionary-tools/blob/master/hebrew-hspell.txt.combined.new
* `wordlists/es_GL_wordlist.combined`: https://github.com/chavaone/openboard/blob/master/dictionaries/es_GL_wordlist.combined.gz
* all others in `wordlists`: https://github.com/openboard-team/openboard/tree/master/dictionaries, most of these are default AOSP keyboard wordlists
* `wordlists_experimental/en_emoji.combined`: adapted from [gemoji](https://github.com/github/gemoji/blob/master/db/emoji.json)
* all others in `wordlists_experimental`: created using [`create_wordlist_from_sentences.py`](create_wordlist_from_sentences.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/ (under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license)

[`create_wordlist_from_sentences.py`](create_wordlist_from_sentences.py) is still experimental, rather slow and may produce bad dictionaries in some languages. See the `example` functions on how the script can be used.

In the experimental dictionaries, names are typically missing as they don't pass the _hunspell_ spellcheck.
A "potentially_offensive" attribute is added for some words, which sometimes seems unnecessary. Currently this is coming from the "nosuggest" attribute of the used _hunspell_ dictionaries, which occurs for offensive words as well as for weird / rare word forms.
Other flags are currently missing, same for shortcuts (e.g. ill -> I'll or écoeuré -> écœuré, as found in AOSP dictionaries).

-----

`wordlist.combined` file infos (mostly guessed, didn't find documentation):
* header is necessary
  * format like `dictionary=main:en_us,locale=en_US,description=English (US),date=1414726260,version=54`
  * all of these fields are necessary, though `description` is not used
  * German dictionaries also have `REQUIRES_GERMAN_UMLAUT_PROCESSING=1`
* each word is in a line like ` word=re,f=0,flags=abbreviation,originalFreq=99,possibly_offensive=true`
  * `word` is the word (necessary)
  * `f` is frequency, from 0 to 255(?) (necessary)
    * higher value is more likely to get suggested / corrected
    * special value `whitelist`, possibly equal to 15
    * `f=0` will not be suggested if bad words are blocked, and will never be added to user history
      * possible bug: words with `possibly_offensive=true` and `f=0` will be suggested when not blocking offensive words, but other words with `f=0` are still not suggested
  * `originalFreq`: unclear, is this used?
  * `flags`: `medical`, `technical`, `hand-added`, `babytalk`, `abbreviation`, `offensive`, `technical`, `nonword`, and probably more: are they used for anything?
  * `possibly_offensive=true` stops the word from being suggested when blocking offensive words
  * `not_a_word=true` will not be suggested, use together with `shortcut`
  * `shortcut=<s>` (below a `<word>`) will suggest `<s>` when the `<word>` is typed
    * which `f` to use? maybe only 0-14 and `whitelist` allowed
    * what does `f` do here?
  * `bigram=<b>` (below a `<word>`) will suggest `<b>` as next word before typing any letters
    * what does `f` do here? Looks like 1, 2, and 3 are used for the usual 3 bigram entries
