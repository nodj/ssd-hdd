# ssd-hdd
Windows tool that mirror a ssd folder on hdd

## What??
This soft moves a folder from a SSD to a HDD, freeing some precious space.
The original folder is moved, but a link replaces it, so that all your stuff is still accessible from the SSD, while the paths are still OK.

## But... How?
This is super easy to use thanks to the contextual menu!
- Right-clic on the folder to move,
- choose ssd -> hdd,
- you're done!

## Is... Is that magic?
Nope. Sorry. ssd-hdd works with NTFS junctions.
The file system can create an 'alias' for a folder, that behave as the real folder, but taking almost no space.
This means that the mirroring is quite transparent, but some rare application may have some issue with those junctions.

## I wrote this soft for me
Use it at your own risk. I can't promise a bug-free software.
I can't emphasis this enough...
While I don't try to kill your data, a bug is always possible, so if you are sure you want to use it, please, PLEASE make a backup of moved folder beforehand.
This app *will erase* your data after the copy (of course). This is why you should backup your precious stuff in the case something fails durring the process.
I use it frequently, without any issue, all is fine, but no one knows what can happen to your data...

## todo
 - some check after the copy, before the erase operation!
 - a revert option
 - a gui ?
 - etc...

I hope you will like it =)

nodj
