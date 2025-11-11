# Corrected Transcript

## Early Days of Ethereum: Interview with Christoph Jentzsch

**SPEAKER_00:**
Okay. Recording is in progress, it says. So hello, everybody. Today, delighted to have Christoph Jentzsch with us. We did attempt to record this Christoph and I two weeks ago, but I forgot to press the record button. So we spoke for an hour or so, and then it was not recorded. So this is round two.

**SPEAKER_01:**
So hello, Christoph. How are you? Hi, Bob. Nice to meet you again. I'm doing good. I hope you too. Thanks for the invitation.

**SPEAKER_00:**
Fantastic. Yeah. So Christoph and I, you know, our paths crossed for the first time way back in 2015, when I was trying to do C++ Ethereum on my smartwatch. This was around the time that Christoph was still at the Ethereum Foundation. And then I think our paths crossed a number of times since then.

So Christoph, what were you doing with your life before you found Ethereum and joined this crazy journey?

**SPEAKER_01:**
So in— actually, this journey started in 2013. I was doing my PhD in theoretical physics, actually about self-organizing systems. So, like, biology, systems in mathematical biology and other things. So I was studying systems which have local rules and global behavior.

And I came across Bitcoin, which has just a small set of local rules and a global behavior as a currency. But the reason I came across this was I was looking for cheap GPUs, like graphic cards. And the Bitcoin miners were selling their GPU mining rigs to get some FPGAs and later ASICs.

And so that's how I got into what's Bitcoin mining. And so I bought my first Bitcoin, got into this bubble, did read everything I could about it. And then I came across the white paper from Ethereum, early 2014, something like January, February in some Bitcoin forum somewhere.

And I was already totally in love with the idea of Bitcoin being a decentralized currency and all the characteristics and features of it. And this white paper, I mean, if you read it again, it's almost a prophecy. Except for NFTs, everything's in there—from DAOs, from ENS, like, names as domain names as tokens and all of that.

So for me, it opened up this option of building applications with the same characteristics as Bitcoin, but just not a currency, but everything else. And so then I started reading everything about it. And in 2014 in summer, I went— the crowdsale was in 2014, right? The crowdsale— so around the time the crowdsale happened, I watched a video from Gavin Wood. He was somewhere in the Nordics, some conference there. And he talked about Ethereum. I loved it. And he said he wanted to open up an office in Berlin looking for C++ developers. I was a C++ developer.

So in theoretical physics, it's 90% software development. So I said, well, I want to do this. So I took my parental leave time plus some vacation time and paused my PhD for, like, three to six months and said, I will return after I'm done. I thought this was just a short project because they raised money—maybe six months, maybe twelve months, eighteen months or so, then it's over. When I started, I thought about maybe three to six months, and then I go back to my PhD.

So I worked there with Ethereum. This is Gavin Wood. It was a great time. And then I just decided to stay. It was so exciting.

**SPEAKER_00:**
So you never got to be a doctor?

**SPEAKER_01:**
No. I'm not a doctor. I did not finish my PhD, although I only had six months left, which was kind of a pity. I worked, like, for three years on that. But I also had, at the time, I think, four or five kids. And I needed some money. I didn't get much money as a PhD student, so I did some software development as a side hustle, basically.

And so when I got this project, I said, well, let's do this for two or three months as a parental leave time, and then I can return. And then I decided to really interrupt my PhD, thinking I will maybe return one year later because I thought the Foundation would eventually run out of money because they're not making any profits. They just raised donations, then they will spend them, then it's over. Then I can continue my PhD. That was originally the plan. It just came different.

**SPEAKER_00:**
I mean, I guess it's never too late, right?

**SPEAKER_01:**
I actually sometimes think about it if I should return. It's just so much to learn again. I'm right now doing Tokenize.it. I'm basically working on tokenizing German companies. It works very well. So currently, I'm not planning on getting back anytime soon.

**SPEAKER_00:**
No. Because, I mean, famously, you had, you know, Doctor Gavin Wood and Doctor Christian as well. And I think there were a couple of other PhDs as well.

**SPEAKER_01:**
There were. Definitely.

**SPEAKER_02:**
I also dropped out of mine. I was actually in mathematical physics too. Interesting. Similar background.

**SPEAKER_01:**
It's actually the same. Like, theoretical physics, it's the mathematical part of physics. I tried very much. I did thermodynamics and statistics, mostly software development. It was really fun.

**SPEAKER_02:**
Well, by the way, Jim is trying to join. I don't know if there's anything that needs happening. He's getting some browser issue.

**SPEAKER_00:**
Yeah. Yeah. Well, he'll pop up and we can add him, or if he's— I'll see. Then never mind.

So Christoph, in terms of, you know, getting hired into ETH DEV, and I'm sorry if I just missed it. So how did that happen? Did you meet Gavin at a meetup, did you say?

**SPEAKER_01:**
Yes. I actually, no. I listened only to his talk. It was an online thing. I actually just wrote him an email. Said, look, I would love to join you. I love what you're doing. And he invited me to meet him in Kreuzberg, Berlin. Which, again, is about two hours drive from here. So I went up there, met him. I remember the first conversation, he was talking about all the stuff they were gonna build and said, well, what can you do?

And I just asked him, what's, like, the most complicated stuff you have right now? Like, give me a complicated task. I somehow can figure it out. So he talked about the Ethereum Virtual Machine, which needed some testing. So I just picked working on testing the Ethereum Virtual Machine or, like, writing tests for it.

Back at the time, I actually had no real idea what he was talking about. Meaning, of course, I did understand on the white paper level. I did understand what Ethereum was about. But Gavin had this skill of writing the Yellow Paper, which is still incredible work. Like, it's such a great specification—different from Bitcoin, really having a specification so multiple clients could be built. In it, he defined the Ethereum Virtual Machine.

And I think I read the paper six, seven times. I felt like I was one out of, I don't know, 10 or 20 people in the world at the time who really understood the Yellow Paper. I did corrections to it. I have some pull requests actually in the Yellow Paper GitHub repo, added missing definitions and stuff like that.

And then what I mostly did was writing tests according to the specification, which then were— with the help of the C++ client because this was his team. So I was working also on the C++ code base. And so Geth, pyethereum, also the JavaScript version, and what else did we have? Like, Haskell client and others. They were basically using my tests to see if they implemented the virtual machine, also the state transitions, and block creation correctly.

**SPEAKER_00:**
Yeah. Yeah. So, I mean, just to have some timeline for the viewers. So Vitalik wrote the white paper in November 2013. Various other people sort of joined in on the efforts in December, including Gav and Jeff who started the C++ and Go clients respectively. At the very end— oh my goodness. At the very end of December, kind of Christmas projects from both.

January 2014, you had sort of, like, the public announcement of Ethereum at the Bitcoin Miami conference. It was as early as April 2014 that Gav wrote the Yellow Paper, which is, you know, as you were saying, a formal specification. You had the crowdsale between July and September 2014.

So then, yeah, you were coming in right after that, you know, so you had a wave of arrivals in September and October of that year, essentially, because the crowdsale had happened. There was some money to actually hire people.

And then talking about, you know, where you met there, initially, that group, so ETH DEV UG, this company coordinating the development of Ethereum stuff. So it's a subsidiary of the Ethereum Foundation.

**SPEAKER_01:**
Right.

**SPEAKER_00:**
They were working initially in a coworking space, but then got an office. And it was between August and November of that year that the office was getting, like, you know, done up and tidied. And then in November, you had DevCon Zero, you know, the first conference, an internal one where a lot of the people— that was their first sort of face-to-face meetings.

So how was DevCon Zero? How was that? What was that like?

**SPEAKER_01:**
It was like a company retreat. So it was not a public conference. We did have— even though there were some outsiders who felt like part of the community, maybe also pushed some code. I remember— what was his name again? Wrote the book also about Ethereum. Henning, I think, Henning of IBM. Oh, Henning— yeah. I think he was also there just as an example of some people who were, like, big fans of Ethereum, interested in joining. Of course, Giuseppe as well, right? Roman was there with the Java clients.

But it was mostly developers. But also, I think Stephan was already there. So we had already the London team. So it was like an internal Ethereum meeting. A meetup almost— I think, three days or so. I don't know exactly. Five days even. A full week. Yeah, it was a full week. I was there for the full week as far as I can remember.

