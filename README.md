# FastPay
## (A django Mobile Banking Platform like PalmPay with some extra Features. This Repo will be very available for any and every)

<!-- [Slides -> github.com/DavidWells/advanced-markdown](https://github.com/DavidWells/advanced-markdown/) -->

## Stack
- Backend => Python (Django and Django RestFramework)
- Frontend => Js (Vue), css => Tailwind or Bulma
- Mobile App => Flutter or Kotlin

## Packages To be Introduced
- Django
- Django Rest Framework
- Celery
- Django Anymail (Mailgun) `Production`
- Factory Boy
- Pillow
- Paystack / Flutterwave
- Django Redis (Caching)
- Isort
- Flake8
- Django mptt > Highly Unlikely
- Coverage
- Pytest
- pytest-django
- Celery Beat
- Postgresql (Dev)
- Docker Postgressql (Production)
- python-decouple (Personal Preference)
- Nginx
- psycopg2 (Postgres)
- 
`Other Packages will be included when needed`

## Intallation Guide
<!-- AUTO-GENERATED-CONTENT:START (TOC:collapse=true&collapseText="Click to expand") -->
<details>
<summary>"Click to expand"</summary>

- [Setup](#setup)
- [Features](#features)
- [Deployment Options](#deployment-options)
- [Advanced Formatting tips](#advanced-formatting-tips)
  - [`left` alignment](#left-alignment)
  - [`right` alignment](#right-alignment)
  - [`center` alignment example](#center-alignment-example)
  - [`collapse` Sections](#collapse-sections)
  - [`additional links`](#additional-links)
  - [Badges](#badges)
- [Useful packages](#useful-packages)
- [Useful utilities](#useful-utilities)
- [How Serverless uses markdown](#how-serverless-uses-markdown)
  - [DEMO](#demo)
- [Other Markdown Resources](#other-markdown-resources)

</details>
<!-- AUTO-GENERATED-CONTENT:END -->

## Setup

Create a Virtual Env (Windows)

```bash
$ py -m venv venv
```

Create a Virtual Env (Linux)

```bash
$ virtualenv venv
```

Activating The Environment (Windows)
```powershell
$ venv/Scripts/activate
```

Activating The Environment (Linux)
```powershell
$ source venv/bin/activate
```

Cloning this Repo to the same directory
```powershell
$ git clone https://github.com/officialalkenes/hoomia.git .
```

Cloning this Repo
```powershell
$ git clone https://github.com/officialalkenes/hoomia.git
```


Install developer and application packages.
Note: `redis` installation can be tedious for windows user. I might include a installation guideline in the future.
`rabbitmq` is very easy to use also

Installing Requirements.txt
```bash
$ pip install -r requirements.txt
```

## Features

- Banking Operations like Deposit and Withdrawal
- In-Banking Transfer
- User Authentication
- Coupon System
- Referral Coupon
- In app Purchases (Airtime & Data)
- Billing System
- Newsletter and Subscribers Mail
- Push Notification
## Deployment Options
- aws ec2
- heroku
- python anywhwere
- Digital ocean
---

- **Open** - Anyone can submit content, fix typos & update anything via pull requests
- **Version control** - Roll back & see the history of any given post
- **No CMS lock in** - We can easily port to any static site generator
- **It's just simple** - No user accounts to manage, no CMS software to upgrade, no plugins to install.

---

## Feature Implementation Link

if you need my feature implementation guidelines, [follow this link]('https://www.searchenginejournal.com/ecommerce-guide/must-have-website-features/'). I will also implement some features of well recognized e-commerce platforms.

A related example of is [here](https://www.jumia.com.ng/) & [here](https://www.amazon.com/). Expect some Modifications though.

## Chatbot Implementation

Since this is a not a standard application, the use of channels might be too overwhelming. Scalability is top priority.

### `left` alignment

<img align="left" width="100" height="100" src="http://www.fillmurray.com/100/100">

This is the code you need to align images to the left:
```
<img align="left" width="100" height="100" src="http://www.fillmurray.com/100/100">
```

---

### `right` alignment

<img align="right" width="100" height="100" src="http://www.fillmurray.com/100/100">

This is the code you need to align images to the right:
```
<img align="right" width="100" height="100" src="http://www.fillmurray.com/100/100">
```

---

### `center` alignment example

<p align="center">
  <img width="460" height="300" src="http://www.fillmurray.com/460/300">
</p>

```
<p align="center">
  <img width="460" height="300" src="http://www.fillmurray.com/460/300">
</p>
```

---

### Adding video

To add video you need to upload your video file and reference it inline

```
https://user-images.githubusercontent.com/1702215/158075475-c23004ab-827a-45ad-bdba-aee29ac5b582.mp4
```

Example:

https://user-images.githubusercontent.com/1702215/158075475-c23004ab-827a-45ad-bdba-aee29ac5b582.mp4

### light/dark mode images

Tip via this [tweet](https://twitter.com/stefanjudis/status/1465775940034781186). Swap out images based on theme settings

```
![Logo](./dark.png#gh-dark-mode-only)
![Logo](./light.png#gh-light-mode-only)
```

### Using [footnotes](https://github.blog/changelog/2021-09-30-footnotes-now-supported-in-markdown-fields/)

Here is a simple footnote[^example]. With some additional text after it.

[^example]: Example footnote

```
Here is a simple footnote[^1]. With some additional text after it.

[^1]: My reference.
````

### Tiny text in markdown

Normal text here.

<sup><sub>Tiny text is here. Awwwww its so cuteeeeeeeeeee</sub></sup>

**How?**

```
<sup><sub>Add your tiny text</sub></sup>
```

### `collapse` Sections

Collapsing large blocks of text can make your markdown much easier to digest

<details>
<summary>"Click to expand"</summary>
this is hidden block
</details>

```
<details>
<summary>"Click to expand"</summary>
this is hidden
</details>
```

Collapsing large blocks of Markdown text

<details>
<summary>To make sure markdown is rendered correctly in the collapsed section...</summary>

 1. Put an **empty line** after the `<summary>` block.
 2. *Insert your markdown syntax*
 3. Put an **empty line** before the `</details>` tag

</details>

```
<details>
<summary>To make sure markdown is rendered correctly in the collapsed section...</summary>

 1. Put an **empty line** after the `<summary>` block.
 2. *Insert your markdown syntax*
 3. Put an **empty line** before the `</details>` tag

</details>
```

---

### `additional links`

[Website](http://www.serverless.com) • [Email Updates](http://eepurl.com/b8dv4P) • [Gitter](https://gitter.im/serverless/serverless) • [Forum](http://forum.serverless.com) • [Meetups](https://github.com/serverless-meetups/main) • [Twitter](https://twitter.com/goserverless) • [Facebook](https://www.facebook.com/serverless) • [Contact Us](mailto:hello@serverless.com)

```
[Website](http://www.serverless.com) • [Email Updates](http://eepurl.com/b8dv4P) • [Gitter](https://gitter.im/serverless/serverless) • [Forum](http://forum.serverless.com) • [Meetups](https://github.com/serverless-meetups/main) • [Twitter](https://twitter.com/goserverless) • [Facebook](https://www.facebook.com/serverless) • [Contact Us](mailto:hello@serverless.com)
```

---

### Badges

<div align="center">

[![CI](https://github.com/fastify/fastify/workflows/ci/badge.svg)](https://github.com/fastify/fastify/actions/workflows/ci.yml)
[![Package Manager CI](https://github.com/fastify/fastify/workflows/package-manager-ci/badge.svg)](https://github.com/fastify/fastify/actions/workflows/package-manager-ci.yml)
[![Web SIte](https://github.com/fastify/fastify/workflows/website/badge.svg)](https://github.com/fastify/fastify/actions/workflows/website.yml)
[![Known Vulnerabilities](https://snyk.io/test/github/fastify/fastify/badge.svg)](https://snyk.io/test/github/fastify/fastify)
[![Coverage Status](https://coveralls.io/repos/github/fastify/fastify/badge.svg?branch=main)](https://coveralls.io/github/fastify/fastify?branch=main)
[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://standardjs.com/)

</div>

---

### Nice looking file tree

For whatever [reason](https://twitter.com/alexdotjs/status/1421015442286596100) the `graphql` syntax will nicely highlight file trees like below:

```graphql
# Code & components for pages
./src/* 
  ├─ src/assets - # Minified images, fonts, icon files
  ├─ src/components - # Individual smaller components
  ├─ src/fragments - # Larger chunks of a page composed of multiple components
  ├─ src/layouts - # Page layouts used for different types of pages composed of components and fragments
  ├─ src/page - # Custom pages or pages composed of layouts with hardcoded data components, fragments, & layouts
  ├─ src/pages/* - # Next.js file based routing
  │  ├─ _app.js - # next.js app entry point
  │  ├─ _document.js - # next.js document wrapper
  │  ├─ global.css - #  Global CSS styles
  │  └─ Everything else... - # File based routing
  └─ src/utils - # Utility functions used in various places
```

---

## Useful packages

1. [gray-matter](https://www.npmjs.com/package/gray-matter)

  YAML front-matter is your friend. You can keep metadata in markdown files

  ```
  title: Serverless Framework Documentation
  description: "Great F'in docs!"
  menuText: Docs
  layout: Doc
  ```

2. [Remark](https://www.npmjs.com/package/remark)

  Useful for rendering markdown in HTML/React

3. [Markdown Magic](https://github.com/DavidWells/markdown-magic)

  - [Repo](https://github.com/DavidWells/markdown-magic)
  - [Plugins](https://github.com/DavidWells/markdown-magic#plugins)
  - Show automatic doc generation. [Example 1](https://github.com/DavidWells/markdown-magic/blob/master/examples/generate-readme.js#L15-L23)   | [Example 2](https://github.com/serverless/examples/blob/master/generate-readme.js#L71-L87)

---

## Useful utilities

1. [Schedule Posts](https://github.com/serverless/post-scheduler) - Post scheduler for static sites

  Show DEMO

2. [Zero friction inline content editing](https://jekyll-anon.surge.sh/gods/2015/02/18/vesta.html)

  Show DEMO

3. [Byword](https://bywordapp.com/) & [Typora](https://typora.io/) - Good Editors

4. [Monodraw](https://monodraw.helftone.com/) - Flow charts for days

6. [Kap](https://getkap.co/) - Make gifs

4. [IDE markdown preview](https://atom.io/packages/markdown-preview)

5. Stuck on WordPress? Try [easy-markdown plugin](https://github.com/DavidWells/easy-markdown)

---

## How Serverless uses markdown

Serverless.com is comprised of 3 separate repositories

- https://github.com/serverless/blog
- https://github.com/serverless/serverless | Shoutout to [Phenomic.io](https://phenomic.io/)
- https://github.com/serverless/site

**Why multiple repos?**

1. We wanted documentation about the framework to live in the serverless github repo for easy access
2. We wanted our blog content to be easily portable to any static site generator separate from the implementation (site)
3. `prebuild` npm script pulls the content together & processes them for site build

A single repo is easier to manage but harder for people to find/edit/PR content.

---

### DEMO

- Site structure
- Serverless build process
- [Validation](https://github.com/serverless/blog/blob/master/.travis.yml#L10)
- [Editing Flow](https://serverless.com/framework/docs/providers/aws/cli-reference/deploy/)
- Github optimizations
  - [Link from top of each doc to live link on site](https://github.com/serverless/serverless/blob/master/docs/providers/aws/events/schedule.md)
  - use markdown magic =) to [auto generate tables](https://github.com/serverless/examples) etc
  - [Hide yaml frontmatter from github folks](https://github.com/serverless/serverless/blame/master/docs/providers/aws/events/schedule.md#L1-L7)
  - consider linking everything to site

## Other Markdown Resources

- [Markdown snippets](https://github.com/markdown-templates/markdown-snippets)
- [Verb](https://www.npmjs.com/package/verb) - Documentation generator for GitHub projects
- [ACSII docs](http://asciidoctor.org/) - Markdown alternative
- [Markdown parser performance comparison](https://github.com/Expensify/App/issues/3983#issue-942245008)
- [Handy markdown templates](https://github.com/G3root/readme-generator/blob/9219c5ee638f3b8ff429c5b514d4d211661ae136/src/data/project-block-list.ts)
