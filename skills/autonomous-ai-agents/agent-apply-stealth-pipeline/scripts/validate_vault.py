#!/usr/bin/env python3
"""
Statically re-runnable ATS pre-flight validation probe for Agent Apply.
"""

import sys
import json

def test_payload(payload_path):
    with open(payload_path, 'r') as f:
        data = json.load(f)
    assert "personal" in data, "Missing 'personal' section in vault"
    assert "email" in data["personal"], "Missing email in personal section"
    print("✅ Profile vault validation passed.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_payload(sys.argv[1])
    else:
        test_payload("/data/project_agent_apply/config/profile_vault.json")