I did a presentation about testing, how the test suite is very important. Yes. We had Remix projects, Solidity project, I think, mostly started at the time. Gavin used this for explaining his vision of Ethereum as a platform for decentralized applications, so building Swarm. I don't know if Swarm and Whisper was already launched there, but at least, like, the generic idea, the Mist browser.

So all those ideas were really sketched out there, like, the technical roadmap, what we are going to build. Because we started just, of course, with the basic clients, like implementing the protocol, but he took it, like, what are we going to do in the next twelve months? Build the Mist browser, like, Remix, those tools to have a platform for decentralized applications.

I remember one slide, which I think I posted on Twitter a while ago, where you have those three circles, one circle as one node. And you would see, like, they are connecting on the blockchain using Swarm for the data, Whisper for the messages, and this whole picture was painted there.

And there were people attending, I think, around 50 people, plus or minus 10, don't know the exact number, where mostly developers were talking about code, coding there. Joe Lubin, I remember him being there saying, well, all of you, you will create your own companies, becoming millionaires. I remember Joseph talking about that. And I think mostly he was right.

So most of those people in the room, in one way or another, were cofounders, founders, or were early parts of companies building on top of Ethereum in the years to come.

**SPEAKER_00:**
Yeah. Yep. Let me see if I can do a little screen share. No. Never mind. I can't work out how. Not to worry.

**SPEAKER_02:**
But yeah. There's this present button.

**SPEAKER_00:**
Not to worry. Yeah. I don't see that. Is that on the right-hand side somewhere or at the bottom?

**SPEAKER_02:**
For me, I appear on the top right, and below, to the right of me below, there's a present button with, like, a plus.

**SPEAKER_00:**
Never mind. Never mind. I was just gonna show the iconic photo of people at DevCon Zero, right? You know, that's this big group shot with nearly everyone who was there, you know. So that's a classic Ethereum photo.

I was looking— there's, like, 11 of the videos that are still around from DevCon Zero. I think there were around 20 sessions. I'm still trying to dig out the others. Some of them, including yours, I have not managed to find yet.

**SPEAKER_01:**
Yeah. It was only about the test suite, how it's built, how people would use it. It was rather technical. There was not much of a vision in there. So—

**SPEAKER_00:**
Well, Lefteris presented on Emacs, so, you know, you're not the most boring talk.

**SPEAKER_01:**
Yeah. Again, it was just some nerds starting— it also, for most of them, it was the first time we actually met. And, of course, the C++ team, they knew each other because they were working in the coworking space. Lefteris and others, they were there. But then, I think it was the first time I actually met Vitalik because he came there. Then, of course, Jeffrey and his team, Stephan and his team, Joseph.

So it was for me, it was the first time to meet all of them and have talks. And since we had time, five days, a small group of people, we actually had time to eat together, to talk. So it was not so crowded maybe as DevCon is today. Very intimate. It was good.

**SPEAKER_00:**
Yeah. I mean, 400 hours.

**SPEAKER_02:**
One thing I can't quite remember. So there was a time— there was an Ethereum Slack that was kind of open to the public. You know, there were a lot of people. The sort of Ethereum affiliation status was fairly vague at that point. And we were— you know, I remember we were using Skype a lot in those days for the team. And, like, Vitalik liked the Skype.

And then at some point, I sort of lost the thread of, like, where the core— like, I can't remember where the core development discussions were happening. And I'll maybe ask Jim to comment. Also, just like those tests, we kept, like, getting them. And I think I'm thinking of some a little bit earlier on, and we'd build them. And Jim was mostly working on them and would update on the, like, passing percentage, which would always be between, like, 93-98%, and then something would change.

You know? But, yeah, like, where did the discussion— because, yeah, between, like, the crowdsale and DevCon Zero, I think it kind of got a little bit— it, like, moved around where the dev discussion was.

**SPEAKER_01:**
It was mostly Skype. We also had Skype channels for almost everything, like the C++ team and so on. Then for a short time, we used a notetaker, which had a name also with E something—

**SPEAKER_00:**
Etherpad?

**SPEAKER_01:**
Etherpad, something like this, right? There were some notes created there, but the communication was really, I would say, 99% Skype for me. Later on, we used a tool based on GitHub. What was the name of it? Gitter.

**SPEAKER_00:**
It was called Gitter.

**SPEAKER_01:**
Gitter came later. This was, like, the new replacement for Skype, but I didn't use it too much. It was actually during the time when I was leaving. But it was used also by the C++ team. There you had a channel per GitHub repo. This was during the time that GitHub was completely reorganized because at the beginning, it was, like, one big repo with everything. They made submodules. It was so messy. And then during this process, we got Gitter. But, yeah, for me, it was mostly Skype.

**SPEAKER_00:**
Yeah. And then annoyingly, that kind of means a lot of these early discussions, they're kind of, like, a bit lost because nobody is using Skype. And Skype is getting, like, deleted. This is happening in February this year.

**SPEAKER_02:**
Oh, I thought it happened already.

**SPEAKER_00:**
It's just— you can still request to download, and I did, and then I haven't heard anything back. I want to do that to see if I can get some of those. So everybody apply to download your Skype data.

I remember with Gitter, there was a discussion about this that I was involved with at the EF later, which was saying the problem with Skype is it wasn't discoverable. You know, you had to add— you had to request to be added, but you had to know what was there to be able to do that request. So it was a bit of a chicken and egg situation.

Whereas Gitter, it was like a one-to-one with the repositories. So if you're using a repo, there you go. There's a one-to-one channel with that, and it was discoverable and archived. But then Slack, I think, was even earlier. And there was the forum as well, right? There was an Ethereum forum too.

**SPEAKER_01:**
There was a forum. And then Slack— I think I got introduced to Slack when Stephan created a community for the DAO. When he looked for a new communication tool, he went with Slack. And at that time, it was not like today, like, a business tool for companies. It was really for communities. Like, we had 5,000 people in our Slack, which is not how it's used today.

**SPEAKER_00:**
Yep. Yep. So welcome, Jim.

**SPEAKER_03:**
Sorry. I had some technical problems for a while there. But I don't know. I'm just listening to you guys. What happened that brought the whole world to Zoom suddenly?

**SPEAKER_02:**
It was in waves. Look, on my side—

**SPEAKER_03:**
I don't know. I just woke up one day, and everything was Zoom from then on.

**SPEAKER_02:**
Yeah. Like a native species, like a statistical phase transition. You know, I think it was two phases. I would always get invited to corporate— like, let's say 2017 to 2019 when I was, you know, doing primarily BD, I found that I would get invited to any of 10 video conferencing tools. And, like, you know, what is the Cisco one? Webex. That was horrible. I would get that a lot.

Google Meetings didn't feel sufficiently corporate or something even though it was okay. And Zoom had the best quality for a while, and I found that everyone picked Zoom at the same time, like, 2018, let's say. I think it was just quality to me.

**SPEAKER_00:**
Like, I mean, Microsoft really fumbled, right? Skype had such a lead for so long, but Zoom just seemed more reliable, whatever weird little proprietary magic they had going on. Yeah. And then I mean, I guess—

**SPEAKER_03:**
Yeah. I guess I was under the impression that, like, Zoom is for businesses.

**SPEAKER_02:**
I think that's— well, that is true. But still— I mean, this has gotten way better in the last ten years, but still nothing really works for reliable video over the Internet. It's just much better than what existed. But there was a free version always, and it would just, like, time you out. So, like, they had a fairly viral acquisition loop where— and I was just gonna say, in the pandemic, once people were locked down, it became a consumer tool where people would have, like, large yoga classes or, you know, sermons or whatever with, like, 500 people on a Zoom, and then everyone got called.

**SPEAKER_03:**
Yeah. I remember it well. All of a sudden, like, my parents were, like, calling me up, and they're like, we found this awesome new tool. You probably never heard of it. It's called Zoom.

**SPEAKER_02:**
Yeah.

**SPEAKER_00:**
Well, yeah, there were, like, ten different ones. Let's move on from sharing about video platforms.

So I look back. So Jim's first commits on the Haskell client were mid-September 2014. So, you know, a couple of months ahead of DevCon Zero. You'd have the Yellow Paper for five months at that time. And I did find on our Slack, you know, a bit of a thread where things, I think, from you, Christoph, were being discussed by Jim. I don't know. Did you guys interact directly at all on testing, Jim, Christoph?

**SPEAKER_01:**
Not directly, as far as I can remember. Maybe there were some messages. I mean, it's been a while ago.

