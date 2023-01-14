
# StoryCoder.dev

ReadMe and Contribution Guidelines – Version of 29th August 2022

--> SEE also website [storycoder.dev](https://storycoder.dev) for easier reading!

Hello everyone

and welcome to the storycoder.dev open source project. This project aims at bringing the beauty of coding together with the beauty of story reading, writing and telling; because the beauty of coding is the story behind it. Or the other way round as well: The beauty of the story is the coding behind it. So both ways work!

Table of contents of this ReadMe:

1) What is storycoder.dev?
2) How To Collaborate
Write and Upload a Story
Upload Code Solutions
Code of Conduct
3) Contact Community


## What is storycoder.dev?
storycoder.dev ist an open source project to which anyone can contribute. The project consists of writing stories of all genres (comedy, action, detective, love stories, drama, fairy tales, fiction, historical, etc.). Somewhere in the story there is a code to solve which can be solved in all programming languages you know, for example Dart, Python, C#, C++, Javascript, Typescript, Java, Ruby and many more! The aim is to create stories with the respective coding solutions.

See stories below:

### Story 1: Poseidons Ice Cubes 🧊🧊🧊⚓️

It’s boat day today ⛵ with beautiful weather at the sea 🌅, and all is packed to seize the day to the fullest, to ‘carpe diem’ 😃, just as famous Roman poet Horace had suggested to do everyday . However, for some reason, the mighty water God Poseidon 🔱🧜‍♂ has not enjoyed his drinks 🍹 last night as much as he usually does; and threw a lot of spare ice cubes from the drinks into the sea 🌊! Thus, the water got extensively colder 🥶; to be more specific it is 11.475 Seidons cold now, which is 14 Seidons colder than normally. Thus today swimming is not allowed. Seidon is the temperature unit of the sea. 1 Seidon devided by 1.37 equals 1 Degree Celsius. Print the water temperature 🌡️ in both entities with max two fraction digit with an equation on a normal, ice-cube free day! (LillyCode, creative commons license CC BY-NC-SA)

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

--> see solution of other programming languages on github: https://github.com/roseTech/storycoder.dev

### Story 2 Cruel Teacher 🧹📝

On a beautiful Friday morning the teacher happily gets her daily latte, the sun shines through her witch like gray hair, and she carries her beloved morning news 📰 paper called ‘cruel teaching methods’. Happy 😊 she is, because today is exam day 🗒️, where she soothingly sits in the old wooden chair, sipping coffee ☕️ and reading in an undisturbed way while students sweat through her unconquerable exam. To make sure her morning passes as quietly as planned for her, she enforces strict methods. With her favorite number being 7, with every passing minute that students come late to her computer science exam 💻, they have to increasingly pay a penalty of $7 💸. Ten of her students are late while dropping in one minute after the other minute right after the regular start. The teacher is furious, her hair stands up, with her beloved coffee time beeing constantly interrupted. However, she takes comfort in earning money! Print how much money she will have earned in the end!(LillyCode, creative commons license CC BY-NC-SA)

Tags:
- Coding Level: Beginner
- Coding Ideas: loop for, sum up list
- Story Content: Teacher, Coffee, Exam,
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

--> see solution of other programming languages on github: https://github.com/roseTech/storycoder.dev


### Vision

The combination of reading and enjoying stories while also coding and/ or learn to code is the vision of this project, because life itself consists of stories. The aim is to have many stories with many coding solutions in different programming languages and for beginners to learn coding through stories.

At the moment the coding in the stories is simple code, targeted at beginner coders to learn to code while enjoying stories.  However in the same stories later on or in further stories, more difficult coding shall be included for more advanced coders.

### History

The project originally arose by creating stories to learn the Dart programming language and has then expanded to code the stories in other programming languages as well.

## How to collaborate?

“Oh I like this project! How can I contribute to this open source project?”
There are a lot of ways you can contribute, see below:

I’m a coder, how can I help?

### If you are a coder

- you could solve the coding problems in the stories already written in the programming language(s) you know and upload the solutions in the github repository (github.com/roseTech/storycoder.dev), see below for instructions.
- you could provide coding documentation for beginners, so they can use the story to learn coding
- you could write a story implementing coding into it
- you could simply enjoy reading our stories
- you could share your IT knowledge for further ideas of the project (UI, making the project available to everybody, implementing new features, new ideas, etc.)

### For everyone

- You could get attracted to coding and learn a programming language by reading the stories and solving the codes, which is one of the visions of the project
- You could write a story and someone else, a coder, can implement a code to solve
- You could use any other skills you have: Proof Reading stories, marketing, further knowledge,  etc.
- You could simply enjoy reading stories
- You could share our site and tell people about storycoder.dev
- You could give feedback, share ideas, possibly implement an idea, etc.

### Upload a story

“Awesome; I would love to write and upload a story. How shall I do it?”

Example of a story:

You can write a story and implement code in it similarly to the stories you already see on the website storycoder.dev. See as example the first three stories ever written:

- AAA_Sample_Story_Poseidon’s_Ice_Cubes
- AAA_Sample_Story_Cruel_Teacher
- AAA_Sample_Story_Bazar

(Note: The beginning ‘AAA_’ is only named this way for these three Sample Stories so they stay on top of Github)

