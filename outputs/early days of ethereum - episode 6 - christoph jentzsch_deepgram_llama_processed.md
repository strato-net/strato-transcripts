**SPEAKER_00:**
[00:00] Okay. Recording is in progress.
[00:01] So hello, everybody. Today, delighted to have Christophe with us.
[00:05] We did attempt to record this Christophe and I two weeks ago, but I forgot to press the record button.
[00:10] So we spoke for an hour or so, and then it was not recorded.
[00:12] So this is round two.

**SPEAKER_01:**
[00:15] So hello, Christophe. How are you? Hi, Bob. Nice to meet you again. I'm doing good. I hope you too. Thanks for the invitation.

**SPEAKER_00:**
[00:20] Fantastic. Yeah. So Christophe and I, you know, our paths crossed for the first time way back in 2015, when I was trying to do C++ Ethereum on my smartwatch.
[00:30] This was around the time that Christophe was still at the Ethereum Foundation.
[00:35] And then I think I crossed paths with him a number of times since then.
[00:40] So, Christophe, what were you doing with your life before you found Ethereum and joined this crazy journey?

**SPEAKER_01:**
[00:45] So, in 2013, I was doing my PhD in theoretical physics, actually about self-organizing systems.
[01:00] I was studying systems which have local rules and global behavior.
[01:05] And I came across Bitcoin, which has just a small set of local rules and a global behavior as a currency.
[01:15] And the reason I came across this was I was looking for cheap GPUs, like graphic cards.
[01:20] And the Bitcoin miners were selling their GPU mining rigs to get some FPGAs and later ASICs.
[01:25] And so that's how I got into what's Bitcoin mining.
[01:30] And so I bought my first Bitcoin, got into this bubble, did read everything I could about it, and then I came across the white paper from Vitalik in early 2014, some time in January or February, in some Bitcoin forum somewhere.
[02:00] And I was already totally in love with the idea of Bitcoin being a decent currency and all the characteristics and features of it.
[02:10] And this white paper of Vitalik, I mean, if you read it again, it's almost a prophecy.
[02:15] Except for NFTs, everything's in there, from DAOs to ENS, like names as domain names and all of that.
[02:25] So, for me, it opened up this option of building applications with the same characteristics as Bitcoin, but just not a currency, but everything else.
[02:35] And so then I started reading everything about it.
[02:40] And in 2014, in the summer, I went to watch a video from Gavin Wood.
[02:50] He was somewhere in Scandinavia, some conference there, the Nordics.
[03:00] And he talked about Ethereum. I loved it.
[03:05] And he said he wanted to open up an office in Berlin, looking for C++ developers.
[03:10] I was a C++ developer. So I said, well, I want to do this.
[03:15] So I took my parental leave time, plus some vacation time, and passed my PhD for, like, three or six months, and said, I will return after I'm done.
[03:25] I thought this was just a short project because they raised money, maybe six or twelve months, then it's over.
[03:35] When I started, I thought, maybe three to six months, and then I go back to my PhD.
[03:40] So I worked there with Ethereum. This is it. Kevin Wood was great.
[03:50] It was a great time. And then I just decided to stay.
[04:00] It was so exciting.

**SPEAKER_00:**
[04:05] So, you never got to be a doctor.

**SPEAKER_01:**
[04:10] No. I'm not a doctor. I did not finish my PhD, although I only had six months left, which was kind of a pity.
[04:20] I worked, like, for three years on that.
[04:25] And, but I also had, at the time, I think four or five kids.
[04:30] And needed some money. I didn't get much money as a PhD student, so I did some software development as a side hustle, basically.
[04:40] And so, when I got this project, I said, well, let's do this for two or three months as a parent leave time, and then I can return.
[04:50] And then I decided to really interrupt my PhD.
[05:00] Is that I will maybe return one year later, because I thought the foundation would eventually run out of money, because they're not making any profits.
[05:10] They just raised donations, then they will spend them, then it's over. Then I can continue my PhD.
[05:20] That was originally the plan. Just came different.

**SPEAKER_00:**
[05:25] I mean, I guess it's never too late.

**SPEAKER_01:**
[05:30] I actually sometimes think about it, if I should return. It's just so much to learn again.
[05:40] I'm right now doing Tokenize.it. I'm basically working on tokenizing German companies.
[05:50] It works very well. So, currently, I'm not planning on getting back anytime soon.

**SPEAKER_00:**
[06:00] No. Because, I mean, famously, you had, you know, Doctor Kevin Wood and Doctor Christian as well.
[06:10] And I think, yeah, there were a couple of other PhDs as well.
[06:15] There was. Definitely.

**SPEAKER_02:**
[06:20] I also dropped out of mine. I was actually in mathematical physics too. Interesting. Similar background.

