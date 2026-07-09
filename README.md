# Materials Atlas

Materials Atlas is a curated map of Computational Materials Science.

Its purpose is to reduce years of exploration into a coherent understanding of the field: what matters, why it matters, where to start, what to learn next, who is shaping the field, which tools are standard, which papers changed the field, which software is actually used, and which problems remain unsolved.

Materials Atlas is built for understanding before collection. Every page should reduce uncertainty for a reader trying to enter, study, practice, or contribute to Computational Materials Science.

## What This Is

Materials Atlas is an engineering field guide, graduate reading roadmap, research atlas, and ecosystem map for Computational Materials Science and adjacent fields.

It is intended to help readers answer questions such as:

- What is this field?
- Why does it matter?
- Where should I start?
- What should I learn next?
- Which ideas are foundational?
- Which papers changed the field?
- Which tools are considered standard?
- Which datasets are trusted?
- Who is shaping the field?
- Which institutions and companies matter?
- What problems remain unsolved?

## What This Is Not

Materials Atlas is not:

- a wiki
- a personal knowledge management system
- a second brain
- a note dump
- a collection of bookmarks
- a dashboard
- a database
- a generated content site
- a substitute for reading primary sources

Completeness is not the goal. A large uncurated repository would be a failure even if it contained many links.

## Intended Audience

The primary audience is a software engineer with a Metallurgical and Materials Engineering background transitioning into:

- Computational Materials Science
- Materials Informatics
- Scientific Software Engineering
- AI for Materials

The secondary audience is anyone who wants a research-grade overview of the field without spending years reconstructing the map from scattered papers, tools, courses, talks, and institutional knowledge.

## Design Principles

Materials Atlas is organized for retrieval, not storage.

People do not usually begin with a resource type. They begin with a domain, a problem, or a learning goal. A reader is more likely to ask "How do I understand density functional theory?" than "Which folder contains books?"

For that reason, domains are the primary organizing principle. Resources are secondary indexes. The editorial rules for future pages live in [EDITORIAL.md](EDITORIAL.md).

## Navigation

The initial repository is intentionally small:

- [EDITORIAL.md](EDITORIAL.md) defines the editorial standard for all future pages.
- [ROADMAP.md](ROADMAP.md) defines the high-level learning progression.
- [domains/](domains/) defines how future domain pages will organize knowledge.
- [resources/](resources/) defines how secondary resource indexes should work.
- [ecosystem/](ecosystem/) defines how people and institutions should be mapped.

The first curated indexes now exist where they have enough signal to be useful:

- [resources/books/](resources/books/) for durable books.
- [resources/papers/](resources/papers/) for paper selection philosophy and starter anchors.
- [resources/software/](resources/software/) for foundational software infrastructure.
- [resources/videos/](resources/videos/) for high-value long-form learning material.
- [ecosystem/researchers/](ecosystem/researchers/) for researchers who shape the field.
- [ecosystem/labs/](ecosystem/labs/) for institutions with durable influence.

No domain pages are created yet. Content still earns structure.

## Architecture Freeze

The repository architecture is intentionally stable.

Future work should primarily add or improve curated content inside the existing structure. Structural changes should be rare and require exceptional justification: they should make the atlas easier to navigate and maintain, not merely create a new place to put things.

## Why Domains Come First

Domains are the main way the field becomes understandable.

A mature domain page should eventually connect concepts, history, canonical papers, software, datasets, researchers, laboratories, industrial adoption, open problems, and learning order. The meaning lives in that relationship, not in any isolated resource list.

Resource types remain useful, but they should support domain pages rather than replace them.

## Why Resources Are Secondary

Books, papers, datasets, software, courses, videos, and conferences are important. They are not the primary map.

A paper matters because of what it changed. A software package matters because of where it is used. A dataset matters because of what questions it supports. Those meanings belong first in domains.

The `resources/` directory exists for secondary indexes only. It should help readers find included resources across the atlas, but it should not become the main navigation model.

## Contribution Philosophy

Contributions should improve understanding.

A useful contribution may add a resource, remove a weak resource, clarify a domain boundary, improve a learning sequence, explain why a tool matters, or identify a missing primary source. Use [EDITORIAL.md](EDITORIAL.md) as the authority for contribution quality.