The stories and the code solutions are uploaded on another website called github.com/roseTech/storycoder.dev. You can open a free account on github or use your existing one and upload a story in the repository called github.com/roseTech/storycoder.dev. Later on, the story is planned to be uploaded on storycoder.dev as well.

When uploading, make sure to consider the following points:

1. Write a story you want considering the code of conduct (see below) and implement a coding problem in it.
2. Choose a catchy title for your story, which will also be the ‘new folder’s title’ of a story. Every story gets a new folder in the Github repository which you will have to create called Story_Name. See how it has been done so far. You can use emojis to make the story more vivid.
3. Write ‘tags’ underneath your story. What is a tag? A tag is a form to categorize your story, which will be implemented to find your story quicker later on. Write four different forms of tags for the following:

- Coding Level: beginner, medium or advanced
- Coding Ideas: methods, functions, documentation for beginners
- Story Content: 3-5 Keywords of the story content
- Story Genre: comedy story, fiction, detective, etc.

4. Upload your story in a new file called Story_Name.txt. By uploading the story other people can read it and write solutions for it, as this is the purpose of this open source project. Later, the story will be put on storycoder.dev.  If you would like to put your name/ artistic name underneath the story as authorship, you can do that. You can even use the creative common license abbreviations from creativecommons.org/licenses/?lang=en to tell the reader what one can do with the story.
5. If you can code, give a coding solution to the story you wrote and upload it in a new file called Storys_Name.(name of coding language)  see the following example: Poseidons_Ice_Cubes.dart.
6. If you don’t know how to implement code because you’re not a coder, you can still write and upload a story, however in a different folder called ‘stories without implemented code yet’.
7. Get orientation on how to do it with the first three ever written stories on Github which are marked with ‘AAA-Sample-Story_”

### Upload Code Solutions

1. Read through some stories you like and write the solution code, then upload the solution in the respective github story folder with a new file called Storys_Name.(name of coding language),  see the following example: Poseidons_Ice_Cubes.dart
2. Provide documentation on how to solve your code for beginners
3. If there is already a code solution in the programming language you’ve wanted to write a solution in, but you have a different solution, you can add it in the same file (don’t open a new file), so as to prevent multiple files with the same programming language. Sometimes it happens that multiple readers come up with a different solution, as the coding tasks are embedded in linguistic stories. This is all right and shows the ambiguity of language production and language understanding. Provide documentation for the reader to better understand your solution.
4. Please only upload code that runs properly as to prevent learners form learning a false code. Test your code first, see ways to do that below.

### Code of Conduct
- While writing stories has a large linguistic and artistic component to it, no stories which contain racism, discrimination of any kind, brutality, etc. are allowed.
- No stories with explicit names of people are allowed to protect identities
- This project adopts the Contributor Covenant Code of Conduct. Please read here: https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.txt
- In case of breach of code of conduct, report to info((att))storycoder.dev.

3) Contact Community
If you have any questions, ideas, feedback, etc. contact others working on this project on the discord server called ‘StoryCoder.dev’. If you don’t have discord yet, you can download it for free on https://discord.com/ .

There is also a contact e-mail info((att))storycoder.dev. Please post your questions etc. on discord, as they are relevant to all the other contributors as well.

Hopefully, any of the above mentioned collaboration ideas appeal to you (or if not, come up with your idea 💡 and we’ll see where/ if we can fit it in) and you would like to collaborate on this project. Please discuss on the discord server ‘StoryCoder.dev’ how you would like to additionally contribute to this project.

### Team

The team of storycoder.dev is you! Every single one who contributes in this open source project forms the team! Thank you for your collaboration!

### Thank you Note

First and foremost a huge thank you goes to all and every single one of you who has or will collaborate or contribute to this open source project in any shape or form: Thank you very much for your time, devotion, dedication and knowledge that you provide. An open source project like this only works with people like you willing to share and contribute! Thank you very much for believing in the vision of this project!

## How to test language XYZ

(sorted alphabetically)

| Language    | Webpages                                                |
| ----------- | ------------------------------------------------------- |
| Bash        | https://www.mycompiler.io/new/bash                      |
| C#          | https://dotnetfiddle.net                                |
| C++         | https://www.onlinegdb.com/online_c++_compiler/          |
| Clojure     | https://tryclojure.org/                                 |
| Dart        | https://dartpad.dev/                                    |
| Erlang      | https://onecompiler.com/erlang                          |
| Go          | https://www.onlinegdb.com/online_go_compiler            |
| Haskell     | https://replit.com/languages/haskell                    |
| Java        | https://www.sololearn.com/compiler-playground/java      |
| JavaScript  | https://playcode.io/javascript                          |
| Kotlin      | https://play.kotlinlang.org                             |
| Perl        | https://onecompiler.com/perl                            |
| Prolog      | https://www.jdoodle.com/execute-prolog-online/          |
| Python      | https://www.onlinegdb.com/online_python_compiler        |
| Ruby        | https://replit.com/languages/ruby                       |
| Rust        | https://www.onlinegdb.com/online_rust_compiler          |
| Swift       | https://www.tutorialspoint.com/compile_swift_online.php |
| Type Script | https://www.typescriptlang.org/play                     |

Your languages is not on this list? Try one the following internet pages:

- https://www.jdoodle.com/
- https://onecompiler.com/
- https://www.onlinegdb.com/
