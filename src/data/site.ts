// All site content lives here. Edit this file to update the page.

export const profile = {
  name: 'Kevin Kraus',
  role: 'Software Engineer',
  pitch: 'I turn ideas into working software and help teams scale it, with AI built in properly.',
  location: 'Hamburg',
  email: 'hello@kevinkrs.com',
  linkedin: 'https://www.linkedin.com/in/kraus-kevin/',
  github: 'https://github.com/kevinkrs',
};

export const intro = [
  'I love building things, from a first idea to something real people use.',
  'I’ve been curious about AI systems since my undergrad studies. Now agentic AI is taking over the world, and I build with it every day.',
  'Right now I’m reading about AI ethics and security.',
];

export const services = [
  {
    title: 'From idea to software',
    text: 'You have an idea. I build it into a working product, end to end.',
  },
  {
    title: 'Scaling your software',
    text: 'Your product works and is growing. I help your team take it further.',
  },
  {
    title: 'AI that does real work',
    text: 'I build AI agents into your systems and make sure your team can rely on them.',
  },
];

// Only organisation, position, location and an optional one-line note are shown.
export type Row = { org: string; title: string; location: string; note?: string };

export const experience: Row[] = [
  {
    org: 'BCG Platinion', title: 'AI Architect', location: 'Hamburg',
    note: 'Agentic pipelines that write, review and test code in a regulated MedTech setting.',
  },
  {
    org: 'HIVESOUND GmbH', title: 'Co-Founder & AI Lead', location: 'Hamburg',
    note: 'Built a voice AI assistant for beekeepers, bootstrapped the idea, won the AI Ideation, EXIST and InnoFounder scholarships, and now serves 1,000+ beekeepers.',
  },
  {
    org: 'UKE', title: 'Scientific Research Assistant', location: 'Hamburg',
    note: 'Applied NLP research in clinical informatics, with a peer-reviewed publication.',
  },
  {
    org: 'Self-employed', title: 'Full-Stack Developer', location: 'Hamburg',
    note: 'Co-developed PLANIT//PRIMA, a data protection platform, with FastAPI and Vue.js.',
  },
  {
    org: 'Celver AG', title: 'Working Student, Data Engineering', location: 'Hamburg',
    note: 'Data pipelines and customer onboarding for a data analytics platform.',
  },
];

export const education: Row[] = [
  {
    org: 'University of Hamburg', title: 'M.Sc. Information Systems', location: 'Hamburg' },
  { org: 'Yonsei University', title: 'M.Sc. Computer Science (Exchange)', location: 'Seoul' },
  { org: 'Karlsruhe Institute of Technology', title: 'B.Sc. Industrial Engineering', location: 'Karlsruhe' },
];
