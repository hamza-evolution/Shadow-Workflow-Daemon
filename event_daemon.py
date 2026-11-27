import asyncio, json

async def dispatch_event(topic: str, payload: dict) -> str:
    await asyncio.sleep(0.005)
    return json.dumps({'topic': topic, 'dispatched': True, 'items': len(payload)})

if __name__ == '__main__':
    print(asyncio.run(dispatch_event('b2b.recon', {'target': 'US-Logistics'})))
