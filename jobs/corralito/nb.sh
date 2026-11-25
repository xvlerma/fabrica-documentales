python3 mkbatch.py > /tmp/batch.json && python3 -c "
import json;u=json.loads(open('/tmp/batch.json').read().splitlines()[0]);print(json.dumps([dict(node_id=x['node_id'],prompt=x['prompt'],voice_id=x['voice_id']) for x in u],ensure_ascii=False))"
