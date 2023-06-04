---
Coding Level:
Coding Ideas:
Category: story
Title: Sharing is Caring
Story Genre:
Story Content:
Author: Emilia Tech4
Story License: CC BY-NC-SA 4.0 International
Image License:
Image Source:
Audio Source: Coqui TTS https://github.com/coqui-ai/TTS
Parental Rating: 6+
Language: en
---

# Sharing is Caring

This story is dedicated to the famous Christmas hacking taking place during
advent.

Scene: Santa and the elves Cody, Louisa, Sleepy, Noisy, Buildy, Calcy, Singy,
Sneaky and Drinky.

And Santa excitingly, but also slightly stressed, looks at his overly punctual,
never late watch and shouts: “Elves, let’s move it, move it, the rucksacks are
finally on board, we need to depart!”

The elves happily, but also utterly exhausted, take their cushioned Christmassly
decorated seats in Santa’s overloaded sleigh! Coloured presents, fir tree
branches, reindeer equipments, cookies, open milk jugs, and a lot of personal
traveling items are on board of this sleigh (yes, almost unbelievable, but some
elves heavily exaggerated on the allowed amount of personal baggage). But Santa
was courageously relaxed about this, as he knows in the end that some elves,
mostly always the same ones, exceed the allowed baggage limit also when they
travel on planes! On top of the vast amount of personal belongings, each elves
carries a lot a lot of sweets: 100 pieces of cookies, caramel bonbons, chocolate
Christmas trees, chewing gums, candies and ginger breads each in their
rucksacks.

“Yeyy”, said Noisy, “we’re going on a road trip”, while heartily listening to
Christmas carols on his inherited old school disc man! Excitement arises, and
the elves’ hearts start beating faster, except for the really tired elves,
they’re bound to fall asleep, among them is Sleepy. Louisa, also known as the
bookworm elf, deepens into her late grandma’s favorite Christmas story book.
Cody, however, is doing the 5th day of Christmas hacking today on his new (N-1)1
computer, as he somehow found a way to get the challenge a day prior. Buildy, on
the other hand, is building a wooden mini sleigh, whereas Singy is singing,
Calcy is doing math and Drinky is drinking cinnamon latte.

And then there is Sneaky, who, because everyone else is doing something,
decides, out of sneakishness, to take away food from Louisa’s bag. Noisy sees
this, thinks to himself: “How unfair is that, so typical of Sneaky”; but then
decides to also take food from other elves’ bags as well. And the sneakishness
among the elves continues. Santa isn’t so happy about that and thus wants to
know two things:

## Questions

1) Print the highest amount of food type that each elf carries in the end. (eg.
   The highest amount of food type per elf). Round the amounts of food types to
   full numbers. Output should be:

- Cody = Print highest amount of food type for Cody: Either cookies or caramel
  bonbons or chocolate Christmas trees or chewing gums or candies or ginger
  breads; and the respektive amount rounded to full numbers.
- Louisa = Same procedure
- Sleepy = Same procedure
- Noisy = Same procedure
- Buildy = Same procedure
- Calcy = Same procedure
- Singy = Same procedure
- Sneaky = Same procedure
- Drinky = Same procedure

2) Calculate the total amount of all food types per elf in the end. Print which
   elf has the highest amount of total food types and the respective amount.
   Round the amounts to full numbers. Output should be:

- Cody = Sum of Cody's cookies and caramel bonbons and chocolate Christmas trees and chewing gums and candies and ginger breads; and the amount rounded to full numbers.
- Louisa = Same procedure
- Sleepy = Same procedure
- Noisy = Same procedure
- Buildy = Same procedure
- Calcy = Same procedure
- Singy = Same procedure
- Sneaky = Same procedure
- Drinky = Same procedure

Print: The elf's name with the highest amount of food types and the respective
amount rounded to full numbers.

Santa, together with his elves, decides that after coding this story, they would
put all their foods on the table and share. And the moral of the story is:
Sharing is caring!

## Non-Codable Questions

Take a Guess.

1) The story contains many (pop) cultural references to books, music, tech,
   etc.; what are they?
2) Before coding take a guess: Which elves do you think carries the most food
   pieces?

## Documentation

### Sitting positions of the elves in the sleigh

Reindeers santa reindeers

Front of the sleigh:

| 1.    | 2.     | 3.     |
| ----- | ------ | ------ |
| Cody  | Louisa | Sleepy |
| Noisy | Buildy | Calcy  |
| Singy | Sneaky | Drinky |

At the beginning each elf has 100 pieces of each food type, which are: cookies,
caramel bonbons, chocolate Christmas trees, chewing gums, candies and ginger
breads.

- Every elf having a neighbour to the right takes 2 cookies each from that
  neighbour, and 1/6 of the combined amount of stolen cookies gets eaten.
- Every elf having a neighbour to the left takes 5 caramel bonbons each from
  that neighbour, and 1/3 of the combined amount of stolen bonbons gets eaten.
- Every elf in the middle that has neighbours left and right, takes from them
  each 3 chocolate Christmas trees, and none get eaten.
- Every elf having an elf sitting behind them, takes 6 chewing gums each from
  that elf, and 1/4 of the combined amount of stolen cheewing gum gets eaten.
- Every elf having an elf sitting in front of them, takes 7 candies each from
  that elf, and 1/2 of the combined amount of stolen candies gets eaten.
- Every elf having an elf sitting in front and in the back of them, takes 8
  ginger breads each from that elf, and 2/5 of the combined amount of stolen
  ginger breads gets eaten.

### See example below for the Cookies

- Cody takes two cookies from Lousia
- Noisy takes two cookies from Buildy
- Singy takes two Cookies from Drinky
- Louisa takes two cookies from Sleppy
- Buildy takes two cookies from Calcy
- Sneaky takes two cookies from Calcy

-> All in all 2x6 cookies have been stolen (=12 cookies); 1/6 of this amount (=
2 cookies) gets eaten; so 10 stolen cookies remain, which are equally
distributed among the cooky thieves: 10/6 = 1.66

In the end:

- Cody has: 100 + 2 + 1.66  cookies
- Noisy has: 100 + 2 + 1.66  cookies
- Singy has: 100 + 2 + 1.66  cookies
- Louisa has: 100 - 2 + 2 + 1.66 cookies
- Buildy has: 100 - 2 + 2 + 1.66 cookies
- Sneaky has: 100 - 2 + 2 + 1.66 cookies
- Sleepy has: 100 - 2 cookies
- Calcy has: 100 - 2 cookies
- Drinky: 100 - 2 cookies

And then the next task is repeated in a similar way.

After a copious candy and sweets eating feast, all the elves and Santa fall
contentedly asleep, as the reindeers continue the journey in the darkness of a
December night, sharing and eating up the rest of the candies.
