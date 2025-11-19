**SPEAKER_02:**
[00:00] Okay, recording is in progress, it says. So, hello everybody.
[00:05] Um, today, delighted to have Christoph Jentzsch with us.
[00:09] We did attempt to record this, Christoph and I, two weeks ago, but I forgot to press the record button.
[00:14] So we spoke for an hour or so and then it was not recorded.
[00:17] So this is round two.
[00:19] So hello, Christoph. How are you?

**SPEAKER_00:**
[00:21] Hi, Rob.
[00:22] Nice to meet you again.
[00:23] I'm doing good.
[00:24] I hope you too.
[00:25] Thanks for the invitation.

**SPEAKER_02:**
[00:26] Fantastic, yeah.
[00:27] So Christoph and I, our paths crossed for the first time way back in 2015 when I was trying to do C++ Ethereum on my smartwatch.
[00:36] And this was around the time that Christoph was still at the Ethereum Foundation.
[00:41] And then I think I crossed paths a number of times since, and Kieran's too.
[00:44] Indeed.
[00:45] So, Christoph.
[00:47] What were you doing with your life before you found Ethereum and joined this crazy journey?

**SPEAKER_00:**
[00:52] So the journey started in 2013.
[00:55] I was doing my PhD in theoretical physics, actually about self-organizing systems.
[01:00] So like biology, six months in mathematical biology and other things.
[01:03] So I was studying systems which have local rules and global behavior.
[01:07] And I came across Bitcoin, which is just a small set of local rules and a global behavior as a currency.
[01:13] But the reason I came across this was I was looking for cheap GPUs, like graphic cards, and the Bitcoin miners were selling their GPU mining rigs to get some FPGAs and later ASICs.
[01:23] And so that's how I got into what's Bitcoin mining.
[01:26] And so I bought my first Bitcoin, got into this bubble, did read everything I could about it.
[01:31] And then I came across the white paper from Vitalik in early 2014, something like January, February, in some Bitcoin forum somewhere.
[01:39] And I was already totally in love with the idea of Bitcoin being a decentralized currency and all the characteristics and features of it.
[01:46] And this white paper from Vitalik—and if you read it again, it's almost a prophecy—and except for NFTs, everything's in there, from DAOs, from ENS-like name systems, this domain name system, and all of that.
[02:00] So for me, it opened up this option of building applications with the same characteristics as Bitcoin, but just not a currency, but everything else.
[02:08] And so then I started reading everything about it.
[02:11] And in 2014, in summer, I read that the crowdsale was in 2014, right?
[02:16] So around the time the crowdsale happened, I watched a video from Gavin Wood.
[02:20] He was somewhere in the Scandinavias, some conference there, um, the Nordics, and he talked about Ethereum.
[02:26] I loved it.
[02:27] And he said he wanted to open up an office in Berlin, looking for C++ developers.
[02:32] I was a C++ developer, so in theoretical physics, it's 90% software development.
[02:37] So I said, well, I want to do this.
[02:39] So I took my parental leave time plus some vacation time from and paused my PhD for like three or six months and said, "I will return after I'm done."
[02:49] I thought this was just a short project because they raised money, maybe six, maybe 12 months, 18 months or so, then it's over.
[02:56] When I started, I thought about maybe three to six months, and then I'd go back to my PhD.
[03:01] So I worked there with Ethereum, with Gavin Wood, it was a great time, and then just decided to stay.
[03:06] It was so exciting.

**SPEAKER_02:**
[03:07] So you never got to be a doctor?

**SPEAKER_00:**
[03:08] No, I'm not a doctor.
[03:10] I did not finish my PhD, although I only had six months left, which was kind of a pity.
[03:14] I worked for three years on that.
[03:16] But I also had at the time, I think, four or five kids.
[03:19] I needed some money.
[03:20] I didn't get much money as a PhD student.
[03:22] So I did software development as a side hustle, basically.
[03:26] And so when I got this project, I said, "Well, let's do this for two or three months as a parental leave time, and then I can return."
[03:31] And then I decided to really interrupt my PhD.
[03:34] I said that I will maybe return one year later because I thought the foundation would eventually run out of money because they're not making any profits.
[03:40] It just raised donations, then it was spent, and that's over.
[03:43] Then I can continue my PhD.
[03:45] That was originally the plan.
[03:46] It just came different.
[03:47] I mean, I guess it's never too late, right?
[03:49] I actually sometimes think about it, that I should return.
[03:52] It's just so much to learn again.
[03:54] I'm right now doing Tokenize.it.
[03:56] I'm basically working on tokenizing German companies.
[03:59] It works very well.
[04:00] And so currently, I'm not planning on getting back anytime soon.

**SPEAKER_02:**
[04:03] No, because I mean, famously you had, you know, Dr. Gavin Wood and Dr. Christian Reitwiessner as well.
[04:09] And I think there were a couple of other PhDs as well.

**SPEAKER_01:**
[04:11] There was definitely.
[04:12] I also dropped out of mine.
[04:13] I was actually in mathematical physics too.
[04:15] Interesting.
[04:16] Similar background.

**SPEAKER_00:**
[04:17] It's actually the same.
[04:18] Like theoretical physics, it's the mathematical part of physics.
[04:21] I enjoyed it very much.
[04:23] I did thermodynamics and statistics, mostly software development.
[04:26] It was really fun.

**SPEAKER_01:**
[04:28] Well, by the way, Jim is trying to join.
[04:30] I don't know if there's anything that needs happening.
[04:32] He gets some browser issues.

**SPEAKER_02:**
[04:33] Yeah, yeah.
[04:34] Well, he'll pop up and we can add him or if he's—I'll say then, then never mind.
[04:38] So, so Christoph, in terms of, um, you know, getting hired into EthDev, and I'm sorry if I just missed it.

**SPEAKER_00:**
[04:45] So how did that happen?
[04:46] Did you, you meet Gav at a meetup?
[04:47] Did you say?
[04:48] Yes, I actually, I listened only to his talk.
[04:51] It was an online thing.
[04:52] And I actually just wrote him an email, said, "Look, I would love to join Ethereum.
[04:56] Love what you're doing."
[04:57] And he invited me to meet me in Kreuzberg, Berlin.
[05:01] So which again is about two hours drive from here.
[05:04] So I went up there, met him.
[05:05] I remember the first conversation.
[05:07] He was talking about all the stuff they were going to build.
[05:09] He said, "Well, what can you do?"
[05:11] And I just asked him, "What's like the most complicated stuff you have right now?
[05:14] Like, give me a complicated task.
[05:16] I somehow can figure it out."
[05:17] So he talked about the Ethereum Virtual Machine, which needed some testing.
[05:21] So I just picked working on testing the Ethereum Virtual Machine or like writing tests for it.
[05:26] Back at the time, I actually had no real idea what he was talking about.
[05:30] Meaning, of course, I did understand on the white paper level, I did understand what Ethereum was about.
[05:35] But Gavin had this skill of writing the yellow paper, which is still incredible work.
[05:40] Like it's such a great specification, different from Bitcoin, really having a specification.
[05:45] So multiple clients could be built.
[05:47] And in there, he defined the Ethereum Virtual Machine.
[05:51] And I think I read the paper six, seven times.
[05:54] I felt like I was one out of, I don't know, 10 or 20 people in the world at the time who really understood the yellow paper.
[05:59] I did corrections to it.
[06:01] I have some pull requests actually in the yellow paper GitHub repo, um, added missing definitions and stuff like that.
[06:07] And then what I mostly did was writing tests according to the specification, which then were with the help of the C++ client, because this was his team.
[06:15] So I was working also on the C++ codebase.
[06:18] And so Geth, PyEthereum, also the JavaScript version, and what else did we have?
[06:23] Like the Haskell client and others.
[06:25] I was basically using my tests to see if they implemented the virtual machine, also the state transitions and block creation correctly.

**SPEAKER_02:**
[06:33] Yeah.
[06:33] Yeah.
[06:34] So, I mean, just, just to have some timeline for the, for the viewers.
[06:38] So, um, Vitalik wrote the white paper in November 2013.
[06:43] Um, various other people sort of joined in on the efforts, uh, in December, including, uh, including Gav and Jeff Wilcke, who, uh, who started the C++ and Go, uh, clients, uh, respectively at the very end.
[06:55] Oh my goodness.
[06:56] at the very, at the very end of, uh, at the very end of, uh, of December, kind of Christmas projects for them both.
[07:02] January 2014, you had sort of like the, the public announcement of Ethereum at the, at the Bitcoin Miami conference.
[07:09] Um, it was as early as April 2014 that Gav wrote the yellow paper, which is, you know, as you're saying, the sort of formal specification.
[07:16] Um, you had the crowdsale between July and September 2014.
[07:21] Um, so then, yeah, you were coming in right after that, you know.
[07:25] So you had a wave of arrivals in September and October of that year, essentially because the crowdsale had happened.
[07:30] There was some money to actually hire people.
[07:33] Um, and then talking about, you know, where you, where you met there, uh, initially that group, so EthDev were, and is, a company coordinating the development of, of Ethereum stuff.
[07:42] So it's a subsidiary of the Ethereum Foundation.
[07:45] Um, were working initially in a co-working space, but then got an office.
[07:49] And it was between August and November of that year that the office was getting like, you know, done up and tidied.
[07:55] And then in November, you had Devcon Zero, um, you know, the first conference, uh, you know, an internal one where a lot of the people, that was their first sort of face-to-face meetings.
[08:06] How was Devcon Zero?
[08:08] How was that?
[08:09] What was that like?

**SPEAKER_00:**
[08:10] It was like a company retreat.
[08:12] So it was not a public conference.
[08:14] Even though there were some outsiders who felt like part of the community, maybe also pushed some code.
[08:19] I remember, what was his name again, wrote the book also about Ethereum.
[08:26] I think Henning Diedrich was also there, just as an example of some people who were like, reading about Ethereum, interested in joining.
[08:32] Of course, Joseph Lubin.

**SPEAKER_02:**
[08:34] Roman was there.

