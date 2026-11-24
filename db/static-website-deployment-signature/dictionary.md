# Dictionary entries — The Static Website Deployment Database

Key terms of this database, defined in plain words.

## static site

A website made of finished pages served exactly as written, with no program running behind them to build pages on request.

## deployment

Carrying a finished set of pages from the maker's desk to the public place where readers find them, with checks on the way.

## build

Turning source files into the finished pages a static site serves, done once before deployment, never while a reader waits.

## release

One named version of a site, with its files fixed and its date written down, so it can be checked, kept, or rolled back.

## staging

A private copy of a site, built the same way as the public one, where a release is checked before anyone else sees it.

## rollback

Returning a live site to the previous release when the new one fails, by pointing the public place back at the old files.

## checksum

A short fingerprint computed from a file, used to prove that the file that arrived is the file that was sent.

## atomic deploy

A deployment that swaps the old release for the new one in a single step, so no reader ever sees a half-old, half-new site.

## cache

A stored copy of a page kept close to readers, which must be cleared when a new release changes the page, or readers see the old one.

## preview

A temporary public address for one release, where reviewers can read it before it becomes the live site.

## deployment log

The written record of every deployment, naming the release, the time, the files, and whether it succeeded or failed.

## source files

The maker's own files, written by hand, from which the finished pages are built; the deployment carries the finished pages, not the sources.

