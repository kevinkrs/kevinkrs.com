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
  "Currently, I work full-time as a freelance engineer.",
];

export const services = [
  {
    title: 'Full-Stack Software Development',
    text: 'From rough idea to a product people actually use, end to end with Vue.js, React and Python. Like PLANIT//PRIMA, a data protection platform, and HIVESOUND, a voice assistant now serving 1,000+ beekeepers.',
  },
  {
    title: "AI that gets shit done",
    text: 'AI in production, not in a demo. I trained ML models on real-world data at UKE and HIVESOUND, and shipped agentic pipelines to production at HIVESOUND and BCG Platinion.',
  },
  {
    title: 'Ship it to production',
    text: "I bring code live for real users on GCP and Azure. I shipped and run HIVESOUND's voice assistant, and took agentic pipelines into production at BCG Platinion.",
  },
];

// Only organisation, position, location, an optional one-line note and tech stack are shown.
export type Row = { org: string; title: string; location: string; note?: string; stack?: string[] };

export const experience: Row[] = [
  {
    org: 'BCG Platinion', title: 'AI Architect', location: 'Hamburg',
    note: 'Agentic pipelines that write, review and test code in a regulated MedTech setting.',
    stack: ['Python', 'Azure'],
  },
  {
    org: 'HIVESOUND GmbH', title: 'Co-Founder & AI Lead', location: 'Hamburg',
    note: 'Built a voice AI assistant for beekeepers, bootstrapped the idea, won the AI Ideation, EXIST and InnoFounder scholarships, and now serves 1,000+ beekeepers. Trained anomaly detection models based on datasets of bee buzzing.',
    stack: ['PyTorch', 'Flutter', 'LangGraph', 'GCP'],
  },
  {
    org: 'UKE', title: 'Scientific Research Assistant', location: 'Hamburg',
    note: 'Applied NLP research in clinical informatics, with a peer-reviewed publication.',
    stack: ['Python', 'PyTorch'],
  },
  {
    org: 'Celver AG', title: 'Working Student, Data Engineering', location: 'Hamburg',
    note: 'Data pipelines and customer onboarding for a data analytics platform.',
    stack: ['Databricks', 'PySpark', 'Spark SQL', 'Azure'],
  },
];

export const education: Row[] = [
  {
    org: 'University of Hamburg', title: 'M.Sc. Information Systems', location: 'Hamburg' },
  { org: 'Yonsei University', title: 'M.Sc. Computer Science (Exchange)', location: 'Seoul' },
  { org: 'Karlsruhe Institute of Technology', title: 'B.Sc. Industrial Engineering', location: 'Karlsruhe' },
];