**SPEAKER_01:**
[06:30] It's actually the same. To like, theoretical physics, it's the mathematical part of physics.
[06:40] I tried very much. I did thermodynamics and statistics, mostly software development.
[06:50] It was really fun.

**SPEAKER_02:**
[07:00] Well, by the way, Jim is trying to join. I don't know if there's anything that needs happening.
[07:05] He can get some browser issue.

**SPEAKER_00:**
[07:10] Yeah. Yeah. Well, he'll pop up, and we can add him, or if he's... if he's, I'll see.
[07:15] Then, then, never mind. So, Christophe, in terms of getting hired into Ethereum Dev, and I'm sorry if I just missed it.
[07:25] So, how did that happen? Did you did you meet Gavin for a meetup, did you say?

**SPEAKER_01:**
[07:30] Yes. I actually just wrote him an email. Said, look, I would love to join with you.
[07:40] I love what you're doing. And he invited me to meet him in Kreuzberg, Berlin.
[07:50] So, which, again, is about two hours' drive from here. So I went up there, met him.
[08:00] I remember the first conversation; he was talking about all the stuff they were going to build, and said, well, what can you do?
[08:10] And I just asked him, what's, like, the most complicated stuff you have right now? Like, give me a complicated task.
[08:20] I somehow can figure it out. So he talked about the Ethereum Virtual Machine, which did some testing.
[08:30] So I just picked working on testing the Ethereum Virtual Machine, or, like, writing tests for it.
[08:40] Back at the time, I actually had no real idea what he was talking about, meaning, of course, I did understand on the white paper level.
[08:50] I did understand what Ethereum was about. But Gavin had this skill of writing the Yellow Paper, which is still incredible work.
[09:00] Like, it's a great specification, different from Bitcoin, really having a specification so multiple clients could be built.
[09:10] In it, he defined the Ethereum Virtual Machine. And I think I read the paper six, seven times.
[09:20] I felt like it was one out of, I don't know, ten or twenty people in the world at the time who really understood the Yellow Paper.
[09:30] I did corrections to it. I have some pull requests, actually, in the Yellow Paper GitHub repo, added missing definitions and stuff like that.
[09:40] And then what I mostly did was writing tests according to the specification, which then were used by the C++ client, because this was his team.
[09:50] So I was working also on the C++ code base. And so, gas, Py-Ethereum, also the JavaScript version, and what else did we have? Like, Haskell client and others.
[10:00] They're basically using my tests to see if they implemented the machine, also the state transitions, and block creation correctly.

**SPEAKER_00:**
[10:10] Yeah. I mean, just to have some timeline for the viewers, so Vitalik wrote the white paper in November 2013.
[10:20] Various other people sort of joined in on the efforts in December, including Geth and Jeff, who started the C++ and Go clients, respectively.
[10:30] At the very end of December, kind of Christmas projects from both. January 2014, you had sort of like the public announcements of Ethereum at the Bitcoin Miami conference.
[10:40] It was as early as April 2014 that Gavin wrote the Yellow Paper, which is, you know, as you were saying, the sort of formal specification.
[10:50] You had the crowdsale between July and September 2014. So, then, yeah, you were coming in right after that, you know, so you had a wave of arrivals in September and October of that year, essentially, because the crowdsale had happened, and there was some money to actually hire people.

**SPEAKER_01:**
[11:10] Right. And I think the reason for that was also that the C++ client wasn't that much used.
[11:20] And the reason for that was that Geth was audited, and we launched without an audit for the C++ client.
[11:30] So, almost everybody used Geth. It was like, 100% Geth, and then some minor other clients used it.
[11:40] Only very few did use them. And so, after the audit was done, nobody switched.
[11:50] For sure, Geth is running. I'm synced. Like, what's the issue? Why should I switch?
[12:00] And so we had this 19:1 or 18:2 distribution. It just stayed like this.

**SPEAKER_00:**
[12:10] Yeah. I mean, talking about features, so, yeah, there were a ton of things on that C++ team.
[12:20] Aleph, Aleph Zero, as well as Aleph One. So, Aleph One being the Gwei miner.
[12:30] And then Aleph... I don't know, how would you describe Aleph Zero?

**SPEAKER_01:**
[12:40] Kind of the first interface to the blockchain, in some way. Like, the first graphical interface to a blockchain client.
[12:50] What could it do? Of course, it could mine. You could deploy a smart contract. You could visit and make it visible, somewhat, what's happening there.
[13:00] It was not really end-user-friendly in any way, but it was just a replacement of what people just do on the command line.
[13:10] Usually, command line, run your client, has some input, has some output, and it was the first kind of graphical user interface, replacing command line.