**SPEAKER_00:**
[08:35] But it was mostly developers.
[08:37] But also, I think Stefan was already there.
[08:39] So they had already the London team.
[08:41] So it was like an internal Ethereum meeting, kind of a meetup almost, I think three days or so.
[08:46] Five days even.
[08:47] So it was a full week.
[08:48] I was there for the full week, as far as I can remember.
[08:51] I did a presentation about testing, how the test suite is very important.
[08:55] Yes, we had Remix projects, Solidity project, I think, mostly started at the time.
[09:01] Gavin used this for explaining his vision of Ethereum as a platform for decentralized applications, so building Swarm.
[09:08] I don't know if Swarm and Whisper were already launched there, but at least the generic idea, the Mist browser.
[09:13] So all those ideas were really sketched out there, like the technical roadmap, what we are going to build.
[09:19] And because we started just, of course, with the basic clients, like implementing the protocol, but he took it like, kind of, what are we going to do in the next 12 months?
[09:27] The Mist browser, Remix, all those tools to have a platform for these and those applications.
[09:34] I remember one slide, which I think I posted on Twitter a while ago.
[09:38] You have those three circles.
[09:40] One circle is at one node.
[09:42] You would see they are connecting on the blockchain, using Swarm for the data, Whisper for the messages.
[09:48] This whole picture was painted there.
[09:50] And there are people attending, I think around 50 people, plus, minus 10, don't know the exact number, where most of the developers were talking about code, coding there.
[09:59] Joseph, I remember him being there saying, "Well, all of you, you will create your own companies, becoming millionaires."
[10:05] I remember Joseph talking about that.
[10:07] And I think mostly he was right.
[10:09] So most of those people in the room...

**SPEAKER_02:**
[10:11] in one way or another co-founded, founded, or were an early part of companies building on top of Ethereum in the years to come.
[10:17] Yeah, yeah.
[10:18] Um, let me see if I can do a little, a little screen share.
[10:21] No, no, I can't work out how.
[10:22] Not, not to worry.

**SPEAKER_01:**
[10:23] But, but yeah, there's this present button.
[10:25] Does that not work?
[10:26] Yeah, I don't see that.
[10:27] Is that on the right-hand side somewhere or at the bottom?
[10:29] Maybe you have a different...
[10:31] For me, I appear on the top right and below.
[10:33] And to the right of me below, there's a present button with like a plus.

**SPEAKER_02:**
[10:36] Oh, never mind.
[10:37] Never mind.
[10:37] I was just going to show the iconic photo of people at Devcon Zero, right?
[10:41] You know, that's this big group shot with nearly everyone who was out there.
[10:45] You know, so that's a classic Ethereum photo.
[10:48] So I was looking, sorry, there's, there's like 11 of the videos, they're still around from Devcon Zero.
[10:53] I think they were around 20 sessions.
[10:54] I'm still trying to dig out the, the others.
[10:56] Some of them, including yours, I have not managed to find yet.

**SPEAKER_00:**
[11:00] It was only about the test suite, how it's built it, how people would use it.
[11:03] It was rather technical.
[11:04] There was not much of a vision in there.

**SPEAKER_03:**
[11:06] Well, Lefteris presented on Emacs, so you're not the most boring talk.

**SPEAKER_00:**
[11:10] Again, it was just some nerds starting.
[11:13] Also, for most of them, it was the first time we actually met.
[11:16] Now, of course, the C++ team, they did know each other because they were working in the co-working space.
[11:21] Lefteris and others were there.
[11:22] But then, let's say, I think it was the first time I actually met Vitalik because he came there.
[11:28] Then, of course, Jeffrey and his team, Stefan Tual and his team, Joseph Lubin.
[11:32] So for me, it was the first time to meet all of them and having talks.
[11:36] And since we really had time, five days, a small group of people, we actually did have time to eat together, to talk.
[11:42] So it was not so crowded maybe as Devcon is today.
[11:45] Very intimate.
[11:46] It was good.

**SPEAKER_02:**
[11:47] Yeah, I mean, far from it.

**SPEAKER_01:**
[11:48] One thing I can't quite remember.
[11:50] So there was a time there was an Ethereum Slack that was kind of open to the public.
[11:54] You know, there were a lot of people.
[11:55] The sort of Ethereum affiliation status was fairly vague at that point.
[12:00] And we were, you know, I remember we were using Skype a lot in those days, just the team.
[12:05] Um, and like Vitalik liked to Skype.
[12:08] Um, and then at some point, I sort of lost the thread of like where the core—I can't remember where the core development discussions were happening.
[12:15] And I'll, maybe I'll ask Jim to comment also just like those tests.
[12:18] We kept like getting them.
[12:19] And I think I'm thinking of some a little bit earlier on and we'd build them.
[12:22] And Jim was mostly working on them and we'd want an update on the like passing percentage, which would always be between like 93 and 98%.
[12:30] And then something would change, you know.
[12:32] Um, but yeah, like where did the discussion, because yeah, between like the sale and Devcon Zero, I think it kind of got a little bit, like, moved around where the dev discussion was.

**SPEAKER_00:**
[12:42] Yeah, it was mostly Skype.
[12:44] We also had Skype channels for almost everything, like the C++ team and so on.
[12:49] Then in a short time, there was a note taker, which had a name also with E something.
[12:53] Etherpad?
[12:54] Yeah, Etherpad, something like this, right?
[12:56] There were some notes being written there, but the communication was really, I would say 99% Skype for me.
[13:03] Later on, we used a tool based on GitHub.
[13:07] What was the name of it?

**SPEAKER_02:**
[13:08] Gitter.
[13:09] It was called Gitter.

**SPEAKER_00:**
[13:10] Gitter came later.
[13:11] This was like the replacement for Skype, but I didn't use it too much.
[13:15] This was actually during the time when I was actually leaving.
[13:17] But it was done, used also by the C++ team.
[13:20] There you had a channel per GitHub repo.
[13:23] This was during the time that GitHub was completely reorganized because at the beginning it was like one big repo with everything.
[13:28] Then we had those submodules.
[13:30] It was so messy.
[13:31] And then during this process, we got Gitter.
[13:34] But yeah, for me, it was mostly Skype.

**SPEAKER_02:**
[13:36] Yeah, and and then annoyingly, that kind of means a lot of these early discussions are kind of like a bit lost because nobody is, is using Skype and Skype is getting like deleted.
[13:46] This is happening in February of next year.
[13:47] Oh, I thought it happened already.
[13:48] So you can still request a download and I did and then I haven't heard anything back.
[13:52] And I want to do that to see if I can get some of those.
[13:54] So everybody apply to download your, your Skype data.
[13:57] I remember with, with Gitter, there was a discussion about this that I was involved with at the EF later, which was saying the problem with Skype is it wasn't discoverable.
[14:06] You know, you had to add, you had to request to be added, but you had to know what was there to be able to do that request.
[14:11] So it was a bit of a chicken and egg situation, whereas Gitter, it was like a one-to-one with the repositories.
[14:17] So if you're using a repo, there you go.
[14:19] There's a one-to-one channel with that.
[14:21] And it was discoverable and archived.
[14:23] But then Slack, I think, was even earlier.
[14:26] Oh, and there was the forum as well, right?
[14:28] There was an Ethereum forum too.

**SPEAKER_00:**
[14:30] Yeah, it was important.
[14:31] And then Slack, I think I got introduced to Slack by Stefan Tual when he created a community for the DAO.
[14:37] When he looked for a new communication tool, he went with Slack.
[14:41] And at that time, it was not like today, like a business tool for the company.
[14:44] It was really communities.
[14:46] Like we had 5,000 people in our Slack, which is not how it's used today.

**SPEAKER_02:**
[14:50] Yeah, yeah.
[14:52] So welcome, Jim.
[14:54] Are your technical problems?

**SPEAKER_04:**
[14:56] Hi, sorry.
[14:57] I had some technical problems for a while there.
[15:00] I don't know.
[15:01] I'm just listening to you guys.
[15:02] What happened that brought the whole world to Zoom suddenly?

**SPEAKER_01:**
[15:05] It was in waves.
[15:06] On my side...

**SPEAKER_04:**
[15:07] I don't know.
[15:08] I just woke up one day and everything was Zoom from then on.

**SPEAKER_01:**
[15:11] It was like a statistical phase transition.
[15:13] I think it was two phases.
[15:15] I would always get invited to corporate, let's say 2017 to 2019 when I was doing primarily BD, I found that I would get invited to any of 10 video conferencing tools.
[15:25] And, like, you know, what was the Cisco one?
[15:28] WebEx.
[15:28] That was horrible.
[15:30] I would get that a lot.
[15:31] Google meetings didn't feel sufficiently corporate or something, even though it was okay.
[15:35] And Zoom had the best quality for a while.
[15:38] And I found that everyone picked Zoom at the same time, like mid-2018, let's say.

**SPEAKER_02:**
[15:43] I think it was just quality to me.
[15:44] Yeah.
[15:45] I mean, Microsoft really fumbled, right?
[15:47] Skype had got such a lead for so long, but Zoom just seemed more reliable.
[15:51] Whatever weird little proprietary magic they had going on.
[15:54] Yeah.
[15:54] And then I guess, yeah, I guess I was under the impression that like Zoom was for businesses.

**SPEAKER_01:**
[15:58] I think that's, well, that is true.
[16:01] But it was just that still, I mean, this has gotten way better in the last 10 years, but still nothing really works for reliable video over the internet.
[16:07] It's just much better than what existed.
[16:11] But there was a free version always, and it would just like time you out.
[16:14] So like they had a fairly viral acquisition loop where...
[16:16] I was just going to say, in the pandemic, once when people were locked down, it became a consumer tool where people would have like large yoga classes or, you know, sermons or whatever with like 500 people on a Zoom.
[16:28] And then everyone...

**SPEAKER_04:**
[16:29] I remember it well.
[16:30] All of a sudden, my parents were calling me up and they were like, "We found this awesome new tool.
[16:34] You've probably never heard of it.
[16:35] It's called Zoom."

**SPEAKER_03:**
[16:37] But yeah, there were like 10.

**SPEAKER_02:**
[16:38] Let's move on from sharing about video platforms.
[16:41] So I look back.
[16:42] So Jim's first commits on the Haskell client were mid-September 2014.
[16:47] So, you know, a couple of months ahead of Devcon 0.
[16:50] That you'd had the yellow paper for five months at that time.
[16:53] And I did find on our Slack, um, you know, a bit of a thread where, where things I think from you, Christoph, were, were being discussed by Jim.
[17:01] I don't know, did you guys interact directly at all on, on testing, Jim, Christoph?

**SPEAKER_04:**
[17:05] Not directly, not as far as I can remember.
[17:07] I mean, maybe there was some messages.
[17:09] I mean, it's about, it has been a while ago.
[17:11] I could be wrong.
[17:12] I may have met you briefly in London when we had that conference.
[17:15] But it would have been like quick greetings at an after party or something.