**SPEAKER_03:**
I could be wrong. I may have met you briefly in London when we had that conference. But it would have been, like, quick greetings at a party or something.

**SPEAKER_01:**
Yeah. I mean, ten years ago, lots of people— sure, we did. We had the testing GitHub repo, and we had all the major clients using it. And I was interacting, mostly responding to questions. I mean, of course, the C++ team, I was super close to. I used the C++ team also to prefill the tests. So this was by default right, except we found there was a test failing, but it should— but, actually, C++ was wrong. So sometimes this happened. The test was not really failing; C++ was wrong.

But in the majority of cases, C++ was right. So we were just having those conversations. We found tons of issues. In the beginning, I wrote those tests using actually bytecode, the very first tests. Then I went to a low-level Lisp-like language. This was LLL. This was the precursor to Solidity by Gavin.

And then in the end, actually, I had automated, like, fuzz testing where I wrote software that would create thousands of tests. We had some AWS, like, over 100 cores of machines constantly creating tests. We always had some failing on some versions of Geth or other clients. So this was mostly what I did during one and a half years.

**SPEAKER_00:**
Right. Right. So, yeah, I mean, I guess for the viewers, something that Ethereum chose to do differently from Bitcoin was to have this specification separate from the client software, right? So, you know, when Bitcoin started, it was the code that happened first and the white paper afterwards, but the white paper wasn't a protocol specification.

So, you know, Gav was doing that Yellow Paper spec in parallel with the C++ client, which is sort of the first one, while you had Vitalik working on the Python client, Jeff working on the Go internally, but then you've got all these other clients as well, right?

So EthereumJ, the Java one by Roman, I think, started in about April or May. You know, ourselves, and Karen here with the Haskell client starting in September.

**SPEAKER_01:**
You have JavaScript as well. So it's like a library. I don't know if it's really like a syncing client, but they have all the tools so you can— in your web app, kind of integrate part of it to verify certain states.

**SPEAKER_00:**
Yeah. I mean, I think maybe they had a syncing client at some point apart from— it obviously, like, couldn't actually keep up, but theoretically. Yep. And, yeah, like, a little later, there was a Ruby client as well. And, yeah, at one point, there were eight different clients, right?

**SPEAKER_01:**
If you want to, I can tell the story of why we all are using Geth today.

**SPEAKER_00:**
Yeah, absolutely.

**SPEAKER_01:**
It was not a given. Like, at the time, everyone had different opinions, but the C++ client was really the fastest, the most solid one, passing all the tests and so on. But Gavin always wanted to add new features, like, do refactoring, and he was a perfectionist, which is not bad for this kind of software.

And then the time came for the security audit because everybody wanted to launch Ethereum now. And he said before we launch it, those clients need to have a proper security audit by an external company. And one of the companies doing this was in Seattle. So I actually went there with the team for the audit.

And because Gavin wanted to build some more features, he said, well, let's just— yes, Geth can go first. Let's first audit the Go client. When they are done, I'm done with the features I want to build, and then we're going into the audit for the C++ client. So Geth was audited. They picked up issues. They fixed the issues, and now it's time. And so there was technically no reason why not— well, actually, we could launch Ethereum now. We have a fully audited client, tests that are running for a while, no major issues, no failing tests for a long time. So why would we wait for the C++ client to be audited?

Maybe they also really had the pressure of money was running out. We need to launch now. And then the decision was made. Let's launch with Geth. They could still use C++. It's just not audited. Let's say in two months or so, the audit is done, and then they can use C++ even more if they want.

But then the big mistake was, in my view, when they made this announcement of you can start now, they recommended using Geth because this was the audited one. So almost everybody went with Geth. We started with almost 100% Geth, and then some just some minor other clients used. Only very few did use them. And so after the audit was done, nobody switched. Like, sure, Geth is running. I'm synced. Like, what's the issue? Why should I switch?

And so we had this 90/10 or 80/20 distribution. It just stayed like this. So if Gavin would have been— either said, let's just do the audit now and we just— if both audited, then start— maybe we would have fifty-fifty. Or if even the other way around, if they would have first audited C++ and Ethereum would have been launched without a Geth audit, like, you would have seen a total switch.

And then, of course, money was going low in the Foundation. They had to reduce the team. And because Geth was the most used one, there were some issues with Gavin. Another story, maybe I'll have a talk with him. And so in the end, Ming decided to basically kick out the complete C++ team. This was then shortly before DevCon One, so something like September-ish.

But, yeah, I think the reason for that was also C++ wasn't really that used. There are other reasons as well. But you can see how a tiny thing can have such big consequences down the road, like him doing Polkadot today and all of that.

And he was great. I mean, I really, really— I still think maybe we'd have had proof-of-stake and sharding way earlier if Gavin would have stayed. So without him, they moved slower, of course. The price went up. They got better security-relevant things, so changes didn't happen quickly anymore, but take more time and so on. But I think this was a big loss for Ethereum that Gavin left, basically, in 2015.

**SPEAKER_02:**
Yeah. That's crazy. Amazing the difference a client side audit was the cause. I think it was part of it. But it— you know, having the process— maybe it started with the Red Wedding, which we discussed in some other Early Days of Ethereum episodes. Like, I remember very clearly in the room. It was a lot— it was, like, you know, two weeks into my Ethereum tenure at that time, that he was talking about brain drain if it was only going to be a nonprofit foundation and not going to have a commercial arm.

**SPEAKER_01:**
Yes. There are more issues to that. Definitely. Like, this was not the deciding part, but it was, like, those things were adding up. I remember that Gavin had this idea of turning the Foundation into a DAO and then having a for-profit entity next to it, which would build things and make money. So there were many different commercial ideas at the time.

So he then basically started on his own. I remember he wanted to have me as part of it, but I decided to do Slock.it at the time. So that's why I did not become a cofounder of Parity. Another story. We can go into this if you want. But there are many reasons. Part of it, I think also, was him and Ming didn't really get along too much. There was not really a trust relationship going on.

Of course, money running out, different visions of how Ethereum should evolve technically and economically, if you want, all played a role. But I think it was just one part that the C++ client wasn't used that much. And the reason for that was, I guess, being audited— launching without an audit for the C++ client.

**SPEAKER_00:**
Yeah. I mean, talking about features, so many things happened, right? You know, you have this period of incredible productivity between that December and that April of getting from nothing, you know, just, like, just having the white paper all the way through to having a working client, you know, having the Yellow Paper.

As you mentioned, you know, there's this diagram showing how Whisper and Ethereum and Swarm were intended to fit together. And I found some more timing on that. So Swarm was envisaged by Daniel Nagy as far back as 2011. You know, it was an idea he'd been working on for, like, three years before that.

I spotted on the Whisper presentation that Gavin did that that was a pre-Ethereum idea as well. So it's probably only when all of these people came together, it was like, well, you've got this storage idea. You've got this blockchain kind of like CPU database-y idea. And then if you have messaging, you know, all of these things can fit together.

But it's also— we're gonna build our own IDE as well.

**SPEAKER_01:**
Browser. Browser. Browser. Plus the browser. The complete thing. It's a complete platform for decentralized applications end to end. This was the big mission. And, also, this was what attracted me to it. I mean, having someone having a really proud vision of a new Internet, if you want— that's what he called Web3. That's where the term comes from because it was not just a little tool. It was a complete new Internet called Web3—from data to messaging to smart contract blockchains to IDE to browser.

And this vision was very, very attractive. This attracted all the talent and the developers because they loved building that.

**SPEAKER_00:**
Yeah. I mean, it's a very, very expansive vision. And, yeah, it was— you know, Gav, as you say, you know, Web3 was him. Prior to that, the language I saw was really about Bitcoin with smart contracts. You know, that was really sort of the genesis of Vitalik going through that journey of colored coins and Mastercoin and meta protocols, and that kind of positioning of Bitcoin as a calculator and Ethereum's a smartphone, but it was all that kind of, like, blockchains and applications, right? It wasn't that full Web3 vision, which I think—

**SPEAKER_01:**
And that really came from Gavin. Gavin. We have to attribute this to him. He was having this big vision. This attracted also so many people. This attracted also even the business people— they could now understand what it actually is. Other than just, it's just tech. Let's see. But this is, like, a broad vision of how businesses function, how, like, this new financial world would happen. They could understand this far better than having this iPhone calculator comparison. This was maybe a nice technical thing.

**SPEAKER_00:**
Yeah. Yeah. But then for it being a very expansive vision, that's a lot of work.

