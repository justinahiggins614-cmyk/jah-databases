# Dictionary entries — The Website Uptime Monitoring Database

Key terms of this database, defined in plain words.

## uptime

The share of time a site was answering, counted over days or months, shown as a number beside the site.

## check

One question asked of a site, such as asking for its home page, answered by the site or by silence, and written down with its time.

## probe

A check sent from a place far from the site, so that the answer shows what a far-away visitor would see, not only what the site's own room sees.

## downtime

A time when a site does not answer, counted from the first failed check to the first passing check, and written into the history.

## alert

A message that a site may be down, sent when checks fail in a row, naming the site, the time, and the failing check.

## false alarm

An alert raised when a site is actually working, often because one probe's road was broken, which must be read and marked so the rule can be improved.

## interval

The time between checks, chosen so that a failure is found quickly without asking the site so often that the asking itself becomes a burden.

## threshold

The number of failed checks in a row that must happen before an alert is sent, so one stray failure does not wake anyone.

## response time

The time between asking a site and receiving its answer, which grows when the site is busy and which the monitor records beside every check.

## history

The past record of a site's checks, shown day by day, so that anyone can see how often it failed and for how long.

## maintenance window

An announced time for planned work, during which the monitor expects the site to be quiet and does not raise alerts.

## ledger

The monitor's own written record of every check, every failure, and every alert, kept in order.