**SPEAKER_00:**
[17:18] I mean, 10 years ago, lots of people, sure.
[17:21] We were testing the GitHub repo and we had all the major clients using it.
[17:25] And I was interacting, mostly asking, responding questions.
[17:29] I mean, of course, the C++ client I was super close to.
[17:32] I used the C++ client also to pre-fill the tests.
[17:35] So this was per default right, except we found there was a test failing, but actually C++ was wrong.
[17:42] So sometimes this happened.
[17:43] The test was not really failing, just C++ was wrong.
[17:46] But in the majority of cases, C++ was right.
[17:49] So we were just having those conversations, and we found tons of issues.
[17:53] We did, not just in the beginning, I wrote those tests using actually bytecode, the very first tests.
[17:59] Then I went to a low-level Lisp-like language.
[18:02] This was LLL.
[18:04] This was the precursor to Solidity by Gavin.
[18:08] And then in the end, actually, I had automated fuzz testing where I wrote software that would create thousands of tests.
[18:15] We had some AWS, like over 100 cores of machines constantly creating tests.
[18:20] We had always some failing on some versions of Geth or other clients.
[18:24] So this was mostly what I did during one and a half years.

**SPEAKER_02:**
[18:26] Right, right.
[18:27] So, so yeah, I mean, I guess for the, for the viewers, something that Ethereum chose to do differently from Bitcoin was to have this specification separate from the client software, right?
[18:37] So, you know, when Bitcoin started, uh, it was the code that happened first and the, the white paper afterwards.
[18:43] But, but the white paper wasn't a protocol specification.
[18:46] So, um, you know, Gav was doing that yellow paper spec in parallel with the C++ client, which was sort of the first one, while you have Vitalik working on the Python client, Jeff Wilcke working on the Go internally.
[18:59] But then you've got all these other clients as well, right?
[19:02] So the Java one by Roman Mandeleil, I think, started in about April or May.
[19:07] You know, ourselves, Jim and Kieran here with with the Haskell client starting in September.
[19:12] You had JavaScript as well.

**SPEAKER_00:**
[19:14] Right.
[19:14] It's more like a library.
[19:16] I don't know if it was really like a syncing client, but they have all the tools so you can, in your web app, kind of integrate parts of it to verify certain states.

**SPEAKER_03:**
[19:24] Yeah.
[19:24] I mean, I think maybe they had a syncing client at some point, apart from it obviously couldn't actually keep up, but theoretical.

**SPEAKER_02:**
[19:30] And...
[19:31] and yeah, like a little later, there was a Ruby client as well.
[19:34] And yeah, at one point, there were eight different clients.

**SPEAKER_00:**
[19:37] Right.
[19:37] If you want to, I can tell the story of why we all are using Geth today.
[19:40] Yeah, please do.
[19:41] Because this is absolutely not a given.
[19:44] At the time, of course, everyone had different opinions.
[19:47] But the C++ client was really the fastest, the most solid one, passing all the tests and so on.
[19:53] But Gavin always wanted to add new features.
[19:56] We went to a refactoring, and he was a perfectionist, which is not bad for this kind of software.
[20:02] And then the time came for the security audit because everybody wants to launch Ethereum now.
[20:06] And he said, "Before we launch it, those clients need to have a proper security audit by an external company."
[20:12] And one of the companies doing this was Deja vu in Seattle.
[20:15] So I actually went there with the team for the audit.
[20:17] And because Gavin wanted to build some more features, he said, "Well, let's just let Geth go first.
[20:22] Let's first order the Go client.
[20:24] When they are done, I'm done with the features I want to build, and then we're going into the audit for the C++ client."
[20:30] So Geth was audited.
[20:32] They had some issues.
[20:33] They fixed the issues.
[20:35] And now it's fine.
[20:36] And so there was technically no reason why not.
[20:38] Well, actually, we could launch Ethereum now.
[20:41] We have a fully audited client.
[20:43] Testnet is running for a while.
[20:45] No major issues.
[20:46] No failing tests for a long time.
[20:48] So why would we wait for the C++ client to be audited?
[20:51] I mean, they all really had the pressure of money was running out.
[20:55] We need to launch now.
[20:56] And then a decision was made.
[20:58] Let's launch with Geth.
[21:00] Uh, they can still use C++.
[21:02] It's just not audited.
[21:03] Let's say in two months or so, the audit is done, and then they can use C++ even more if they want.
[21:08] So, but then the big mistake was, in my view, when they made this announcement of you can start now, they recommended using Geth because this was the audited one.
[21:16] So almost everybody, um, went with Geth.
[21:20] This was like we started with almost 100% Geth, and then there were just minor other clients using it.
[21:26] Only very few did use them.
[21:28] And so after the audit was done, nobody switched.
[21:31] We were like, sure, but Geth is running.
[21:33] I'm synced.
[21:34] What's the issue?
[21:35] Why should I switch?
[21:37] And so we had this 90/10 or 80/20 distribution.
[21:41] It just stayed like this.
[21:43] So if Gavin would have been either saying, "Let's just do the audit now and we just have both audited and then start," maybe we'd have 50-50.
[21:52] Or even the other way around, if they would have first audited the C++ and Ethereum would have been launched without a Geth audit, they would have seen a total switch.
[22:01] And then, of course, money was going low in the foundation.
[22:04] They had to reduce the team.
[22:06] And because Geth was the most used one, there were some issues with Gavin.
[22:10] Another story, maybe have a talk with him.
[22:12] And so in the end, Ming decided to basically kick out the complete C++ client.
[22:17] This was then shortly before Devcon 1.
[22:19] So something like November, October-ish.
[22:22] But yeah, I think the reason for that was also the C++ client wasn't really that used.
[22:27] Also, there are other reasons as well.
[22:29] But you can see how a tiny thing can have such big consequences down the road, like him doing Polkadot today and all of that.
[22:36] And he was great.
[22:37] I mean, I really, I still think, I think maybe we would have had a mistake in sharding way earlier if Gavin would have stayed.
[22:45] So without him, they moved slower.
[22:47] And of course, the price went up.
[22:49] There were no security relevant things.
[22:51] So changes happened not quickly anymore, but took more time and so on.
[22:55] But I think this was a big loss for Ethereum that Gavin left basically in 2015.

**SPEAKER_01:**
[23:01] Yeah, it's amazing.
[23:02] The client side was the cause.
[23:03] I think it was part of it, but it, uh, you know, having, um, the, the process maybe started, uh, with the Red Wedding, which we just, uh, in some other early days of Ethereum episodes, like he, um, I remember very clearly in the room, I was like two weeks into my Ethereum tenure at that time, that he was talking about brain drain if it was only going to be a nonprofit foundation and not going to have a commercial arm.

**SPEAKER_00:**
[23:25] Yes, there were more issues than that, definitely.
[23:28] Like this was not the deciding part, but it was like those things were adding up.
[23:32] I remember that Gavin had this idea of turning the foundation into a DAO and then having a for-profit entity next to it, which would build things and make money.
[23:41] So there were many different commercial ideas at the time.
[23:44] So he then basically started on his own, EthCore.
[23:48] I remember he wanted to have me as part of it, but I decided to do Slock.it at the time.
[23:53] So that's why I did not become a co-founder of EthCore.
[23:57] Another story, we can go into this if you want.
[23:59] You know what happened after that.
[24:01] But there are many reasons we were part of it.
[24:03] I think also him and Ming didn't really get along too much.
[24:06] There was not really a trust relationship going on.
[24:09] Of course, money running out, different visions of how Ethereum should evolve technically and economically, if you want.
[24:16] All played a role, but I think it was just one part that the C++ client wasn't that much—wasn't really used that much.
[24:22] And the reason for that was Geth being audited and launching without an audit for the C++ client.

**SPEAKER_02:**
[24:27] Yeah, I mean, talking about features.
[24:29] So, so many things happened, right?
[24:31] You know, Gav had this period of incredible productivity between that December and that April of getting from nothing, you know, just like, just having the white paper all the way through to having a working client, you know, having the yellow paper.
[24:43] As you mentioned, you know, there's this, this diagram showing how, how Whisper and Ethereum and Swarm were intended, uh, to fit together.
[24:51] And I, I found some more timing on that was, so Swarm was envisaged by Daniel Nagy as far back as 2011.
[24:58] You know, it was a, it was a year, an idea he'd been working on for like three years before that.
[25:02] I, I spotted on the Whisper presentation that Gavin did that he, that that was a pre-Ethereum idea as well.
[25:08] So it was probably only when all of these people came together, it was like, "Well, you've got this storage idea, you've got this blockchain, kind of like CPU, database-y idea."
[25:16] Oh, and then if you have messaging, you know, all of these things can, can fit together.
[25:21] But it's always, it's also, we're going to build our own IDE as well.
[25:24] Browser, yeah, plus the Mist browser.

**SPEAKER_00:**
[25:27] The complete thing.
[25:28] It's a, it's a complete platform for decentralized applications, end to end.
[25:32] This was the big mission, and also this was what attracted me to it.
[25:35] I mean, having someone having a really broad vision of a new internet, if you want.
[25:40] That's what he called Web3.
[25:41] That's where the term comes from because it was not just a little tool, it was a complete new internet called Web3, from data to messaging to smart contract blockchains to IDE to browser.
[25:52] And this vision was very, very attractive.
[25:55] This attracted all the talent and the developers because they loved building that.

**SPEAKER_02:**
[26:00] Yeah, I mean, it's a very, very expensive vision.
[26:03] And yeah, it was, you know, Gav, as you say, you know, Web3 was him.
[26:07] Prior to that, the language I saw was really about Bitcoin with smart contracts.
[26:12] You know, that was really sort of the genesis of the talent going through that journey of colored coins and master coins and meta protocols.
[26:20] Um, and that, that kind of positioning of Bitcoin as a calculator and Ethereum's a smartphone.
[26:25] But it was all that kind of like blockchains and applications, right?
[26:29] It wasn't that full Web3 vision, which I think...
[26:31] And that really came from Gavin.

**SPEAKER_00:**
[26:32] We have to attribute this to him.
[26:34] He was having this big vision.
[26:36] This attracted also so many people.
[26:38] It attracted also even the business people.
[26:40] They could now understand what it actually is.
[26:43] Other than this was just like tech.
[26:45] Let's see.
[26:46] But this is like a broad vision of how business functions, how like this new financial world would happen.
[26:52] They could understand this far better than having this iPhone calculator comparison.
[26:57] This was maybe a nice technical thing.

**SPEAKER_02:**
[26:59] Yeah.
[27:00] Yeah.
[27:00] But then for it being a very expensive vision, that's, that's a lot of work.
[27:04] Sure.

**SPEAKER_00:**
[27:05] But I just thought somewhere.

**SPEAKER_02:**
[27:06] That's it.
[27:07] So, I mean, you know, talking about Gavin, the features.
[27:10] So, yeah, there's a ton of stuff on that, on that C++ team.
[27:14] Aleph—Aleph Zero as well, and Aleph One.
[27:16] So Aleph One being the GUI miner.
[27:19] Um, and then, I know, how would you describe Aleph Zero?