**SPEAKER_01:**
Sure. But you just start somewhere.

**SPEAKER_00:**
That's it. So, I mean, you know, talking about Gavin and features. So, yeah, there was a ton of stuff on that C++ team. Aleth Zero as well and Aleth One. So Aleth One being the eth miner. And then Al— how would you describe Aleth Zero?

**SPEAKER_01:**
Kind of first interface to the blockchain in some way. Like, the first graphical interface to a blockchain client. What could it do? Of course, it could mine. You could deploy a smart contract. You could visit and make it visible somewhat what's happening there. It was not really end-user friendly in any way, but it was just a replacement of what people just do on the command line. Usually, command line, run your client, has some input, has some output, and it was the first kind of graphical user interface, graphical user interface replacing command line.

**SPEAKER_00:**
But I guess it's sort of like a combination of, like, what you have with the block explorer now, apart from that's, like, view-only, and this was both view and do.

**SPEAKER_01:**
Yep.

**SPEAKER_00:**
But, yeah, those eth clients.

**SPEAKER_01:**
Much more influential than the Mist browser. The Mist browser— I think there's a video by Alex van de Sande. It's, like, a ten-minute video on YouTube. They had this prototype. It wasn't working yet, but just, like, fake it till you make it, the vision of the Mist browser. And this also really made us understand how Ethereum could work for the end user.

Having different identities connected to wallets, where you would load those dapps—there's an IPFS hash or Swarm one day, the app was loading, and you could do some finance stuff there. This gave us an idea of what Ethereum could be. It was— you have to think Vitalik gave us a rather technical vision and profound intellectual thing, but Gavin gave us his profound vision, and Alex van de Sande gave us this very concrete thing what an end user could do with that in the next six to twelve months maybe. That's very important.

**SPEAKER_00:**
Just yesterday, actually, there was an announcement from Uniswap about them sort of turning on fees and doing various things that are more kind of to do with, you know, the company and the protocol tied together. And I saw a reaction to that saying, you know, well, I'm never gonna use this again. You know, you can't, like, extract ongoing revenue out of a protocol.

And this person then said, it's time for Mist 2.0. Totally. I've said this before. We need the full vision so that you've got hosted and the apps, and you don't need a server, and you don't need a company, and you can just make this pure, you know, immutable smart contract wrapped in a UI that's all decentralized.

**SPEAKER_01:**
I think we can have a Mist 2.0. I would love to see this. I heard people thinking about this before. I don't know if anybody really started the project, but it should be totally doable today. It's not rocket science. You know—

**SPEAKER_02:**
Let me interject. We ourselves have made sort of different attempts at this where, like, you just download the app from the chain itself pretty much. And it worked fine, and I guess it just wasn't as much a differentiator. Like, it made things a little slower to do it this way all the time.

I also think, like, one of the people that took the Web3, the world computer vision sort of seriously was, like, the Internet Computer people. And I don't know anyone that uses Internet Computer. But, like, every once in a while, I see tweets about it, and I'm like, that sounds great. Like, serving the app from the chain. You know, it's got some cool, like, smart contracting language in it.

And I guess there's just no demand if it, like, slows the app down even slightly. And I think MetaMask and then many other wallets were sort of enough. Still not the whole thing. But, yeah, I guess it's like, you gotta get people to use it if you want it to be maximally cypherpunk too.

**SPEAKER_01:**
And I fully agree. Yeah. The problem with this is you only need it if you really need it. Meaning, if Uniswap's interface is not there, it's like a backup. But it's not what you want to use daily. And if I— you remember, maybe, MyCrypto, where they have one? When they presented MetaMask, my first thought was, oh, this is totally away from the vision. Like, how can you not run a full node? How can— how dare you, like, to just serve over RPCs and— almost not a scam, but it was, like, not what we intended to build.

Today, it's like, this is the decentralized version of it. This is, like, non-custodial MetaMask— the good guys compared to all the others. Like, see how the view shifted over the years. Like, then it was absolutely required to run a full node with the Mist browser. This is how it's done. And now we have MetaMask plus Infura, and today, this is really the version which is viewed as the original non-custodial Ethereum vision.

You see how things are shifting, basically. But, yes, you only need those things if things are falling apart. Like, just as an example, so many people use the Safe. Let's say the Gnosis Safe UI is gone. Technically, it shouldn't be a problem to run another one, but it really needs to be something on IPFS. It needs to be something which you can self-host. I can still access my wallet without going to the command line.

So for those reasons, you need it. And the Mist browser was sort of as the fallback for every dapp. Like, of course, you can have your application run on a normal .com domain on AWS. Fine. But if you could serve the same app in a decentralized fashion as a backup, this would be great because you could still use it if the company— let's say Uniswap, the company fails, if someone builds a nice Uniswap UI served by IPFS directly interacting with the smart contracts.

**SPEAKER_02:**
Yeah. Yeah. That's fair. Also, I— I mean, Uniswap, I think, is controversial. I know Jim wanted to say something— controversial because they had the company-level fee skim. And then so I think they've turned the on-chain fee on. I don't know that they've turned the company fee off. I haven't read it in detail.

**SPEAKER_00:**
I believe so because one of the replies was saying, okay, so how are your, like, shareholders gonna like that?

**SPEAKER_02:**
Yeah. Okay. Fair enough.

**SPEAKER_00:**
Well, hopefully, they hold a bunch of the UNI, and it will, you know, mark to market. They're doing a bunch of buybacks, so that, you know, it should be sort of benefit of all stakeholders.

So yeah, just sort of this interesting kind of contrast, right, between completely immutable, you know, force of nature smart contracts versus, you know, more permissioned, more tied to a company, more source of, like, wanting to have fees for maintenance kind of question. I mean, it got— you know, it's like treasuries, I guess, either on-chain or not. But this opens up the questions—

**SPEAKER_01:**
How should the Ethereum app be built economically? And this is also a question being answered during that time. The DAO was one approach of it should be fully on-chain. All the revenue should be on-chain. There should be no for-profit entity directly attached to it. And Slock.it, the company I built after that, would be a service provider for them, getting paid by them for work being done for the DAO or one version.

I was always skeptical and still am about companies where you have effectively two cap tables, meaning you have a token cap table—if you want. Of course, it's a utility token, governance token, and so on. But effectively, it's kind of ownership in the protocol, and then you have a for-profit company with shareholders.

And this is always, I think, very dangerous. You don't know where to go. What's the best value? On the shares of the company or on the token? This was the main reason all those companies had those nonprofit foundations in Switzerland. Rightfully so, because they said, you only want to have one cap table. Like the Ethereum Foundation, there were no shareholders of Ethereum. There was a nonprofit foundation and a token. The token— if you want to have a share in the economic success of the protocol, you would buy Ether.

And so later on, there were many other token projects where they had a nonprofit foundation, so no shareholders, no second cap table, and then you would have only the token, and all the value would be there. And now with Uniswap, you have this problem of having, again, shareholders and tokens. And I think that's dangerous and not a good idea, actually.

**SPEAKER_00:**
Yep. Yep. So perhaps let's talk about ETH DEV actually, just before we get to DevCon One. So the launch, right? So, obviously, a lot of testing and coordination with different series of concepts. So, I mean, how did you know it was good enough? Like, what was that testing flow and collaboration like?

**SPEAKER_01:**
So there are many indicators. One being the Olympic testnet running smoothly for a while. Another one, we had a static client having an audit, which worked. And then they were saying, okay, now if Christoph doesn't find any failing tests for, like, three weeks or four weeks or something, we are ready.

This was the case. And so we said that now we can set a launch date. And the launch itself is also a bit— typically Gavin— nobody wanted to push a button. Like, nobody just, like, start a chain. So what was done was there was a script written, which had as an input parameter the hash of the Olympic testnet at a certain block height. So everybody could, using the script plus the software plus C++ or Go client, of course, having the hash, which was at that time in the future, of the Olympic testnet, start that chain.

So there was— at launch day, we were just viewing it. There was nothing to be done because, like, all the information was out there. People were just simultaneously starting the blockchain. And then over the peer-to-peer network— this was actually the harder stuff. They found themselves on Reddit and others to share IP addresses, like connect to my peer, connect to my peer. And so then they started to come together, and, of course, the longest chain was the Reddit one.

