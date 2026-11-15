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
  "I'm an engineer who turned a love for building things into a job. From rough idea to prototype to a product people use, I've been through that cycle many times, and starting something new still excites me every time. Today I do it full-time as a freelance engineer.",
  "My path into AI started during my undergrad in Karlsruhe and took me through Seoul to Hamburg. Along the way I built deep expertise in machine learning, and for the last two years I've focused on agentic AI systems built on LLMs. With AI, what a small team can build keeps growing, and I'm keen to see what comes next.",
];

export const services = [
  {
    title: 'Full-Stack Software Development',
    text: 'From rough idea to a product people actually use, end to end. Like PLANIT//PRIMA, a data protection platform, and HIVESOUND, a voice assistant now serving 1,000+ beekeepers.',
  },
  {
    title: "AI that gets shit done",
    text: 'AI in production, not in a demo. I trained ML models on real-world data at UKE and HIVESOUND, and shipped agentic pipelines to production at HIVESOUND and BCG Platinion. And I set up coding harnesses like Claude Code with agentic orchestration, so AI writes code your team can trust.',
  },
];

// Only organisation, position, location, an optional one-line note, tech stack and link are shown.
export type Row = { org: string; title: string; location: string; note?: string; stack?: string[]; url?: string };

export const experience: Row[] = [
  {
    org: 'BCG Platinion', title: 'AI Architect', location: 'Hamburg',
    note: 'Agentic pipelines that write, review and test code in a regulated MedTech setting.',
    stack: ['Python', 'Azure'],
  },
  {
    org: 'HIVESOUND GmbH', title: 'Co-Founder & AI Lead', location: 'Hamburg', url: 'https://hivesound.ai',
    note: 'Built a voice AI assistant for beekeepers, bootstrapped the idea, won the AI Ideation, EXIST and InnoFounder scholarships, and now serves 1,000+ beekeepers. Trained anomaly detection models based on datasets of bee buzzing.',
    stack: ['TypeScript', 'PyTorch', 'Flutter', 'LangGraph', 'GCP'],
  },
  {
    org: 'UKE', title: 'Scientific Research Assistant', location: 'Hamburg',
    note: 'Applied NLP research in clinical informatics, with a peer-reviewed publication.',
    stack: ['Python', 'PyTorch'],
  },
  {
    org: 'PLANIT//PRIMA', title: 'Freelance Full-Stack Developer', location: 'Hamburg', url: 'https://www.planitprima.com/de/',
    note: 'Co-developed a data protection platform, from first prototype to product.',
    stack: ['Vue.js', 'Python'],
  },
  {
    org: 'Celver AG', title: 'Working Student, Data Engineering', location: 'Hamburg',
    note: 'Data pipelines and customer onboarding for a data analytics platform.',
    stack: ['Databricks', 'PySpark', 'Spark SQL', 'Azure'],
  },
];

// The tools I build with right now. Bump setupUpdated when you change the list.
export const setupUpdated = 'November 2026';
export const setup: { name: string; note?: string }[] = [
  { name: 'Claude Code', note: 'Trimmed down, with most of its default context switched off' },
  { name: "Matt Pocock's skills · HumanLayer skills", note: 'Repeatable workflows for planning, TDD and review' },
  { name: 'Caveman · Ponytail', note: 'Fewer tokens, smaller diffs' },
  { name: 'Claude Mem', note: 'Memory across sessions (experimental)' },
  { name: 'Herdr' },
  { name: 'Ghostty', note: 'Terminal' },
  { name: 'OrbStack', note: 'Containers' },
  { name: 'Apple Notes · Apple Reminders', note: 'Keeping track of stuff' },
];

export const education: Row[] = [
  {
    org: 'University of Hamburg', title: 'M.Sc. Information Systems', location: 'Hamburg' },
  { org: 'Yonsei University', title: 'M.Sc. Computer Science (Exchange)', location: 'Seoul' },
  { org: 'Karlsruhe Institute of Technology', title: 'B.Sc. Industrial Engineering', location: 'Karlsruhe' },
];