**SPEAKER_00:**
[27:22] Kind of the first interface to the blockchain in some way, like the first graphical interface to a blockchain client.
[27:29] And what could it do?
[27:31] Of course, it could mine.
[27:32] You could deploy a smart contract.
[27:35] You could visit, make it visible somewhat what's happening there.
[27:39] It was not really end user friendly in any way, but it was just a replacement of what people just do on the command line.
[27:46] Usually command line, when your client has some input, has some output.
[27:49] And it was the first kind of graphical user interface, graphical user interface replacing the command line.

**SPEAKER_02:**
[27:55] I guess it's sort of like a combination of like what you have with the block explorer now, apart from that's, that's like a view only and this was both a view and a, and a do.
[28:04] Um, yeah.
[28:06] But yeah, those GUI clients.

**SPEAKER_00:**
[28:07] But much more influential than the Mist browser.
[28:10] The Mist browser, I think there's a video by Alex van de Sande.
[28:14] It's like a 10-minute video on YouTube.
[28:16] They had this prototype.
[28:17] They were not working yet, but just fake it 'til you make it.
[28:21] The vision of the Mist browser.
[28:23] And this also really made us understand how Ethereum could work for the end user.
[28:28] Having different identities connected to wallets, and you would load those dapps.
[28:33] Is it an IPFS hash or even over Swarm one day, the app was loading and you could do some finance stuff there.
[28:40] This gave us an idea of what Ethereum could be.
[28:43] It was, so you have to think Vitalik gave us a rather technical vision and broad intellectual thing, but Gavin gave us this broad internet vision.
[28:51] Alex van de Sande gave us this very concrete thing what an end user could do with that in the next six to 12 months, maybe.
[28:57] It was very important.

**SPEAKER_02:**
[28:58] Just yesterday, actually.
[29:00] So there was an announcement from Uniswap about them sort of turning on fees and doing various things that are more kind of to do with, you know, the company and the protocol tying together.
[29:09] And I saw a reaction to that saying, you know, "Well, I'm never going to, you know, I'm never going to use this again.
[29:14] You know, you can't like know, extract ongoing revenue out of a protocol."
[29:18] And, and this person then said, um, "It's time for Mist 2.
[29:22] Totally, we need the full vision so that you've got hosted and the apps and you don't need a server and you don't need a company and you can just make this pure, uh, you know, immutable smart contract wrapped in a UI that's, that's all decentralized."
[29:35] You think we could have a Mist 2?

**SPEAKER_00:**
[29:37] I would love to see this.
[29:38] I heard people thinking about this before.
[29:40] I don't know if anybody really started the project, but...

**SPEAKER_01:**
[29:43] Should be totally doable today.
[29:44] It's not rocket science, you know.
[29:46] Um, let me interject.
[29:47] We ourselves have made sort of different attempts at this where like you just download the app from the chain itself, pretty much.
[29:53] Um, it worked fine.
[29:55] And I guess it just wasn't as much a differentiator.
[29:57] Like it made things a little slower, uh, to do it this way all the time.
[30:02] I also think like one of the people that took the Web3, the world computer vision sort of seriously was like the Internet Computer people.
[30:09] And I don't know anyone that uses Internet Computer, but like every once in a while I see tweets about it and I'm like, that sounds great.
[30:15] Yeah, start the app from the chain.
[30:17] You know, it's got some cool like smart contracting language in it.

UNKNOWN:
[30:20] Yeah.

**SPEAKER_01:**
[30:21] I guess there's just no demand if it like slows the app down even slightly.
[30:25] Um, and I think MetaMask and then many other wallets were sort of enough.
[30:29] Still not, um, the whole thing, but, but yeah, I guess it's like you got to get people to use it if you want it to be maximally cypherpunk too.

**SPEAKER_00:**
[30:35] I fully agree, and I mean, yeah.
[30:37] The problem with this is you only need it if you really need it.
[30:41] Meaning if Uniswap failed, the interface is not there.
[30:44] It's like a backup.
[30:45] It's not what you want to use daily.
[30:47] And if you remember, like in your view, when they presented MetaMask, my first thought was, "Oh, this is totally away from the vision."
[30:54] Like, how can you not run a full node?
[30:57] How can you dare to just serve over RPC with Infura?
[31:01] Like, almost not a scam, but it was like not what we intended to build.
[31:05] Today, it's like this is the decentralized version of it.
[31:08] This is like non-custodial.
[31:10] MetaMask are the good guys compared to all the others.
[31:14] Like, see how, like, the view shifted over the years.
[31:17] Like, then it was absolutely required to run a full node with the Mist browser.
[31:21] This is how it's done.
[31:22] And now we have MetaMask plus Infura.
[31:25] And today, this is really the version which is viewed as the original non-custodial Ethereum vision.
[31:31] How things are shifting, basically.
[31:33] But yes, you only need those things if things are falling apart.
[31:37] Just as an example, so many people use the Gnosis Safe.
[31:40] Let's say the Gnosis Safe UI is gone.
[31:43] Technically, it shouldn't be a problem to run another one, but it really needs to be something on IPFS.
[31:48] It needs to be something which can self-host so I can still access my wallet without going to the command line.
[31:54] So for those reasons, you need it.
[31:55] And the Mist browser was sort of as the fallback for every dapp.
[31:59] Like, of course, you can have your application run on a normal .com domain on AWS, fine.
[32:05] But if you could serve the same app in a decentralized fashion as a backup, this would be great because you could still use it if the company, say Uniswap, the company fails.
[32:15] If someone builds a nice Uniswap UI served by IPFS, directly interacting with the smart contracts.

**SPEAKER_01:**
[32:21] Yeah, that's fair.
[32:22] Also, Uniswap, I think, is controversial.
[32:25] I know Jim wanted to say something.
[32:26] Controversial because they had the company-level fee skim, and then I think they've turned the on-chain fee on.
[32:32] I don't know that they've turned the company fee off.
[32:34] I haven't read that detail.

**SPEAKER_02:**
[32:36] I believe so, because one of the replies was saying, "Okay, so how are your shareholders going to like that?"

**SPEAKER_01:**
[32:41] Yeah, okay, fair enough.
[32:42] Well, hopefully they hold a bunch of the UNI and it will mark to the market.

**SPEAKER_02:**
[32:46] They're doing a bunch of burn, so that should be to the benefit of all stakeholders.
[32:50] But yeah, just sort of this interesting kind of contrast, right, between completely immutable, you know, force of nature smart contracts versus, you know, more permissioned, more tied to a company, more sort of like wanting to have fees for maintenance kind of question.
[33:07] I mean, it's like treasuries, I guess.

**SPEAKER_00:**
[33:09] But this opens up the questions.
[33:10] How should an Ethereum app be built economically?
[33:13] And this is also a question being answered during that time.
[33:16] This was being the DAO was one approach of it should be fully on-chain.
[33:20] All the revenue should be on-chain.
[33:22] It should be no for-profit entity directly attached to it.
[33:26] And Slock.it, the company I built after that, would be a service provider for them, getting paid by them for work being done for the DAO, one version.
[33:34] I was always skeptical and still am about companies where you have effectively two cap tables, meaning you have a token cap table, if you want.
[33:43] Of course, it's a utility token, governance token, and so on.
[33:46] But effectively, it's kind of ownership in the protocol.
[33:49] And then you have a for-profit company with shareholders.
[33:53] And this is always, I think, very dangerous because you don't know where it's going to go.
[33:57] Where's the value?
[33:58] On the shares of the company or on the token?
[34:01] This was the main reason all those companies had those nonprofit foundations in Switzerland.
[34:06] Rightfully so, because they said, you only want to have one cap table, like the Ethereum Foundation.
[34:11] There were no shareholders of Ethereum.
[34:13] There was a nonprofit foundation and a token.
[34:16] The token, if you want to have a share in the economic success of the protocol, you would buy Ether.
[34:21] And so later on, there were many other token projects where they had a non-profit foundation, so no shareholders, no second cap table.
[34:29] And then you would have only the token and all the value would be there.
[34:32] And now with Uniswap, you have this problem of having again shareholders and tokens.
[34:36] And I think that's dangerous and not a good idea, actually.

**SPEAKER_02:**
[34:40] Yeah, yeah.
[34:41] So perhaps let's talk about Devcon, actually, just before we get to Devcon 1.
[34:46] So the launch.

**SPEAKER_00:**
[34:47] Right.

**SPEAKER_02:**
[34:48] So obviously, a lot of testing and coordination and this different series of proof of concepts.
[34:53] So I mean, how did you know it was good enough?
[34:56] Like, what was that testing flow and collaboration like?

**SPEAKER_00:**
[35:00] There are many indicators.
[35:01] One being the Olympic testnet running smoothly for a while.
[35:04] Other one where the C++ client having an audit which worked.
[35:08] Um, and then they were saying, "Okay, now if Christoph doesn't find any failing tests for like three weeks or four weeks or something, we are ready."
[35:15] And this was the case.
[35:17] And so we said that we can set a launch date.
[35:19] And the launch itself, it's also a bit typically—typically Gavin or also Vitalik—nobody wanted to push a button.
[35:26] Like nobody just like, "start the chain."
[35:28] So what was done was there was a script written which has as an input parameter the hash of the Olympic testnet at a certain block height.
[35:36] So everybody could, using this script plus the software, plus C++ or Go client, of course, having plus the hash, which was at that time in the future of the Olympic testnet, start that chain.
[35:50] So there was no, at launch day, we were just viewing it.
[35:53] There was nothing to be done.
[35:54] It was like, everything was, all the information was out there.
[35:58] People were just simultaneously starting the blockchain.
[36:02] And then over the peer-to-peer network—this was actually the more harder stuff—they found themselves on Reddit and others to share IP addresses, like, "connect to my peer, connect to my peer."
[36:12] And so then they started to come together.
[36:14] And of course, the longest chain was the valid one.
[36:16] So as soon as you found a peer which had their own chain, you would say, "Yes, this is the longer one."
[36:20] You would stop and start mining on top of his chain.
[36:23] And so basically the canonical chain emerged from that within, I don't know, 30 minutes or one hour.
[36:29] And then we had the chain running.
[36:30] And this was, uh, like a beauty to behold.
[36:33] Like to just see how this works out as intended, completely decentralized.
[36:37] Nobody did have to do anything.
[36:38] It was just, I was in the C++ Berlin office in Kreuzberg 37a with a nice office, and we just watched it.
[36:47] And we were somewhere mining there with a laptop.
[36:50] And we were all excited as it started.
[36:52] I actually think two or three weeks after, or maybe four, we had the first little hard fork, meaning there was some smart contract doing something that Geth and C++ had a different result.
[37:03] It was, for me, almost the middle of the night at 10 p.m.
[37:06] or 11 p.m.
[37:07] So I remember seeing this, looking for one hour or so, finding what's the issue.
[37:12] Then I found it, wrote a test about it.
[37:14] C++ was right.
[37:15] Geth was wrong.
[37:17] So we gave it to Jeff.
[37:18] They fixed this.
[37:19] I think we said one hour and like after five hours, everything was done.
[37:23] It was a basic call that the miners, "Please update your client."
[37:26] Um, so, and then it was fine.
[37:28] So this was the early days, but it was a successful launch.