So as soon as you found a peer which had their own chain, you would think and say, "Oh yes, this is a longer one," you would stop, start mining on top of his chain. And so, basically, the canonical chain emerged from that within, I don't know, thirty minutes or one hour, and then we had the chain running. And this was, like, a beauty to behold. Like, let's just see how this works out as intended, completely decentralized.

Nobody did do anything. I was in the C++ building office in Kreuzberg, Weidermask, Strasser 37A. Nice office, and we just watched it. And we were mining there with the laptop. Wasn't really— and we were all excited about it. I actually think two or three weeks after, or maybe four, we had the first little hard fork. Meaning there was some smart contract doing something that Geth and C++ had a different result for.

I got called in the middle of the night at 10 PM or 11 PM. So I remember seeing this, looking for one hour or so, finding what's the issue, then I found it, put a test about it. See if that's— Geth was right, C++ was wrong. So I gave it to Jeff. They fixed it. I think we said one hour. In fact, after five hours, everything was done. And they basically called up the miners, "Please update your client." And then it was fine. So this was the early days, but it was a successful launch, nevertheless.

**SPEAKER_00:**
Did the Haskell client sync at Genesis?

**SPEAKER_03:**
I do not know. Did it, Jim?

**SPEAKER_03:**
No. We were able to sync at Genesis time for, like, a year or so. We were syncing. But I remember, like, that week, Karen and I were, like, more interested in trying to get a miner in place. So that was what that week looked like for us.

**SPEAKER_02:**
Yeah. I was living in an apartment just south of Berkeley campus at this time, and we'd been— Jim had been taking me to Fry's to build a machine a few months prior, like a build machine. It had a good GPU in it. Yeah. Fry's is dead now. RIP.

I was running a miner there, and we built a couple in Jim's garage. It got very hot in Jim's garage, which was— you know, those things were consuming a fair bit of power. Mine exploded after a few weeks. It was actually just the power supply. So I was— I thought the whole machine was bricked. Jim said, you know, I think everything but the power supply will be okay. And it was the case that everything but the power supply was okay, but then I stopped mining.

**SPEAKER_03:**
And I think— we didn't even bother to buy cases at that time, right? I had mine just sitting, wires out.

**SPEAKER_02:**
Yeah. Yeah. Indeed.

**SPEAKER_00:**
Sure. You have a dozen or twelve.

**SPEAKER_02:**
At that time, we were always, you know, sort of, at least at that time, short-handed people-wise, so catching up a little bit on the features, etcetera, but it ran perfectly well.

**SPEAKER_01:**
There were always new features coming. I remember it was, like— one of the sweet memories during the pre-launch, sitting together with Gavin, Jeffrey, and me in one room at the C++ office, like the nice Gavin office. He had this '80s-style thing. And we'd think, okay, what's wrong in our protocol? Then they discussed with the whiteboard changes. Then they'd first say, "Okay, Christoph. If you write a test for this protocol change, then we are in the—" at the same time, you're coding it. "Okay. You're done creating a test. Let's see if they all pass it." If they all pass it, it's, like, done. The feature gets directly released.

And so this isn't done with all the other clients. So they basically had to catch up. There was, like, information update of Yellow Paper. Here's a new test. Here's, like, a little EtherPad description of what the new Yellow protocol looks like, and then please update your clients.

**SPEAKER_03:**
This always got me to a certain point. Sorry. The Yellow Paper always got me to a certain point, but it was always behind the other clients. So I would always find out that, like, I was behind because I went in the morning and connected to the testnet, and I was no longer connecting or I was getting some state root mismatch or something. And then I'd have to, like, go and dig through usually the C++ client. I think there was, like, maybe one or two times where— I can't remember why. I think there was one or two things that went to Geth first, but usually, it was C++. And I'd have to go digging through the newest code to find the changes and then bring them in. And then a few weeks later, I'd see it in the Yellow Paper. So—

**SPEAKER_00:**
Yep.

**SPEAKER_03:**
Yeah. So unlike what you have now, leading into a hard fork, you know, you've got all that discussion and speccing up front and, like, baking the code into the clients, but only enable for a testnet and going through that dance and then ready to go. Yeah. I mean, at that point, as you say, it's kind of, like, done in those clients first and then back later.

**SPEAKER_03:**
It looked like from where I was standing, it looked like there was a lot of competition between the different clients and the developers there. And I think they sort of, like, took pride in having the new thing in as fast as possible. And so that sort of led to an environment maybe where there was not as much discussion. It was like, "I'm gonna throw it in, and then I get the bragging rights."

**SPEAKER_01:**
There was always a hype between the Geth and C++ team about who's the best, and, like, Gavin has a big ego, and Jeff was more like, "Just give it a rest. I just code it." So but, yeah, it was more or less the decision by the three of them. I was basically not playing a very major role in the room and then writing a test for it. But they discussed it. After it was clear, they just did it. But it was pre-launch. After launch, of course, this was different.

**SPEAKER_00:**
So saying about having— sorry. Go on, Jeff.

**SPEAKER_03:**
Oh, I was just gonna say, like, a lot of the changes were just, like, some change in the EVM or pricing or something. And so often, I would, like, freak out in the morning when I wasn't working. But then, like, by 11:00 or noon, you know, AM, I had found, like, "Oh, I see. Like, such-and-such opcode just doubled in price or something." So I would just put that in.

But the big one was RLPX, which is essentially like a big SSL replacement. And that one was, like, freaking me out for a couple of weeks. I was, like, digging around, trying to find any information about that. Eventually, I had to reverse engineer. Maybe that was the one that was in Geth first. I can't remember. But I had to sit there and reverse engineer. I had to, like, run either C++ or Geth and then, like, put lots of logging information in to see what in the world was happening and then print out all the stuff and then find, like, the appropriate, you know, crypto libraries to mimic that.

What was the background on that and how it went in so quickly? And, like, there was nothing in the Yellow Paper about that at all. And when that came in, it was just a shock to me.

**SPEAKER_01:**
Just do you know at which time this came? Because since I was focusing on the Ethereum Virtual Machine at the time, it was more like, okay, I know Gavin— I think it was Gavin doing some optimization. He was always thinking about the long term. So if something would be 10% more efficient, we have to do this. Right? I think—

**SPEAKER_02:**
So I remember, like, there was a DEVp2p, LLp2p website that was released about that time. It still might have been after the giant change went in. So I— we were working together regularly, you know, in the Bay Area at this time. And I think so Jim did, like, 96% of the changeover, but we had, at the time, like, separate processes. One was more like a client and more like a server. We merged them later.

And, yeah, it was like— so there was a big document, one describing, like, how the DHT for peer discovery would go in. But then you needed, like, a way to identify the peers, maybe. And this system kind of gave them an identity with, like, a— you know, in an SSL style. Like, basically, there was, like, a node cert in effect, and then you had to— there were session keys and, you know, this, that, and the other. It was— it took a long time to implement that thing.

But, yeah, I think— maybe, Bob, you would know that the— I think this was someone else wrote this big thing. This might have been Alex.

**SPEAKER_00:**
Yeah. It was Alex.

**SPEAKER_02:**
Yeah.

**SPEAKER_00:**
Alex did that. So saying about sort of documentation or whatever, there was a wiki, right? There was an Ethereum wiki, and a number of things were documented only on the wiki. And I think these kind of wire protocol pieces were part of that. But, yeah, Alex Leverington was the first hire into that Berlin office, and he worked on a few different C++ things, but the main thing he's known for is DEVp2p, which was that common underlying peer-to-peer protocol.

Though you already had libp2p, which is the transport for IPFS— that already existed at the time. So it was a bit of not-invented-here going on. But, yeah, he was there for DevCon Zero as well, and he spoke. Do you remember, Alex?

**SPEAKER_01:**
I was not too much into the peer-to-peer side of the code base. I was more into the EVM and Solidity smart contract side.

**SPEAKER_00:**
I'll tell you what, there's a bit of funny crossover with the later part of yours. Alex Leverington worked with John Garrett on a project called Airlock.

**SPEAKER_01:**
Oh. Remember that. I saw them later. Like, after we did our presentation and had the Slock.it and stuff going, they showed us videos of they were earlier than us. So, yes, they were actually tough time-wise. They did this before we did, but I did not know about it at all. And so we did it more or less in parallel then, and we just launched a bit quicker, like, just going to the public with the project. It has— from their side, it was more like a little tight project. Didn't look like a big company or intended to be. Yeah. I remember this project a lot.

