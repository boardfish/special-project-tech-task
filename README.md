# `git gud` - Learning to use `git`, a version control tool

## What is `git`?

`git` is one of the most widely-used tools in the software development industry,
but it's applicable just about anywhere else, both inside and outside the field
of computer science. It's a **version control** tool - you can keep track of
different versions of your code, whether they're full releases or just a
one-line fix. `git` has a variety of benefits, such as:

- pinpointing where something broke in your code
- enabling collaboration with others, using branches
- allowing you to more easily back up your code and work offline

Whatever your use for it, every **commit** you make in `git` tells a story -
decisions that were made, ways in which things were implemented, and even some
mishaps. It's a bit like writing a diary and taking a timelapse of your code at the same time!

## How to use `git`

### Committing

**Commits** are the string that ties `git` together. They're **snapshots** of 
the code at some point in time, with a message attached to detail what changed. Let's look at how to make a commit.

When you edit a file normally, the process looks like this:

1. Edit the file.
2. Save the file.

Git gives you a few more things you need to do afterwards:

3. **Stage** your changes.
4. **Commit**.

You might also then **push**. But what does all this mean?

#### Staging files

If you **stage** a file, you add the changes you've made to the file onto the **stage**. When you then **commit**, all changes on the stage are included in that commit.

To stage a file, use the `git add` command. `git add <filename>` stages the file(s) you give it. 

You might also stage a file by accident - perhaps there's a file with some passwords in that you only use on your device? Remove files from the stage (without changing or deleting them) with `git reset <filename>`.

To get an idea of what's been staged and what hasn't, use `git status`. `git status` reports back like this:

```
On branch readme
Your branch is up-to-date with 'origin/readme'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        file_not_committed_yet

no changes added to commit (use "git add" and/or "git commit -a")
```

- `README.md` is a file that I've committed before. Git knows it exists, but I've made changes to it that I haven't
  committed yet.
- `file_not_committed_yet` is a file that I've never added to a commit before. Git isn't **tracking** this file - it
  doesn't know it exists yet.

If I run `git add README.md`, it'll show up like this:

```
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   README.md
```

This means my changes to `README.md` are staged, but if I edit the file and save it again, any further changes I make
will need to be staged again.

##### Shortcuts

Often you'll just want to stage everything you've changed, but sometimes you'll want to be more picky about it. So if you want to:

- add everything, even files you haven't committed before, to the stage: `git add -A`
- add only files you've changed to the stage: `git add -p`

#### Committing

Then, all that's left to do is to `git commit` and supply a descriptive message about the changes you've just made, such as "Write section about staging files". And after that, it's time to `git push` your code over to whichever server you're keeping it on and synchronise your changes.

Let's have a look at how commits show up in `git log`:

```
commit c6813f8f4805d752b7480c585c3cda669b576365
Author: Simon Fish <si@mon.fish>
Date:   Mon Mar 2 14:44:49 2020 +0000

    Write tests for various dates, skip years tests at first
    
    Students can delete the skip lines to enable those tests if they get
    that far. I'll write another block of tests for important dates for 2020
    only.
```

So, what have we got here?

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

## One more thing...

If you manage to get the tests passing, remove the lines starting with `@unittest.skip(...)` to reveal another set of
tests. These will push you to get the program working for **different years**, so you can have a look at some other
dates from across history. Pay particular attention to **leap years**!

### Tips

- This year starts on a Wednesday (`2`)...but what did last year start on? Or the year before? There's a pattern here...
- Leap years are divisible by 4, but multiples of 100 aren't leap years unless they're *also* divisible by 400. 
