import json
import os

log_file = r'C:\Users\ADMIN\.gemini\antigravity\brain\4da35071-891c-4622-8b22-c8d4ae8b08b4\.system_generated\logs\transcript_full.jsonl'
html_files = {}

try:
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get('type') == 'PLANNER_RESPONSE' and data.get('tool_calls'):
                    for tc in data['tool_calls']:
                        if tc['name'] == 'write_to_file':
                            args = tc['args']
                            if 'CodeContent' in args and 'TargetFile' in args and args['TargetFile'].endswith('.html'):
                                path = args['TargetFile'].strip('"')
                                content = args['CodeContent']
                                # Replace escaped quotes and newlines
                                content = content.replace('\\"', '"').replace('\\n', '\n')
                                # Strip the surrounding quotes if present
                                if content.startswith('"') and content.endswith('"'):
                                    content = content[1:-1]
                                html_files[path] = content
            except Exception as e:
                pass
except Exception as e:
    print(f"Error reading log: {e}")

for path, content in html_files.items():
    try:
        # We need to make sure the paths use standard slashes to avoid issues
        clean_path = path.replace('\\\\', '\\')
        with open(clean_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Recovered: {clean_path}")
    except Exception as e:
        print(f"Error writing {clean_path}: {e}")
