# tabletop-librarian

An unofficial open source mod manager for Tabletop Simulator (TTS)

## Why?

TTS provides mods as a list of assets. If any of those links are deleted, then the entire mod is effectively destroyed. When copyrights are being protected for actively available games, that isn't a problem. When an abandoned title that is loved is lost to bit rot, then the community is worse off than had it been before.

The third party software TTS Mod Manager is almost perfect, but it is closed source and hasn't been updated in a while. There are dozens of other projects with similar goals, but TTS Mod Manager is the only widely used competitor.

## Goals

1. Retrieve remote assets and cache them locally to completely preserve board game mods
2. Provide endpoints to store and retrieve both TTS style mods and full archive style mods
3. Very light mod management (naming, folder structure, etc)
4. Convert mods between formats (i.e. turn a TTS mod into something an open source alternative could use)