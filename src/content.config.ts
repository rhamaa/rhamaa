import { z, defineCollection } from 'astro:content';

const experience = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    company: z.string(),
    location: z.string().optional(),
    startDate: z.coerce.date(),
    endDate: z.coerce.date().optional(),
    responsibilities: z.array(z.string()).default([]),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false)
  })
});

const education = defineCollection({
  type: 'content',
  schema: z.object({
    institution: z.string(),
    program: z.string(),
    location: z.string().optional(),
    startDate: z.coerce.date(),
    endDate: z.coerce.date().optional(),
    notes: z.array(z.string()).default([]),
    draft: z.boolean().default(false)
  })
});

const certificates = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    organization: z.string(),
    date: z.coerce.date(),
    link: z.string().optional(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false)
  })
});

const projects = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    category: z.enum(['IoT', 'Software', 'AI/ML', 'Cloud', 'Other']).default('Other'),
    image: z.string().optional(),
    tech: z.array(z.string()).default([]),
    bullets: z.array(z.string()).default([]),
    link: z.string().optional(),
    github: z.string().optional(),
    date: z.coerce.date(),
    draft: z.boolean().default(false)
  })
});

const posts = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    author: z.string().default('Firdaus Nuur Rhamadhan'),
    image: z.string().optional(),
    tags: z.array(z.string()).default([]),
    category: z.string().optional(),
    draft: z.boolean().default(false)
  })
});

export const collections = { experience, education, certificates, projects, posts };
