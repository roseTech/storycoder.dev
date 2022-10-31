# StoryCoder.dev

ReadMe and Contribution Guidelines – Version of 31st October 2022

--> SEE also website [storycoder.dev](https://storycoder.dev) for easier reading!

Hello everyone

and welcome to the storycoder.dev open source project. This project aims at bringing the beauty of coding together with the beauty of story reading, writing and telling, because the beauty of coding is the story behind it. Or the other way round as well: the beauty of the story is the coding behind it. So both ways work! 

Table of contents of this README:

1. [What is storycoder.dev?](storycoder.dev#what-is-storycoderdev)
1. [How to collaborate](storycoder.dev#how-to-collaborate)
    * [Write and upload a story](storycoder.dev#upload-a-story)
    * [Upload code solutions](storycoder.dev#upload-code-solutions)
    * [Read the Code of Conduct](storycoder.dev#code-of-conduct)
1. [How to contact the community](storycoder.dev#contact-community)


## What is storycoder.dev?
storycoder.dev is an open source project to which anyone can contribute. The project consists of writing stories of all genres (comedy, action, detective, love stories, drama, fairy tales, fiction, historical, etc.). Somewhere in the story, there is code to solve, which can be solved in all programming languages you know, for example Dart, Python, C#, C++, Javascript, Typescript, Java, Ruby, Swift, and many more! The aim is to create stories with the respective coding solutions.

See stories below:

### Story 1: Poseidon's Ice Cubes 🧊🧊🧊⚓️

It’s boat day today ⛵ with beautiful weather at the sea 🌅, and all is packed to seize the day to the fullest, to ‘carpe diem’ 😃, just as famous Roman poet Horace had suggested to do every day. However, for some reason, the mighty water god Poseidon 🔱🧜‍♂ has not enjoyed his drinks 🍹 last night as much as he usually does, and threw a lot of spare ice cubes from the drinks into the sea 🌊! Thus, the water got extensively colder 🥶; to be more specific it is 11.475 Seidons cold now, which is 14 Seidons colder than normally. Thus, today swimming is not allowed. Seidon is the temperature unit of the sea. One Seidon divided by 1.37 equals one degree Celsius. Print the water temperature 🌡️ in both units with max two fraction digit with an equation on a normal, ice-cube free day! (LillyCode, creative commons license CC BY-NC-SA).

Tags:

- Coding Level: Beginner
- Coding Ideas: define digits, division
- Story Content: Greek God, Poseidon, Temperature, Water, Seize The Day
- Story Genre: Historical Fiction

Solution in Dart programming language: 

```dart
void main() {
  double tempSeidon = 11.475 + 14.0;
  double tempCelsius = tempSeidon / 1.37;
  print(‘${tempSeidon.toStringAsFixed(2)}Seidons) = ${tempCelsius.toStringAsFixed(2)}Celsius’);
}
```

--> see solutions in other programming languages on GitHub: https://github.com/roseTech/storycoder.dev

### Story 2: Cruel Teacher 🧹📝

On a beautiful Friday morning, the teacher happily gets her daily latte, the sun shines through her witch-like gray hair, and she carries her beloved morning newspaper 📰, the "Cruel Teacher Times". Happy 😊 she is, because today is exam day 🗒️, where she soothingly sits in the old wooden chair, sipping coffee ☕️ and reading in an undisturbed way while students sweat through her unconquerable exam. To make sure her morning passes as quietly as planned, she enforces strict methods. With her favorite number being 7, with every passing minute that students come late to her computer science exam 💻, they have to increasingly pay a penalty of $7 💸. Ten of her students are late, each arriving one minute later than the student before them, starting just after the tardy bell rings. The teacher is furious, her hair stands up, with her beloved coffee time beeing constantly interrupted. However, she takes comfort in earning money! Print how much money she will have earned in the end. (LillyCode, creative commons license CC BY-NC-SA).

Tags:
- Coding Level: Beginner
- Coding Ideas: for loop, sum up list
- Story Content: Teacher, Coffee, Exam
- Story Genre: Comedy

Solution in Dart programming language: 

```dart
void main() {
  const iterations = 10;
  const p = 7;
  final sum = List.generate(iterations, (i) => p * (i + 1)).reduce((sum, e) => sum + e);
  print(sum);
}
```

--> see solutions in other programming languages on GitHub: https://github.com/roseTech/storycoder.dev


### Vision

The combination of reading and enjoying stories while also coding and/or learning to code is the vision of this project, because life itself consists of stories. The aim is to have many stories with many coding solutions in different programming languages and for beginners to learn coding through stories. 

At the moment, the coding in the stories is simple code, targeted at beginners. However, in the same stories later on, or in further stories, more difficult challenges shall be included for more advanced coders.

### History

The project originally arose by creating stories to learn the Dart programming language and has then expanded to code the stories in other programming languages as well. 

## How to collaborate?

“Oh I like this project! How can I contribute to this open source project?” 😊
There are a lot of ways you can contribute, see below:

I’m a coder, how can I help?

### If you are a coder

- You could solve the coding problems in the stories already written in the programming language(s) you know and upload the solutions in the GitHub repository (github.com/roseTech/storycoder.dev). See below for instructions. 
- You could provide coding documentation for beginners, so they can use the story to learn coding.
- You could write a story implementing coding into it.
- You could simply enjoy reading our stories.
- You could share your IT knowledge for further ideas of the project (UI, making the project available to everybody, implementing new features, new ideas, etc.).

### For everyone

- You could get attracted to coding and learn a programming language by reading the stories and solving the coding challenges, which is one of the visions of the project.
- You could write a story and someone else, a coder, can implement a coding challenge to solve.
- You could use any other skills you have: proofreading stories, marketing, further knowledge, etc.
- You could simply enjoy reading stories.
- You could share our site and tell people about storycoder.dev.
- You could give feedback, share ideas, possibly implement an idea, etc.

### Upload a story

“Awesome; I would love to write and upload a story. How shall I do it?”

Example of a story: 

You can write a story and implement code in it similarly to the stories you already see on the website [storycoder.dev](https://storycoder.dev/). Review the first three stories ever written as examples:

- AAA_Sample_Story_Poseidon’s_Ice_Cubes
- AAA_Sample_Story_Cruel_Teacher
- AAA_Sample_Story_Bazar

(Note: The `AAA_` prefix is only included to force these three sample stories to the top of GitHub.)

The stories and the code solutions are uploaded on another website called github.com/roseTech/storycoder.dev. You can open a free account on GitHub or use your existing one and upload a story in the repository called github.com/roseTech/storycoder.dev. Later on, the story is planned to be uploaded on storycoder.dev as well. 

When uploading, please consider the following:

1. Write a story you want considering the [Code of Conduct](storycoder.dev#code-of-conduct) and implement a coding problem in it. 
1. Choose a catchy title for your story, which will also be the ‘new folder’s title’ of a story. Every story gets a new folder in the GitHub repository, which you will have to create, called `Story_Name`. See how it has been done so far. You can use emojis to make the story more vivid. 
1. Include `tags` underneath your story. What is a tag? A tag is a form to categorize your story, which will be implemented to find your story quicker later on. Write four different forms of tags for the following: 
    * Coding Level: beginner, medium or advanced 
    * Coding Ideas: methods, functions, documentation for beginners
    * Story Content: 3-5 keywords of the story content
    * Story Genre: comedy story, fiction, detective, etc.
1. Upload your story in a new file called `Story_Name.txt`. By uploading the story, other people can read it and write solutions for it, as this is the purpose of this open source project. Later, the story will be put on storycoder.dev.  If you would like to put your name/ artistic name underneath the story as authorship, you can do that. You can even use the Creative Commons license abbreviations from creativecommons.org/licenses/?lang=en to tell the reader what one can do with the story. 
1. If you can code, give a coding solution to the story you wrote and upload it in a new file called Storys_Name.(name of coding language). See the following example: Poseidons_Ice_Cubes.dart.
1. If you don’t know how to implement code because you’re not a coder, you can still write and upload a story, however in a different folder called `stories without implemented code yet`.
1. Get orientation on how to do it with the first three ever written stories on GitHub which are prefixed with `AAA-Sample-Story_`.

### Upload code solutions

1. Read through some stories you like and write the solution code, then upload the solution in the respective GitHub story folder with a new file called Storys_Name.(name of coding language). See the following example: Poseidons_Ice_Cubes.dart.
1. Provide documentation on how to solve your coding challenge for beginners.
1. If there is already a code solution in the programming language you’ve wanted to write a solution in, but you have a different solution, you can add it in the same file. (Please don’t open a new file, so as to prevent multiple files with the same programming language.) Sometimes it happens that multiple readers come up with a different solution, as the coding tasks are embedded in linguistic stories. This is all right and shows the ambiguity of language production and language understanding. Provide documentation for the reader to better understand your solution.
1. Please only upload code that runs properly so as not to confuse learners. Test your code first; see ways to do that below. 

### Code of Conduct
- While writing stories has a large linguistic and artistic component to it, no stories which contain racism, discrimination of any kind, brutality, etc. are allowed.
- No stories with explicit names of people are allowed to protect identities.
- This project adopts the Contributor Covenant Code of Conduct. Please read here: https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.txt. 
- In case of breach of code of conduct, report to info(at)storycoder.dev. 

### Contact community
If you have any questions, ideas, feedback, etc. contact others working on this project on the Discord server called ‘StoryCoder.dev’. If you don’t have Discord yet, you can download it for free on https://discord.com/ .

There is also a contact e-mail info(at)storycoder.dev. Please post your questions etc. on Discord, as they are relevant to all the other contributors as well. 

Hopefully, any of the above-mentioned collaboration ideas appeal to you (or if not, come up with your idea 💡 and we’ll see where/ if we can fit it in) and you would like to collaborate on this project. Please discuss on the Discord server ‘StoryCoder.dev’ how you would like to additionally contribute to this project. 

### Team

The team of storycoder.dev is you! Every single one who contributes in this open source project forms the team! Thank you for your collaboration!

### Thank you note

First and foremost a huge thank you goes to all and every single one of you who has or will collaborate or contribute to this open source project in any shape or form: Thank you very much for your time, devotion, dedication and knowledge that you provide. An open source project like this only works with people like you willing to share and contribute! Thank you very much for believing in the vision of this project! 

## How to test language XYZ (sorted alphabetically)

Clojure

- Web:
  - https://tryclojure.org/
- Linux Setup: apt install clojure
- Linux Run: clojure ./story.clj

C++

- Web:
  - https://www.onlinegdb.com/online_c++_compiler/
- Linux Setup: apt install g++
- Linux Run: g++ story.cpp -o story && ./story

C#

- Web:
  - https://dotnetfiddle.net
- Linux Setup:
  - apt install dotnet-sdk-6.0
- Linux Run: ???

Dart

- Web:
  - https://dartpad.dev/
- Setup: https://dart.dev/get-dart

Erlang

- Web:
  - https://replit.com/languages/erlang

Go

- Web:
  - https://www.onlinegdb.com/online_go_compiler
- Linux Setup: apt install golang
- Linux Run: ???

Java Script

- Web:
  - https://playcode.io/javascript
- Linux Setup: apt install nodejs
- Linux Run: node story.js

Python

- Web:
  - https://www.onlinegdb.com/online_python_compiler
- Linux Setup: apt install python3
- Linux Run: python3 story.py

Rust

- Web:
  - https://www.onlinegdb.com/online_rust_compiler
- Linux Setup: apt install rustc
- Linux Run: rustc story.rs && ./story

Swift

- Swift Playgrounds for Apple iPad: https://apps.apple.com/us/app/swift-playgrounds/id908519492
- Xcode IDE for Mac: https://apps.apple.com/us/app/xcode/id497799835?mt=12

Type Script

- Web:
  - https://www.typescriptlang.org/play
- Linux Setup: ???
- Linux Run: ???
