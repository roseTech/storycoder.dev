
const sentences = `
Thank you for a time I will never forget.

Thank you for a time when days seemed endless, even more the nights.

Thank for a time when we thought life was gonna be forever and opportunities were gonna be eternal.

Thank you for a time when we believed there is no tomorrow.

Thank you for a time when we looked at each other and we thought that’s all we need.

Thank you for a time when experience didn’t matter because we didn’t have any.

Thank you for a time when we saw each other and believed we were whole.

Thank you for a time when everything was enough because we didn’t have anything.

Thank you for a time when who we were didn’t matter.

Thank you for a time when things seemed complicated even though they were really very simple.

Thank you for your honesty because we didn’t know any different.

Thank you for a time when life wasn’t planned out.

Thank you for the love that was truly unconditional.

Thank you for the time when living a day meant living the day.

Thank you for a time when we kept on failing and yet this didn’t matter.

Thank you for a time when we forgave each other.

Thank you for the moments that no one can ever take back.

Thank you for the fact that beauty stays forever.

Thank you for the belief that to this day, could I ever go back, I’d do it all again, right the way it was.
`;

const prefix = 'Thank you for';
const sorted = sentences.split('\n').filter($ => $.startsWith(prefix)).sort();

console.log(sorted);