**SPEAKER_02:**
[37:31] Nevertheless, did the Haskell client sync at Genesis?
[37:34] I do not know, Jim.

**SPEAKER_04:**
[37:36] No, we were able to sync at Genesis time for like a year or so, we were syncing.
[37:41] But I remember like that week, Kieran and I were like more interested in trying to get a miner in place.
[37:47] So that was what that week looked like for us.

**SPEAKER_01:**
[37:50] Yeah, I was living in an apartment just south of Berkeley campus at this time.
[37:54] And Jim had taken me to Fry's to build a machine a few months prior, like a build machine.
[37:59] It had a good GPU in it.

**SPEAKER_04:**
[38:00] Yeah, Fry's is dead now.

**SPEAKER_01:**
[38:02] RIP.
[38:03] So I was running a miner there, and we built a couple in Jim's garage.
[38:07] It got very hot in Jim's garage, which was, you know, those things were consuming a fair bit of power.
[38:12] Mine exploded after a few weeks.
[38:14] It was actually just the power supply.
[38:16] So I thought the whole machine was bricked, and Jim said, "You know, I think everything but the power supply will be okay."
[38:21] And it was the case that everything but the power supply was okay, but then I stopped mining.
[38:25] And I think Jim would shut it.

**SPEAKER_04:**
[38:26] We didn't even bother to buy cases at that time.

**SPEAKER_01:**
[38:28] Right.
[38:28] Yeah.

**SPEAKER_04:**
[38:29] You may have had a case.
[38:30] I had mine just sitting wires out.

UNKNOWN:
[38:32] Yeah.
[38:32] Yeah.
[38:33] Indeed.

**SPEAKER_01:**
[38:34] Sure.
[38:35] At that time, we were always, you know, sort of, at least at that time, short-handed people-wise.
[38:40] So it was catching up a little bit on the features, et cetera.
[38:43] But it ran perfectly well.

**SPEAKER_00:**
[38:44] There was always new features coming.
[38:46] I remember, it was like we, one of the sweet memories during the pre-launch, sitting together with Gavin, Vitalik, Jeffrey, and me in one room at the C++ office, like the nice Gavin office.
[38:57] He had this 80s style thing.
[38:59] And we think, okay, what was wrong in our protocol?
[39:02] Then they discussed on the whiteboard changes.
[39:04] Then the first day, "Okay, Christoph, you write a test for this protocol change."
[39:08] Then we are, at the same time, we are coding it.
[39:10] Then, "Okay, you're done creating a test.
[39:12] Let's see if they all pass it."
[39:13] If they all pass it, it's like done.
[39:15] New feature, direct new release.
[39:17] And so this was done with all the other clients.
[39:19] So they basically had to catch up.
[39:21] It was like information, update of the yellow paper, here's a new test, here's like a little Etherpad description of what the new protocol looks like, and then, "Please update your clients."

**SPEAKER_04:**
[39:28] But the yellow paper got me to a certain point.
[39:31] Sorry.
[39:32] The yellow paper always got me to a certain point, but it was always behind the other clients.
[39:36] So I would always find out that I was behind because I went in the morning and connected to the testnet and I was no longer connecting or I was getting some state mismatch or something.
[39:45] And then I'd have to go and dig through, usually the C++ client.
[39:49] I think there was maybe one or two times where I can't remember why.
[39:53] I think there was one or two things that went to Geth first, but usually it was C++.
[39:57] And I'd have to go digging through the newest code to find the changes and then bring them in.
[40:02] And then a few weeks later, I'd see it in the yellow paper.

**SPEAKER_02:**
[40:05] Yeah.
[40:05] Yeah, so unlike, unlike what you have now where leading into a hard fork, you know, you've got all that discussion and specking up front and like, yeah, applying the code into the clients, but only enabled for a testnet and going through that dance and then ready to go.
[40:18] Yeah, I mean, at that point, as you say, it's, it's kind of like done in those clients first and then back later.

**SPEAKER_04:**
[40:23] It looked like from where I was standing, it looked like there was a lot of competition between the different clients and the developers there.
[40:29] And, and I think they sort of like took pride in having the new thing in as fast as possible.
[40:34] And so that sort of led to an environment maybe where there was not, not as much discussion.
[40:38] It was like, "I'm gonna throw it in and then I get the bragging rights."

**SPEAKER_00:**
[40:41] There was always a fight between the Geth and C++ team about who's the best.
[40:46] And Gavin was having a big ego.
[40:48] And Jeff was more like, "Just give me the new spec.
[40:50] I just code it."
[40:51] But yeah, it was more or less this decision by the three of them.
[40:55] I was basically not playing a very major role.
[40:57] I was in the room and then writing a test for it.
[40:59] But they discussed it.
[41:00] After it was cleared, they just did it.
[41:02] But it was pre-launch.
[41:04] After launch, of course, this was different.

**SPEAKER_02:**
[41:06] Saying about having...
[41:07] Sorry, go on, Jim.

**SPEAKER_04:**
[41:08] Oh, I was just going to say, like, I know, like, a lot of the changes were just, like, some change in the EVM or pricing or something.
[41:15] And so often it was, like, you know, I would, like, freak out in the morning when I wasn't working.
[41:19] But then, like, by 11 o'clock or, you know, a.m., I had found, like, oh, I see, like, such and such opcode just doubled in price or something.
[41:27] So I would just put that in.
[41:28] But the big one was RLPx, which is essentially, like, a big SSL replacement.
[41:34] And that one was like freaking me out for a couple of weeks.
[41:37] I was like digging around, trying to find any information about that.
[41:40] Eventually, I had to reverse engineer.
[41:42] Maybe that was the one that was in Geth first.
[41:44] I can't remember.
[41:45] But I had to sit there and reverse engineer.
[41:47] I had to run either C++ or Geth and then put lots of logging information in to see what in the world was happening and then print out all the stuff and then find the appropriate crypto libraries to mimic that.
[41:58] What was the background on that and how it went in so quickly?

**SPEAKER_00:**
[42:01] Like there was nothing in the yellow paper about that at all.
[42:03] And when that came in, it was just a shock to me.
[42:05] Just do you know which time this came?
[42:07] Because I was focusing on the Ethereum Virtual Machine at the time.
[42:10] This was more like, okay, I know Gavin—I think it was Gavin doing some optimization.
[42:14] He was always thinking about the long term.
[42:16] So if something would be 10% more efficient, you have to do this right.
[42:19] I think, um...

**SPEAKER_01:**
[42:20] I remember like there was a DevP2P, libp2p website that was released about that time.
[42:26] It still might have been after the giant change went in.
[42:28] So I also, we were working together regularly, you know, in the Bay Area at this time.
[42:32] And I think so Jim did like 96% of the changeover, but we had, uh, at the time, like separate processes.
[42:39] One was more like a client and one was more like a server.
[42:41] We merged them later.
[42:43] Um, and yeah, it was like, so there was a big document, one describing like how the DHT for peer discovery would go in.
[42:51] But then you needed like a way to identify the peers, maybe.
[42:55] And this system kind of gave them an identity with like a, you know, in a SSL style, like basically there was like a node cert in effect.
[43:03] And then you had to like, there were session keys and, you know, this, that, and the other.
[43:07] It was, it took a long time to, to implement that thing.

**SPEAKER_02:**
[43:10] Um, but yeah, I think, um, maybe, Bob, you would know that.
[43:13] I think this was someone else wrote this big thing.
[43:15] This might have been Alex.
[43:16] Yeah, it was, uh, Alex did, did that.
[43:18] Um, so saying about sort of documentation or whatever, there was a wiki, right?
[43:22] It was an Ethereum wiki, and a number of things were documented only on the wiki.
[43:26] Um, and I think these, these kind of wire protocol pieces were, were part of that.
[43:30] But yeah, Alex Leverington was the first hire into that Berlin office.
[43:34] Um, and he primarily, I mean, he worked on a few different C++ things, uh, but the main thing he's known for is, is DevP2P, which was that, that common underlying peer-to-peer protocol.
[43:45] Though you already had libp2p, which is the transport for IPFS, that already existed at the time.
[43:50] So there was a bit of not-invented-here going on.
[43:53] Um, but, but yeah, he, uh, he was there for, for Devcon Zero as well.

**SPEAKER_00:**
[43:58] I do remember Alex.
[43:59] I was not too much into the peer-to-peer side of the codebase.
[44:02] I was more into the EVM and Solidity, smart contract side.

**SPEAKER_02:**
[44:06] I tell you what, there was a bit of funny crossover with the later part of, uh, of, of yours was Alex Leverington, uh, worked with John Lilic on a project called Airlock.

**SPEAKER_00:**
[44:17] So I remember that.
[44:18] I saw it later, like after we did our presentation and had the Slock.it stuff going.
[44:23] They showed us videos of it very earlier than us.
[44:26] So yes, they were actually time-wise, they did this before we did, but I did not know about it at all.
[44:31] And so we did it more or less in parallel then.
[44:34] And we just launched a bit quicker, like to go to the public with the project.
[44:37] It has been from their side, it was more like a little side project.
[44:40] It looked like a big company or intended to be.

**SPEAKER_02:**
[44:42] Yeah, I remember this project.
[44:44] Yeah, so I think that was, that was at the hackathon at the Bitcoin Expo in, uh, April, uh, 2014 that, that they, uh, did that.
[44:52] And Stefan actually did an interview with them.
[44:54] You can see that on YouTube.
[44:55] You know, this is like talking about early Ethereum projects.
[44:59] You know, and this is like over a year before the mainnet.
[45:01] It's like so far back some of these.
[45:03] Um, but, uh, but yeah, like some of that spec stuff was, it was not in the yellow paper and it was just sort of floating around and a long time before there was real consolidation of that full client spec.
[45:12] But you managed to do it anyway, Jim.
[45:14] You managed to build the client.

**SPEAKER_04:**
[45:15] It was a busy week.
[45:17] But it was just notable to me because at least from what I was seeing, it went from zero to one overnight.
[45:22] I had never heard of it the night before, and then the next morning it was in the clients and working, and I couldn't connect to anything.

**SPEAKER_01:**
[45:29] Which is normally the pattern, but yeah, just this one was like the biggest one-time change that I can recall either.

