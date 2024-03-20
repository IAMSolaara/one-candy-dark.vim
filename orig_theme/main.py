import json
from pathlib import Path
import shutil

ORIGINAL_THEME_FILE = Path(".") / "OneCandy" / "themes" / "One Candy-color-theme.json"
TMP_THEME_FILE = Path(".") / "one_candy_edited.json"


def is_lang(lang: str, token_color):
    if "name" in token_color:
        if lang.lower() in token_color["name"].lower():
            return True
    if "scope".lower() in token_color:
        if any([lang.lower() in x.lower() for x in token_color["scope"]]):
            return True
    return False


def main():
    if not TMP_THEME_FILE.exists():
        shutil.copy(ORIGINAL_THEME_FILE, TMP_THEME_FILE)

    data = json.load(open(TMP_THEME_FILE))
    lang = "php"

    if (Path(".") / "token_colors" / lang).exists():
        return

    token_colors = [x for x in data["tokenColors"]]
    this_lang_token_colors = [x for x in token_colors if is_lang(lang, x)]

    json.dump(
        this_lang_token_colors,
        open((Path(".") / "token_colors" / lang).with_suffix(".json"), "w"),
        indent=2,
    )

    data["tokenColors"] = [x for x in token_colors if x not in this_lang_token_colors]

    json.dump(
        data,
        open(TMP_THEME_FILE, "w"),
        indent=2,
    )


if __name__ == "__main__":
    main()
