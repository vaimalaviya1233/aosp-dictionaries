This repository contains dictionaries for AOSP keyboard and compatible apps, as well as word lists used to create the dictionaries.
For creating _.dict_ files, you can run `dicttool_aosp.jar` (taken from https://github.com/remi0s/aosp-dictionary-tools), e.g. `java -jar dicttool_aosp.jar makedict -s <language>_wordlist.combined -d main_<language>.dict` or use the `WordlistCombined.compile` function (see [examples script](scripts/exampls.py))

Word lists and dictionaries follow the pattern `<type>_<locale>`, with the file ending being `.dict` for dictionaries and `.combined.gz` for wordlists. Note that word lists are gzip-compressed.

# Dictionaries
* [Arabic main](dictionaries/main_ar.dict): Arabic dict created from Wikipedia and OpenSubtitles by Rafail Mastoras, v18, 2018-11-14, 117081 entries, source: https://github.com/remi0s/aosp-dictionary-tools/blob/master/dictsCreated/WikiAndOpenSubtitles/ar_wordlist.combined
* [Armenian main](dictionaries/main_hy.dict): Eastern Armenian Dict, v18, 2022-05-07, 210743 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/hy_wordlist.combined.gz
* [Bulgarian main](dictionaries/main_bg.dict): Български, v18, 2020-05-26, 414922 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/bg_wordlist.combined.gz
* [Catalan main](dictionaries/main_ca.dict): Catalan wordlist from OpenSubtitles by Guillem Solà i Boeck, v18, 2023-08-26, 65649 entries, source: https://codeberg.org/Helium314/aosp-dictionaries/pulls/3
* [Croatian main](dictionaries/main_hr.dict): Hrvatski, v44, 2014-02-24, 210081 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/hr_wordlist.combined.gz
* [Czech main](dictionaries/main_cs.dict): Čeština, v44, 2014-02-24, 171544 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/cs_wordlist.combined.gz
* [Danish main](dictionaries/main_da.dict): Dansk, v44, 2014-02-24, 178449 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/da_wordlist.combined.gz
* [Dutch main](dictionaries/main_nl.dict): Nederlands, v54, 2014-10-31, 178444 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/nl_wordlist.combined.gz
* [English (Australia) main](dictionaries/main_en_AU.dict): English (AU), v47, 2014-06-10, 157472 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/en_AU_wordlist.combined.gz
* [English (United Kingdom) main](dictionaries/main_en_GB.dict): English (UK), v54, 2014-10-31, 157469 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/en_GB_wordlist.combined.gz
* [English (United States) main](dictionaries/main_en_US.dict): English (US), v54, 2014-10-31, 160715 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/en_wordlist.combined.gz
* [English emoji](dictionaries/emoji_en.dict): Emoji for English words, v44, 2014-02-24, 442 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/en_emoji.combined.gz
* [Esperanto main](dictionaries/main_eo.dict): Esperanto, v47, 2014-06-10, 27842 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/eo_wordlist.combined.gz
* [Finnish main](dictionaries/main_fi.dict): Suomi, v44, 2014-02-24, 223363 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/fi_wordlist.combined.gz
* [French emoji](dictionaries/emoji_fr.dict): Emoji pour mots français, v44, 2014-02-24, 440 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/fr_emoji.combined.gz
* [French main](dictionaries/main_fr.dict): Français, v54, 2014-10-31, 190425 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/fr_wordlist.combined.gz
* [Galician main](dictionaries/main_gl.dict): Galego, v18, 2021-02-07, 0 entries, source: https://github.com/chavaone/openboard/blob/master/dictionaries/es_GL_wordlist.combined.gz
* [Georgian main](dictionaries/main_ka.dict): ქართული, v18, 2016-03-12, 100000 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/ka_wordlist.combined.gz
* [German main](dictionaries/main_de.dict): Deutsch, v54, 2014-10-31, 205914 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/de_wordlist.combined.gz
* [Greek main](dictionaries/main_el.dict): Ελληνικά, v44, 2014-02-24, 184303 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/el_wordlist.combined.gz
* [Hebrew main](dictionaries/main_he.dict): Hebrew dictionary fi8les from Hspell ver 1.4 (Hspell was written by Nadav Har'El and Dan Kenigsberg), v1, 2021-02-16, 468559 entries, source: https://github.com/Hananel-Hazan/aosp-dictionary-tools/blob/master/hebrew-hspell.txt.combined.new
* [Hebrew main](dictionaries/main_iw.dict): עברית, v44, 2014-02-24, 94799 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/iw_wordlist.combined.gz
* [Hinglish main](dictionaries/main_hinglish.dict): Hinglish wordlist, v18, 2023-08-27, 209337 entries, source: https://github.com/Helium314/openboard/issues/95#issuecomment-1694667133, https://drive.proton.me/urls/3AJSJ3NPNW#vpeMalUbTjAt
* [Hungarian main](dictionaries/main_hu.dict): Hungarian, v18, 2016-09-07, 66005 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/hu_wordlist.combined.gz
* [Italian main](dictionaries/main_it.dict): Italiano, v54, 2014-10-31, 172831 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/it_wordlist.combined.gz
* [Latvian main](dictionaries/main_lv.dict): Latviešu, v44, 2014-02-24, 200570 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/lv_wordlist.combined.gz
* [Lithuanian main](dictionaries/main_lt.dict): Lietuvių, v44, 2014-02-24, 198160 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/lt_wordlist.combined.gz
* [Luxembourgish main](dictionaries/main_lb.dict): Lëtzebuergesch, v18, 2013-09-30, 71255 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/lb_wordlist.combined.gz
* [Norwegian Bokmål main](dictionaries/main_nb.dict): Norsk bokmål, v44, 2014-02-24, 171008 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/nb_wordlist.combined.gz
* [Polish main](dictionaries/main_pl.dict): Polski, v54, 2014-10-31, 195099 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/pl_wordlist.combined.gz
* [Portuguese (Brazil) main](dictionaries/main_pt_BR.dict): Português (Brasil), v54, 2014-10-31, 170044 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/pt_BR_wordlist.combined.gz
* [Portuguese (Portugal) main](dictionaries/main_pt_PT.dict): Português (Portugal), v54, 2014-10-31, 218457 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/pt_PT_wordlist.combined.gz
* [Romanian main](dictionaries/main_ro.dict): Română, v53, 2014-10-03, 1125204 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/ro_wordlist.combined.gz
* [Russian main](dictionaries/main_ru.dict): Русский, v54, 2014-10-31, 220492 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/ru_wordlist.combined.gz
* [Serbian main](dictionaries/main_sr.dict): Српски, v44, 2014-02-24, 191608 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/sr_wordlist.combined.gz
* [Slovenian main](dictionaries/main_sl.dict): Slovenščina, v44, 2014-02-24, 59998 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/sl_wordlist.combined.gz
* [Spanish main](dictionaries/main_es.dict): Español, v54, 2014-10-31, 236193 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/es_wordlist.combined.gz
* [Swedish main](dictionaries/main_sv.dict): Svenska, v54, 2014-10-31, 196739 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/sv_wordlist.combined.gz
* [Toki Pona main](dictionaries/main_tok.dict): toki pona dict by jan Talya using data from ilo Linku 2022 survey, v18, 2023-08-12, 0 entries, source: https://codeberg.org/Helium314/aosp-dictionaries/issues/1, license: CC by-sa 3.0 and 4.0 combined
* [Turkish main](dictionaries/main_tr.dict): Türkçe, v54, 2014-10-31, 180841 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/tr_wordlist.combined.gz
* [Ukrainian main](dictionaries/main_uk.dict): Українська, v18, 2013-08-14, 1285562 entries, source: https://github.com/openboard-team/openboard/blob/v1.4.5/dictionaries/uk_wordlist.combined.gz

# Experimental dictionaries
* [Arabic main](dictionaries_experimental/main_ar.dict): wordlist for ar, v18, 2023-09-09, 470783 entries, source: source: created using [`wordlist.py`](scripts/wordlist.py) and [`wordlist_combined.py`](scripts/wordlist_combined.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/, license: source lists under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* [Bangla main](dictionaries_experimental/main_bn.dict): wordlist for bn, v18, 2023-09-08, 113494 entries, source: source: created using [`wordlist.py`](scripts/wordlist.py) and [`wordlist_combined.py`](scripts/wordlist_combined.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/, license: source lists under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* [Bulgarian main](dictionaries_experimental/main_bg.dict): wordlist for bg, v18, 2023-09-08, 898359 entries, source: source: created using [`wordlist.py`](scripts/wordlist.py) and [`wordlist_combined.py`](scripts/wordlist_combined.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/, license: source lists under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* [Czech main](dictionaries_experimental/main_cs.dict): wordlist for cs, v18, 2023-09-09, 3154785 entries, source: source: created using [`wordlist.py`](scripts/wordlist.py) and [`wordlist_combined.py`](scripts/wordlist_combined.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/, license: source lists under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* [English (United Kingdom) main](dictionaries_experimental/main_en_GB.dict): wordlist for en_GB, v18, 2023-09-08, 392170 entries, source: source: created using [`wordlist.py`](scripts/wordlist.py) and [`wordlist_combined.py`](scripts/wordlist_combined.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/, license: source lists under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* [English (United States) main](dictionaries_experimental/main_en_US.dict): wordlist for en_US, v18, 2023-09-08, 285063 entries, source: source: created using [`wordlist.py`](scripts/wordlist.py) and [`wordlist_combined.py`](scripts/wordlist_combined.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/, license: source lists under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* [English Scientific Symbols](dictionaries_experimental/symbols_en.dict): Scientific Symbols for English language, v19, 2023-09-08, 27 entries, source: https://codeberg.org/Helium314/aosp-dictionaries/pulls/4
* [English emoji](dictionaries_experimental/emoji_en.dict): Emoji for English words, v1, 2023-07-19, 2304 entries, source: adapted from [gemoji](https://github.com/github/gemoji/blob/master/db/emoji.json)
* [French Emojis](dictionaries_experimental/emoji_fr.dict): Emojis pour mots Français, v50, 2023-07-19, 2270 entries, source: https://codeberg.org/Helium314/aosp-dictionaries/pulls/8
* [French Symboles Scientifiques](dictionaries_experimental/symbols_fr.dict): Symboles scientifiques pour la langue Française, v50, 2023-09-08, 82 entries, source: https://codeberg.org/Helium314/aosp-dictionaries/pulls/5
* [French main](dictionaries_experimental/main_fr.dict): wordlist for fr, v18, 2023-09-09, 670922 entries, source: source: created using [`wordlist.py`](scripts/wordlist.py) and [`wordlist_combined.py`](scripts/wordlist_combined.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/, license: source lists under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* [German (Austria) main](dictionaries_experimental/main_de_AT.dict): wordlist for de_AT, v18, 2023-09-08, 1493104 entries, source: source: created using [`wordlist.py`](scripts/wordlist.py) and [`wordlist_combined.py`](scripts/wordlist_combined.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/, license: source lists under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* [German main](dictionaries_experimental/main_de.dict): wordlist for de, v18, 2023-09-08, 1383471 entries, source: source: created using [`wordlist.py`](scripts/wordlist.py) and [`wordlist_combined.py`](scripts/wordlist_combined.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/, license: source lists under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* [Italian main](dictionaries_experimental/main_it.dict): wordlist for it, v18, 2023-09-09, 202588 entries, source: source: created using [`wordlist.py`](scripts/wordlist.py) and [`wordlist_combined.py`](scripts/wordlist_combined.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/, license: source lists under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* [Russian main](dictionaries_experimental/main_ru.dict): wordlist for ru, v18, 2023-09-08, 1542489 entries, source: source: created using [`wordlist.py`](scripts/wordlist.py) and [`wordlist_combined.py`](scripts/wordlist_combined.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/, license: source lists under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* [Spanish main](dictionaries_experimental/main_es.dict): wordlist for es, v18, 2023-09-09, 698767 entries, source: source: created using [`wordlist.py`](scripts/wordlist.py) and [`wordlist_combined.py`](scripts/wordlist_combined.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/, license: source lists under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* [Ukrainian main](dictionaries_experimental/main_uk.dict): wordlist for uk, v18, 2023-09-08, 1348502 entries, source: source: created using [`wordlist.py`](scripts/wordlist.py) and [`wordlist_combined.py`](scripts/wordlist_combined.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/, license: source lists under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* [Vietnamese main](dictionaries_experimental/main_vi.dict): wordlist for vi, v18, 2023-09-16, 11755 entries, source: source: created using [`wordlist.py`](scripts/wordlist.py) and [`wordlist_combined.py`](scripts/wordlist_combined.py), using word lists available at https://wortschatz.uni-leipzig.de/en/download/, license: source lists under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

# Scripts
The python scripts is still experimental, rather slow and may produce bad dictionaries in some languages. See the [examples](scripts/examples.py) on how the scripts can be used.

In the experimental dictionaries, names are typically missing as they don't pass the _hunspell_ spellcheck.
A `possibly_offensive` attribute is added for some words, which sometimes seems unnecessary. Currently this is coming from the "nosuggest" attribute of the used _hunspell_ dictionaries, which occurs for offensive words as well as for weird / rare word forms.
Furthermore, `possibly_offensive` words and `shortcut`s are taken from Android wordlists for the same locale (existing dictionary merged using default options except `f="overwrite", bigrams=False, other=False`). Other flags are currently missing.

An empty dictionary is available in dictionaries/empty.dict.

# Wordlist information

`wordlist.combined` file infos (from wordlists/sample.combined and guessed):
* header is necessary
  * format like `dictionary=main:en_us,locale=en_US,description=English (US),date=1414726260,version=54`
  * all of these fields are necessary, though `description` may not be shown to the user
  * **Note:** `version` should be greater than 18 for the dictionary to work with all AOSP keyboards (not necessary for https://github.com/Helium314/openboard though)
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