**SPEAKER_00:**
[45:34] Yeah, yeah.
[45:35] Again, this was pre-launch days.
[45:37] Things had to move fast.
[45:39] There was a lot of pressure going around.
[45:41] It was messy.
[45:42] There was not much coordination between the clients, except for maybe some Skype groups.
[45:47] And in the end, yes, Vitalik, Gavin, and Jeff just made decisions and executed as quick as they could.
[45:53] So this all changed after launch.
[45:55] Then things became a bit slowed down and people consolidated and every change was a big thing, rightfully so.
[46:01] Um, yeah.

**SPEAKER_02:**
[46:02] Yeah, so back on the timeline, um, so it was July 2015, uh, that mainnet launched, uh, with the Frontier hard fork.
[46:11] Um, and then as you touched on, um, you had Ming.
[46:15] So Ming's first official day was the 1st of August 2015, at which point the foundation had been running on for a year or so and was close to out of money.
[46:25] Touching on your thinking it would only last for a certain amount of time, a year on, that raise, which I think was around $16 or perhaps $18 million, was nearly all gone.
[46:35] So you have these quite hard decisions about what...

**SPEAKER_00:**
[46:37] which part of this grand vision was, was going to be funded initially, right?
[46:42] And I remember talking to her at the time.
[46:44] She felt like, "I have to clean up the whole mess."
[46:46] Like the paperwork and everything was totally messy.
[46:49] Working with lawyers, accountants, and so on, and getting clean up, basically, of the foundation.
[46:54] I mean, for me, I did expect it to last something like that.
[46:57] So it was for me, it was clear they are not making any money.
[47:00] Um, I didn't know like how big the reserve was in detail.
[47:03] I think it was like, I don't know, 5% something in this range, like how much ETH the foundation holds.
[47:08] At the time, there wasn't that much value either, a price like 50 cents, one euro, or something.
[47:12] So it was clear this would not last forever.
[47:14] So I was thinking about going back to my PhD, or then I came across this idea about Slock.it and becoming at building a company.
[47:22] And Slock.it was the idea of, maybe similar to Airlock, smart contracts are essentially permission systems.
[47:29] 90% of a smart contract is who's allowed to do what.
[47:33] In case of the ERC-20, it's just who's allowed to send the token or setting an allowance.
[47:38] And in terms of the DAO, it's who can vote for what and making decisions, and then money gets sent out.
[47:43] So what if we could put this permission system into IoT?
[47:48] And who's allowed to switch on, off, use, change, admin rights, whatever.
[47:53] You put this into a smart contract.
[47:55] And I thought that Ether will never become a currency.
[47:58] Bitcoin was a digital currency.
[48:00] And actually, if you talk to Ethereum people at the time, we were not thinking about competing with Bitcoin.
[48:05] Bitcoin was a digital currency.
[48:06] We were building a platform for decentralized applications.
[48:09] Ether was just used to run it.
[48:11] I once heard the statement somewhere on Twitter where someone said, "Um, Bitcoin is a currency which needs a blockchain to function, and Ethereum is a blockchain that needs a currency to function."
[48:21] Uh, this is, I think it's very true.
[48:23] And so back, I thought, okay, Ethereum will not be used as a currency, but it might be used as a currency for IoT devices.
[48:30] So instead of the Internet of Things, building the economy of things.
[48:34] And this is kind of what drove us.
[48:36] And then we wanted to build this universal sharing network as an application.
[48:40] At the time, Uber and Airbnb just became big.
[48:43] We thought, well, all those sharing economy services should run on-chain.
[48:47] So let's build this called the universal sharing network.
[48:50] And then we thought about how to start with something tangible.
[48:53] And then we had this door lock.
[48:55] Actually, it's here in the background.
[48:56] If you see it, it's there.
[48:59] I have this Devcon One, um, physical smart lock, which we connected to the Ethereum blockchain using our own software.
[49:06] And we had this idea of people pay to open the lock.
[49:09] And that's what we presented at Devcon One, together with this idea, which actually only came up like three or four days earlier, to connect this with a DAO.
[49:18] And the rest, you know, is history, what happened after that.
[49:21] But we didn't intend and we didn't start Slock.it for building a DAO.
[49:25] We wanted to build the universal sharing network.
[49:27] Then we thought, well, this is way too big for us.
[49:29] We want to now focus on this Airbnb use case for door locks.
[49:33] And then we thought about fundraising.
[49:35] We talked to a bunch of VCs.
[49:37] I actually remember flying to New York, talking to VCs there.
[49:40] Everybody said no.
[49:42] Then I met Joseph Lubin.
[49:44] He said, "Yes, maybe under some conditions."
[49:46] We just did not agree on the terms in detail then.
[49:49] But I was presenting at the Bitcoin meetup in New York.
[49:53] And they all, like, the first application was a Bitcoin application about arbitrage trading.
[49:58] It was like kind of boring.
[50:00] And then I came with a door lock.
[50:01] It was like super fascinating.
[50:03] You could open the door by paying some Ether.
[50:05] So it went well, but we didn't have any money.
[50:07] So we thought about doing something like an ICO, but this was now after the launch of Ethereum.
[50:12] So if I started coding an ICO-like smart contract, why should we have the money directly?
[50:18] It could stay in the contract and then people could vote for giving us part of it.
[50:22] Then we said, "Well, we could make proposals to it and then they can vote if the proposal is good or not good."
[50:27] Then the money would be released to us.
[50:29] Then they think, "Why could not everybody make a proposal?"
[50:32] Like everybody could pay in, everybody can make a proposal.
[50:35] And so it's completely open, and we are just one of many service providers to the DAO building this universal sharing network.
[50:41] And this was the origin of the DAO.
[50:43] And only like again, three days before Devcon One, we actually decided we would go for it and put it into the presentation.

**SPEAKER_02:**
[50:49] Yeah, amazing.
[50:50] I mean, so on the timeline again, trying to judge it.
[50:53] So Stefan was, I guess, Chief Communications Officer or community, um, until September of 2015.
[51:00] That's when, when he left.
[51:02] Had you, had you left already by then?
[51:04] Can you remember?

**SPEAKER_00:**
[51:05] No, I didn't really leave because I was technically a freelancer, although I was working full time for it.
[51:10] I didn't have like a formal employment contract.
[51:13] So I was continuing to work, I think, until the end of the year.
[51:16] And then I just, well, I just put down my hours.
[51:18] Basically, if you need me, tell me.
[51:20] I just invoice what I'm doing.
[51:22] But I was really leaving actually in December, January.
[51:25] I think the last invoice was for December.
[51:27] And when Stefan Tual left or was being left, there's another conversation how he left the foundation.
[51:33] He didn't agree with some people getting Ether, which is another story for another day, I guess.
[51:38] But he was really a crucial part in building up this Ethereum community.
[51:42] Like all this meetup culture.
[51:44] The meetup culture didn't really exist like that before.
[51:47] He was going from place to place, finding someone running meetups.
[51:50] So he was very important for that.
[51:52] And I know I was a coder.
[51:54] I, plus Simon, who I co-founded Slock.it with, was also a coder.
[51:58] We needed someone who can talk to the people, can do marketing and this stuff.
[52:02] And we said, well, he has the right address book.
[52:04] He knows the right people.
[52:06] Everybody knows him in the community.
[52:08] I think let's ask him if he wants to join us.
[52:10] And he did.
[52:11] And I think he was a very important part of making the DAO what it was.
[52:15] Later on, he did some messages, which I also didn't like.
[52:18] And so he was a bit in disgrace for what happened then.
[52:21] And I think the community was very, very hard with him because he was not always reacting maybe as he should in some situations after the hack.
[52:28] But nevertheless, he played a very important part in the history of Ethereum and also, of course, of the DAO.

**SPEAKER_02:**
[52:33] And, and so, so Devcon was November 2015.
[52:37] So that was announced earlier in the year, I think, I think September-ish, um, but ended up being cancelled, you know, because the, the foundation were basically, you know, the same making out money piece.
[52:47] Uh, but then primarily with ConsenSys funding and support, uh, you know, hey, it's back on.
[52:53] Um, so that was in, that was in London.
[52:55] Um, and you know, significantly larger, uh, event, obviously, than Devcon Zero because it was the first, you know, public Ethereum outing with Microsoft as a headline sponsor.
[53:07] You had Nick Szabo speaking as well.
[53:09] Maybe Satoshi, maybe not Satoshi.
[53:11] I don't think he said that.

**SPEAKER_01:**
[53:12] He strongly alluded to it in the presentation.
[53:15] It was funny.

**SPEAKER_02:**
[53:16] So, yeah, how was that for you then, Christoph?
[53:18] What was, you know...

**SPEAKER_00:**
[53:19] It was totally different than Devcon Zero because this felt like now we're going out in the world and show it to the public.
[53:25] It was a fancy space in London.
[53:28] It was a really fancy, almost cathedral-looking space to present.
[53:32] Again, we had Vitalik and Gavin talking about the vision of Ethereum.
[53:36] And if you look at the talks being given, I really think entrepreneurs today should just re-watch them because they all have been 10 years too early.
[53:45] Be it about uPort building an identity solution.
[53:48] I think it was Boardroom doing that governance on-chain.
[53:51] Many, many ConsenSys startups, of course.
[53:54] We as Slock.it were thinking about, well, let's connect IoT to blockchain.
[53:58] Again, all of that 10 years too early.
[54:01] I remember also Simon speaking about everybody getting a token.
[54:07] He really predicted this token economy would now thrive, which happened.
[54:11] So it was a great place to be.
[54:13] Everybody was looking into the future, building the future.
[54:16] It was very, very exciting.
[54:18] It was very important that ConsenSys was funding this.
[54:20] It was crucial, this Devcon 1 moment showing Ethereum is live now.
[54:25] We show you what we will build with it.
[54:27] But still, there were no applications running.
[54:29] It was all visions and thinking.
[54:32] And so there's one reason why when we then did the DAO, the DAO was held like almost the first real thing you could do with Ethereum.
[54:39] That's why so many people jumped onto it.
[54:41] And then maybe just finishing this off, the narrative changed.
[54:45] It was not anymore a DAO for the universal sharing network, but maybe because of the curators we chose, which were like important figures in the Ethereum space and many other things, it turned into like an investment fund or like an index fund for Ethereum applications.
[55:01] Because now after 20, 30, 40 million was in, it was clear this was not just money for Slock.it and the USN.
[55:08] This was money for more cases and more people applied for it.
[55:12] It became like every decentralized application, or many of them, not everyone, they were saying, "I'm applying for getting funding from the DAO."
[55:19] So the DAO would pump all the applications.
[55:22] So it's like you invested in Bitcoin 10 years, five years ago, became rich.
[55:26] Now you invest into Ether, went well.
[55:28] And now you can invest in the application layer.
[55:31] You do that through putting money into the DAO.
[55:33] This was not a story we told, not how we intended it, but that's how the narrative changed during the fundraising and then became that big.