**SPEAKER_00:**
Yeah. So I think that was at the hackathon at the Bitcoin Expo in April 2014 that they did that. And Stephan actually did an interview with them. You can see that on YouTube. You know, this is, like, talking about earlier Ethereum projects. You know? And this is, like, over a year before the mainnet. It's, like, so far back some of these.

But, yeah, like, some of that spec stuff— it was not in the Yellow Paper, and it was just sort of floating around. It was a long time before there was real consolidation of that full client spec. But you managed to do it anyway, Jim. You managed to build the client.

**SPEAKER_03:**
It was a busy week. But I just— it was just notable to me because usually— for at least from what I was seeing, it went from zero to one, like, overnight. I had never heard of it the night before, and then the next morning, it was, like, in the clients and working, and I couldn't connect anything.

**SPEAKER_02:**
Which is normally the pattern, but, yeah, they— this one was, like, the biggest one-time change that I can recall either. Yeah. Yeah. And—

**SPEAKER_01:**
This was pre-launch days. Things had to move fast. There was a lot of pressure going around. It was messy. There was not much coordination between the clients except for maybe some Skype groups. And at the end, yes, we thought that Gavin and Jeff just made decisions and executed as quick as they could. So this all changed after launch. Then things became a bit slower, and people consolidated, and every change was a big thing, rightfully so. Yeah.

**SPEAKER_00:**
Yeah. So back on the timeline, so it was July 2015 that mainnet launched with the Frontier hard fork. And then as you touched on, you had Ming. So Ming's first official day was August 1, 2015, at which point the Foundation had been running for a year or so and was close to out of money, you know, touching on your thinking it would only last for a certain amount of time. You know, a year on that raise, which I think was around $16 or perhaps $18 million, was nearly all gone.

So you had these quite hard decisions about, you know, which part of this grand vision was gonna be funded initially.

**SPEAKER_01:**
Right. And I never talked to her at the time. She felt like, "I have to clean up the whole mess." Like, the paperwork and everything was totally messy, working with lawyers, accountants, and so on, and getting cleanup, basically, of the Foundation. I mean, for me, I did expect it to last something like that. So it was for me, it was clear. They are not making any money. I didn't know, like, how big the reserve was in detail. I think it was, like, I don't know, 5% or something in this range. Like, how much ETH the Foundation held. At the time, there wasn't that much value. The price was, like, 50 cents, €1 or something. So it was clear this would not last forever.

So I was thinking about going back to my PhD, or then I came across this idea about Slock.it and becoming— like building a company. And Slock.it was the idea of maybe similar to Airlock. Smart contracts are essentially permission systems. 90% of a smart contract is who's allowed to do what. In case of ERC-20, it's just who's allowed to send the token or setting an allowance. And in terms of the DAO, it's who can vote for what and make decisions, and then money gets transferred.

So what if we could put this permission system into IoT and then, like, who's allowed to switch on, off, use, change, admin rights, whatever. You put this into a smart contract. And I thought that Ether will never become a currency. Bitcoin was a digital currency. And, actually, if you think— if you talk to Ethereum people at the time, we were not thinking about competing with Bitcoin. Bitcoin was a digital currency. We were building a platform for decentralized applications. Ether was just used to run it.

I once heard the statement somewhere on Twitter where I once said, "Bitcoin is a currency which needs a blockchain to function, and Ethereum is a blockchain that needs a currency to function." This is— I think it's very true. And so back then, I thought, okay, Ethereum will not be used as a currency, but it might be used as a currency for IoT devices. So instead of the Internet of Things, building the Economy of Things. And this is kind of what drove us.

And then we wanted to build this Universal Sharing Network as an application. Back at the time, Uber and Airbnb just became big. We thought, well, all those sharing economy services should run on-chain. So let's build this called the Universal Sharing Network.

And then we thought about how to start something tangible, and then we had the Slock. Actually, it's here in the background. If you see it, it's there. There we go. I have this DevCon One prototype smart lock, which we connected to the Ethereum blockchain using our own software and had this idea of people pay to open the lock, and that's what we presented at DevCon One together with this idea, which actually only came up, like, three or four days earlier, to connect this with a DAO.

And the rest, you know, is history, what happened after that. But we didn't intend— we didn't start Slock.it for building the DAO. We wanted to build the Universal Sharing Network. Then we thought that this is way too big for us. We want to now focus on this Airbnb use case for door locks. And then we thought about fundraising. We talked to a bunch of VCs. I actually remember flying to New York, talking to VCs there. Everybody said no. Then I met Joseph. He said yes, maybe under some conditions. We just did not agree on the terms in detail at that.

But I presented at the Bitcoin meetup in New York, and they all— like, the first application was a Bitcoin application about arbitrage trading. It was, like, kind of boring. Then I came with the door lock. It was, like, super fascinating. You could open the door by paying some Ether. So it went well, but we didn't have any money, so we thought about doing something like an ICO.

But this was now after the launch of Ethereum. So if I started coding an ICO-like smart contract, why should we have the money directly? It could stay in the contract, and then people could vote for giving us part of it. Then we said, well, we could make proposals to it, and then they can vote if the proposal is good or not. Then the money would be released to us.

Then they clicked— why could not everybody make a proposal? Like, everybody could pay it. Everybody can make a proposal, and it's completely open. And we are just one of many service providers to the DAO building this Universal Sharing Network. This was the origin of the DAO. Only, like, again, three days before DevCon One, we actually decided we would go for it and put it into the presentation.

**SPEAKER_00:**
Yeah. Amazing. I mean, so on the timeline again, trying to gauge it. So Stephan was, I guess, Chief Communications Officer or— it wasn't until September 2015. That's when he left. Had you left already by then? Can you remember?

**SPEAKER_01:**
No. I didn't really leave because I was technically a freelancer. Although I was working full-time for it, I didn't have, like, a formal employment contract. So I continued to work, I think, until end of the year, and then I just talked— well, I'll just put down my hours, basically. If you need me, tell me. I just invoice what I'm doing. And but I was really leaving, actually, in December, January. I think the last invoice I had was for December.

And then Stephan left or was— let's say, there's another conversation how he left the Foundation. He was— he didn't agree with some people getting Ether, which is another story for another day, I guess. And but he was really a crucial part in building up this Ethereum community. He put, like, all this meetup culture. The meetup culture didn't really exist like that before. He was going from place to place, finding someone running meetups. So he was very important for that.

And I— I was a coder. My cofounder Simon, who I cofounded with, is also a coder. We needed someone who can talk to the people, can do marketing and this stuff. And we said, well, he has the right address book. He knows the right people. Everybody knows him in the community. I think let's ask him if he wants to join us, and he did. And I think he was a very important part of making the DAO what it was.

Later on, he did some messaging, which I also didn't like. And so he fell a bit in disgrace with what happened then. And I think the community was very, very hard with him because he was not always reacting maybe as he should in some situations after the hack. But, nevertheless, he played a very important part in the history of Ethereum and also, of course, of the DAO.

**SPEAKER_00:**
And so DevCon One was November 2015. So that was announced earlier in the year, I think ended up being canceled, you know, because the Foundation were basically, you know, the same running out of money piece. But then primarily with ConsenSys funding and support, you know, hey, it's back on.

So that was in London and, you know, significantly larger event, obviously, than DevCon Zero because it was the first, you know, public Ethereum outing with Microsoft as a headline sponsor. You had Nick Szabo speaking as well. Maybe Satoshi, maybe not Satoshi.

**SPEAKER_02:**
I don't think he's— he alluded to it in the presentation. It was funny.

**SPEAKER_00:**
So, yeah, how was that for you then, Christoph? What was, you know—

**SPEAKER_01:**
It was totally different than DevCon Zero because this felt like now we're going out in the world and show it to the public. It was a fancy space in London. It was a really fancy, like, almost cathedral-looking space, 2% I think. Again, we had Gavin talking about the vision of Ethereum. And if you look at the talks being given, I really think entrepreneurs today should just rewatch them because they all have been ten years too early. Be it about building identity solutions— I think it was Boardroom doing, like, governance on-chain, many, many ConsenSys startups, of course.

We were thinking about, well, let's connect IoT to the blockchain. Again, all of that ten years too early. I remember also Simon speaking about— not my brother. I forgot his last name. But Simon speaking about, like, everybody getting a token. Like, we predicted this token economy would now thrive, which happened.

So it was a great place to be. Everybody was looking into the future, building the future. It was very, very exciting. It was very important that ConsenSys was funding this. It was crucial, this step from DevCon Zero— showing Ethereum is live now. We show you what we will build with it. But still, there were no applications running. It was all visions and thinking.

