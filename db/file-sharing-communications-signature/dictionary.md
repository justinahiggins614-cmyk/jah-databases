# Dictionary entries — The File Sharing Communications Database

Key terms of this database, defined in plain words.

## file

A named set of bytes, kept whole, with a name, a size, and a fingerprint that proves it arrived unchanged.

## share

Giving a named person the right to receive a file, with the file's name, size, and fingerprint written beside the offer.

## sender

The person who offers a file, named in the record, who must be able to prove the file they sent is the file they meant.

## receiver

The person named to receive a file, the only person the share is offered to, until the sender names another.

## transfer

The carrying of a file from sender to receiver, counted byte by byte, until the whole file has arrived or the failure is named.

## fingerprint

A short value computed from a file, used to prove that the file that arrived is the file that was sent, byte for byte.

## receipt

A written note that a file arrived whole, naming the file, the receiver, and the time, kept by both sides.

## link

A written address that stands in for a share, given to the receiver so they can fetch the file when they are ready.

## expiry

The date after which a share no longer works, written beside the share, so that a file does not stay open forever.

## chunk

One piece of a file, sent and checked on its own, so that a failed piece can be sent again without sending the whole file.

## resume

Continuing a transfer from where it stopped, by asking which pieces already arrived, instead of starting over.

## transfer log

The written record of every share, every transfer, and every receipt, kept in order, naming file, sender, receiver, and time.