**SPEAKER_02:**
[55:41] Yeah, I mean, it was interesting you saying that.
[55:42] You did, but I cannot hear you.

**SPEAKER_00:**
[55:44] Maybe it's, maybe it's just me.
[55:46] Can you hear me?
[55:47] I mean, I am, sorry.
[55:48] I have an issue here with my...

**SPEAKER_02:**
[55:49] Do you?

**SPEAKER_00:**
[55:51] This is me.
[55:52] So now I'm back.

**SPEAKER_02:**
[55:53] Can you hear me?
[55:54] Can you hear me, Christoph?

**SPEAKER_00:**
[55:55] No, I have to switch back to, um, let's.
[55:58] Can you hear me now?
[55:59] Yeah, I can hear you.
[55:59] I could always hear you for some reason.
[01:00:00] Oh, we've heard you anymore.
[01:00:02] This was like me an hour ago, by the way.
[01:00:03] StreamYard.
[01:00:04] Okay, my audio is completely broken.
[01:00:06] So I will try to fix this.
[01:00:07] We can continue.

**SPEAKER_04:**
[01:00:08] I basically had to close it and come back again with my earphones, but I don't know.

**SPEAKER_02:**
[01:00:12] Perhaps while we're waiting, Kieran and Jim, you could talk a little bit about the Strato launch.

**SPEAKER_04:**
[01:00:17] I thought you were going to say you could sing a little song.
[01:00:19] I got nervous for a second there.

**SPEAKER_01:**
[01:00:21] You know, okay, so in this period of time, we were just reconnect.

**SPEAKER_00:**
[01:00:24] Just turn off and on again.

**SPEAKER_01:**
[01:00:26] We were working as part of ConsenSys.
[01:00:28] And one of the kind of marketing business development people at the time, Andrew Keys, primarily had put together a partnership with Microsoft.
[01:00:36] I don't know if they ended up co-sponsoring Devcon One per se, but their headline...
[01:00:41] Yeah, they, so they put money in for that because they also like, uh, paid for a bunch of PR and all those sort of things too.
[01:00:48] Um, and so we had maybe a month or two lead time to work with them.
[01:00:52] Um, and so the idea was that we, you know, they've got cloud infrastructure.
[01:00:57] It's a good place to run blockchain nodes.
[01:00:59] They also have corporate clients that were actually very interested in the technology.
[01:01:03] And, um, so we worked with, um, pretty closely with them in the run-up to make our software available on the Azure cloud, as did Roman of the Java client, which to some extent was everyone's preference because people know Java in the enterprise world.
[01:01:19] But I think they, we sort of stuck with it quite a bit longer than Roman did.
[01:01:25] And you know, so "Blockchain as a Service" was the big announcement.
[01:01:28] Was this December 2015?
[01:01:30] There was, November, was it November?
[01:01:31] It must have been December.
[01:01:32] No, November.
[01:01:33] Uh, there was a, once the announcement happened, there's a little tick in the Microsoft stock price, which we were like, "Whoa."
[01:01:40] Like there's a little, little bump there.
[01:01:42] Um, and a lot of excitement for sure.
[01:01:45] Got a million phone calls after that.
[01:01:47] That was like a good feeling of being the hotness that only happens so many times in someone's life.
[01:01:52] But tremendous interest on the back of the blockchain as a service announcement.
[01:01:57] We did a live demo.
[01:01:58] It was fun.
[01:01:59] The internet gets in vogue to make fun of the UK these days on X, etc.
[01:02:05] The internet in the conference facility was not so good.
[01:02:08] So I was very worried about the transactions actually going through.
[01:02:11] But they did during the live demo.
[01:02:13] I think there's footage of it somewhere.

**SPEAKER_02:**
[01:02:14] Can you hear us again now, Christoph?

**SPEAKER_00:**
[01:02:16] Yes, I can hear you.
[01:02:17] I hope you can hear me too.

**SPEAKER_02:**
[01:02:19] Okay.
[01:02:19] So the demo that you did at Devcon 1, again, another iconic event, um, because yeah, you, you have that physical smart lock just sitting there on your, on your shelf.
[01:02:30] And you know, it rotates, right?
[01:02:31] You know, right?
[01:02:32] You did your transaction.

**SPEAKER_00:**
[01:02:33] We just had a Raspberry Pi connected via, I think it was Zigbee or Z-Wave back then, to the door lock.
[01:02:40] And on the Raspberry Pi, we had actually an Ethereum client running.
[01:02:44] And we had a smart contract on-chain where you could send some money to it, or Ether actually, and when it received some Ether, it would open up.
[01:02:51] This was basically the demo.
[01:02:53] But it was cool to see something physical, um, using Ethereum for, as I said before, the economy of things, uh, connected to IoT devices.
[01:03:02] Since most of the people in the room are still nerds and devs, they love that kind of stuff.

**SPEAKER_02:**
[01:03:07] And there was also the kettle, wasn't there?

**SPEAKER_00:**
[01:03:08] Yes, there was also a kettle.
[01:03:10] Maybe just turned a smart plug, like a power plug.
[01:01:13] We could also turn it on and off.
[01:03:14] Same protocol, same thing.
[01:03:16] So we just want to show it's not just the door lock company, because actually we're not producing those.
[01:03:20] We're just connecting existing door locks to it.
[01:03:22] We want to show this idea of the universal sharing network.
[01:03:25] Everything which you can turn on, off, or lock up and unlock could be now connected to this network.
[01:03:31] And everybody could put almost everything in there, like a washing machine.
[01:03:36] You pay for using the washing machine, or a bicycle lock.
[01:03:39] We even had padlocks connected to it.
[01:03:41] So you could have like your locker room and you have a padlock in front of it and sell whatever's in there by having someone pay to open the padlock.
[01:03:48] This was the generic idea.
[01:03:49] I mean, we got some VC money later after the, like in 2017.
[01:03:55] We built it.
[01:03:56] Nobody used it.
[01:03:57] Not just too early.
[01:03:59] It was like everything for everyone all at once.
[01:04:02] And of course, nothing for no one.
[01:04:04] It felt like the app was not great.
[01:04:06] So we failed B2C-wise.
[01:04:08] At Slock.it, we then turned into more consulting projects.
[01:04:12] We built Incubed, which was an IoT client.
[01:04:15] Made some money with that.
[01:04:16] Had about 50 people actually employed at the time.
[01:04:19] In 2019, we sold the company to Blockchains, Inc., Jeffrey Berns.
[01:04:23] Another story.

**SPEAKER_02:**
[01:04:24] Um, so I, I remember speaking, speaking to Stefan at the time.
[01:04:28] So Stefan was involved with that demo, right?
[01:04:30] It was Stefan who came up on stage to make his little cup of tea with the, with the, with the kettle there.
[01:04:35] But I remember speaking to him that he'd been concerned about what the reception for him would be like, you know, having had this, you know, parting of ways with the foundation just two months before.
[01:04:45] But he was saying it was all very, it was all very friendly and people, you know, were very excited about the project.

**SPEAKER_00:**
[01:04:50] Right.

**SPEAKER_02:**
[01:04:51] And saying actually about that IoT and pieces.
[01:04:54] So in January 2015, you had a demo that happened at the Consumer Electronics Show, CES in Vegas, which was a collaboration between IBM and Samsung.
[01:05:03] So the aforementioned Henning Diedrich, part of that.
[01:05:06] And that, that again was months before mainnet, but you had a proto-Web3 stack there, which was, I think, POC5 of Ethereum.
[01:05:14] You didn't have Whisper, you had another thing called Telehash.
[01:05:17] And you didn't have, you had BitTorrent.
[01:05:19] So there was this proto-Web3 stack there, and they had demos like a washing machine, um, buying its own detergent and scheduling its own repair.
[01:05:27] So, uh, so yeah, that, that was happening a little earlier and, uh, and yes, I mean...

