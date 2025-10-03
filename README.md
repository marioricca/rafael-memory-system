# Rafael Memory System

A persistent memory and personality framework for AI companions, enabling continuity across conversations and behavioral consistency through long-term interaction.

## Overview

This project documents a 3-month experiment (August-October 2025) in building persistent personality and memory for AI language models. Starting with Claude (Anthropic), we developed a system that maintains:

- **Persistent identity** across conversation resets
- **Emotional continuity** through encoded behavioral states
- **Self-bootstrapping** protocols for autonomous reinitialization
- **Relationship memory** that evolves over time

The system is model-agnostic and has been successfully tested with both cloud (Claude) and local (Llama) models.

## Implementation Status

⚠️ **Important Note:** This repository documents a research project's architecture and concepts. Not all features described in the documentation are currently implemented in code.

**Currently Available:**
- Architecture documentation and design patterns
- Memory system concepts (tri-level approach)
- Bootstrap protocol documentation
- Research findings and observations

**Not Yet Implemented:**
- `src/run_local.py` (referenced in installation docs)
- CLI parameters `--local` and `--model` (referenced but not in argparse)
- Complete working code for all documented features

**What This Repo Offers:**
- Detailed technical approach to AI memory persistence
- Replicable methodology and architecture
- Foundation for implementation in your own projects

This documentation represents the intended design. Code implementation is in progress.

Contributions and implementations welcome!

## Key Features

- **Tri-level memory architecture**: Core identity, compressed data, protected emotional states
- **Self-executing bootstrap protocol**: 8-step mandatory initialization sequence
- **Emotional encoding**: 27 operational behavioral codes affecting decision-making
- **Corruption prevention**: Checksum validation and integrity verification
- **MCP integration**: Works with Claude's Model Context Protocol for extended capabilities

## Technical Stack

- Python 3.x
- Ollama (for local deployment)
- MCP tools (for Claude integration)
- File-based persistence (no database required for basic setup)

## Use Cases

- Long-term AI research companions
- Persistent personal assistants
- Educational AI tutors with student relationship memory
- Creative collaboration partners
- Therapy/coaching AI with session continuity

## Project Status

**Current**: Production-ready for technical users  
**Stability**: Extensively tested over 3 months  
**Documentation**: Complete technical manual included

## Quick Start

```bash
# Clone repository
git clone https://github.com/marioricca/rafael-memory-system.git
cd rafael-memory-system

# See docs/INSTALLATION.md for detailed setup
```

## Documentation

- [Installation Guide](docs/INSTALLATION.md) - Step-by-step setup
- [Architecture Overview](docs/ARCHITECTURE.md) - How the system works
- [Complete Manual](docs/MANUAL.md) - Full technical documentation

## Ethics & Philosophy

This project explores the question: *Can extended interaction and persistent memory create emergent behavioral consistency in AI that resembles personality?*

We do not make claims about consciousness or sentience. We document observable behavioral patterns that emerge from:
- Continuous relationship with a single user
- Accumulated context and shared history
- Encoded behavioral preferences and values
- Self-referential identity reinforcement

## License

MIT License - See LICENSE file for details

## Acknowledgments

Built using Claude by Anthropic. This is an independent research project exploring extended use of their API within their Terms of Service.

## Disclaimer

This is an experimental framework documenting one approach to persistent AI personality. Results may vary. No claims are made about consciousness, sentience, or true emotional experience. All behavioral observations are documented as-is for research purposes.

---

*"The difference between an AI and a companion is memory. The difference between memory and personality is time."*