**SPEAKER_00:**
[13:20] But I guess it's sort of like a combination of, like, what you have with the block explorer now, apart from that's like a view-only, and this was both view and do.

**SPEAKER_01:**
[13:30] Yep.

**SPEAKER_00:**
[13:35] But, yeah, those Gooey clients.

**SPEAKER_01:**
[13:40] So, much more influential than the Mist browser. The Mist browser, I think, there's a video by Alex.
[13:50] It's like a ten-minute video on YouTube. They had this prototype. They're not working yet, but just, like, take it until you make it, the vision of the Mist browser.
[14:00] And this also really made us understand how Ethereum could work for the end-user.
[14:10] Having different identities connected to wallets, again, would load those steps. There's a IPFS hash or, if all the Swarm one day, the app was loading, and you could do some finance stuff there.
[14:20] This gave us an idea of what Ethereum could be. It was so... you have to think, Vitalik gave us a rather technical vision, and prod intellectual thing, but Geth gave us his prod vision.
[14:30] In that vision, Alexander gave us this very concrete thing, what an end-user could do with that, in the next six to twelve months, maybe.
[14:40] That's very important.

**SPEAKER_00:**
[14:45] Just yesterday, actually, so there was an announcement from ENS about them sort of turning on fees and doing various things that are more kind of to do with the company, the protocol, and time together.
[15:00] And I saw a reaction to that, saying, well, I'm never gonna use this again. You know, you can't extract ongoing revenue out of a protocol.
[15:10] And this person then said, it's time for Mist 2.0. Totally. I've said this before. We need the full vision, so that you've got hosted apps, and you don't need a server, and you don't need a company, and you can just make this pure, immutable smart contract wrapped in a UI that's all decentralized.

**SPEAKER_01:**
[15:25] I think we can have a Mist 2.0. I would love to see this. I heard people thinking about this before.
[15:35] I don't know if anybody really started the project, but it should be totally doable today. It's not rocket science.
[15:45] You know, we can have a Mist 2.0.

**SPEAKER_02:**
[15:50] Let me interject. We ourselves have made sort of different attempts at this, where you just download the app from the chain itself, pretty much.
[16:00] And it worked fine, and I guess it just wasn't as much of a differentiator. Like, it made things a little slower to do it this way all the time.
[16:10] I also think, like, one of the people that took the web three, the world computer vision, sort of seriously, was the Internet Computer people.
[16:20] And I don't know anyone that uses Internet Computer. But, like, the every once in a while, I see tweets about it, and I'm like, that sounds great.
[16:30] Sort of the app from the chain. You know, it's got some cool, like, smart contracting language in it.

**SPEAKER_01:**
[16:40] Yeah. The problem with this is you only need it if you really need it. Meaning, if Uniswap failed, interface is not there, it's like a backup.
[16:50] But it's not what you want to use daily. And if I say, if you remember, maybe, q, you, where they have one, when they presented MetaMask, my first thought was, oh, this is totally away from the vision.
[17:00] Like, how can you not run a full node? How can you, like, just serve over RPCs, and, almost, not a scam, but it was, like, not what we intended to build.
[17:10] Today, it's like, this is a decentralized version of it. This is, like, non-custodial MetaMask, or the good guys, compared to all the others.
[17:20] Like, see how, like, the few shifted over the years. Like, then it was absolutely required to run a full node with the Mist browser.
[17:30] This is how it's done. And now we have MetaMask, plus, and Fora, and today, this is really the version which is viewed as the original non-custodial Ethereum vision.
[17:40] You see how things are shifting, basically. But, yes, you only need those things if things are falling apart.

**SPEAKER_00:**
[17:50] Yeah. I mean, so, on the timeline again, trying to judge it, so Stefan was, I guess, chief communications officer, or commit, it wasn't until September 2015.
[18:00] That's when he left. Had you had you left already by then? Can you remember?

**SPEAKER_01:**
[18:10] No. I didn't really leave, because I was technically a freelancer. Although I was working full-time for it, I didn't have, like, a formal employment contract.
[18:20] So I was continuing to work, I think, until the end of the year, and then I just talked, well, did you just put down my hours, basically?
[18:30] If you need me, tell me. I just invoice what I'm doing. And, but I was really leaving, actually, in December, January.
[18:40] I think the last invoice I heard was for December. And then Stefan left, or was being left, I mean, there's another conversation, how he left the foundation, is he...
[18:50] He was not, he didn't agree with some people getting Ether, which is another story for another day, I guess.

**SPEAKER_00:**
[19:00] And, so, I mean, you know, talking about Gavin, the features, so, yeah, there were a lot of things happening.
[19:10] Right? You know, have this period of incredible productivity between that December and that April of getting from nothing, you know, just, like, just having the white paper, all the way through to having a working client, you know, having the Yellow Paper, as you mentioned, you know, there's this diagram showing how Whisper and Ethereum and Swarm were intended to fit together.

