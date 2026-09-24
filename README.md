# Realistic Berry Bush Grafting

This is a mod that allows you to combine berry bush graftings in a
somewhat realistic fashion. See [the mod description](./DESCRIPTION.md)
for more information on how it works in the game.

## Mod Considerations

This mod is a content-only mod. While there is probably an easier way to
achieve all this using a code mod, that C# code would actively have to
be maintained, while a content mod should basically work on any version
of the game. Additionally, content mods cannot really inject malware
into the game, making them more trustworthy to players.

As there are a lot of possible trait combinations and even more ways to
get these combinations by grafting two cuttings, the recipe files are
not checked into this repository. Instead, a Python script is provided
to generate these recipe files:

```sh
python scripts/generate.py
```

## Contribution

Have a bug, suggestion or feature request? Feel free to open an issue on
this repository! Want to provide your own JSON files or assets to this
repository? Fork it and open a pull request!
