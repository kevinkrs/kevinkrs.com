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
  "As an engineer and builder, I turned my love for creating things into my job a couple of years ago. From rough idea to a working prototype to a fully fledged product – I've cycled through this process many times in the last couple of years and I'm still fascinated by it every time I start something new. In times of AI the possibilities are nearly unlimited and I'm quite keen to find out what comes next.",
  "Machine Learning and Artificial Intelligence have had my curiosity since my undergrad days in Karlsruhe, through Seoul and Hamburg. Since then I’ve built expertise throughout ML and for the last two years in agentic AI systems leveraging the power of LLMs.",
  "Agentic AI is taking over the world and reshaping industries, and I'm happy I get to build with it every day.",
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
    title: "AI that gets shit done",
    text: 'Unsure how to leverage the newest tech in your idea or product? Let me help turn an idea into a trustworthy AI pipeline fully integrated into your existing tech landscape.',
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
    note: 'Built a voice AI assistant for beekeepers, bootstrapped the idea, won the AI Ideation, EXIST and InnoFounder scholarships, and now serves 1,000+ beekeepers. Trained anomaly detection models based on datasets of bee buzzing.',
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