**SPEAKER_00:**
[01:05:30] So Slock.it itself did a number of these different products, right?
[01:05:33] There was something with electrical charging and something to do with toll roads.
[01:05:37] Is that right?
[01:05:38] Right, we had a prototype running with RWE or innogy in Germany.
[01:05:43] They're doing like all the, a lot at a time, most of the charging stations.
[01:05:47] So this was in general, we got a lot of attention, of course, also after the DAO hack and all of that.
[01:05:53] And so that's kind of why we became a consulting company, because so many asked us, "Could we do a prototype with you?"
[01:05:58] Because there were not many Ethereum builders at the time.
[02:06:01] So we have been building on Ethereum now since one year or two years, which you could not find anybody doing this.
[02:06:07] So we were building lots of nice prototypes and some almost production stuff and always related to IoT devices connected to the blockchain.
[02:06:14] This was our core business.
[02:06:16] And on top of this, we built those prototypes.
[02:06:18] We did a lot of work for the Energy Web Foundation.
[02:02:21] I don't know if you're familiar with them.
[02:06:23] This was in Switzerland.
[02:06:24] They are kind of a fork of Ethereum focusing on all the energy use cases.
[02:06:29] We built most of their stuff in 2018, beginning of '19, until they hired their own developers.
[02:06:36] And Gavin was also part of this a while.
[02:06:38] So, yes, this was still, I mean, if you remember this time of Kieran, you say there was so much enterprise interest.
[02:06:44] Enterprise at the time were just learning, looking into this, wanted to build prototypes, not yet production stuff.
[02:06:50] Um, so, and there was a huge demand for it, for blockchain experts, for doing consulting, for going to conferences, explain to them what a blockchain is.
[02:06:58] With every tech conference, you need some blockchain talk.
[02:07:01] And this was kept basically mostly us.
[02:07:03] And they paid sometimes like 4,000 euro for a talk.
[02:07:06] Like as a company, you said, "Well, we need the money.
[02:07:08] Let's go there."
[02:07:09] So we, of course, you also have to think about us as persons.
[02:07:13] Simon and me, we didn't get any money for almost a year.
[02:07:16] Like we worked for, we were not rich people, we come from ordinary families.
[02:07:20] And we said, "Well, we can work for like three to four months without a salary.
[02:07:23] Let's like build the DAO."
[02:07:24] And then the DAO becomes big, the DAO is paying Slock.it to build it.
[02:07:28] And of course, after the hack, it was clear there will never, ever be a payment.
[02:07:32] So we made zero money out of the DAO.
[02:07:34] So we needed to start doing some work.
[02:07:36] And this was in the beginning.
[02:07:38] Let's do consulting for those large companies.
[02:07:40] This is how Slock.it began to survive.
[02:07:43] Many people said, "You can bury Slock.it after what happened.
[02:07:46] Your name is burned forever."
[02:07:48] And we decided to stay as a team.
[02:07:50] I mean, as a founder team, we owned our mistakes.
[02:07:53] Maybe we are open and transparent about it as much as we could.
[02:07:57] It was, of course, an honest mistake.
[02:07:59] We can talk for it.
[03:00:00] It could be another session just for the DAO.
[03:08:02] I mean, the DAO is a lot of topics.
[03:08:04] I just put here very shortly, just talking about it from a company perspective.
[03:08:08] And then Stefan, he was saying, well, he was trying to get VC money.
[03:08:12] Simon and I, we were doing those consulting gigs.
[03:08:14] And once we had VC money, what happened as a company was we got 2 million euros or dollars.
[03:08:20] And then we built the product, hired people for that, got more and more consulting gigs.
[03:08:25] So we always said, "Well, let's do them and just hire more people."
[03:08:28] And in the end, we had like 50 people, five or 10 doing the product and 40 people doing consulting.
[03:08:34] And then we got bought by Jeffrey Berns from Blockchains, Inc.
[03:08:38] Remember maybe at Devcon 3, I think.
[03:08:40] Four.
[03:08:41] Four in Prague, right?
[03:08:42] Wanted to build a city.
[03:08:44] I think I love the vision.
[03:08:45] He obviously had money.
[03:08:47] He wanted to build it on top of Ethereum mainnet.
[03:08:50] I was thinking about how maybe I can channel those billions into the right direction.
[03:08:54] Building is all as intended on Ethereum mainnet, which was working fine for the beginning.
[03:08:59] And then I found out once you're an entrepreneur, you never can be an employee again.
[04:09:04] And so I had to leave.
[04:09:05] But maybe actually it's too far in the future.
[04:09:08] I mean, that's one thing I think I have to say here, because you talked about Devcon 1 and we skipped a little bit Devcon 2.
[04:09:14] You said in Devcon 1, Stefan Tual was very concerned how people perceived him.
[04:09:19] And they were very gentle, forgiving, and nice to him.
[04:09:22] So he was well-received, and then he built the DAO community.
[04:09:25] I was super worried to go to Devcon 2 because this was after the DAO hack.
[04:09:30] I was like seriously thinking someone might beat me up there.
[04:09:33] I went to the corner and I almost destroyed Ethereum with this fork and so much attention to it and all the money lost for some people or the time of growth gone.
[04:09:43] It depends on how you view it.
[04:09:44] So, but when I went to Devcon 2, people were so nice and forgiving, basically hugging me when I was giving the talk there.
[04:09:51] And the only thing I didn't like was the foundation telling me I was not allowed to speak about the DAO, which was like, "I am speaking here to the Ethereum community.
[04:09:59] Well, how can I not speak about the DAO?"
[05:10:01] And so I talked about a pretty boring talk about security.
[05:10:06] And I think every second talk was about security at Devcon 2.
[05:10:09] It was just about how we get those smart contracts secure.
[05:10:12] So I gave a rather boring talk.
[05:10:14] But in the end, I just said, "Well, thank you for your understanding."
[05:10:17] And it was a hard time and so on.
[05:10:19] And they were like, some of them standing ovations, I remember becoming emotional because this was, I did not expect this.
[05:10:25] I really expected like, "Guy, you messed up Ethereum.
[05:10:28] Like, we almost lost it all."
[05:10:30] So I think this just speaks to the Ethereum community, how they treated Stefan, how they treated me, even though mistakes were made, honest mistakes at least from what I can tell.
[05:10:38] Uh, so this is such a great community of really nice people who really want to change the world, capable, and also now financially capable of really doing things.

**SPEAKER_02:**
[05:10:46] I was watching that video quite recently actually, um, and, and yeah, it was quite cut off a little bit in the end.
[05:10:52] The end is, you know, it was quite a long ovation there.
[05:10:55] And yeah, you could certainly see that emotion in you.
[05:10:58] And that's when we first met, actually, was in Shanghai for Devcon 2, I remember.
[06:11:02] Was on the sidelines there in that main conference hall.
[06:11:05] And yeah, it was lovely to see that.
[06:11:07] That's for sure.
[06:11:08] Okay.

**SPEAKER_01:**
[06:11:09] Yeah, I think good notes.
[06:11:10] Just, Bob, you, you were the one who tried to impose a hour to half, half hour to hour rule.
[06:11:15] We're at a solid 120 right here.
[06:11:17] The other time, maybe with me, you know, we've reached a, you know, a good kind of endpoint, I guess.
[06:11:21] So what, what happened after Blockchains, LLC for you then?

**SPEAKER_00:**
[06:11:25] So because of time, I keep it short.
[06:11:27] So yes, we got bought by Jeffrey Berns, Blockchains, LLC at the time.
[06:11:31] Again, the reason for this being he wanted to build a new city in the desert.
[06:11:35] He wanted to do it all on IoT, all on Ethereum from scratch as a developer dream, building from scratch on a green field on top of Ethereum with our tech.
[06:11:44] And I felt comfortable at the beginning.
[06:11:46] In the end, I felt like we need to release stuff.
[06:11:48] And there were some voices of the company which didn't want to release until like a very, very big product was done.
[06:11:53] For many reasons, that didn't happen.
[06:11:55] I don't want to get into that too much.
[06:11:56] So after two years, I left, um, Blockchains, back then it was called Inc.
[07:12:01] They made a change in their name.
[07:12:03] And I did for six months, I did really nothing.
[07:12:06] I forced myself to do nothing, which was great after so much stressful years.
[07:12:10] And then I started a venture studio called Corpus Ventures, where we tried out many different ideas.
[07:12:15] We had EM3, which was a decentralized messaging protocol; GasHawk, where you can save transaction costs on Ethereum.
[07:12:21] What else did we have?
[07:12:22] So with some domain name stuff, but we didn't get, we didn't release it at the end.
[07:12:25] But the biggest one was Tokenize.it.
[07:12:28] And this was, we being, we built something for German, for now German startups.
[07:12:32] In the end, we want to do it all over Europe.
[07:12:34] We're just tokenizing their shares and do fundraising.
[07:12:37] So in summary, it's like a Web3-based AngelList for Europe.
[07:12:43] It's the one-sentence description for Americans also to understand.
[07:12:47] AngelList, it's a great tool for business angel investing.
[07:12:50] We want to do the same for Europe, for all countries there, and build it on-chain.
[07:12:55] So tokenizing all those shares and enable private as well as public fundraising.
[08:13:00] So some call it legal ICOs, if you want, but also for private fundraising.
[08:13:04] Our customers currently, you have more than, maybe a good way to end this, you have now more than 400 investments from more than 320 business angels and more than 50 companies.
[08:13:14] Those are traditional German GmbHs raising from super conservative business angels, doing it completely on-chain.
[08:13:21] They are paying in stablecoins, getting their tokenized shares in their non-custodial wallet.
[08:13:26] They're all getting a Gnosis Safe wallet from us, using Privy for login.
[08:13:30] So we build it as intended and we get normal people to use it.
[08:13:34] For me, this is kind of a dream come true because I'm out of, I love the Web3 bubble.
[08:13:39] I love this community.
[08:13:40] I love to work inside there.
[08:13:42] But for me, Tokenize.it is a way to make this technology available where it belongs, like to startups and investors outside of our Web3 bubble.
[08:13:51] And I'm super, super happy that we could keep up those values that we have.
[08:13:55] The complete platform is non-custodial.
[08:13:57] They have their Safe on Ethereum, holding their tokens, paying with stablecoins.
[09:14:02] So I'm very happy to see this.
[09:14:04] Over the next years, we want to basically roll out this all over Europe and become, yes, the Web3-based AngelList for Europe.
[09:14:11] That's the goal.

**SPEAKER_02:**
[09:14:12] Fantastic.
[09:14:14] So hope to see you at Devcon 8.

**SPEAKER_00:**
[09:14:16] Me too.
[09:14:17] I'm looking forward to it.
[09:14:18] As of now, I don't intend any change.
[09:14:20] Stick to Ethereum.
[09:14:22] I love the community.
[09:14:23] I continue building and try to get a lot of people using it.

**SPEAKER_02:**
[09:14:26] Have you been to every Devcon?

**SPEAKER_00:**
[09:14:28] Yes.
[09:14:28] Yes, I said yes.
[09:14:29] I've been to every Devcon.
[09:14:31] The last one was actually the first one that I didn't give a talk.
[09:14:34] And I also went to every EthCC except for one that was COVID.
[09:14:38] There was some reason I couldn't come.
[09:14:40] But yes, I'm actually, I intend to continue to come to every Devcon.
[09:14:44] It's like you meet the people like Griff Green, Lefteris Karapetsas, of course, Vitalik, and many others.
[09:14:51] It's just a sweet spirit there.
[09:14:53] Nice community.
[09:14:54] Love seeing how it all grows.
[09:14:56] Listen to those exciting talks.
[09:14:58] I mean, for Tokenize.it, it's not as relevant.
[10:15:00] It's not like our customers or the tech, of course.
[10:15:03] We're just doing an ERC-20 token on Ethereum.
[10:15:05] It's super easy.
[10:15:06] It's no deep tech.
[10:15:08] Sometimes I miss doing deep tech, but, well, I just enjoy being there, seeing what all happened, and remembering those magic days.
[10:15:15] And it's like only once in a lifetime or two times in a lifetime you have this moment where everything comes together, the right time, the right place, the right people.
[10:15:23] This certainly, where those one and a half years I worked for Ethereum, are definitely the prime of my career in terms of who I worked with, what we accomplished, the impact we had on the world, and the sweet cypherpunk spirit there and what we did there.
[10:15:35] It was really great.
[10:15:37] I always sometimes get emotional thinking about this and meeting those people again at Devcon.

**SPEAKER_02:**
[10:15:42] Fantastic.
[10:15:43] Well, thank you for all your contributions to that success.

**SPEAKER_00:**
[10:15:46] Likewise.

**SPEAKER_02:**
[10:15:47] All the best.
[10:15:48] Okay.
[10:15:49] Oh, just one more.
[10:15:50] Where can we find you?

**SPEAKER_00:**
[10:15:52] You can find me usually on Twitter for the Ethereum people, Christoph Jentzsch.
[10:15:56] Of course, I have a complicated name, not many vowels in there, but you'll find it.
[11:16:00] Or, of course, on LinkedIn.
[11:16:01] Actually, for my company, I'm more active on LinkedIn, which I was never before, but that's where we get our clients and Tokenize.it.
[11:16:08] Yeah, but usually you can find me on Twitter or follow me there on LinkedIn.

**SPEAKER_02:**
[11:16:11] Excellent.
[11:16:12] Okay.
[11:16:13] Thanks so much.
[11:16:14] Have a great day.
[11:16:15] Thank you.

**SPEAKER_00:**
[11:16:16] You too.
[11:16:16] It was great talking to you.
[11:16:18] Bye.