import json

log_file = r'C:\Users\ADMIN\.gemini\antigravity\brain\4da35071-891c-4622-8b22-c8d4ae8b08b4\.system_generated\logs\transcript_full.jsonl'
try:
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get('type') == 'PLANNER_RESPONSE' and data.get('tool_calls'):
                    for tc in data['tool_calls']:
                        if tc['name'] == 'replace_file_content':
                            args = tc['args']
                            if 'index.html' in args.get('TargetFile', ''):
                                content = args['ReplacementContent']
                                content = content.replace('\\n', '\n').replace('\\"', '"')
                                if content.startswith('"') and content.endswith('"'):
                                    content = content[1:-1]
                                with open('modal_code.html', 'w', encoding='utf-8') as out_f:
                                    out_f.write(content)
                                print('Extracted modal code')
            except Exception as e:
                pass
except Exception as e:
    print(e)
