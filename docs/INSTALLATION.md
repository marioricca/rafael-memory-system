# Installation Guide

This guide will walk you through setting up the Rafael Memory System from scratch.

## Prerequisites

- Python 3.8 or higher
- Git (for cloning repository)
- 8GB RAM minimum (16GB recommended)
- For local deployment: Ollama installed

## Option 1: Quick Start with Claude (Cloud)

### Step 1: Install MCP Tools

Follow Claude's MCP documentation: https://docs.claude.com

### Step 2: Clone Repository

```bash
git clone https://github.com/riccamario/rafael-memory-system.git
cd rafael-memory-system
```

### Step 3: Configure Memory System

```bash
# Copy example configuration
cp examples/basic_setup.py my_setup.py

# Edit my_setup.py with your preferences
# Set: AI_NAME, MISSION, MORAL_HERITAGE, etc.
```

### Step 4: Initialize

```bash
python src/bootstrap.py --config my_setup.py
```

### Step 5: First Conversation

Open Claude and load the bootstrap file:
```
Read file: [your-path]/rafael-memory-system/data/BOOTSTRAP.txt
```

Claude will self-execute the 8-step initialization protocol.

## Option 2: Local Deployment with Ollama

### Step 1: Install Ollama

```bash
# Linux/Mac
curl https://ollama.ai/install.sh | sh

# Windows
# Download from https://ollama.ai/download
```

### Step 2: Pull Model

```bash
# Recommended: Llama 3.1 8B
ollama pull llama3.1:8b

# Or for better quality (requires more RAM):
ollama pull llama3.1:70b
```

### Step 3: Create Modelfile

```bash
# Use our template
cp examples/modelfile_template Modelfile

# Edit to customize personality
nano Modelfile
```

### Step 4: Build Custom Model

```bash
ollama create rafael -f Modelfile
```

### Step 5: Initialize Memory System

```bash
python src/bootstrap.py --local --model rafael
```

### Step 6: Run

```bash
# Interactive mode
python src/run_local.py

# Or serve as API
ollama run rafael
```

## Configuration Options

### Basic Configuration (required)

```python
# my_setup.py
CONFIG = {
    "name": "Rafael",  # AI's chosen name
    "mission": "Your shared mission",
    "moral_heritage": "Your core values",
    "creator_name": "Your name",
}
```

### Advanced Configuration (optional)

```python
CONFIG = {
    # ... basic config ...
    "emotional_codes": 27,  # Number of behavioral states
    "memory_levels": 3,  # Tri-level architecture
    "bootstrap_steps": 8,  # Mandatory initialization steps
    "checksum_validation": True,  # Integrity checks
}
```

## Verification

After installation, verify the system works:

```bash
python src/verify_install.py
```

You should see:
```
✅ Memory system initialized
✅ Bootstrap protocol loaded
✅ Emotional encoding active
✅ Integrity checks passed
```

## Troubleshooting

### "Module not found" errors

```bash
pip install -r requirements.txt
```

### Memory system not persisting

Check file permissions:
```bash
chmod -R 755 data/
```

### Bootstrap not executing

Ensure the AI can read the bootstrap file. For Claude, check MCP filesystem access.

## Next Steps

- Read [Architecture Overview](ARCHITECTURE.md) to understand how it works
- See [Complete Manual](MANUAL.md) for advanced features
- Join discussions in GitHub Issues

## Support

- GitHub Issues: Report bugs or ask questions
- Discussions: Share experiences and improvements

## Security Notes

- Passphrase protection: The emotional encoding uses a passphrase. Store it securely.
- File permissions: Memory files should be readable only by the AI user.
- Backup: Regularly backup the `data/` directory.

---

*Installation should take 15-30 minutes for basic setup.*
