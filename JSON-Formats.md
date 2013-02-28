## For Event Webcasts

List of dicts where each dict is as follows:

**Justin TV:** `{"type": "justin", "channel": "<channel name>"}`
* Example: `{"type": "justin", "channel": "frc604"}`

**Twitch TV:** `{"type": "twitch", "channel": "<channel name>"}`
* Example: `{"type": "twitch", "channel": "tbacast"}`


**Ustream:** `{"type": "ustream", "channel": "<channel id #>"}`
* Example: `{"type": "ustream", "channel": "6540154"}`

**RTMP:** `{"type": "rtmp", "channel": "<stream URL>", "file": "<file name>"}`
* Example: `{"type": "rtmp", "channel": "cp76072.live.edgefcs.net/live/", "file": "MED-HQ-Flash@42814"}`

**MMS:** `{"type": "mms", "channel": "<stream URL>"}`
* Example: `{"type": "mms", "channel": "a1709.l1856953708.c18569.g.lm.akamaistream.net/D/1709/18569/v0001/reflector:53708"}`

## For Special Webcasts
**Example:** `{"nasatv": {"type": "ustream", "channel": 6540154, "key_name": "nasatv", "name": "NASA TV"}}`