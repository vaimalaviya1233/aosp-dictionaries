This repository contains dictionaries for AOSP keyboard and compatible apps, as well as word lists used to create the dictionaries.
Use [`dicttool_aosp.jar`](https://github.com/remi0s/aosp-dictionary-tools) and run `java -jar dicttool_aosp.jar makedict -s <language>_wordlist.combined -d main_<language>.dict`

Source of the word lists:
* `wordlists/ar_wordlist.combined.gz`: https://github.com/remi0s/aosp-dictionary-tools/blob/master/dictsCreated/WikiAndOpenSubtitles/ar_wordlist.combined
* `wordlists/he_wordlist.combined.gz`: https://github.com/Hananel-Hazan/aosp-dictionary-tools/blob/master/hebrew-hspell.txt.combined.new
* `wordlists/es_GL_wordlist.combined.gz`: https://github.com/chavaone/openboard/blob/master/dictionaries/es_GL_wordlist.combined.gz
* `wordlists/tok_wordlist.combined.gz`: https://codeberg.org/Helium314/aosp-dictionaries/issues/1 (CC by-sa 3.0 and 4.0 combined license)
* all others in `wordlists`: https://github.com/openboard-team/openboard/tree/master/dictionaries, most of these are default AOSP keyboard wordlists
* `wordlists_experimental/en_emoji.combined`: adapted from [gemoji](https://github.com/github/gemoji/blob/master/db/emoji.json)
* all others in `wordlists_experimental`: created using [`create_wordlist_from_sentences.py`](create_wordlist_from_sentences.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/ (under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license)

[`create_wordlist_from_sentences.py`](create_wordlist_from_sentences.py) is still experimental, rather slow and may produce bad dictionaries in some languages. See the `example` functions on how the script can be used.

In the experimental dictionaries, names are typically missing as they don't pass the _hunspell_ spellcheck.
A "potentially_offensive" attribute is added for some words, which sometimes seems unnecessary. Currently this is coming from the "nosuggest" attribute of the used _hunspell_ dictionaries, which occurs for offensive words as well as for weird / rare word forms.
Other flags are currently missing, same for shortcuts (e.g. ill -> I'll or écoeuré -> écœuré, as found in AOSP dictionaries).

An empty dictionary is available in dictionaries/empty.dict.

-----

`wordlist.combined` file infos (from wordlists/sample.combined and guessed):
* header is necessary
  * format like `dictionary=main:en_us,locale=en_US,description=English (US),date=1414726260,version=54`
  * all of these fields are necessary, though `description` may not be shown to the user
  * `version` should be greater than 18 for the dictionary to work with all AOSP keyboards (not necessary for https://github.com/Helium314/openboard though)
  * German dictionaries also have `REQUIRES_GERMAN_UMLAUT_PROCESSING=1`
* each word is in a line like ` word=re,f=0,flags=abbreviation,originalFreq=99,possibly_offensive=true`
  * `word` is the word (necessary)
  * `f` is the logarithm of word frequency, integer from 0 to 255 (necessary)
    * higher value is more likely to get suggested / corrected
    * special value `whitelist`, possibly equal to 15
    * `f=0` will not be suggested if bad words are blocked, but will not be considered a typo. Such a word will never be added to user history
      * possible bug: words with `possibly_offensive=true` and `f=0` will be suggested when not blocking offensive words, but other words with `f=0` are still not suggested
  * `originalFreq`: unclear, is this used?
  * `flags`: `medical`, `technical`, `hand-added`, `babytalk`, `abbreviation`, `offensive`, `technical`, `nonword`, and probably more: are they used for anything?
  * `possibly_offensive=true` stops the word from being suggested when blocking offensive words
  * `not_a_word=true` will not be suggested, use together with `shortcut`
  * `shortcut=<s>` (below a `<word>`) will suggest `<s>` when the `<word>` is typed
    * needs to have `f` with values from 0 to 14, or the special value `whitelist`
    * what does `whitelist` actually do?
  * `bigram=<b>` (below a `<word>`) will suggest `<b>` as next word before typing any letters
    * needs to have `f`
    * the value of `f` should be higher than the `f` for the `<word>`, but the available AOSP wordlist for US English actually uses 1, 2 and 3 for the 3 bigram suggestions (still seems to work)