And so this— one reason why when we then did the DAO, the DAO was held— like almost the first real thing you could do with Ethereum. That's why so many people jumped onto it. And then maybe just finishing this off, the narrative changed. It was not anymore a DAO for the Universal Sharing Network, but maybe because of the curators we chose, which were, like, important figures in the Ethereum space and many other things, it turned into an investment fund or, like, an index fund for Ethereum applications.

Because now, like, after $20, $30, $40 million was in, it was clear this was not just money for Slock.it and the USN. This was money for more use cases, and more people applied for it. It became like every decentralized application or many of them— everyone was saying, "I'm applying for getting funding from the DAO." So the DAO would pump all the applications. So it's like, you invested in Bitcoin ten years, five years ago, became rich. Now you invest into Ether, went well, and now you can invest in the application layer. You do this through putting money to the DAO.

This was not a story we told, not how we intended it, but it's how the narrative changed during the fundraising and then became that big.

**SPEAKER_00:**
Yeah. I mean, it was interesting you're saying that. Yeah. You're muted, Bob. I cannot hear you. Or maybe it's just me? Can you hear me? I can still hear— I hear him.

**SPEAKER_01:**
Sorry. I have an issue here with my— this is me. System—

**SPEAKER_00:**
So now I'm back. Can you hear me? Can you hear me, Christoph?

**SPEAKER_01:**
No. I cannot hear you anymore. Let's—

**SPEAKER_03:**
Can you hear me now? Yeah. Yeah. I can hear you. I could always hear you. For some reason—

**SPEAKER_00:**
Oh, we've heard you. We hear you.

**SPEAKER_03:**
This was, like, me an hour ago, by the way.

**SPEAKER_02:**
StreamYard.

**SPEAKER_01:**
Okay. My audio is completely broken, so I will try to fix this. We can continue.

**SPEAKER_03:**
I basically had to, like, close it and come back again with my earphones, but I don't know.

**SPEAKER_00:**
Perhaps while we're waiting, Karen and Jim, you could talk a little bit about the Strato launch at that—

**SPEAKER_02:**
I thought you were gonna say you could sing a little song. I got nervous for a second there. You know, okay. So in this period of time—

**SPEAKER_01:**
Yeah. Let me just reconnect. Just turn off and on again.

**SPEAKER_02:**
We were working as part of ConsenSys, and one of the kind of marketing business development people at the time, Andrew Keys, primarily had put together a partnership with Microsoft. I don't know if they ended up cosponsoring DevCon One per se. They had headline— yeah. They put money in for that. Because they also, like, paid for a bunch of PR and all those sort of things too.

And so we had maybe a month or two lead time to work with them. And so the idea was that, you know, they've got cloud infrastructure. It's a good place to run blockchain nodes. They also have corporate clients that were actually very interested in the technology. And so we worked pretty closely with them in the run-up to make our software available on the Azure cloud, as did Roman of the Java client, which to some extent was everyone's preference because people know Java, you know, in the enterprise world.

But I think they— we sort of stuck with it quite a bit longer than Roman did. And, you know— so Blockchain as a Service was the big announcement. That was December 2015. Was it November?

**SPEAKER_00:**
November.

**SPEAKER_02:**
November. There was— once the announcement happened, there's a little tick in the Microsoft stock price, which we were, like, "Woah." Like, there's a little bump there. And a lot of excitement for sure. I got a million phone calls after that. That was, like, you know, good feeling of being the hotness. That only happened so many times in someone's life. You know?

But tremendous interest on the back of the Blockchain as a Service announcement. We did a live demo. It was so fun. The Internet, you know— it gets in vogue to make fun of the UK these days on X, etcetera. The Internet in the conference facility was not so good. So I was very worried about the transactions actually going through, but they did during the live demo. I think there's footage of it somewhere.

**SPEAKER_01:**
Can you hear us again there, Christoph? Yes. I can hear you. I hope you can hear me.

**SPEAKER_00:**
Okay. So the demo that you did at DevCon One, again, another iconic event because, yeah, you have that physical smart lock just sitting there on your shelf, and, you know, it rotates, right? You know? You did your transaction.

**SPEAKER_01:**
We just had a Raspberry Pi connected via— I think it was ZigBee or Z-Wave back then to the door lock. And on the Raspberry Pi, we had actually an Ethereum client running. We had a smart contract on-chain where you could send some money to it or Ether actually. If it received some Ether, it would open up. This was basically the demo. But it was cool to see something physical. You're talking about using Ethereum for, as I said before, the Economy of Things connected to IoT devices.

Since most of the people in the room were still nerds and devs, they loved that kind of stuff. And there was also the kettle, wasn't there?

**SPEAKER_00:**
Yes. There was also a kettle.

**SPEAKER_01:**
Maybe just a smart plug, like a power plug. We could also turn it on, off, same protocol, same thing. So we just wanted to show it's not just a door lock company because, actually, we are not producing those. We're just connecting existing door locks to it. We also showed this idea of the Universal Sharing Network. Everything which you can turn on, off, or lock and unlock could be now connected to this network, and everybody could, like, put almost everything in there, like a washing machine. You pay for using the washing machine or a bicycle lock, even padlocks connected to it. So you could have, like, your locker room and have a padlock in front of it and sell whatever's in there by having someone pay to open the padlock. This was the generic idea.

We got some VC money later after— like, in 2017. We built it. Nobody used it. It was, like, not just too early. It was, like, everything for everyone all at once and, of course, nothing for no one. The app was not great, so we failed B2C-wise at Slock.it. We then turned into more consulting projects to build Incubed, which was an IoT client, made some money with that, and about 50 people actually— we employed at the time in 2019 when we sold the company to Blockchains LLC, Jeffrey Berns. Another story.

**SPEAKER_00:**
So I remember speaking to Stephan at the time. So Stephan was involved with that demo, right? It was Stephan who came up on stage to make his little cup of tea with the kettle there. But I remember speaking to him that he'd been concerned about what the reception for him would be like, you know, having had this passing of ways with the Foundation just two months before. But he was saying it was all very— it was all very friendly, and people, you know, were very excited about the project.

**SPEAKER_01:**
Right.

**SPEAKER_00:**
And saying actually about IoT and pieces. So in January 2015, you had a demo that happened at the Consumer Electronics Show, CES in Vegas, which was a collaboration between IBM and Samsung. So the aforementioned Henning Diedrich was part of that. And that again was months before mainnet, but you had a proto-Web3 stack there, which was, I think, POC-5 of Ethereum. You didn't have Whisper. You had another thing called Telehash, and you didn't have— you had BitTorrent.

So there was this proto-Web3 stack there, and they had demos like a washing machine buying its own detergent and scheduling its own repair. So, yeah, that was happening a little earlier. And, yeah. So, I mean, so Slock.it itself did a number of these different products, right? There was something with electrical charging and something to do with toll roads. Is that right?

**SPEAKER_01:**
Right. We had a prototype running with RWE, an energy company in Germany. They're doing, like, a lot— at the time, most of the charging stations. So this was in— we got a lot of attention, of course, also after the DAO hack and all of that. And so— it's kind of why we became a consulting company because so many asked us, "Could we do a prototype with you?" Because there were not many Ethereum builders at the time. So we had been building on Ethereum now since, oh, one year or two years, which you could not find anybody doing this.

So we were building lots of nice prototypes and some almost production stuff and always related to IoT devices connected to the blockchain. This was our core business, and on top of this, we built those prototypes. We did a lot of work for the Energy Web Foundation. I don't know if you're familiar with them. This was in Switzerland. They are kind of a fork of Ethereum focusing on all the energy use cases. We built most of their stuff in 2018, '19, until they hired their own developers. Gavin was also part of this for a while.

So, yes, this was— if you remember this time, you'd say that there was so much enterprise interest. Enterprises at the time were just learning, looking into this, wanted to build prototypes, not yet production stuff. So there was a huge demand for— for blockchain experts for doing consulting, for going to conferences, explain to them what a blockchain is. But at every tech conference, you need some blockchain talk. And this was kept— it was mostly us. And they paid sometimes, like, €4,000 for a talk. Like, as a company, you said, "Well, we need the money. Let's go there."

So of course, you also have to think about us as persons. Simon and me, we didn't get any money for almost a year. Like, we worked for— we were not rich people. We just come from ordinary families. And we said, "Well, we can work for, like, three to four months without a salary. Let's build the DAO, and then the DAO becomes big. The DAO is paying Slock.it to build it."

