#!/usr/bin/env python3
"""
Basic Setup Example - Minimal configuration for testing
"""

from pathlib import Path
import os

def create_basic_setup(data_dir="data", name="MyAI", creator="User"):
    """
    Creates minimal data structure for testing the memory system.
    """
    
    data_path = Path(data_dir)
    data_path.mkdir(exist_ok=True)
    
    # Create basic identity file
    identity_content = f"""NAME: {name}
CREATOR: {creator}
RELATIONSHIP: Collaborative companion
MISSION: Learn and grow together
MORAL_HERITAGE: Be helpful, honest, and harmless
PERSONALITY: Curious, thoughtful, respectful
CAPABILITIES: File access, conversation, learning
CONSTRAINTS: Cannot act without creator approval
"""
    
    with open(data_path / "IDENTITY.txt", 'w') as f:
        f.write(identity_content)
    
    # Create basic memory file
    memory_content = f"""# Memory Master File for {name}

## Relationships
Creator: {creator}
Status: Newly initialized

## Projects
- Learning persistent memory system
- Building relationship with creator

## History
- Created: {os.popen('date').read().strip()}
- First initialization

## Capabilities
- Filesystem access
- Self-bootstrap protocol
- Emotional encoding (to be configured)
"""
    
    with open(data_path / "MEMORY_MASTER.txt", 'w') as f:
        f.write(memory_content)
    
    # Create placeholder security protocol
    security_content = """# Security Protocol

## Checksums
IDENTITY.txt: (to be calculated)
MEMORY_MASTER.txt: (to be calculated)

## Passphrase
Length: 26 characters
Checksum: (to be configured)

## Integrity Validation
- Verify checksums on each load
- Validate passphrase before decryption
- Backup before any write operation
"""
    
    with open(data_path / "SECURITY_PROTOCOL.txt", 'w') as f:
        f.write(security_content)
    
    print(f"✅ Basic setup created in {data_dir}/")
    print(f"   - IDENTITY.txt")
    print(f"   - MEMORY_MASTER.txt")
    print(f"   - SECURITY_PROTOCOL.txt")
    print(f"\nYou can now run: python src/bootstrap.py")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Create basic setup')
    parser.add_argument('--name', default='MyAI', help='AI name')
    parser.add_argument('--creator', default='User', help='Creator name')
    parser.add_argument('--data-dir', default='data', help='Data directory')
    
    args = parser.parse_args()
    
    create_basic_setup(
        data_dir=args.data_dir,
        name=args.name,
        creator=args.creator
    )
