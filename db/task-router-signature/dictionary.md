# Dictionary entries — The Task Router Database

Key terms of this database, defined in plain words.

## task

One piece of work to be done, named, with its inputs, its deadline, and the worker it was given to.

## router

The program that decides which worker does each task, by the rules written in its routing table.

## queue

The ordered line of tasks waiting for a worker, first in, first out, except that urgent tasks jump the line.

## worker

A program or a person that does tasks, one at a time, and reports each one done or failed.

## priority

How urgent a task is, judged by its deadline and by who is waiting for it.

## routing rule

One written rule for matching tasks to workers, such as the fastest worker first, or the worker who did it last.

## retry

Trying a failed task again, after a wait, up to a fixed number of times, and then marking it failed for good.

## deadline

The time by which a task must be finished, promised when the task was made.

## throughput

How many tasks are finished in a given time, counted by the router and shown on its board.

## backpressure

The router slowing new work when its workers are full, so the queue never grows beyond what can be done.

## dead letter

A task that failed too many times, set aside in its own list with the reason, for a person to judge.

## ledger

The router's own written record of every task, every routing, and every result, kept in order.

