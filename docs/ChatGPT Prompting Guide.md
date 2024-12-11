---
title: "Guide to Prompting ChatGPT for Creating an AI-Driven DeltaV Engineering Assistant"
tags: [AI, DeltaV, Engineering, Prompt-Design, Knowledge-Base]
---

# Guide to Prompting ChatGPT for Creating an AI-Driven DeltaV Engineering Assistant

This document provides a strategy for interacting with ChatGPT (or similar LLMs) to guide you through creating a custom AI solution for DeltaV engineering tasks, including the use of vertical agents, infrastructure setup, and source file analysis.

## 1. Provide Context and Goals

Clearly state your project's objectives so the AI understands what you’re building.

**Example Prompt:**
> "I want to create a custom AI-based solution that can serve as a technical engineering assistant for DeltaV configuration projects. The solution should reference a large library of HTML-based documentation (DeltaV Books Online) to assist with hardware installation, configuration, troubleshooting, and advanced control strategies."

## 2. Consider Vertical Agents

If you plan to implement specialized sub-agents (vertical agents) for different domains (e.g., Installation, Configuration, Graphics, Troubleshooting), explicitly mention this approach and ask for feasibility and integration suggestions.

**Example Prompt:**
> "I’m considering using vertical agents, each focusing on a particular domain of DeltaV expertise. Is this a good approach, and how would I structure these agents so they can work together effectively?"

## 3. Describe the Source Files

Explain the volume, type, and organization of your reference materials, so the AI can suggest parsing and indexing strategies.

**Example Prompt:**
> "I have ~6,859 HTML files, 101 JPGs, 2,202 GIFs, and 1,560 PNGs that form the DeltaV Books Online. The main entry point is `c_main_suitehelp.html`. How should I approach parsing and indexing these files to enable the AI to reference them?"

## 4. Ask for Infrastructure Setup Guidance

Request a step-by-step plan for creating the necessary architecture: parsing the documentation, building a retrieval system, and integrating with an LLM.

**Example Prompt:**
> "Please give me a step-by-step infrastructure guide for building this solution, including:
> 1. Parsing and structuring the HTML documentation into a knowledge base.
> 2. Using vector embeddings and a vector database for semantic search.
> 3. Integrating the LLM with retrieval capabilities.
> 4. Orchestrating vertical agents, if appropriate."

## 5. Iterative Refinement

Begin with a high-level outline, then drill down into specifics as needed. After the AI provides a broad plan, follow up with targeted questions.

**Follow-Up Example:**
> "You mentioned vector embeddings. Which libraries or services would you recommend? How granular should the embeddings be—per HTML file, per section, or per paragraph?"

## 6. Start High-Level Before Details

Ask for a conceptual architecture first. Once you have that, move into technical details.

**Example Prompt:**
> "Before diving into specifics, can you outline a high-level architecture of the entire solution? Include components such as the ingestion pipeline, vector database, LLM integration, and user interface."

## 7. Position the AI as an Expert Consultant

Tell the AI to act as a senior solutions architect. Have it detail best practices, milestones, required skill sets, and resources.

**Example Prompt:**
> "Act as a senior AI solutions architect and provide a roadmap with milestones. Highlight what skills my team needs and where to learn more about these technologies."

---

**Summary of the Prompting Approach:**

1. **Set Context & Goals:** Explain what you want to build and why.
2. **Clarify Vertical Agents:** If using specialized sub-agents, clarify their roles and ask for guidance.
3. **Detail Data Sources:** Describe your HTML files and what you need from them.
4. **Infrastructure Guidance:** Request a technical roadmap for integrating parsing, indexing, embeddings, and LLM retrieval.
5. **Iterative Deepening:** Start from a high-level overview and gradually request more detail.
6. **Expert Perspective:** Have the AI act as a consultant, providing best practices and skill requirements.

By following these guidelines, you can effectively prompt ChatGPT to help you design a robust, AI-driven DeltaV engineering assistant that leverages your local HTML-based documentation.  
