# `git gud` - Learning to use `git`, a version control tool

## What is `git`?

`git` is one of the most widely-used tools in the software development industry,
but it's applicable just about anywhere else, both inside and outside the field
of computer science. It's a **version control** tool - you can keep track of
different versions of your code, whether they're full releases or just a
one-line fix. This *can* be used to establish which changes were made in each
update of a piece of software, but at any level, every **commit** you make
in `git` tells a story - decisions that were made, ways in which things were
implemented, and even some mishaps.

**Commits** are the string that ties `git` together. They're **snapshots** of 
the code at some point in time, with a message attached to detail what changed.

## Why do folks use `git`?

### Keeping track of the development process

Instead of using comments to document changes and choices, sometimes they'll be 
documented in commit history. Let's have a look:

```
commit c6813f8f4805d752b7480c585c3cda669b576365
Author: Simon Fish <si@mon.fish>
Date:   Mon Mar 2 14:44:49 2020 +0000

    Write tests for various dates, skip years tests at first
    
    Students can delete the skip lines to enable those tests if they get
    that far. I'll write another block of tests for important dates for 2020
    only.
```

So, what have we go here?

The long hex string at the top is a **commit hash**. It might seem totally random, but it's actually
[a lot of information about the commit encoded with SHA-1](https://gist.github.com/masak/2415865). Okay, you didn't need
to know that part...but what you *do* need to know if that if you want to know what the code looked like at that point
in time, you'd do this:

```
git checkout c6813f
```

Think to yourself "hey, let's **check out** what the code looked like at this point in time" - "this point in time"
being the commit hash.

There are also details of when the commit was made and who the commit was made by. The message is really important -
commit early and often so that you can summarise things quickly on the first line. You can use the rest of the message
space, if you wish, to document anything you think is particularly important to know in the future.

### Collaborating with others

This isn't something there'll be an exercise on, but it's good to have a little context on. `git` is great for working
with others, but why wouldn't you code in Google Docs, say? Because everyone edits at the same time, and with code, that
could have some nasty side effects. It's got its uses, which is why editor features exist to let you do that if you
wish, but typically, various different people will work on various different features across a huge codebase, and any
overlaps will need to be resolved. That's why `git` has **branches**.

Branches allow you to, well, 'branch off' from any commit and make some changes, whatever the reason may be - a feature,
a fix, a refactor. You can then **merge** this branch back into the one you branched off, and combine the changes you
made with anything that happened since you branched off. If you edited some of the same lines as other people, `git`
will show you both and allow you to **resolve conflicts** so that the merge finishes smoothly.

### Making code publicly available

There are a lot of `git` providers online - **GitHub** might be the most familiar to you. Others include **BitBucket**
and **GitLab**, but it's also possible to host your own `git` server using free or proprietary software. Free options
include **Gitea** and **GitLab CE**, but the three main providers also offer their services to enterprise.

## Your challenge

Do you know what day of the week your birthday falls on this year? Well, you're about to write something that'll help
you figure it out!

Get the tests in `tests.py` to pass by creating a class `GetBirthDay`. `GetBirthDay`'s initialiser takes a `day`,
`month` and `year`.

 `GetBirthDay` should have a method `day_index`, which returns the day of the week (0-indexed!) that the date in
 `GetBirthday` falls on. For example, my birthday falls on a Wednesday, so `2` should be returned.

```python
>>> GetBirthDay(8, 4, 2020).day_index()
2
```

If it's passed an invalid date (like the 30th of February), it should `raise ValueError`.

Focus on making sure things work for dates in **2020 only** to start with, and don't forget to **commit** to save your
progress.

Expect output like this after running `python tests.py -v`:

```
test_errors_if_dates_outside_feb_limits (__main__.TestGetBirthDay) ... skipped 'Delete this line for the extension task'
test_errors_if_dates_outside_month_limits (__main__.TestGetBirthDay) ... ok
test_errors_if_year_outside_limits (__main__.TestGetBirthDay) ... ok
test_important_dates (__main__.TestGetBirthDay) ... skipped 'Delete this line for the extension task'
test_important_dates_this_year (__main__.TestGetBirthDay) ... ok
test_outputs_within_limits (__main__.TestGetBirthDay) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK (skipped=2)
```

### Tips, if you're stuck on the algorithm

- This year starts on a Wednesday (`2`). Might want to bear that in mind!
- March 3rd might be the 3rd day of March...but which day of the *year* is it?
- The modulo operator (`%`) is good for wrapping numbers within a range. It's normally used for checking if numbers are
- even (`x % 2 == 0`), but where might you use it here?

## This is to go even further beyond!

If you manage to get the tests passing, remove the lines starting with `@unittest.skip(...)` to reveal another set of
tests. These will push you to get the program working for **different years**, so you can have a look at some other
dates from across history. Pay particular attention to **leap years**!

### Tips

- This year starts on a Wednesday (`2`)...but what did last year start on? Or the year before?
- Leap years are divisible by 4, but multiples of 100 aren't leap years unless they're *also* divisible by 400. 