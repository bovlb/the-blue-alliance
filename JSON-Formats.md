## For Event Webcasts

List of dicts where each dict is as follows:

**Livestream:** `{"type": "livestream", "channel": "<channel id #>", "file": "<event id #>"}`
* Example: `{"type": "livestream", "channel": "3136927", "file": "1964881"}`

**Justin TV:** `{"type": "justin", "channel": "<channel name>"}`
* Example: `{"type": "justin", "channel": "frc604"}`

**MMS:** `{"type": "mms", "channel": "<stream URL>"}`
* Example: `{"type": "mms", "channel": "a1709.l1856953708.c18569.g.lm.akamaistream.net/D/1709/18569/v0001/reflector:53708"}`

**Twitch TV:** `{"type": "twitch", "channel": "<channel name>"}`
* Example: `{"type": "twitch", "channel": "tbacast"}`

**Ustream:** `{"type": "ustream", "channel": "<channel id #>"}`
* Example: `{"type": "ustream", "channel": "6540154"}`

**RTMP:** `{"type": "rtmp", "channel": "<stream URL>", "file": "<file name>"}`
* Example: `{"type": "rtmp", "channel": "cp76072.live.edgefcs.net/live/", "file": "MED-HQ-Flash@42814"}`

## For Special Webcasts
**Example:** `[{"type": "twitch", "channel": "frcgamesense", "key_name": "firstchamplive", "name": "#FIRSTChampLIVE"}, {"type": "twitch", "channel": "first_archimedes", "key_name": "2016arc", "name": "Archimedes Division"}, {"type": "twitch", "channel": "first_carson", "key_name": "2016cars", "name": "Carson Division"}, {"type": "twitch", "channel": "first_carver", "key_name": "2016carv", "name": "Carver Division"}, {"type": "twitch", "channel": "first_curie", "key_name": "2016cur", "name": "Curie Division"}, {"type": "twitch", "channel": "first_galileo", "key_name": "2016gal", "name": "Galileo Division"}, {"type": "twitch", "channel": "first_hopper", "key_name": "2016hop", "name": "Hopper Division"}, {"type": "twitch", "channel": "first_newton", "key_name": "2016new", "name": "Newton Division"}, {"type": "twitch", "channel": "first_tesla", "key_name": "2016tes", "name": "Tesla Division"}, {"type": "twitch", "channel": "frcgamesense", "key_name": "2016cmp", "name": "Einstein Field"}, {"type": "twitch", "channel": "first_franklin", "key_name": "franklin", "name": "Franklin Field"}, {"type": "twitch", "channel": "first_edison", "key_name": "edison", "name": "Edison Field"}, {"type": "twitch", "channel": "first_fll_a", "key_name": "fll_a", "name": "FLL Field A"}, {"type": "twitch", "channel": "first_fll_b", "key_name": "fll_b", "name": "FLL Field B"}, {"type": "twitch", "channel": "first_fll_c", "key_name": "fll_c", "name": "FLL Field C"}, {"type": "twitch", "channel": "first_fll_d", "key_name": "fll_d", "name": "FLL Field D"}, {"type": "twitch", "channel": "first_conferences", "key_name": "conferences", "name": "FIRST Conferences"}]`