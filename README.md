# Reddit Read-Only Reader

A small local Python application for authorized, read-only access to publicly available Reddit content.

## Purpose

This project is intended to provide a local Python workflow for reading and analyzing publicly available Reddit posts and permitted comments.

The application is designed as a personal, non-commercial utility and does not provide a Reddit-facing service.

The user selects the public subreddits and retrieval parameters when running the application.

## Intended API Usage

The application requires read-only access to:

- Public subreddit posts
- Public post metadata
- Public comments associated with retrieved posts
- Public subreddit listings/search functionality where supported

The application does not require write access.

## Actions Not Performed

The application does not:

- Create posts
- Create comments
- Vote
- Send messages
- Moderate communities
- Modify Reddit content
- Follow or manipulate users
- Send automated outreach
- Attempt to bypass Reddit access controls or API limits

## Data Handling

Retrieved content is processed locally for the user's own analysis.

The application does not:

- Sell or redistribute Reddit data
- Train or fine-tune machine-learning/AI models using Reddit data
- Attempt to identify or deanonymize Reddit users
- Match Reddit usernames to off-platform identities
- Infer sensitive personal characteristics about Reddit users

Only the minimum data required for the intended analysis is retrieved.

## Subreddit Scope

The initial intended use is limited to public communities relevant to the topic being analyzed.

Example communities include:

- r/SaaS
- r/startups
- r/CustomerSuccess

The application does not require access to private communities.

The subreddit list is user-selected and may change depending on the topic being analyzed.

## Technical Architecture

The application runs locally as a Python program.

```text
User
  │
  ▼
Local Python Application
  │
  ▼
Authorized Reddit API
  │
  ▼
Public Reddit Content
  │
  ▼
Local Analysis
```

There is no Reddit-facing web application and no automated posting or interaction.

## Why a Local Python Application?

The intended workflow is a user-driven, on-demand reader rather than a Reddit-native application.

The user needs to be able to:

1. Select a public subreddit.
2. Specify the desired retrieval parameters.
3. Retrieve permitted public content.
4. Process the returned content locally.
5. Repeat the process for another public subreddit when needed.

The application therefore requires a local Python execution environment and does not require a Reddit-native user interface.

## Devvit Compatibility

I have reviewed Reddit's current Developer Platform and PRAW-to-Devvit migration documentation.

The primary technical question is whether Devvit currently supports this exact workflow:

> A local, user-driven Python application performing bounded, read-only, on-demand retrieval of public posts/comments from a changing set of public subreddits for local processing.

The application does not require Reddit-native UI, automated posting, moderation, or event-driven Reddit workflows.

If this workflow is currently supported by Devvit, I would appreciate guidance toward the appropriate Devvit API/capability.

If it is not supported, I am requesting the minimum read-only API access necessary for this bounded use case.

## Rate Limiting and Responsible Use

The application is intended to operate within Reddit's applicable API limits and policies.

It does not attempt to circumvent rate limits, authentication requirements, or other access controls.

Requests are intentionally bounded rather than performing unrestricted bulk collection.

## Status

This repository is a minimal demonstration of the intended API integration and access pattern.

It is not intended to be a commercial Reddit application or a public Reddit service.

## License
Personal use only. Not distributed as a public/commercial application.
