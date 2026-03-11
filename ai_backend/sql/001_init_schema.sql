create extension if not exists "pgcrypto";

create table if not exists users (
  id uuid primary key default gen_random_uuid(),
  email text unique not null,
  full_name text not null,
  role text not null check (role in ('student', 'teacher', 'admin')),
  metadata jsonb default '{}'::jsonb,
  created_at timestamptz default now()
);

create table if not exists subjects (
  id uuid primary key default gen_random_uuid(),
  board text not null,
  class_name text not null,
  subject_name text not null,
  syllabus jsonb not null,
  created_at timestamptz default now()
);

create table if not exists study_plans (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references users(id) on delete cascade,
  plan text not null,
  metadata jsonb default '{}'::jsonb,
  created_at timestamptz default now()
);

create table if not exists question_papers (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references users(id) on delete cascade,
  paper text not null,
  metadata jsonb default '{}'::jsonb,
  created_at timestamptz default now()
);

create table if not exists notes (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references users(id) on delete cascade,
  notes text not null,
  metadata jsonb default '{}'::jsonb,
  created_at timestamptz default now()
);

create table if not exists doubts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references users(id) on delete cascade,
  doubt jsonb not null,
  resolution text not null,
  created_at timestamptz default now()
);

create table if not exists training_questions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references users(id) on delete cascade,
  questions text not null,
  metadata jsonb default '{}'::jsonb,
  created_at timestamptz default now()
);

create index if not exists idx_study_plans_user_id on study_plans(user_id);
create index if not exists idx_question_papers_user_id on question_papers(user_id);
create index if not exists idx_notes_user_id on notes(user_id);
create index if not exists idx_doubts_user_id on doubts(user_id);
create index if not exists idx_training_questions_user_id on training_questions(user_id);