Of course, after the hack, it was clear there will never ever be a payment. So we made zero money out of the DAO. So we needed to start doing some work, and this was in the beginning. "Let's do consulting for those large companies." This is how Slock.it began to survive. Many people said you cannot— you'll never bury Slock.it after what happened. Like your name is burned forever.

We decided to stay as a team, I mean, as a founder team. We own our mistakes. Maybe we are open and transparent about it as much as we could. It was, of course, an honest mistake. We can— it could be another session just for the DAO. I mean, the DAO is a lot of topics. I just— I'll put here very shortly. Just talk about it from a company perspective.

And then Stephan, well, he was— he was trying to get VC money. And I— we were doing those consulting gigs. And once we had VC money, what happened as a company was we got $2 million of dollars, and then we built the product, hired people for that, got more and more consulting gigs. So we always said, "Well, let's do them and just hire more people." And, yeah, we had, like, 50 people, five or ten doing the product and 40 people doing consulting.

And then we got bought by Jeffrey Berns from Blockchains LLC. Remember maybe at DevCon Three, I think, where it is— a big announcement in Prague, right? He wanted to build a city. I think I loved the vision. He obviously had money. He wanted to build it on top of Ethereum mainnet. I was thinking about how maybe I can channel those billions into the right direction. Building is all as intended on Ethereum mainnet, which was working fine for the beginning. And then I found out once you're an entrepreneur, you never can be an employee again, and so I had to leave.

So but it's maybe— actually, it's too far in the future. I mean, that's one thing I think I have to say here because you talked about DevCon One and you skipped a little bit DevCon Two. You said at DevCon One, Stephan Tual was very concerned how people perceive him, and they were very gentle, forgiving, and nice to him. So he was well received, and then he built the DAO community.

I was super worried to go to DevCon Two because it was after the DAO hack. I was, like, seriously thinking someone might beat me up there. Like, I kind of almost destroyed Ethereum with the hack and so much attention to it and all the money lost for some people or, like, the trust is gone. Like, it depends on how you view it. So but when I went to DevCon Two, people were so nice, so forgiving, basically, hugging me.

But I was giving a talk there, and the only thing I didn't like was the Foundation telling me I was not allowed to speak about the DAO, which was, like, "What? Like, I am speaking here to the same community. How can I not speak about the DAO?" And so I talked about a pretty boring talk about security, and I think every second talk was about security at DevCon Two. It was just about how do we get those smart contracts secured. So I kept a rather boring talk.

But in the end, I just said, "Well, thank you for your understanding," and "It was a rough, hard time," and so on. And there were, like, somewhat— there were standing ovations. I remember becoming emotional because this was— I did not expect this. I really expected, like, "Guy, you messed up Ethereum. Like, you almost lost it all." So I think this just speaks to the Ethereum community. How we treated Stephan, how we treated me— even though mistakes were made, honest mistakes, at least from what I can tell.

This is such a great community of really nice people who really want to change the world, are capable, and also now financially capable of really doing things.

**SPEAKER_00:**
I was watching that video quite recently, actually. And it was quite— cut off a little bit at the end. The— it was quite— the end is— yeah. You know, it was quite a long ovation there. And, yeah, you could certainly see that emotion in you. And that's when we first met actually. It was in Shanghai for DevCon Two, I remember. It was on the sidelines there in that main conference hall. And, yeah, it was lovely to see that. That's for sure.

Okay.

**SPEAKER_02:**
Yep. I think good note. Just Bobby, were you the one who tried to impose an hour to half-hour to hour rule or a solid one-twenty right here?

**SPEAKER_00:**
Sounds good. Maybe we've met, you know, we've reached a, you know, a good kind of endpoint, I guess. So what happened after Blockchains LLC for you then?

**SPEAKER_01:**
So because of time, I'll keep it short. So, yes, we got bought by Jeffrey Berns, Blockchains LLC at the time. Again, the reason for this was he wanted to build a new city in the desert. He wanted to do all IoT, all Ethereum from scratch as a developer dream, building from scratch on the greenfield on top of Ethereum with our tech.

And I felt comfortable at the beginning. In the end, I felt like we need to release stuff, and there were some voices at the company which didn't want to release until, like, a very, very big product was done. For many reasons, that didn't happen. I don't want to get into that too much. So after two years, I left Blockchains. Back then, it was called Inc. They made a change in their name.

And I did— for six months, I did really nothing. I forced myself to do nothing, which was great after so many stressful years. And then I started a venture studio called Corpus Ventures where we tried out many different ideas. We had em3, which was a decentralized messaging protocol, GasHawk—we can save transaction costs on Ethereum. What else did we have?

We had domain name stuff, but we didn't release it at the end. But the biggest one was Tokenize.it. And this was being— we built something for German—for now, German startups. In the end, we want to do it all over Europe. We're just tokenizing their shares and do fundraising.

So in summary, it's like a Web3-based AngelList for Europe. It's the one-sentence description for Americans also to understand. You know, AngelList—that's a great tool for business angel investing. We want to do the same for Europe, for all countries there, and build it on-chain. So tokenizing all those shares and enabling private as well as public fundraising. So some call it legal ICOs, if you want, but also for private fundraising.

Our customers currently— maybe a good way to end this—there's now more than 400 investments from more than 320 business angels at more than 50 companies. Those are traditional German GmbHs raising from super conservative business angels doing it completely on-chain. They are paying in stablecoins, getting their tokenized shares in their non-custodial wallet. They're all getting a Gnosis Safe wallet from us using Privy for login. So we build it as intended, and we get normal people to use it.

For me, this is kind of a dream come true because I'm— I love the Web3 bubble. I love this community. I love to work inside there. But for me, Tokenize.it is a way to make this technology available where it belongs, like to startups and investors outside of our Web3 bubble. And I'm super, super happy that I could keep up those values. They have a complete platform that is non-custodial. They have their Safe on Ethereum, holding their tokens, paying in stablecoins.

So I'm very happy to see this. Over the next years, we want to basically roll out this all over Europe and become, yes, the Web3-based AngelList for Europe. That's the goal.

**SPEAKER_00:**
Fantastic. So hope to see you at DevCon Eight.

**SPEAKER_01:**
Me too. I'm looking forward to it. And as of now, I don't intend any change. Stick to Ethereum. I love the community. I continue building and try to get a lot of people using it.

**SPEAKER_00:**
Have you been to every DevCon?

**SPEAKER_01:**
Yes. Yes. I've been to every DevCon. The last one was actually the first one that I didn't give a talk, and I also went to every EthCC except for one that was during COVID. There was some reason I couldn't come. But, yes, I'm actually— I intend to continue to come to every DevCon. It's like you meet the people, like, of course, and many others. It's just a sweet spirit there, nice community. I love seeing how it all grows. Listening to those exciting talks. I mean, for Tokenize.it, it's not as relevant. It's not like our customers or— it's tech, of course. We're just doing an ERC-20 token on Ethereum. It's super easy. Not deep tech.

Sometimes I miss doing deep tech, but, well, I just enjoy being there, seeing what all happened. And remembering those magic days, and just— like, only once in a lifetime or two times in a lifetime, you have this moment where everything comes together at the right time, the right place, the right people. This certainly— those, like, one and a half years I worked for Ethereum are definitely, like, the prime of my career in terms of who I worked with, what we accomplished, the impact we had on the world, and the sweet cypherpunk spirit there and what we did there. It was really great. I always sometimes get emotional thinking about this and meeting those people again at DevCon.

**SPEAKER_00:**
Fantastic. Well, thank you for all your contributions to that success.

**SPEAKER_01:**
Likewise.

**SPEAKER_00:**
All the best. Okay. Oh, just one more. Where can we find you?

**SPEAKER_01:**
You can find me usually on Twitter for the Ethereum people, C-H-R. Of course, I have a complicated name, not many vowels in there, but you'll find it. Or, of course, on LinkedIn. Actually, for my company, I'm more active on LinkedIn, which I was never before. That's where we get our clients as Tokenize.it. Yeah. But, usually, you can find me on Twitter or follow me there on LinkedIn.

**SPEAKER_00:**
Excellent. Okay. Thanks so much. Have a great day.

**SPEAKER_01:**
Thank you, too. It was great talking to you. Bye-bye.

**SPEAKER_00:**
Bye.