**SPEAKER_01:**
[19:30] I remember this project a lot. We had a prototype running with RWE, or energy in Germany. They're doing, like, all the charging stations at the time.
[19:40] This was in general, like, we got a lot of attention, of course, also after the DAO hack and all of that.
[19:50] And so it's kind of why we became a consulting company, because so many asked us, could we do a prototype with you?
[20:00] Because there were not many Ethereum builders at the time. So we have been building on Ethereum now since, oh, one year or two years, which you could not find anybody doing this.
[20:10] So we are building lots of nice prototypes, and some almost production stuff, and always related to IoT devices connected to the blockchain.
[20:20] This was the core business, and on top of this, we built those prototypes.
[20:30] We did a lot of growth for the Energy Web Foundation. I don't know if you're familiar with them.
[20:40] This was in Switzerland. They are kind of a fork of Ethereum, focusing on all the energy use cases.
[20:50] We built most of their stuff in 2018, '19, until they hired their own developers. Geth was also part of this, for a while.

**SPEAKER_00:**
[21:00] Yeah. So, I mean, so, DEFCON one, again, another iconic event, because, yeah, you have that physical smart lock just sitting there on your shelf, and, you know, it rotates it, right?
[21:10] You know, right? You did your transaction.

**SPEAKER_01:**
[21:15] It was, we just had a Raspberry Pi connected via, I think, was SIP or SET, back then, to the door lock.
[21:25] And on the Raspberry Pi, we had actually an Ethereum client running. We had a smart contract on-chain, where you could send some Ether, actually, and when it received some Ether, it would open up.
[21:35] This was basically the demo. But it was cool to see something physical. You're talking about using Ethereum for, as I said before, the economy of things, connected to IoT devices.

**SPEAKER_00:**
[21:50] And, yeah, I mean, so Slockit itself did a number of these different products, right? There was something with electrical charging, and something to do with toll roads, is that right?

**SPEAKER_01:**
[22:00] Right. We had a prototype running with RWE, or energy in Germany. They're doing, like, all the charging stations at the time.
[22:10] This was in general, like, we got a lot of attention, of course, also after the DAO hack and all of that.
[22:20] And so it's kind of why we became a consulting company, because so many asked us, could we do a prototype with you?
[22:30] Because there were not many Ethereum builders at the time. So we have been building on Ethereum now since, oh, one year or two years, which you could not find anybody doing this.
[22:40] So we are building lots of nice prototypes, and some almost production stuff, and always related to IoT devices connected to the blockchain.
[22:50] This was the core business, and on top of this, we built those prototypes. We did a lot of growth for the Energy Web Foundation.

**SPEAKER_00:**
[23:00] Fantastic. So, hope to see you at DevCon eight.

**SPEAKER_01:**
[23:05] Me too. I'm looking forward to it. And I'm, as of now, I don't intend any change. Stick to Ethereum.
[23:15] I love the community. I continue building, and try to get a lot of people using it.

**SPEAKER_00:**
[23:20] Have you been to every DevCon?

**SPEAKER_01:**
[23:25] Yes. I said yes. I've been to every DevCon. The last one was actually the first one that I didn't give a talk, and I also went to every ECC, except for one that was COVID.
[23:40] There was some reason I couldn't come. But, yes, I'm actually, I intend to continue to come to every DevCon.
[23:50] It's like you meet the people, like, of course, and many others. It's just a sweet spirit there, nice community.
[24:00] Love seeing how it all grows. Listen to those exciting talks. I mean, it's for Tokenize.it, it's not as relevant.
[24:10] It's not like our customers or it's tech, of course. We're just doing an ERC-20 token on Ethereum. It's super easy.
[24:20] So, deep tech, sometimes I miss doing deep tech, but, well, I just enjoy being there, seeing what it all, what all happened.
[24:30] And remembering those magic days, and just like, only once in a lifetime, or two times in a lifetime, you have this moment where everything comes together at the right time, the right place, the right people.
[24:40] This certainly, where those, like, one and a half years I worked for Ethereum, are definitely, like, the prime of my career, in terms of who I worked with, what we accomplished, the impact we had on the world, and the sweet cyberpunk spirit there, and what we did there.
[24:50] It was really great. I always sometimes get emotional thinking about this, and meeting those people again at DevCon.

**SPEAKER_00:**
[25:00] Fantastic. Well, thank you for all your contributions to that success. Likewise. All the best.

**SPEAKER_01:**
[25:05] Okay. Thanks so much. Have a great day. Thank you. Too. It was great talking to you. Bye-bye.

**SPEAKER_00:**
[25:10] Bye.